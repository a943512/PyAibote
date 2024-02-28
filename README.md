
1. Support the office automation [RPA] framework of Windows, Web and Android (including device projection screen), and support cloud deployment based on TCP protocol code.

2. Aibote at the bottom provides OCR server, which supports character recognition and positioning, without limiting the number of times of use, and provides yolo image recognition algorithm tools that can be trained by itself for free.

3. Perfect development documents and sample demonstrations, in addition to examples and Demo, there is no pressure to get started

4. The underlying technology is developed based on C/C++ language, which has strong stability and very fast execution speed.

It is strictly forbidden for users to use PyAibote to engage in any illegal and criminal activities, and the users will bear the relevant responsibilities, and PyAibote will not bear any legal responsibilities for this.
Any behavior that users engage in by using PyAibote does not represent PyAibote's will and opinions.



# 安卓系统RPA示例
# Android RPA example


```
# 1. 导入 AndroidBotMain 类
# 1. Import AndroidBotMain class
from PyAibote import AndroidBotMain



# 2. 自定义一个脚本类，继承 AndroidBotMain
# 2. Customize a script class and inherit AndroidBotMain
class CustomAndroidScript(AndroidBotMain):

    # 2.1. 设置是否终端打印输出 DEBUG：输出， INFO：不输出, 默认打印输出
    # 2.1. Set whether the terminal prints output DEBUG: output, INFO: no output, and print output by default
    Log_Level = "DEBUG" 

    # 2.2. 终端打印信息是否存储LOG文件 True： 储存， False：不存储
    # 2.2. Does the terminal print information store the LOG file? True: yes, False: no
    Log_Storage = True  


    # 2.3. 注意：script_main 此方法是脚本执行入口必须存在此方法
    # 2.3. Note: script_main This method must exist in the script execution portal
    def script_main(self):
        # 显示手机最近任务列表
        # Displays the list of recent tasks of the mobile phone
        result = self.recent_tasks()
        print(result)








if __name__ == '__main__':
    # 3. 注意：此处监听的端口号，必须和手机端的脚本端口号一致
    # 3. Note: The port number monitored here must be consistent with the script port number of the mobile phone.
    # 3.1 监听 8888 号端口
    # 3.1 Listening to Port 8888
    CustomAndroidScript.execute("0.0.0.0", 8888)
```



# Windwos系统RPA示例
# Windwos system RPA example

```
# 1. 导入 WinBotMain 类
# 1. Import WinBotMain class
from PyAibote import WinBotMain
import time,os

# 2. 自定义一个脚本类，继承 WinBotMain
# 2. Customize a script class and inherit WinBotMain.
class CustomWinScript(WinBotMain):

    # 2.1. 设置是否终端打印输出 DEBUG：输出， INFO：不输出, 默认打印输出
    # 2.1. Set whether the terminal prints output DEBUG: output, INFO: no output, and print output by default.
    Log_Level = "DEBUG" 

    # 2.2. 终端打印信息是否存储LOG文件 True： 储存， False：不存储
    # 2.2. Does the terminal print information store the LOG file? True: yes, False: no.
    Log_Storage = True  


    # 2.3. 注意：script_main 此方法是脚本执行入口必须存在此方法
    # 2.3. Note: script_main This method must exist in the script execution portal.
    def script_main(self):
        # 查询所有窗口句柄
        result = self.find_windows()
        print(result)








if __name__ == '__main__':
    # 3. IP为:0.0.0.0, 监听 9999 号端口
    # 3. IP: 0.0.0, listening to port 9999.
    # 3.1. 在远端部署脚本时，请设置 Debug=False，客户端手动启动 WindowsDriver.exe 时需指定远端 IP 或端口号
    # 3.1. When deploying the script remotely, please set Debug=False, and the client needs to specify the remote IP or port number when manually starting the WindowsDriver.exe.
    # 3.2. 命令行启动示例：WindowsDriver.exe "192.168.1.88" 9999
    # 3.2. Command line startup example: WindowsDriver.exe "192.168.1.88" 9999
    CustomWinScript.execute("0.0.0.0", 9999, Debug=True)
```



# Web系统RPA示例
# Web system RPA example

```
# 1. 导入 AndoridBotMain 类
# 1. Import the AndoridBotMain class
from PyAibote import WebBotMain


# 2. 自定义一个脚本类，继承 WebBotMain
# 2. Customize a script class and inherit WebBotMain.
class CustomWebScript(WebBotMain):

    # 3. 设置是否终端打印输出 DEBUG：输出， INFO：不输出, 默认打印输出
    # 3. Set whether the terminal prints output DEBUG: output, INFO: no output, and print output by default.
    Log_Level = "DEBUG"  # "INFO"


    # 4. 终端打印信息是否存储LOG文件 True： 储存， False：不存储
    # 4. Does the terminal print information store the LOG file? True: yes, False: no.
    Log_Storage = True  # True


    # 5. 全局隐式等待 [找不到元素重复查找]
    # 5.1 元素未加载等待时间(秒)
    # 5. Global implicit wait [repeated search of element not found]
    # 5.1 element not loaded wait time (seconds)
    Implicit_Waiting = 5

    # 5.2 元素未加载间隔多少时间重复加载(秒)
    # 5.2 How often does the element load repeatedly (seconds)
    Implicit_Waiting_Frequency = 0.5

    # 5.3 超过未加载等待时间是否抛出异常
    # 5.3 Whether to throw an exception when the waiting time for unloading exceeds?
    Implicit_Waiting_Throwing = False


    # 6. 注意：此方法是脚本执行入口
    # 6. Note: This method is a script execution portal.
    def script_main(self):
        result = self.goto("https://baidu.com")
        print(result)

        # 6.1. 显示等待和隐式等待意思一样, 显示等待可以让你在某个局部代码中自定义设置等待时长
        # StartShowWait函数后的代码按照等待10秒，每个0.5秒重复加载，False找不到不抛出异常，此时你如果设置的全局隐式等待将不生效直到结束显示等待
        # 6.1. Displaying waiting means the same as implicit waiting. Displaying waiting allows you to customize the waiting time in a local code.
        The code after the # StartShowWait function is loaded repeatedly every 0.5 seconds according to the waiting time of 10 seconds. If False is not found, no exception will be thrown. At this time, if you set the global implicit waiting, it will not take effect until the display waiting is over.
        self.StartShowWait(10, 0.5, False)

        result = self.goto("https://qq.com")
        print(result)
        result = self.goto("https://www.hao123.com")
        print(result)

        # 6.1 结束显示等待,也是自定义结束局部等待此时如果设置的全局隐式等待后面的代码将按全局隐式等待的设置来执行
        # 6.1 Ending display waiting is also a custom ending local waiting. At this time, if the global implicit waiting is set, the code behind it will be executed according to the setting of global implicit waiting.
        self.EndShowWait()









if __name__ == '__main__':
    # 7. 启动脚本，监听 9999 号端口, 默认使用 Chrome 浏览器
    # 7. Start the script, listen to port 9999, and use Chrome browser by default.

    # 7.1. Debug=True 时，是本地运行脚本，会自动启动 WebDriver.exe 驱动
    # 在远端部署脚本时，请设置 Debug=False，手动启动 WebDriver.exe，启动 WebDriver.exe 时需指定远端 IP 或端口号
    # 7.1. When debug = true, the script is run locally, and the WebDriver.exe driver will be started automatically.
    # When deploying the script remotely, please set Debug=False to manually start WebDriver.exe, and specify the remote IP or port number when starting WebDriver.exe.

    # 7.2. 如本地部署脚本，需要传递 WebDriver 启动参数时，参考下面方式，如不需传递启动参数，则忽略：
    # 7.2. For local deployment scripts, when the WebDriver startup parameters need to be passed, please refer to the following methods. If the startup parameters don't need to be passed, ignore them:
    
    driver_params = {
        "browserName": "chrome",
        "debugPort": 0,
        "userDataDir": "./UserData",
        "browserPath": None,
        "argument": None,
    }

    CustomWebScript.execute("0.0.0.0", 9999, Debug=True, Driver_Params=driver_params)
```
