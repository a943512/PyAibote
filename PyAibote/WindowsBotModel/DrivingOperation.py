import os

class DrivingOperation:
    """
        驱动操作
        Driving operation
    """

    def close_driver(self) -> bool:
        """
            关闭WindowsDriver.exe驱动程序
            Close the WindowsDriver.exe driver

            return: 布尔值
            return: bool
        """
        os.system('taskkill /f /t /im  "WindowsDriver.exe"')
        # return "true" in self.SendData("closeDriver")
        return True 