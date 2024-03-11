"""
	Logger文件
"""

import logging
import os

'''
format 可以指定输出的内容和格式，其内置的参数如下：

%(name)s：Logger的名字

%(levelno)s：打印日志级别的数值

%(levelname)s：打印日志级别的名称

%(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]

%(filename)s：打印当前执行程序名

%(funcName)s：打印日志的当前函数

%(lineno)d：打印日志的当前行号

%(asctime)s：打印日志的时间

%(thread)d：打印线程ID

%(threadName)s：打印线程名称

%(process)d：打印进程ID

%(message)s：打印日志信息
'''

class LoggerRecord(object):
    # 写正常log的函数
    def Custom_Write_logger(self,LogName,FileDirName,LogFileName,Info):# 写入日志信息
        """
            LogName: 类型名称 区分那种的log  没啥用不能去掉，给人看的
            FileDirName: log文件路径
            LogFileName: log文件名称
            Info: log的信息
        """
        if not os.path.exists(FileDirName):
            os.makedirs(FileDirName)
        logger = logging.getLogger(LogName)
        logger.setLevel(logging.DEBUG)# 等级为DEBUG
        fh = logging.FileHandler(f'{FileDirName}{LogFileName}',encoding="utf-8",mode="a")
        fh.setLevel(logging.DEBUG)
        fh_formatter = logging.Formatter('😄😄 %(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s : %(message)s 😄😄')
        
        fh.setFormatter(fh_formatter)
        logger.addHandler(fh)
        logger.debug(Info,exc_info=True)
        logger.removeHandler(fh)
        