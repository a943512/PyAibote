import queue


# 存储Websocket连接key唯一标识
SocketServerClients = {}

# 接受消息队列
WebsocketReceiveMessage = queue.Queue()

# 返回消息队列
WebsocketCallBack = queue.Queue() 