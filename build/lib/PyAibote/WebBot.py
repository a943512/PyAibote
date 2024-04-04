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
import time
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
        Sqlite3DataBaseHandle
    ):

    @abstractmethod
    def script_main(self):
        pass
    
    def handle(self):
        self.info(f"<-<- Client connection at {self.client_address[0]}: {self.client_address[1]}")
        self.debug(f"<-<- Client connection at {self.client_address[0]}: {self.client_address[1]}")
        self.script_main()

    @classmethod
    def execute(self, IP: str, Port: int, Debug: bool = True, Driver_Params: dict = None):
        if Port < 0 or Port > 65535:
            raise OSError("`listen_port` must be in 0-65535.")

        if Debug:
            Driver.WebDriverStart(Port, Driver_Params)
        ThreadingTCPServer.StartThreadingTCPServer(self, IP, Port)
