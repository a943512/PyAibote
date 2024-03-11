import time

class CoordinateOperation:
    """
        坐标操作
        Coordinate operation
    """

    def click(self, point: tuple) -> bool:
        """
            点击坐标
            Click coordinates

            point: x, y坐标
            return: Ture 或者 False

            point: coordinates
            return: Ture or False
        """
        return "true" in self.SendData("click", point[0], point[1])

    def double_click(self, point: tuple) -> bool:
        """
            双击坐标
            Double-click coordinates

            point: 坐标
            return: Ture 或者 False

            point: coordinates
            return: Ture or False
        """
        return "true" in self.SendData("doubleClick", point[0], point[1]) 

    def long_click(self, point: tuple, duration: int) -> bool:
        """
            长按坐标
            Long press coordinate

            point: 坐标
            duration: 按住时长，单位秒
            return: Ture 或者 False

            point: coordinates
            duration: press and hold time, in seconds
            return: Ture or False
        """
        return "true" in self.SendData("longClick", point[0], point[1], duration * 1000) 

    def swipe(self, start_point: tuple, end_point: tuple, duration: float) -> bool:
        """
            滑动坐标
            Sliding coordinate

            start_point: 起始坐标
            end_point: 结束坐标
            duration: 滑动时长，单位秒
            return: Ture 或者 False

            start_point: the starting coordinate
            end_point: end coordinate
            duration: sliding duration, in seconds
            return: Ture or False
        """
        return "true" in self.SendData("swipe", start_point[0], start_point[1], end_point[0], end_point[1], duration * 1000)

    def gesture(self, gesture_path: list, duration: float) -> bool:
        """
            执行手势
            Execute a gesture

            gesture_path: 手势路径，由一系列坐标点组成
            duration: 手势执行时长, 单位秒
            return: Ture 或者 False

            gesture_path: gesture path, which consists of a series of coordinate points
            duration: duration of gesture execution, in seconds
            return: Ture or False
        """

        gesture_path_str = ""
        for point in gesture_path:
            gesture_path_str += f"{point[0]}/{point[1]}/\n"
        gesture_path_str = gesture_path_str.strip()

        return "true" in self.SendData("dispatchGesture", gesture_path_str, duration * 1000) 

    def gestures(self, gestures_path: list) -> bool:
        """
            执行多个手势
            Perform multiple gestures

            [[duration, [x1, y1], [x1, y1]...],[duration, [x1, y1], [x1, y1]...]]  
            duration:手势执行时长, 单位秒
            [x1, y1]: 手势路径，由一系列坐标点组成
            return: Ture 或者 False

            [[duration, [x1, y1], [x1, y1]...],[duration, [x1, y1], [x1, y1]...]]
            duration: duration of gesture execution, in seconds.
            [x1, y1]: gesture path, which consists of a series of coordinate points.
            return: Ture or False
        """

        gestures_path_str = ""
        for gesture_path in gestures_path:
            gestures_path_str += f"{gesture_path[0] * 1000}/"
            for point in gesture_path[1:len(gesture_path)]:
                gestures_path_str += f"{point[0]}/{point[1]}/\n"
            gestures_path_str += "\r\n"
        gestures_path_str = gestures_path_str.strip()

        return "true" in self.SendData("dispatchGestures", gestures_path_str) 

    def press(self, point: tuple, duration: float) -> bool:
        """
            手指按下
            Finger press

            point: 坐标
            duration: 持续时间，单位秒
            return: Ture 或者 False

            point: coordinates
            duration: Duration, in seconds
            return: Ture or False
        """
        return "true" in self.SendData("press", point[0], point[1], duration * 1000) 

    def move(self, point: tuple, duration: float) -> bool:
        """
            手指移动
            Finger movement

            point: 坐标
            duration: 持续时间
            return: Ture 或者 False

            point: coordinates
            duration: duration
            return: Ture or False
        """
        return "true" in self.SendData("move", point[0], point[1], duration * 1000) 

    def release(self) -> bool:
        """
            手指抬起
            Finger lift
        """
        return "true" in self.SendData("release") 

    def press_release(self, point: tuple, duration: float) -> bool:
        """
            按下屏幕坐标点并释放
            Press the screen coordinate point and release it

            point: 按压坐标
            duration: 按压时长，单位秒
            return: Ture 或者 False

            point: press coordinates
            duration: duration of pressing, in seconds
            return: Ture or False
        """
        result = self.press(point, duration)
        if not result:
            return False
        time.sleep(duration)
        result2 = self.release()
        if not result2:
            return False
        return True

