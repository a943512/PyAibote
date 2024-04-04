

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