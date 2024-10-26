"""
    PyAibote安卓云端自动化框架，采用云端服务模式构建。由安卓手机客户端主动连接服务器/电脑服务端程序，
    服务端应采用多线程TCP协议和多个安卓设备通信。构架模式决定了自动化代码部署在云端，能有效防止脚本被第三方恶意破解。
    结合Aibote远程投屏技术，可直接连接远程用户设备做自动化机器人编写，完美解决远程自动化测试需求。独家图色定位算法，
    50毫秒以内的速度遍历查找2340*1080分辨率的设备

    PyAibote Android cloud automation framework is built with cloud service mode. The Android mobile phone client actively connects with the server/computer server program,
    The server should use multithreaded TCP protocol to communicate with multiple Android devices. The architecture mode determines that the automation code is deployed in the cloud, 
    which can effectively prevent scripts from being maliciously cracked by third parties.
    Combined with Aibote remote screen projection technology, it can be directly connected to remote user equipment for automatic robot programming, 
    which perfectly meets the requirements of remote automatic testing. Exclusive color location algorithm,
    Traverse within 50 milliseconds to find the equipment with 2340*1080 resolution.
"""


import os,sys
import time
from multiprocessing import Process
from abc import ABC, abstractmethod
import socketserver,socket
from .Tool import  *
from .AndroidBotModel import *


class AndroidBotMain(
        ABC,
        LoggerRecord,
        ThreadingTCPServer, 
        AndroidLoadWait,
        Driver,
        SendClientData,
        UniversalFunction,
        CoordinateOperation,
        ElementOperation,
        EquipmentOperation,
        ScreenProjectionOperation,
        FileTransfer,
        Control,
        OcrCorrelation,
        YoloService,
        UrlRequest,
        ColorFindingOperation,
        MapFindingOperation,
        ScreenshotOperation,
        AndroidHidCorrelation,
        VerificationCodeOperation,
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
    def execute(self, IP: str, Port):
        ThreadingTCPServer.StartThreadingTCPServer(self, IP, Port)


















