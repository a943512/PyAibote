

class DrivingOperation:
    """
        驱动程序相关
        Driver correlation
    """

    def close_driver(self) -> bool:
        """
            关闭WebDriver.exe驱动程序，服务端会抛错
            Close the WebDriver.exe driver.

            return: 布尔值
            return: bool
        """
        return "true" in self.SendData("closeDriver") 


    def get_extend_param(self) -> str:
        """
            获取驱动程序命令行参数(不包含ip和port)
            Get the driver command line parameters (excluding ip and port)

            return: 成功返回参数，失败返回None
            return: parameter is returned successfully, and None is returned on failure.
        """

        response = self.SendData("getExtendParam")
        if response == "null":
            return None
        return response


    def activate_frame(self, secret_key) -> str:
        """
            激活Web框架
            Activate Web framework

            secret_key：激活框架的秘钥
            secret_key：Key to activate the frame

            return: 成功返回True失败返回False
            return: Returns True successfully and False if it fails
        """

        response = self.SendData("activateFrame", secret_key) 
        return response
    
    
    def set_download_dir(self, dir_name) -> str:
        """
            设置浏览器默认下载目录
            Set the browser default download directory

            dir_name：下载目录
            dir_name: download directory

            return: 成功返回True失败返回False
            return: Returns True successfully and False if it fails
        """

        return "true" in self.SendData("setDownloadDir", dir_name)
