import re
import json

class WindowOperation:
    """
        窗口操作
        Window operation
    """

    def get_window_pos(self) -> dict:
        """
            获取窗口位置和状态
            Get the window position and status.

            return: left和top：浏览器相对于与Windows窗口左上角坐标点，height和width：浏览器本身高度和宽度
            return: left and top: the coordinates of the browser relative to the upper left corner of the Windows window, height and width: the height and width of the browser itself.
        """

        response = self.SendData("getWindowPos")

            response = response.replace("\n","").replace("\t","")

        if response == "null":
            return None
        response = json.loads(response)
        return response

    def set_window_pos(self, status, left: float = 0, top: float = 0, width: float = 0, height: float = 0) -> bool:
        """
            设置窗口位置和窗口大小窗口状态
            Set window position and window size window state

            left:   浏览器相对于与Windows窗口左上角X坐标点     可选参数，浏览器窗口位置，此参数仅 status 值为 "normal" 时有效
            top:    浏览器相对于与Windows窗口左上角Y坐标点     可选参数，浏览器窗口位置，此参数仅 status 值为 "normal" 时有效
            width:  浏览器本身宽度                           可选参数，浏览器窗口位置，此参数仅 status 值为 "normal" 时有效
            height: 浏览器本身高度                           可选参数，浏览器窗口位置，此参数仅 windowState 值为 "normal" 时有效
            status: 正常:"normal"  最小化:"minimized"  最大化:"maximized"  全屏:"fullscreen"
            return: 布尔值

            left: an optional parameter, browser window position, relative to the X coordinate point in the upper left corner of the Windows window. This parameter is only valid when the status value is "normal"
            top: the optional parameter of the browser relative to the Y coordinate point in the upper left corner of the Windows window, and the browser window position. This parameter is only valid when the status value is "normal"
            width: optional parameter of browser width and browser window position. This parameter is only valid when the status value is "normal"
            height: optional parameter of browser height and browser window position. This parameter is only valid when the value of windowState is "normal"
            status: normal: "normal" minimize: "minimized" maximize: "maximized" fullscreen: "full screen"
            return: bool
        """
        return "true" in self.SendData("setWindowPos", status, left, top, width, height) 

    def quit(self) -> bool:
        """
            退出浏览器
            Exit the browser

            return: 布尔值
            return: bool
        """
        return "true" in self.SendData("closeBrowser")
        
    def mobile_emulation(self, width: int, height: int, userAgent: str, platform: str, platformVersion: str, acceptLanguage: str = "", timezoneId: str = "", latitude: float = 0, longitude: float = 0,accuracy: float = 0) -> bool:
        """
            模拟移动端浏览器
            Analog mobile browser

            width: 宽度
            height: 高度
            userAgent: 用户代理
            platform: 系统平台，例如 "Android"、"IOS"、"iPhone"
            platformVersion: 系统版本号，例如 "9.0"，应当与userAgent提供的版本号对应
            acceptLanguage: 可选参数，语言，例如 "zh-CN"、"en"
            timezoneId: 可选参数，时区标识，例如"Asia/Shanghai"、"Europe/Berlin"、"Europe/London" 时区应当与 语言、经纬度 对应
            latitude: 可选参数，纬度，例如 31.230416
            longitude: 可选参数，经度，例如 121.473701
            accuracy: 可选参数，精度，例如 1111
            return: 布尔值

            width: width
            height: height
            userAgent: user agent
            platform: System platform, such as "Android", "IOS" and "iPhone"
            platformVersion: the system version number, such as "9.0", should correspond to the version number provided by userAgent
            acceptLanguage: optional parameter and language, such as "zh-CN" and "en"
            timezoneId: optional parameter, time zone identifier, such as "Asia/Shanghai", "Europe/Berlin" and "Europe/London", the time zone should correspond to the language, latitude and longitude
            latitude: optional parameter, latitude, for example, 31.416
            longitude: optional parameter, longitude, for example, 121.01
            accuracy: optional parameter, precision, such as 1111
            return: Boolean value.

            示例：
            Example:
                self.mobile_emulation(500, 800, "Mozilla/5.0 (Linux; Android 7.0; SM-G950U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36", 
                    "Android", "7.0", "zh-Hans-CN", "Asia/Shanghai", 31.230416, 121.473701, 1111)
        """
        return "true" in self.SendData("mobileEmulation", width, height, userAgent, platform, platformVersion, acceptLanguage, timezoneId, latitude, longitude,accuracy) 



        