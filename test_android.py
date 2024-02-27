# 1. 导入 AndoridBotMain 类
from PyAibote import AndroidBotMain



# 2. 自定义一个脚本类，继承 AndoridBotMain
class CustomAndroidScript(AndroidBotMain):

    # 2. 设置是否终端打印输出 DEBUG：输出， INFO：不输出, 默认打印输出
    Log_Level = "DEBUG" 

    # 3. 终端打印信息是否存储LOG文件 True： 储存， False：不存储
    Log_Storage = True  


    # 4. 注意：script_main 此方法是脚本执行入口必须存在此方法
    def script_main(self):
        # 显示手机最近任务列表
        # Displays the list of recent tasks of the mobile phone
        result = self.recent_tasks()
        print(result)






if __name__ == '__main__':
    # 注意：此处监听的端口号，必须和手机端的脚本端口号一致
    # 监听 8888 号端口
    CustomAndroidScript.execute("0.0.0.0", 8888)