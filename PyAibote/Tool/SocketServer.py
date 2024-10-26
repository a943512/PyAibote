import socket
import socketserver
import subprocess
import threading,multiprocessing


class ThreadingTCPServer(socketserver.BaseRequestHandler):
    """
        启动TCP 服务底层基于socketserver
        Starting TCP service is based on socketserver.
    """
    
    @classmethod
    def StartThreadingTCPServer(self, cls, IP, Port) -> None:
        if type(Port)==int:
            self.server = socketserver.ThreadingTCPServer((IP,Port),cls)   #创建socket链接
            self.server.allow_reuse_address = True
            print(f"Server Stared on {IP}: {Port}")
            self.server.serve_forever()
            
        if type(Port)==list:
            for Pr in Port:
                self.server = socketserver.ThreadingTCPServer((IP,Pr),cls)   #创建socket链接
                self.server.allow_reuse_address = True
                print(f"Server Stared on {IP}: {Pr}")
                # 创建一个线程来启动每个服务器
                thread = threading.Thread(target=self.server.serve_forever)
                # 启动线程
                thread.start()


    def stop_server(self):
        try:
            self.server.shutdown()
            self.server.server_close()
        except Exception as e:
            print(f"Server Close")




