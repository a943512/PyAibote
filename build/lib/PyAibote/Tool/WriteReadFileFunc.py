"""
    读写文件类
"""
from .LoggerFunc import LoggerRecord
import os,json,time
import traceback

class WriteReadFile(LoggerRecord):
    def WriteFile(self,path,data):
        """
            path: 需要写入的文件路径
            data: 需要写入的数据

            path: the file path that needs to be written
            data: data to be written
        """
        try:
            with open(path,'w',encoding='UTF-8') as w:
                w.write(data)
            return "Ok"
        except Exception as e:
            LoggerRecord.Custom_Write_logger(self,"",f"{os.getcwd()}/SysMdelLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log","")
            return "Error"

    def ReadFile(self,path):
        """
            path: 需要读取的文件路径
            Path: the file path to be read.
        """
        try:
            with open(path,'r',encoding='UTF-8') as r:
                Data = r.read()
            return Data
        except Exception as e:
            LoggerRecord.Custom_Write_logger(self,"",f"{os.getcwd()}/SysMdelLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log","")
            return "Error"

    def WriteFileAddTo(self,path,data):
        """
            path: 需要追加写入的文件路径
            data: 需要追加写入的数据

            path: the file path that needs additional writing
            data: data that needs to be written additionally
        """
        try:
            with open(path,'a',encoding='UTF-8') as w:
                w.write(data)
            return "Ok"
        except Exception as e:
            LoggerRecord.Custom_Write_logger(self,"",f"{os.getcwd()}/SysMdelLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log","")
            return "Error"

    def ReadJsonFile(self,path,key=None,Key2=None,Key3=None,Key4=None,Key5=None):
        """
            key: 读取key根目录路径信息
            Key2: 读取key二级目录路径信息
            默认读取所有文件信息

            key: read the key root directory path information
            key2: read the path information of key secondary directory
            read all file information by default
        """
        try:
            ResultData = self.ReadFile(path)
            ResultData = json.loads(ResultData)
            if key and Key2 and Key3 and Key4 and Key5:
                ResultData = ResultData[key][Key2][Key3][Key4][Key5]
            elif key and Key2 and Key3 and Key4:
                ResultData = ResultData[key][Key2][Key3][Key4]
            elif key and Key2 and Key3:
                ResultData = ResultData[key][Key2][Key3]
            elif key and Key2:
                ResultData = ResultData[key][Key2]
            elif key:
                ResultData = ResultData[key]
            return ResultData
        except Exception as e:
            LoggerRecord.Custom_Write_logger(self,"",f"{os.getcwd()}/SysMdelLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log","")
            return "Error"


if __name__ == '__main__':
    wr = WriteReadFile()
    result = wr.ReadJsonFile(f"{os.getcwd()}/ConfigFile.json","LinkDatabaseInfo")
    print(result)









