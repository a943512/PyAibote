# 1. 导入 AndroidBotMain 类
# 1. Import AndroidBotMain class
from PyAibote import AndroidBotMain
import time


# 2. 自定义一个脚本类，继承 AndroidBotMain
# 2. Customize a script class and inherit AndroidBotMain
class CustomAndroidScript(AndroidBotMain):

    # 2.1. 设置是否终端打印输出 DEBUG ：输出， INFO ：不输出, 默认打印输出
    # 2.1. Set whether the terminal prints output DEBUG: output, INFO: no output, and print output by default
    Log_Level = "DEBUG" 
    Websocket_Log_Level = "DEBUG"

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


        # 主函数死循环时手机app连接断开异常捕获跳出死循环demo示例代码
        # while True:
        #     try:
        #         # 死循环中必须加入aibote函数代码
        #         self.get_installed_packages()
        #         print("我是个死循环")       
        #         time.sleep(2)

        #     # 服务端捕获客户端断开异常跳出线程循环结束连接
        #     except OSError as e:
        #         break
            
        #     # 捕获其他非连接断开异常
        #     except Exception as e:
        #         print(e)





if __name__ == '__main__':
    # 3. 注意：此处监听的端口号，必须和手机端的脚本端口号一致
    # 3. Note: The port number monitored here must be consistent with the script port number of the mobile phone.
    # 3.1 监听 9999 号端口
    # 3.1 Listening to Port 9999
    CustomAndroidScript.execute("0.0.0.0", 9999, Qt=None, WebsocketSwitch=False, WebsocketPort=8888)