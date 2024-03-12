"""
	写LOG文件
    LoggerRecord
"""

import logging
import os
from loguru import logger as lg

class LoggerRecord(object):
    
    def Custom_Write_logger(self, LogName, FileDirName, LogFileName, Log_Print, Info):
        """
            自定义写Log文件
            Custom write Log file

            LogName: 类型名称区分那种的log
            FileDirName: log文件夹路径
            LogFileName: log文件名称
            Info: log的信息
            Log_Print: 是否通过终端打印log信息
            return: 成功返回True or 失败返回False

            LogName: the type name distinguishes which kind of log
            FileDirName: log folder path
            LogFileName: log file name
            Info: log information
            Log_Print: whether the Log_Print: Log log information through the terminal
            return: Returns True or success or False on failure
        """
        try:
            if not os.path.exists(FileDirName):
                os.makedirs(FileDirName)
            logger = logging.getLogger(LogName)
            logger.setLevel(logging.DEBUG)# 等级为DEBUG
            fh = logging.FileHandler(f'{FileDirName}{LogFileName}',encoding="utf-8",mode="a")
            fh.setLevel(logging.DEBUG)
            fh_formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s : %(message)s')
            if Log_Print:
                lg.info(Info)
            fh.setFormatter(fh_formatter)
            logger.addHandler(fh)
            logger.debug(Info)
            logger.removeHandler(fh)
            return True
        except Exception as e:
            return False
        