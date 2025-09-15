import websockets
import asyncio
import threading
import json,traceback
from loguru import logger
from . import GlobalVariable


class WebSocketServerThread(threading.Thread):
    """
        运行 WebSocket 服务器的线程
        Thread running WebSocket server
    """

    def __init__(self, ip, port, is_print):
        super().__init__()
        self._loop = None
        self._server = None
        self._running = False
        self._ip = ip
        self._port = port
        self._is_print = is_print

    def debug(self, msg):
        if self._is_print == "DEBUG":
            logger.debug(msg)


    async def handle_connection(self, websocket):
        """
            处理客户端连接的协程
            Ctrip handling client connection
        """
        try:

            self.debug(f"Websocket Client connection at: <-<- {websocket.remote_address}")
            async for message in websocket:
                Msg = json.loads(message)    
                GlobalVariable.SocketServerClients[Msg["Data"]["Token"]] = websocket 

                self.debug(f"Websocket Receive Msg: <-<- {websocket.remote_address}")

                GlobalVariable.WebsocketReceiveMessage.put(Msg)
                await websocket.send(f"Server received: {message}")
        except Exception as e:
            pass

        finally:
            del GlobalVariable.SocketServerClients[Msg["Data"]["Token"]]   
            self.debug(f"Websocket Disconnect: <-<- {websocket.remote_address}")


    async def server_main(self):
        """
            WebSocket 服务器主逻辑
            WebSocket server main logic
        """
        self._running = True
        try:
            self._server = await websockets.serve(self.handle_connection, self._ip, self._port)
            print(f"WebSocket Server Stared on ws://{self._ip}:{self._port}")
            while self._running:
                if not GlobalVariable.WebsocketCallBack.empty():
                    item = GlobalVariable.WebsocketCallBack.get()
                    for token, client in GlobalVariable.SocketServerClients.items():
                        if token == item['Token']:
                            await client.send(str(item))
                await asyncio.sleep(1)
        except Exception as e:
            logger.error(traceback.format_exc())


    def run(self):
        """
            线程入口
            Thread entry
        """
        self._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._loop)
        try:
            self._loop.run_until_complete(self.server_main())
        except asyncio.CancelledError:
            pass
        finally:
            self._loop.close()

    def stop(self):
        """
            停止服务器
            Stop the server
        """
        if self._running:
            self._running = False
            if self._server:
                # 停止服务器
                self._loop.call_soon_threadsafe(self._server.close)


    def is_running(self):
        return self._running
    

class WebSocketServerUse:

    def get_websocket_data(self) -> dict:
        """
            获取WebSocket传递过来的数据
            Get the data passed by WebSocket

            return: 成功返回字典，失败返回空字典
            return: The dictionary was returned successfully, and an empty dictionary was returned if it failed
        """

        if not GlobalVariable.WebsocketReceiveMessage.empty():
            item = GlobalVariable.WebsocketReceiveMessage.get()
            return item
        return {}
    

    def send_websocket_data(self, data) -> bool:
        """
            发送WebSocket数据给客户端需要指定Token
            Sending WebSocket data to the client needs to specify Token

            data: 需要发送到客户端的数据
            data: the data that needs to be sent to the client

            return: 成功返回字典，失败抛错
            return: successfully returned to the dictionary, failed to throw a mistake
        """
        if "Token" not in data:
            raise KeyError("Token is not in data")

        if "Data" not in data:
            raise KeyError("Data is not in data")


        GlobalVariable.WebsocketCallBack.put(data)
        return True
    

    