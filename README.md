
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
    # 注意：此处监听的端口号，必须和手机端的脚本端口号一致
    # Note: The port number monitored here must be consistent with the script port number of the mobile phone.
    # 监听 8888 号端口
    # Listen to port 8888
    CustomAndroidScript.execute("0.0.0.0", 8888)
```
