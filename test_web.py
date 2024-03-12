# 1. 导入 AndoridBotMain 类
from PyAibote import WebBotMain


# 2. 自定义一个脚本类，继承 WebBotMain
class CustomWebScript(WebBotMain):

    # 3. 设置是否终端打印输出 DEBUG：输出， INFO：不输出, 默认打印输出
    Log_Level = "DEBUG"  # "INFO"


    # 4. 终端打印信息是否存储LOG文件 True： 储存， False：不存储
    Log_Storage = True  # True


    # 5. 全局隐式等待 [找不到元素重复查找]
    # 5.1 元素未加载等待时间(秒)
    Implicit_Waiting = 5

    # 5.2 元素未加载间隔多少时间重复加载(秒)
    Implicit_Waiting_Frequency = 0.5
    
    # 5.3 超过未加载等待时间是否抛出异常
    Implicit_Waiting_Throwing = False


    # 6. 注意：此方法是脚本执行入口
    def script_main(self):
        result = self.goto("https://baidu.com")
        print(result)

        # 6.1. 显示等待和隐式等待意思一样, 显示等待可以让你在某个局部代码中自定义设置等待时长
        # StartShowWait函数后的代码按照等待10秒，每个0.5秒重复加载，False找不到不抛出异常，此时你如果设置的全局隐式等待将不生效直到结束显示等待
        self.StartShowWait(10, 0.5, False)

        result = self.goto("https://qq.com")
        print(result)
        result = self.goto("https://www.hao123.com")
        print(result)

        # 6.1 结束显示等待,也是自定义结束局部等待此时如果设置的全局隐式等待后面的代码将按全局隐式等待的设置来执行
        self.EndShowWait()








if __name__ == '__main__':
    # 7. 启动脚本，监听 9999 号端口, 默认使用 Chrome 浏览器

    # 7.1. Debug=True 时，是本地运行脚本，会自动启动 WebDriver.exe 驱动
    # 7.2. 打开终端输入：start chrome.exe --remote-debugging-port=8989 即可创建一个8989的端口浏览器， "debugPort" 参数改为8989即可接管浏览器操作
    # 在远端部署脚本时，请设置 Debug=False，手动启动 WebDriver.exe，启动 WebDriver.exe 时需指定远端 IP 或端口号

    # 7.3. 如本地部署脚本，需要传递 WebDriver 启动参数时，参考下面方式，如不需传递启动参数，则忽略：
    driver_params = {
        "browserName": "chrome",
        "debugPort": 9999,
        "userDataDir": "./UserData",
        "browserPath": None,
        "argument": None,
    }

    CustomWebScript.execute("0.0.0.0", 9999, Debug=True, Driver_Params=driver_params)


