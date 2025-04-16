"""
    PyAibote 轻量化实时数字人，模型大小仅20M。支持windows、Android、IOS、web、小程序 所有平台

    PyAibote Lightweight real-time digital human, the model size is only 20M. Support all platforms of windows, Android, IOS, web and applet
"""


import os,sys
import time
import subprocess
from abc import ABC, abstractmethod
import socketserver,socket
from .Tool import  *
from .DigitalHumanModel import  *
import threading



class HumanBotMain(
        ABC,
        LoggerRecord,
        SendClientData,
        ThreadingTCPServer, 
        DigitalHumanLoadWait,
        NewDigitalHumanOperation

   
    ):

    def __init__(self,*args):
        if len(args) ==1:
            address_info = socket.getaddrinfo(None, args[0], socket.AF_INET, socket.SOCK_STREAM)[0]
            family, socket_type, proto, _, socket_address = address_info
            server = socket.socket(family, socket_type, proto)
            server.bind(socket_address)
            server.listen(1)
            print("WindowsBot Service started successfully ...")
            self.request, self.client_address = server.accept()
            print("WindowsBot Client link succeeded")
        else:
            super().__init__(*args)


    # @abstractmethod
    def script_main(self):
        pass
    
    def handle(self):
        self.info(f"<-<- Client connection at {self.client_address[0]}: {self.client_address[1]}")
        self.debug(f"<-<- Client connection at {self.client_address[0]}: {self.client_address[1]}")
        self.script_main()

    @classmethod
    def execute(self, IP: str, Port: int, Debug: bool = True, Qt = None):
        try:
            if Port < 0 or Port > 65535:
                raise OSError("`listen_port` must be in 0-65535.")
            
            if Qt:
                self.Qt = Qt

            if Debug:
                Driver.DigtalHumanDriverStart(IP, Port)

            ThreadingTCPServer.StartThreadingTCPServer(self, IP, Port)
        except KeyboardInterrupt as e:
            sys.exit(self)

    @classmethod
    def StopSrver(self):
        try:
            self.server.shutdown()  # 停止接受新的连接
            self.server.socket.close()  # 关闭服务器套接字
        except Exception as e:
            pass
















