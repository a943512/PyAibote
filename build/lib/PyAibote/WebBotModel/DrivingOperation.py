

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
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        if response == "null":
            return None
        return response