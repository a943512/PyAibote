"""
    PyAibote Web自动化框架，由WebDriver.exe
    客户端驱动程序连接脚本服务端，采用TCP协议传输命令。
    底层基于chromium内核研发而成的一款web自动化框架,
    因此支持chromium内核的所有浏览器和应用程序, 框架稳定, 运行速度非常快.

    PyAibote Web automation framework, 
    with WebDriver.exe client driver connected to script server and TCP protocol used to transmit commands.
    The bottom layer is a web automation framework based on the chromium kernel, so it supports all browsers and applications of the chromium kernel, 
    and the framework is stable and runs very fast.
"""


import os
import time,subprocess,json,random
from multiprocessing import Process
from abc import ABC, abstractmethod
import socketserver,socket
from .WebBotModel import  *
from .Tool import  *


class WebBotMain(
        ABC,
        LoggerRecord,
        ThreadingTCPServer, 
        UniversalFunction,
        SendClientData, 
        WebLoadWait,
        PagesNavigation,
        ElementOperation,
        KeymouseOperation,
        PopUpWindow,
        WindowOperation,
        DrivingOperation,
        JSinjection,
        CookiesOperation,
        ChatGenerative,
        DataBaseHandle,
        Sqlite3DataBaseHandle,
        IframeOperation
    ):

    def __init__(self,*args):
        if len(args) ==1:
            address_info = socket.getaddrinfo(None, args[0], socket.AF_INET, socket.SOCK_STREAM)[0]
            family, socket_type, proto, _, socket_address = address_info
            server = socket.socket(family, socket_type, proto)
            server.bind(socket_address)
            server.listen(1)
            print("Mix Start WebBot Service")
            self.request, self.client_address = server.accept()
            print("WebBot Client link succeeded")
        else:
            super().__init__(*args)

    @classmethod
    def _build(self, listen_ip, listen_port: int, Debug: bool = True, driver_params: dict = {}) -> object:
        """
            混合开发时启动web驱动
            TCP transit service.

            listen_port: 脚本监听的端口
            return: windows类对象

            listen_port: the port on which the script listens.
            Debug: Is the script deployed locally?
            return: windows class object
        """
        if Debug:
            default_params = {
                "serverIp": "127.0.0.1",
                "serverPort": listen_port,
                "browserName": "chrome",
                "debugPort": 0,
                "userDataDir": f"./UserData{random.randint(100000, 999999)}",
                "browserPath": None,
                "argument": None,
            }
            if driver_params:
                default_params.update(driver_params)
            default_params = json.dumps(default_params)
            
            try:
                print("WebDriver And Windows Mix Model Start WebDriver ...")
                subprocess.Popen(["WebDriver.exe", default_params])
                print("Mix Start WebDriver Successful，Execute Script")
            except FileNotFoundError as e:
                err_msg = "\nStart local WebDriver.exe fail Exception elimination step：\n1. Check WebDriver.exe Path；\n2. WebDriver.exe Add to system environment variable?"
                self.error(f"{err_msg}: " + str(e))

        return WebBotMain(listen_port)

    # @abstractmethod
    def script_main(self):
        pass
    
    def handle(self):
        self.info(f"<-<- Client connection at {self.client_address[0]}: {self.client_address[1]}")
        self.debug(f"<-<- Client connection at {self.client_address[0]}: {self.client_address[1]}")
        self.script_main()

    @classmethod
    def execute(self, IP: str, Port: int, Debug: bool = True, Driver_Params: dict = None):
        try:
            if Port < 0 or Port > 65535:
                raise OSError("`listen_port` must be in 0-65535.")

            if Debug:
                Driver.WebDriverStart(Port, Driver_Params)
            ThreadingTCPServer.StartThreadingTCPServer(self, IP, Port)
        except KeyboardInterrupt as e:
            sys.exit(self)