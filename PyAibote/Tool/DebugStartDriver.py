import json
import subprocess
import random
import platform


class Driver:
    """
        DEBUG模式下自动启动驱动调试浏览器
        Automatically start the driver DEBUGging browser in debug mode.
    """

    @classmethod
    def WebDriverStart(self, Port ,Driver_Params) -> None:
        default_params = {
            "serverIp": "127.0.0.1",
            "serverPort": Port,
            "browserName": "chrome",
            "debugPort": 0,
            "userDataDir": f"./UserData{random.randint(100000, 999999)}",
            "browserPath": None,
            "argument": None,
        }
        if Driver_Params:
            default_params.update(Driver_Params)
        default_params = json.dumps(default_params)
        
        try:
            print("Debug Model Start WebDriver ...")
            subprocess.Popen(["WebDriver.exe", default_params])
            print("Start WebDriver Successful，Execute Script")
        except FileNotFoundError as e:
            err_msg = "\nStart local WebDriver.exe fail Exception elimination step：\n1. Check WebDriver.exe Path；\n2. WebDriver.exe Add to system environment variable?"
            self.error(f"{err_msg}: " + str(e))

    @classmethod
    def WindowsDriverStart(self, IP, Port) -> None:
        try:
            system_info = platform.system()
            if system_info == "Windows":
                DriverName = "WindowsDriver.exe"
                version_info = platform.version()
                major_version = int(version_info.split('.')[0])
                if major_version > 10:
                    DriverName = "WindowsDriver_win7.exe"
                print("Debug Model Start WebDriver ...")
                subprocess.Popen([DriverName, "127.0.0.1", str(Port)])
                print("Start WinDriver Successful，Execute Script")
        except FileNotFoundError as e:
            err_msg = "\nStart local WinDriver.exe fail Exception elimination step：\n1. Check WebDriver.exe Path；\n2. WebDriver.exe Add to system environment variable?"
            self.error(f"{err_msg}: " + str(e))

