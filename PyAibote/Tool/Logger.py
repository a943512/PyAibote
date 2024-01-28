import os
import time
from loguru import logger
from datetime import datetime


class LoggerRecord:
    """
        根据当天日期储存LOG文件
        Generate LOG file according to today's date.
    """
    
    Log_Storage = False
    Log_Level = "DEBUG"
    Log_Format = f"%(asctime)s - %(levelname)s : %(message)s"
    LOGMainPath = "AiBotRunLOG"
    LOGDayPath = f"AiBotRunLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}"
    DEBUGLogPath = f"{LOGDayPath}/DEBUG.log"
    ERRORLogPath = f"{LOGDayPath}/ERROR.log"
    INFOLogPath = f"{LOGDayPath}/INFO.log"

    def CheckFile(self):
        if self.Log_Storage:
            if not os.path.exists(self.LOGMainPath):
                os.makedirs(self.LOGMainPath)

            if not os.path.exists(self.LOGDayPath):
                os.makedirs(self.LOGDayPath)
            
    def Write_logger(self,LogFilePath,Level,Info) -> None:  # 写入日志信息
        """
            将LOG信息写入文件
            Write LOG information to a file.

            :LogFilePath: LOG文件路径
            :Info: LOG的信息
            :return:

            :LogFilePath: LOG file path
            :Info: LOG information
            :return:
        """
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")
        with open(LogFilePath,"a") as w:
            w.write(f"{formatted_time} - {Level} : {Info}\n")

    def debug(self, Msg) -> None:
        if self.Log_Storage:
            self.CheckFile()
            self.Write_logger(self.DEBUGLogPath, "DEBUG" ,Msg)

        if self.Log_Level == "DEBUG":
            logger.debug(Msg)

    def info(self, Msg) -> None:
        if self.Log_Storage:
            self.CheckFile()
            self.Write_logger(self.INFOLogPath, "INFO", Msg)

        if self.Log_Level == "INFO":
            logger.info(Msg)

    def error(self, Msg) -> None:
        if self.Log_Storage:
            self.CheckFile()
            self.Write_logger(self.ERRORLogPath, "ERROR", Msg)
        logger.error(Msg)