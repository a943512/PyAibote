import time
import re

class EquipmentOperation:
    """
         设备操作
         Equipment operation
    """

    def start_app(self, name: str, wait_time: float = 5, interval_time: float = 0.5) -> bool:
        """
            启动 APP
            Start APP

            name: APP名字或者包名
            wait_time: 等待时间，默认取 5秒
            interval_time: 轮询间隔时间，默认取 0.5秒
            return:成功返回True 失败返回False

            name: APP name or package name
            wait_time: waiting time, which is 5 seconds by default
            interval_time: the polling interval, which is 0.5 seconds by default
            return: Returns True successfully, and returns False if it fails
        """

        end_time = time.time() + wait_time
        while time.time() < end_time:
            response = self.SendData("startApp", name)
            if "false" in response or "null" in response:
                time.sleep(interval_time)
            else:
                return True
        return False

    def app_is_running(self, app_name: str) -> bool:
        """
            判断app是否正在运行(无障碍权限开启只判断前台，未开启则包含前后台 是否正在运行)
            Judge whether the app is running (if the barrier-free permission is enabled, only judge whether the foreground is running; if it is not enabled, it includes whether the foreground and background are running)

            return: 成功返回True 失败返回False
            return: Returns True successfully, and returns False if it fails
        """
        return "true" in self.SendData("appIsRunnig", app_name) 

    def get_installed_packages(self) -> list:
        """
            获取已安装app的包名(不包含系统APP)
            Gets the package name of the installed APP (excluding the system app)

            return: 包名列表 或者 空[]
            return: The package name list is either empty []
        """
        resp = self.SendData("getInstalledPackages")
        if resp == "null" or resp == "":
            return []
        return resp.split("|")

    def get_title(self) -> str:
        """
            获取投屏标题
            Get the title of the projection screen

            return: app上的标题信息
            return: Title information on the app
        """
        response = self.SendData("getTitle")
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        return response

    def get_group(self) -> str:
        """
            获取投屏组号
            Get the projection group number

            return: app上的投屏组号
            return: Projection group number on the app
        """
        response = self.SendData("getGroup")
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        return response

    def get_identifier(self) -> str:
        """
            获取投屏编号
            Get the projection number

            return: app上的投屏编号
            return: Projection number on the app
        """
        response = self.SendData("getIdentifier")
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        return response

    def activate_frame(self, secret_key) -> bool:
        """
            激活安卓框架
            Activate Android framework

            secret_key：激活框架的秘钥
            secret_key：Key to activate the frame

            return: 成功返回True失败返回False
            return: Returns True successfully and False if it fails
        """
        response = self.SendData("activateFrame", secret_key) 
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        return response
    def get_device_ip(self) -> str:
        """
            获取设备IP地址
            Get the device IP address

            return: 设备IP地址字符串
            return: device IP address string
        """
        return self.client_address[0]

    def get_android_id(self) -> str:
        """
            获取 Android 设备 ID
            Get AndroID device id

            return: Android 设备 ID 字符串
            return: AndroID device id string
        """
        response = self.SendData("getAndroidId")
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        return response

    def get_window_size(self) -> dict:
        """
            获取屏幕大小
            Get the screen size

            return: 屏幕大小, 字典格式
            return: screen size, dictionary format
        """
        response = self.SendData("getWindowSize")
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        width, height = response.split("|")
        return {"width": float(width), "height": float(height)}

    def get_image_size(self, image_path: str) -> dict:
        """
            获取图片大小
            Get the picture size

            image_path: 图片路径
            return: 图片大小, 字典格式, 失败返回 {'width': -1.0, 'height': -1.0}

            image_path: image path
            return: picture size, dictionary format
        """
        if not image_path.startswith("/storage/emulated/0/"):
            image_path = "/storage/emulated/0/" + image_path
        response = self.SendData("getImageSize", image_path)
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        width, height = response.split("|")
        return {"width": float(width), "height": float(height)}

    def show_toast(self, text: str, duration: float = 3) -> bool:
        """
            Toast 弹窗
            Toast popup window

            text: 弹窗内容
            duration: 弹窗持续时间默认3秒
            return: 成功返回True 失败返回False

            text: pop-up contents
            duration: The default duration of pop-up window is 3 seconds
            return: Returns True successfully, and returns False if it fails
        """
        return "true" in self.SendData("showToast", text, duration * 1000) 

    def send_keys(self, text: str) -> bool:
        """
            发送文本，需要打开 AiBot 输入法
            To send text, you need to open the AiBot input method

            text: 文本内容
            return:  成功返回True 失败返回False

            text: text content
            return: Returns True successfully, and returns False if it fails
        """
        return "true" in self.SendData("sendKeys", text)  

    def send_vk(self, vk: int) -> bool:
        """
            发送 vk , 需要打开 AiBot 输入法
            Send vk

            vk: 虚拟键值
            return: 成功返回True 失败返回False

            虚拟键值按键对照表 https://blog.csdn.net/yaoyaozaiye/article/details/122826340
        """
        return "true" in self.SendData("sendVk", vk) 

    def back(self) -> bool:
        """
            返回
            return

            return: 成功返回True 失败返回False
            return: Returns True successfully, and returns False if it fails
        """
        return "true" in self.SendData("back") 
    
    def home(self) -> bool:
        """
            返回桌面
            Back to the desktop

            return: 成功返回True 失败返回False
            return: Returns True successfully, and returns False if it fails
        """
        return "true" in self.SendData("home") 

    def recent_tasks(self) -> bool:
        """
            显示最近任务
            Show recent tasks

            return: 成功返回True 失败返回False
            return: Returns True successfully, and returns False if it fails
        """
        return "true" in self.SendData("recents")

    def power_dialog(self) -> bool:
        """
            打开 开/关机 对话框，基于无障碍权限
            Open the on/off dialog box, based on accessibility rights

            return:成功返回True 失败返回False
            return: Returns True successfully, and returns False if it fails
        """
        return "true" in self.SendData("powerDialog") 

    def call_phone(self, mobile: str) -> bool:
        """
            拨打电话
            dial

            mobile: 手机号码
            return: 成功返回True 失败返回False

            mobile: mobile phone number
            return: Returns True successfully, and returns False if it fails
        """
        return "true" in self.SendData("callPhone", mobile) 

    def send_msg(self, mobile, text) -> bool:
        """
            发送短信
            send a text message

            mobile: 手机号码
            text: 短信内容
            return: 成功返回True 失败返回False

            mobile: mobile phone number
            text: short message content
            return: Returns True successfully, and returns False if it fails
        """
        return "true" in self.SendData("sendMsg", mobile, text)  

    def get_activity(self) -> str:
        """
            获取活动页
            Get active page

            return: 当前的窗口UI名称
            return: the current UI name of the window
        """
        response = self.SendData("getActivity")
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        return response

    def get_package(self) -> str:
        """
            获取包名
            Get package name

            return: 包名称："com.aibot.client"
            return: package name: "com.aibot.client"
        """
        response = self.SendData("getPackage")
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        return response

    def set_clipboard_text(self, text: str) -> bool:
        """
            设置剪切板文本
            Set clipboard text

            text: 文本
            return: 成功返回True 失败返回False

            text: text
            return: Returns True successfully, and returns False if it fails
        """
        return "true" in self.SendData("setClipboardText", text)

    def get_clipboard_text(self) -> str:
        """
            获取剪切板内容（需要开启Aibote输入法）
            Get the clipboard content

            return: 剪切板内容
            return: Clipboard content
        """
        response = self.SendData("getClipboardText")
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        return response

    def start_activity(self, action: str, uri: str = '', package_name: str = '', class_name: str = '', typ: str = '') -> bool:
        """
            Intent 跳转
            Intent jump

            action: 动作，例如 "android.intent.action.VIEW"
            uri: 跳转链接，例如：打开支付宝扫一扫界面，"alipayqr://platformapi/startapp?saId=10000007"
            package_name: 包名，"com.xxx.xxxxx"
            class_name: 类名
            typ: 类型
            return: True或者 False

            action: Action, such as "android.intent.action.VIEW"
            uri: jump link, for example: open Alipay scan interface, "AlipayQR://PlatformAPI/startapp? saId=10000007"
            package_name: package name, "com.xxx.xxxxx"
            class_name: class name
            typ: type
            return: True or False
        """
        return "true" in self.SendData("startActivity", action, uri, package_name, class_name, typ) 

    def write_android_file(self, remote_path: str, text: str, append: bool = False) -> bool:
        """
            写入安卓文件 
            Write to Android file

            remote_path: 安卓文件默认根目录:/storage/emulated/0/,  文件名必须是.txt后缀结
            text: 写入的内容
            append: 可选参数，是否追加，默认覆盖文件内容
            return: True 或者 False

            remote_path: Android file path /storage/emulated/0/: Android file root directory
            text: the text content to be written
            append: Whether to append the pattern
            return: True or False
        """
        if not remote_path.endswith(".txt"):
            raise TypeError("文件必须是.txt后缀结尾")

        if not remote_path.startswith("/storage/emulated/0/"):
            remote_path = "/storage/emulated/0/" + remote_path
        return "true" in self.SendData("writeAndroidFile", remote_path, text, append)

    def read_android_file(self, remote_path: str) -> str:
        """
            读取安卓文件 
            Read Android file

            remote_path: 安卓文件路径 /storage/emulated/0/: 安卓文件根目录
            return: 文件内容

            remote_path: Android file path /storage/emulated/0/: Android file root directory
            return: file content
        """
        if not remote_path.startswith("/storage/emulated/0/"):
            remote_path = "/storage/emulated/0/" + remote_path

        response = self.SendData("readAndroidFile", remote_path)
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        if response == "null":
            return None
        return response

    def exists_android_file(self, remote_path: str) -> bool:
        """
            安卓文件是否存在
            Does the Android file exist

            remote_path: 安卓文件路径
            return: 存在返回True 不存在返回False

            Remote_path: Android file path
            Return: existence returns True; non-existence returns False
        """
        if not remote_path.startswith("/storage/emulated/0/"):
            remote_path = "/storage/emulated/0/" + remote_path

        return "true" in self.SendData("existsAndroidFile", remote_path)

    def get_android_sub_files(self, android_directory: str = "") -> list:
        """
            获取文件夹内的所有文件(不包含深层子目录)
            Get all files in the folder (excluding deep subdirectories)

            android_directory: 安卓目录,默认为根目录下所有文件名
            return: 文件名列表

            android_directory: Android directory, which defaults to all file names in the root directory
            return: list of file names
        """
        if not android_directory.startswith("/storage/emulated/0/"):
            android_directory = "/storage/emulated/0/" + android_directory

        response = self.SendData("getAndroidSubFiles", android_directory)
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        if response == "null" or response == "":
            return []
        return response.split("|")

    def make_android_dir(self, android_directory: str) -> bool:
        """
            创建安卓文件夹
            Create Android folder

            android_directory: 安卓目录 /storage/emulated/0/: 安卓文件根目录
            return: 成功返回True 失败返回False

            android_directory: Android directory  /storage/emulated/0/: Android file root directory
            return: existence returns True; non-existence returns False
        """
        if not android_directory.startswith("/storage/emulated/0/"):
            android_directory = "/storage/emulated/0/" + android_directory
        return "true" in self.SendData("makeAndroidDir", android_directory) 

    def delete_android_file(self, remote_path: str) -> bool:
        """
            删除安卓文件
            Delete Android files

            remote_path: 安卓文件路径
            return: 成功返回True 失败返回False

            remote_path: Android file path.
            return: Returns True successfully, and returns False if it fails
        """
        if not remote_path.startswith("/storage/emulated/0/"):
            remote_path = "/storage/emulated/0/" + remote_path
        return "true" in self.SendData("deleteAndroidFile", remote_path) 

    def coordinate_transform(self, coordinate: tuple, resolution_a: tuple, resolution_b: tuple) -> tuple:
        """
            根据屏幕分辨率缩放比例，进行不同分辨率坐标转换
            According to the screen resolution scaling, coordinate conversion with different resolutions is carried out.

            coordinate: 需要装换的坐标可以是x,y坐标，也可以是矩形坐标 x1, y1, x2, y2
            resolution_a: 你抓取过坐标的设备标准分辨率
            resolution_b：你需要转换的设备分辨率
            retrun: 元祖

            coordinate: the coordinates to be replaced can be x,y coordinates or rectangular coordinates x1, y1, x2, y2
            resolution_a: The standard resolution of the device for which you have grabbed the coordinates
            resolution_b: The device resolution you need to convert
            retrun: Yuanzu
        """
        
        def convert_coordinates(x, y, resolution_a, resolution_b):
            W_A, H_A = resolution_a  
            W_B, H_B = resolution_b 
            

            scale_x = W_B / W_A
            scale_y = H_B / H_A
            

            x_b = x * scale_x
            y_b = y * scale_y
            
            return (x_b, y_b)

        if len(coordinate) == 2:
            result = convert_coordinates(coordinate[0], coordinate[1], resolution_a, resolution_b)
            return result

        if len(coordinate) == 4:
            result = convert_coordinates(coordinate[0], coordinate[1], resolution_a, resolution_b)
            result2 = convert_coordinates(coordinate[2], coordinate[3], resolution_a, resolution_b)
            return (result[0], result[1], result2[0], result2[1])
        return ()

    def close_driver(self):
        """
            关闭连接
            Close the connection
        """
        self.SendData("closeDriver")

