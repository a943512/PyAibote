import re


class WinHidCorrelation:
    """
        windows hid
        Windows hid correlation
    """

    def init_hid(self) -> bool:
        """
            初始化Hid
            Initialize Hid

            return: True或者False
            return: True or False
        """
        return "true" in self.SendData("initHid") 

    def get_hid_data(self) -> list:
        """
            获取Hid相关数据 先调用 windowsBot.initHid，再调用androidBot.initHid
            Call windowsbot. initHid before calling androidBot.initHid to obtain hid related data.

            return: 激活成功的hid手机的安卓ID
            return: Android ID of successfully activated hid mobile phone
        """
        response = self.SendData("getHidData")
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        if response == "":
            return []
        return response.split("|")

    def hid_press(self, android_id: str, angle: int, x: float, y: float) -> bool:
        """
            按下
            press

            android_id: 安卓id
            angle: 手机旋转角度
            x: 横坐标
            y: 纵坐标
            return: True或者False

            android_id: Android id
            angle: the rotation angle of mobile phone
            x: abscissa
            y: ordinate
            return: True or False
        """
        return "void" in self.SendData("hidPress", android_id, angle, x, y) 

    def hid_release(self, android_id: str, angle: int) -> bool:
        """
            释放
            release

            android_id: 安卓id
            angle: 手机旋转角度
            return: True或者False

            android_id: Android id
            angle: the rotation angle of mobile phone
            return: True or False
        """
        return "void" in self.SendData("hidRelease", android_id, angle) 

    def hid_move(self, android_id: str, angle: int, x: float, y: float, duration: float) -> bool:
        """
            移动
            move

            android_id: 安卓id
            angle: 手机旋转角度
            x: 横坐标
            y: 纵坐标
            duration: 移动时长,秒
            return: True或者False

            android_id: Android id
            angle: the rotation angle of mobile phone
            x: abscissa
            y: ordinate
            duration: moving duration, seconds
            return: True or False
        """
        return  "void" in self.SendData("hidMove", android_id, angle, x, y, duration * 1000) 

    def hid_click(self, android_id: str, angle: int, x: float, y: float) -> bool:
        """
            单击
            click

            android_id: 安卓id
            angle: 手机旋转角度
            x: 横坐标
            y: 纵坐标
            return: True或者False

            android_id: Android id
            angle: the rotation angle of mobile phone
            x: abscissa
            y: ordinate
            return: True or False
        """
        return "void" in self.SendData("hidClick", android_id, angle, x, y) 

    def hid_double_click(self, android_id: str, angle: int, x: float, y: float) -> bool:
        """
            双击
            double click

            android_id: 安卓id
            angle: 手机旋转角度
            x: 横坐标
            y: 纵坐标
            return: True或者False

            android_id: Android id
            angle: the rotation angle of mobile phone
            x: abscissa
            y: ordinate
            return: True or False
        """
        return "void" in self.SendData("hidDoubleClick", android_id, angle, x, y) 

    def hid_long_click(self, android_id: str, angle: int, x: float, y: float, duration: float) -> bool:
        """
            长按
            Long press

            android_id: 安卓id
            angle: 手机旋转角度
            x: 横坐标
            y: 纵坐标
            duration: 按下时长,秒
            return: True或者False

            android_id: Android id
            angle: the rotation angle of mobile phone
            x: abscissa
            y: ordinate
            duration: press duration, seconds
            return: True or False
        """
        return "void" in self.SendData("hidLongClick", android_id, angle, x, y, duration * 1000) 

    def hid_swipe(self, android_id: str, angle: int, startX: float, startY: float, endX: float, endY: float, duration: float) -> bool:
        """
            滑动坐标
            Sliding coordinate

            android_id: 安卓id
            angle: 手机旋转角度
            startX: 起始横坐标
            startY: 起始纵坐标
            endX: 结束横坐标
            endY: 结束纵坐标
            duration: 滑动时长,秒
            return: True或者False

            android_id: Android id
            angle: the rotation angle of mobile phone
            startX: starting abscissa
            startY: starting ordinate
            endX: end abscissa
            endY: end ordinate
            duration: sliding duration, seconds
            return: True or False
        """
        return "void" in self.SendData("hidSwipe", android_id, angle, startX, startY, endX, endY, duration * 1000) 

    def hid_gesture(self, android_id: str, angle: int, gesture_path: list, duration: float) -> bool:
        """
            Hid手势
            Hid gesture

            android_id: 安卓id
            angle: 手机旋转角度
            gesture_path: 手势路径，由一系列坐标点组成
            duration: 手势执行时长, 单位秒
            return: True或者False

            android_id: Android id
            angle: the rotation angle of mobile phone
            gesture_path: gesture path, which consists of a series of coordinate points
            duration: duration of gesture execution, in seconds
            return: True or False
        """
        gesture_path_str = ""
        for point in gesture_path:
            gesture_path_str += f"{point[0]}/{point[1]}/\n"
        gesture_path_str = gesture_path_str.strip()
        return "void" in self.SendData("hidDispatchGesture", android_id, angle, gesture_path_str, duration * 1000) 

    def hid_back(self, android_id: str) -> bool:
        """
            返回
            return

            android_id: 安卓id
            return: True或者False

            android_id: Android id
            return: True or False
        """
        return "void" in self.SendData("hidBack", android_id) 

    def hid_home(self, android_id: str) -> bool:
        """
            返回桌面
            home

            android_id: 安卓id
            return: True或者False

            android_id: Android id
            return: True or False
        """
        return "void" in self.SendData("hidHome", android_id) 

    def hid_recents(self, android_id: str) -> bool:
        """
            最近应用列表
            List of recent applications

            android_id: 安卓id
            return: True或者False

            android_id: Android id
            return: True or False
        """
        return "void" in self.SendData("hidRecents", android_id) 