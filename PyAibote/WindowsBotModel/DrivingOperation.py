import os,re

class DrivingOperation:
    """
        驱动操作
        Driving operation
    """

    def close_driver(self) -> bool:
        """
            远程部署时关闭WindowsDriver.exe驱动程序
            Close the WindowsDriver.exe driver

            return: 布尔值
            return: bool
        """

        return "true" in self.SendData("closeDriver")

    def close_driver_local(self) -> bool:
        """
            本地部署时关闭WindowsDriver.exe驱动程序(避免堆积大量WindowsDriver.exe进程占用系统资源)
            Close the WindowsDriver.exe driver

            return: 布尔值
            return: bool
        """

        os.system('taskkill /f /t /im  "WindowsDriver.exe"')
        return True 

    def activate_frame(self, secret_key) -> str:
        """
            激活Windows框架
            Activate Windows framework

            secret_key：激活框架的秘钥
            secret_key：Key to activate the frame

            return: 成功返回True失败返回False
            return: Returns True successfully and False if it fails
        """

        response = self.SendData("activateFrame", secret_key) 
        return response

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

    def get_windows_id(self) -> str:
        """
            获取Windows 唯一ID用于区分机器
            Get Windows unique ID to distinguish machines.

            return: 成功返回参数，失败返回None
            return: Parameter is returned successfully, and None is returned on failure.
        """

        response = self.SendData("getWindowsId")
        if response == "null":
            return None
        return response