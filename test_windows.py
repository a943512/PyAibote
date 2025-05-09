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




        # 关闭驱动 方法一  终端命令杀死驱动
        # self.close_driver_local()

        # 关闭驱动 方法二  驱动自动断开连接
        # self.close_driver()

        # 关闭驱动 方法三  终端命令杀死驱动
        # os.popen('taskkill /f /t /im  "WindowsDriver.exe"')
        
        # 关闭驱动 方法四  cmd终端直接输入杀死驱动
        # taskkill /f /t /im  "WindowsDriver.exe"



if __name__ == '__main__':
    # 3. IP为:0.0.0.0, 监听 9999 号端口
    # 3. IP: 0.0.0, listening to port 9999.
    # 3.1. 在远端部署脚本时，请设置 Debug=False，客户端手动启动 WindowsDriver.exe 时需指定远端 IP 或端口号
    # 3.1. When deploying the script remotely, please set Debug=False, and the client needs to specify the remote IP or port number when manually starting the WindowsDriver.exe.
    # 3.2. 命令行启动示例：WindowsDriver.exe "127.0.0.1" 9999 {'Name':'PyAibote'}
    # 3.2. Command line startup example: "127.0.0.1" 9999 {'Name':'PyAibote'}
    CustomWinScript.execute("0.0.0.0", 9999, Debug=True, Qt=None)