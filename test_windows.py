# 1. 导入 WinBotMain 类
from PyAibote import WinBotMain
import time,os

# 2. 自定义一个脚本类，继承 WinBotMain
class CustomWinScript(WinBotMain):

    # 2. 设置是否终端打印输出 DEBUG：输出， INFO：不输出, 默认打印输出
    Log_Level = "DEBUG" 

    # 3. 终端打印信息是否存储LOG文件 True： 储存， False：不存储
    Log_Storage = True  


    # 4. 注意：script_main 此方法是脚本执行入口必须存在此方法
    def script_main(self):
        # 查询所有窗口句柄
        # result = self.find_windows()
        # print(result)


        







# 5. 执行脚本，Pycharm 中，直接右键执行
if __name__ == '__main__':
    # IP为:0.0.0.0, 监听 9999 号端口
    # 在远端部署脚本时，请设置 Debug=False，客户端手动启动 WindowsDriver.exe 时需指定远端 IP 或端口号
    # 命令行启动示例：WindowsDriver.exe "192.168.1.88" 9999
    CustomWinScript.execute("0.0.0.0", 9999, Debug=True)