"""
    PyAibote Windows自动化框架，由WindowsDriver.exe客户端驱动程序连接脚本服务端，采用TCP协议传输命令。
    全国领先xpath元素定位算法，一键拾取控件元素、图色 坐标等属性。与安卓端代码统一书写格式，降低用户学习成本。
    独家图色定位算法，50毫秒以内的速度遍历查找1920*1080分辨率的设备

    PyAibote Windows automation framework, with WindowsDriver.exe client driver connected to script server and TCP protocol used to transmit commands.
    The leading xpath element positioning algorithm in China can pick up control elements, color coordinates and other attributes with one click. 
    The writing format is unified with the Android code, which reduces the learning cost of users.
    Exclusive color positioning algorithm, searching for equipment with resolution of 1920*1080 at a speed of less than 50 milliseconds

"""


import os
import time
import subprocess
from abc import ABC, abstractmethod
import socketserver,socket
from .Tool import  *
from .WindowsBotModel import  *


class WinBotMain(
        ABC,
        LoggerRecord,
        ThreadingTCPServer, 
        WinLoadWait,
        SendClientData,
        DrivingOperation,
        WindowOperation,
        KeymouseOperation,
        ColorOperation,
        OcrOperation,
        YoloOperation,
        ElementOperation,
        SystemOperation,
        OtherOperations,
        ExcelOperation,
        VoiceService,
        DigitalHumanOperation,
        VerificationCodeOperation,
        WinHidCorrelation,
        ChatGenerative,
        DataBaseHandle,
        Sqlite3DataBaseHandle
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

    @classmethod
    def _build(self, listen_port: int, Debug: bool = True) -> object:
        """
            使用安卓hid模式时需要启动windows驱动
            Windows driver needs to be started when using Android hid mode.

            listen_port: 脚本监听的端口
            Debug: 脚本是否部署在本地
            return: windows类对象

            listen_port: the port on which the script listens.
            Debug: Is the script deployed locally?
            return: windows class object
        """
        if listen_port < 0 or listen_port > 65535:
            raise OSError("`listen_port` must be in 0-65535.")

        if Debug:
            try:
                subprocess.Popen(["WindowsDriver.exe", "127.0.0.1", str(listen_port)])
                print("Debug Model Start WinDriver ...")
            except FileNotFoundError as e:
                err_msg = "\nStart local WinDriver.exe fail Exception elimination step：\n1. Check WebDriver.exe Path；\n2. WebDriver.exe Add to system environment variable?"
                self.error(f"{err_msg}: " + str(e))
        return WinBotMain(listen_port)

    # @abstractmethod
    def script_main(self):
        pass
    
    def handle(self):
        self.info(f"<-<- Client connection at {self.client_address[0]}: {self.client_address[1]}")
        self.debug(f"<-<- Client connection at {self.client_address[0]}: {self.client_address[1]}")
        self.script_main()

    @classmethod
    def execute(self, IP: str, Port: int, Debug: bool = True):
        if Port < 0 or Port > 65535:
            raise OSError("`listen_port` must be in 0-65535.")
        
        if Debug:
            Driver.WindowsDriverStart(IP, Port)
        ThreadingTCPServer.StartThreadingTCPServer(self, IP, Port)




















