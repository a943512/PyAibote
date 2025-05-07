# 1. 导入 HumanBotMain 类
# 1. Import HumanBotMain class
from PyAibote import HumanBotMain
import time,os


# 2. 自定义一个脚本类，继承 HumanBotMain
# 2. Customize a script class and inherit HumanBotMain.
class CustomWinScript(HumanBotMain):

    # 2.1. 设置是否终端打印输出 DEBUG：输出， INFO：不输出, 默认打印输出
    # 2.1. Set whether the terminal prints output DEBUG: output, INFO: no output, and print output by default.
    Log_Level = "DEBUG" 

    # 2.2. 终端打印信息是否存储LOG文件 True： 储存， False：不存储
    # 2.2. Does the terminal print information store the LOG file? True: yes, False: no.
    Log_Storage = True  


    # 2.3. 注意：script_main 此方法是脚本执行入口必须存在此方法
    # 2.3. Note: script_main This method must exist in the script execution portal.
    def script_main(self):

        # 初始化数字人
        self.init_new_metahuman(r"D:\Project\Aibote\2024-4-11\NewHuman\model", 0.5, False, False, "")

        # 切换数字人形象
        self.new_metahuman_switch_action(r"D:\Project\CompanyInformation\PaidItem\DigitalHuman\Static\Img\666.mp4", 0.5, False)

        # 添加数字人背景
        self.new_metahuman_add_background(r"D:\Project\CompanyInformation\PaidItem\DigitalHuman\Static\Backgroun\1.mp4")


        # 关闭驱动 方法一
        # os.popen('taskkill /f /t /im  "AiDriver.exe"')
        
        # 关闭驱动 方法二  终端直接输入
        # taskkill /f /t /im  "AiDriver.exe"



if __name__ == '__main__':
    # 3. IP为:0.0.0.0, 监听 9999 号端口
    # 3. IP: 0.0.0, listening to port 9999.
    # 3.1. 在远端部署脚本时，请设置 Debug=False，客户端手动启动 WindowsDriver.exe 时需指定远端 IP 或端口号
    # 3.1. When deploying the script remotely, please set Debug=False, and the client needs to specify the remote IP or port number when manually starting the WindowsDriver.exe.
    # 3.2. 命令行启动示例：AiDriver.exe "127.0.0.1" 9999 
    # 3.2. Command line startup example: AiDriver.exe "127.0.0.1" 9999 
    # 3.3 Qt 使用线程启动时传递的Qt对象用来和Qt UI窗口通信
    # 3.3 Qt Use the Qt object passed when the Qt thread starts to communicate with the Qt UI window
    CustomWinScript.execute("0.0.0.0", 9999, Debug=True, Qt = None)