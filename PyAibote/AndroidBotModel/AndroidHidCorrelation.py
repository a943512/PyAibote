import re




class AndroidHidCorrelation:
    """
        hid相关
        Hid correlation
    """

    def __init_accessory(self) -> bool:
        """
            初始化 android Accessory，获取手机 hid 相关的数据
            Initialize android Accessory to get the data related to mobile phone hid

            return: True或者False
            return: True or False.
        """
        return "true" in self.SendData("initAccessory") 

    def init_hid(self, win_driver) -> bool:
        """
            初始化Hid,不能重复调用，重复调用会导致get_hid_data取不到数据
            Initialize Hid, and you can't call it repeatedly. Repeated calls will cause get_hid_data to get no data
            
            hid实际上是由windowsBot 通过数据线直接发送命令给安卓系统并执行，并不是由aibote.apk执行的命令。
            我们应当将所有设备准备就绪再调用此函数初始化。
            Windows initHid 和 android initAccessory函数 初始化目的是两者的数据交换，并告知windowsBot发送命令给哪台安卓设备
            win_driver: windowsDriver 实例，是调用 build_win_driver 的返回值
            return: True或者False

            In fact, hid is a command directly sent by windowsBot to Android system through data line and executed, not by aibote.apk
            We should get all the devices ready before calling this function to initialize
            The initialization purpose of Windows initHid and android initAccessory functions is to exchange data between them and tell windowsBot which Android device to send commands to
            Win_driver: windowsDriver instance, which is the return value of calling build_win_driver
            return: True or False
        """
        
        self.android_id = self.get_android_id()
        self.win_driver = win_driver
        if not self.win_driver:
            return False
        if not self.__init_accessory():
            return False
        self.android_ids = self.win_driver.get_hid_data()
        
        for android_id in self.android_ids:
            if android_id == self.android_id:
                return True
        return False

    def get_rotation_angle(self) -> int:
        """
            获取手机旋转角度
            Get the rotation angle of the mobile phone

            return: 手机旋转的角度
            return: the angle at which the phone rotates.
        """
        response = self.SendData("getRotationAngle")
        return int(response)

    def hid_press(self, coordinate: tuple) -> bool:
        """
            按下
            press

            coordinate: x,y坐标
            return: True或者False

            coordinate x, y: abscissa
            return: True or False
        """
        self.angle = self.get_rotation_angle()
        return  self.win_driver.hid_press(self.android_id, self.angle, coordinate[0], coordinate[1]) 

    def hid_release(self) -> bool:
        """
            释放
            release

            return: True或者False
            return: True or False.
        """
        self.angle = self.get_rotation_angle()
        return self.win_driver.hid_release(self.android_id, self.angle) 

    def hid_move(self, coordinate: tuple, duration: float) -> bool:
        """
            移动
            move

            coordinate: x,y坐标
            duration: 移动时长,秒(移动时间内脚本需保持运行)
            return: True或者False

            coordinate: x,y coordinates
            duration: moving duration, seconds (the script should be kept running during the moving time)
            return: True or False
        """
        self.angle = self.get_rotation_angle()
        return self.win_driver.hid_move(self.android_id, self.angle, coordinate[0], coordinate[1], duration) 

    def hid_click(self, coordinate: tuple) -> bool:
        """
            单击
            click

            coordinate: x, y横坐标
            return: True或者False

            coordinate: x, y abscissa
            return: True or False
        """
        self.angle = self.get_rotation_angle()
        return self.win_driver.hid_click(self.android_id, self.angle, coordinate[0], coordinate[1]) 

    def hid_double_click(self, coordinate: tuple) -> bool:
        """
            双击
            double click

            coordinate: x,y横坐标
            return: True或者False

            coordinate: x,y abscissa
            return: True or False
        """
        self.angle = self.get_rotation_angle()
        return self.win_driver.hid_double_click(self.android_id, self.angle, coordinate[0], coordinate[1]) 

    def hid_long_click(self, coordinate: tuple, duration: float) -> bool:
        """
            长按
            Long press

            coordinate: x,y坐标
            duration: 按下时长,秒(按下时间内脚本需保持运行)
            return: True或者False

            coordinate: x,y coordinates
            duration: press duration, seconds (the script should be kept running during the press duration)
            return: True or False
        """
        self.angle = self.get_rotation_angle()
        return  self.win_driver.hid_long_click(self.android_id, self.angle, coordinate[0], coordinate[1], duration) 

    def hid_swipe(self, Startcoordinate: tuple,Endcoordinate: tuple, duration: float) -> bool:
        """
            滑动坐标
            Sliding coordinate

            Startcoordinate: x,y 起始坐标
            Endcoordinate: x,y 结束坐标
            duration: 滑动时长,秒(滑动时间内脚本需保持运行)
            return: True或者False

            Startcoordinate: x,y start coordinate
            Endcoordinate: x,y end coordinate
            duration: sliding duration, seconds (the script needs to be kept running during sliding time)
            return: True or False
        """
        self.angle = self.get_rotation_angle()
        return self.win_driver.hid_swipe(self.android_id, self.angle, Startcoordinate[0], Startcoordinate[1], Endcoordinate[0], Endcoordinate[1], duration) 

    def hid_gesture(self, gesture_path: list, duration: float) -> bool:
        """
            Hid手势
            Hid gesture

            gesture_path: 手势路径，由一系列坐标点组成
            duration: 手势执行时长, 单位秒(执行时间内脚本需保持运行)
            return: True或者False

            gesture_path: gesture path, which consists of a series of coordinate points
            duration: the duration of gesture execution, in seconds (the script should be kept running during the execution time)
            return: True or False
        """
        self.angle = self.get_rotation_angle()
        return self.win_driver.hid_gesture(self.android_id, self.angle, gesture_path, duration) 

    def hid_back(self) -> bool:
        """
            返回
            return
        """

        return self.win_driver.hid_back(self.android_id) 

    def hid_home(self) -> bool:
        """
            返回桌面
            home
        """
        return self.win_driver.hid_home(self.android_id) 

    def hid_recents(self) -> bool:
        """
            最近应用列表
            List of recent applications
        """
        return self.win_driver.hid_recents(self.android_id) 