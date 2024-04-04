"""
    读写文件
    WriteReadFile
"""

from .LoggerFunc import LoggerRecord
import os,json,time
import traceback

class WriteReadFile(LoggerRecord):
    def WriteFile(self, path, data) -> bool:
        """
            写入文件
            WriteFile

            path: 需要写入的文件路径
            data: 需要写入的数据
            return: 成功返回True or 失败返回False

            path: the file path that needs to be written
            data: data to be written
            return: Returns True or success or False on failure
        """

        try:
            with open(path,'w',encoding='UTF-8') as w:
                w.write(data)
            return True
        except Exception as e:
            WriteReadFile.Custom_Write_logger(self,"",f"{os.getcwd()}/AiBotRunLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log",False,f"{traceback.format_exc()}")
            return False

    def ReadFile(self,path) -> str or bool:
        """
            读取文件
            ReadFile

            path: 需要读取的文件路径
            return: 成功返回文件数据, 失败返回False

            path: the file path to be read
            return: file data is returned successfully, and False is returned if it fails
        """

        try:
            with open(path,'r',encoding='UTF-8') as r:
                Data = r.read()
            return Data
        except Exception as e:
            WriteReadFile.Custom_Write_logger(self,"",f"{os.getcwd()}/AiBotRunLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log",False,f"{traceback.format_exc()}")
            return False

    def WriteFileAddTo(self,path,data)  -> bool:
        """
            追加写入文件
            Additional write file

            path: 需要追加写入的文件路径
            data: 需要追加写入的数据
            return: 成功返回True, 失败返回False

            path: the file path that needs additional writing
            data: data that needs to be written additionally
            return: file data is returned successfully, and False is returned if it fails
        """

        try:
            with open(path,'a',encoding='UTF-8') as w:
                w.write(data)
            return True
        except Exception as e:
            WriteReadFile.Custom_Write_logger(self,"",f"{os.getcwd()}/AiBotRunLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log",False,f"{traceback.format_exc()}")
            return False

    def ReadJsonFile(self, path, key=None, Key2=None, Key3=None, Key4=None, Key5=None) -> str or bool:
        """
            读取json文件
            Read json file

            key: 读取一级嵌套路径信息
            Key2: 读取key二级嵌套路径信息
            ....  最多支持五级嵌套路径, 默认读取所有json文件内的信息
            return: 成功返回json文件字典数据, 失败返回False
            

            Key: Read the first-level nested path information
            Key2: read the second-level nested path information of key
            ... supports up to five nested paths, and reads the information in all json files by default
            return: json file data is returned successfully, and False is returned if it fails
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
            WriteReadFile.Custom_Write_logger(self,"",f"{os.getcwd()}/AiBotRunLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log",False,f"{traceback.format_exc()}")
            return False











