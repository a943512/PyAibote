import socket
import socketserver
import subprocess
import threading


class ThreadingTCPServer(socketserver.BaseRequestHandler):
    """
        启动TCP 服务底层基于socketserver
        Starting TCP service is based on socketserver.
    """
    
    @classmethod
    def StartThreadingTCPServer(self, cls, IP, Port) -> None:
        server = socketserver.ThreadingTCPServer((IP,Port),cls)   #创建socket链接
        print(f"Server Stared on {IP}: {Port}")
        server.serve_forever()








