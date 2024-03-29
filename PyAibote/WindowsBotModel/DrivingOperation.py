import os

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

    def activate_frame(self, secret_key) -> bool:
        """
            激活Windows框架
            Activate Windows framework

            secret_key：激活框架的秘钥
            secret_key：Key to activate the frame

            return: 成功返回True失败返回False
            return: Returns True successfully and False if it fails
        """
        return "true" in self.SendData("activateFrame", secret_key) 
