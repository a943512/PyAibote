import re
import time


class WindowOperation:
    """
        窗口操作
        Window operation
    """

    def find_window(self, class_name: str = None, window_name: str = None) -> str:
        """
            查找窗口句柄，仅查找顶级窗口，不包含子窗口
            Find the window handle, only the top-level window, not the child window

            class_name: 窗口类名
            window_name: 窗口名
            return: 字符串

            class_name: Window class name
            window_name: Window name
            return: character string
        """
        response = self.SendData("findWindow", class_name, window_name)
        if response == "null":
            return None
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        return response

    def find_windows(self, class_name: str = None, window_name: str = None) -> str:
        """
            查找窗口句柄数组，仅查找顶级窗口，不包含子窗口 class_name 和 window_name 都为 None，则返回所有窗口句柄
            Find an array of window handles, only top-level windows are found, and all window handles are returned if class_name and window_name are None

            class_name: 窗口类名
            window_name: 窗口名
            return: 窗口句柄的列表

            class_name: Window class name
            window_name: Window name
            return: List of window handles
        """
        response = self.SendData("findWindows", class_name, window_name)
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        if response == "null":
            return []
        return response.split("|")

    def find_sub_window(self, hwnd: str, class_name: str = None, window_name: str = None) -> str:
        """
            查找子窗口句柄
            Find child window handle

            hwnd: 当前窗口句柄
            class_name: 窗口类名
            window_name: 窗口名
            return: 子窗口句柄或 None

            hwnd: Current window handle
            class_name: Window class name
            window_name: Window name
            return: Child window handle or None
        """
        response = self.SendData("findSubWindow", hwnd, class_name, window_name)
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        if response == "null":
            return None
        return response

    def find_parent_window(self, hwnd: str) -> str:
        """
            查找父窗口句柄
            Find the parent window handle

            hwnd: 当前窗口句柄
            return: 父窗口句柄或 None

            hwnd: Current window handle
            return: Parent window handle or None
        """
        response = self.SendData("findParentWindow", hwnd)
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        if response == "null":
            return None
        return response

    def find_desktop_window(self) -> str:
        """
            查找桌面窗口句柄
            Find the desktop window handle

            return: 桌面窗口句柄或None
            return: Desktop window handle or None
        """
        response = self.SendData("findDesktopWindow")
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        if response == "null":
            return None
        return response

    def get_window_name(self, hwnd: str) -> str:
        """
            获取窗口名称
            Get the window name

            hwnd: 当前窗口句柄
            return: 窗口名称或 None

            hwnd: Current window handle
            return: Window name or None
        """
        response = self.SendData("getWindowName", hwnd)
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        if response == "null":
            return None
        return response

    def show_window(self, hwnd: str, isShow: bool) -> bool:
        """
            显示/隐藏窗口
            Show/hide window

            hwnd: 当前窗口句柄
            isShow: 显示窗口 True 隐藏窗口 False
            return: 布尔值

            hwnd: Current window handle
            isShow: Show window True hide window False
            return: bool
        """
        return "true" in self.SendData("showWindow", hwnd, isShow)

    def get_window_pos(self, hwnd: str, wait_time: float = 5, interval_time: float = 0.5) -> dict:
        """
            获取窗口大小和位置
            Get the window size and location

            hwnd: 窗口句柄
            wait_time: 循环等待的总时间 默认5秒
            interval_time: 每隔多少时间重试一次 默认0.5
            return: left和top：windwos窗口最左侧为起点坐标，width和height：句柄窗口大小，或者超时返回 None

            hwnd: Window handle
            wait_time: Total time of loop waiting
            interval_time: How often do you try again
            return: The leftmost side of the windwos window is the starting point coordinates, width and height: handle window size, or return None
        """

        end_time = time.time() + wait_time
        while time.time() < end_time:
            response = self.SendData("getWindowPos", hwnd)
            if "/" in response:
                response = re.findall(r'/(.*)',response)[0]
            if response == "-1|-1|-1|-1":
                time.sleep(interval_time)
                continue
            else:
                x1, y1, x2, y2 = response.split("|")
                return {"left": x1, "top": y1, "width": x2, "height": y2}
        return None

    def set_window_pos(self, hwnd: str, left: float, top: float, width: float, height: float) -> bool:
        """
            设置窗口位置
            Set window position

            hwnd: 当前窗口句柄
            left: 左上角横坐标
            top: 左上角纵坐标
            width: 窗口宽度
            height: 窗口高度
            return: 布尔值

            hwnd: Current window handle
            left: Upper left abscissa
            top: Upper left ordinate
            width: Window width
            height: Window height
            return: bool
        """
        return "true" in self.SendData("setWindowPos", hwnd, left, top, width, height)

    def set_window_top(self, hwnd: str, top: bool) -> bool:
        """
            设置窗口到最顶层
            Set the window to the top level

            hwnd: 当前窗口句柄
            top: 是否置顶，True 置顶， False 取消置顶
            return: 布尔值

            hwnd: Current window handle
            top: Set top or not, True set top, False cancel set top
            return: bool
        """
        return "true" in self.SendData("setWindowTop", hwnd, top)

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