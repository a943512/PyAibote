import re
import time,json


class ElementOperation:
    """
        元素操作
        Element operation
    """

    def get_element_name(self, hwnd: str, xpath: str, wait_time: float = 5, interval_time: float = 0.5) -> str:
        """
            获取元素名称
            Get the element name

            hwnd: 窗口句柄
            xpath: 元素路径
            wait_time: 等待时间，默认取 5秒
            interval_time: 轮询间隔时间，默认 0.5秒
            return: 元素名称字符串或 None
        
            hwnd: window handle
            xpath: element path
            wait_time: waiting time, which is 5 seconds by default
            interval_time: the polling interval, which is 0.5 seconds by default
            return: element name string or None
        """

        end_time = time.time() + wait_time
        while time.time() < end_time:
            response = self.SendData("getElementName", hwnd, xpath)
            if response == "null":
                time.sleep(interval_time)
                continue
            else:
                return response
        return None

    def get_element_value(self, hwnd: str, xpath: str, wait_time: float = 5, interval_time: float = 0.5) -> str:
        """
            获取元素文本(可编辑的那种文本)
            Gets the element text (editable text)

            hwnd: 窗口句柄
            xpath: 元素路径
            wait_time: 等待时间，默认取 5秒
            interval_time: 轮询间隔时间，默认取 0.5秒
            return: 元素文本字符串或 None

            hwnd: window handle
            xpath: element path
            wait_time: waiting time, which is 5 seconds by default
            interval_time: the polling interval, which is 0.5 seconds by default
            return: element text string or None
        """
        end_time = time.time() + wait_time
        while time.time() < end_time:
            response = self.SendData("getElementValue", hwnd, xpath)
            if response == "null":
                time.sleep(interval_time)
                continue
            else:
                return response
        return None

    def get_element_rect(self, hwnd: str, xpath: str, wait_time: float = 5, interval_time: float = 0.5) -> tuple:
        """
            获取元素矩形，返回左上和右下坐标
            Gets an element rectangle and returns the upper left and lower right coordinates.

            hwnd: 窗口句柄
            xpath: 元素路径
            wait_time: 等待时间，默认取 self.wait_timeout；
            interval_time: 轮询间隔时间，默认取 self.interval_timeout；
            return: 左上和右下坐标

            hwnd: window handle
            xpath: element path
            wait_time: the waiting time, which defaults to self. wait _ timeout
            interval_time: polling interval; self. interval _ timeout is selected by default
            return: upper left and lower right coordinates

        """
        if wait_time is None:
            wait_time = self.wait_timeout

        if interval_time is None:
            interval_time = self.interval_timeout

        end_time = time.time() + wait_time
        while time.time() < end_time:
            response = self.SendData("getElementRect", hwnd, xpath)
            if response == "-1|-1|-1|-1":
                time.sleep(interval_time)
                continue
            else:
                x1, y1, x2, y2 = response.split("|")
                return ((float(x2)+float(x1))/2,(float(y2)+float(y1))/2)
        return ()

    def get_element_window(self, hwnd: str, xpath: str, wait_time: float = 5, interval_time: float = 0.5) -> str:
        """
            获取元素窗口句柄
            Get the element window handle

            hwnd: 窗口句柄
            xpath: 元素路径
            wait_time: 等待时间，默认取 5秒
            interval_time: 轮询间隔时间，默认取 0.5秒
            return: 元素窗口句柄字符串或 None

            hwnd: window handle
            xpath: element path
            Wait_time: waiting time, which is 5 seconds by default
            interval_time: the polling interval, which is 0.5 seconds by default
            return: element window handle string or None
        """

        end_time = time.time() + wait_time
        while time.time() < end_time:
            response = self.SendData("getElementWindow", hwnd, xpath)
            if response == "null":
                time.sleep(interval_time)
                continue
            else:
                return response
        return None

    def click_element(self, hwnd: str, xpath: str, typ: int, wait_time: float = 5, interval_time: float = 0.5) -> bool:
        """
            点击元素
            Click element

            hwnd: 窗口句柄
            xpath: 元素路径
            typ: 操作类型，单击左键:1 单击右键:2 按下左键:3 弹起左键:4 按下右键:5 弹起右键:6 双击左键:7 双击右键:8
            wait_time: 等待时间，默认取 5秒
            interval_time: 轮询间隔时间，默认取 0.5秒
            return:  成功返回True 失败返回 False

            hwnd: window handle
            xpath: element path
            typ: operation type, click left key: 1 click right key: 2 press left key: 3 popup left key: 4 press right key: 5 popup right key: 6 double-click left key: 7 double-click right key: 8
            wait_time: waiting time, which is 5 seconds by default
            interval_time: the polling interval, which is 0.5 seconds by default
            return: Returns True successfully, and returns False if it fails
        """

        end_time = time.time() + wait_time
        while time.time() < end_time:
            response = self.SendData('clickElement', hwnd, xpath, typ)
            if response == "false":
                time.sleep(interval_time)
                continue
            else:
                return True
        return False

    def invoke_element(self, hwnd: str, xpath: str, wait_time: float = 5, interval_time: float = 0.5) -> bool:
        """
            执行元素默认操作(一般是点击操作)
            Perform the default operation of the element (generally click operation)

            hwnd: 窗口句柄
            xpath: 元素路径
            wait_time: 等待时间，默认取 self.wait_timeout；
            interval_time: 轮询间隔时间，默认取 self.interval_timeout；
            return: 成功返回True 失败返回 False

            hwnd: window handle
            xpath: element path
            wait_time: the waiting time, which defaults to self. wait _ timeout
            interval_time: polling interval; self. interval _ timeout is selected by default
            return: Returns True successfully, and returns False if it fails
        """

        end_time = time.time() + wait_time
        while time.time() < end_time:
            response = self.SendData('invokeElement', hwnd, xpath)
            if response == "false":
                time.sleep(interval_time)
                continue
            else:
                return True
        return False

    def set_element_focus(self, hwnd: str, xpath: str, wait_time: float = 5, interval_time: float = 0.5) -> bool:
        """
            设置元素作为焦点
            Set element as focus

            hwnd: 窗口句柄
            xpath: 元素路径
            wait_time: 等待时间，默认取 5秒
            param interval_time: 轮询间隔时间，默认取 0.5秒
            return: 成功返回True 失败返回 False

            hwnd: window handle
            xpath: element path
            wait_time: waiting time, which is 5 seconds by default
            param interval_time: polling interval, which is 0.5 seconds by default
            return: Returns True successfully, and returns False if it fails
        """

        end_time = time.time() + wait_time
        while time.time() < end_time:
            response = self.SendData('setElementFocus', hwnd, xpath)
            if response == "false":
                time.sleep(interval_time)
                continue
            else:
                return True
        return False

    def set_element_value(self, hwnd: str, xpath: str, value: str, wait_time: float = 5, interval_time: float = 0.5) -> bool:
        """
            设置元素文本
            Set element text

            hwnd: 窗口句柄
            xpath: 元素路径
            value: 要设置的内容
            wait_time: 等待时间，默认取 5秒
            interval_time: 轮询间隔时间，默认取 0.5秒
            return: 成功返回True 失败返回 False

            hwnd: window handle
            xpath: element path
            value: what to set.
            wait_time: waiting time, which is 5 seconds by default
            interval_time: the polling interval, which is 0.5 seconds by default
            return: Returns True successfully, and returns False if it fails
        """
        end_time = time.time() + wait_time
        while time.time() < end_time:
            response = self.SendData('setElementValue', hwnd, xpath, value)
            if response == "false":
                time.sleep(interval_time)
                continue
            else:
                return True
        return False

    def scroll_element(self, hwnd: str, xpath: str, horizontal: int= -1, vertical: int = -1, wait_time: float = 5, interval_time: float = 0.5) -> bool:
        """
            滚动元素
            Rolling element

            hwnd: 窗口句柄
            xpath: 元素路径
            horizontal: 水平百分比 -1不滚动
            vertical: 垂直百分比 -1不滚动
            wait_time: 等待时间，默认取 5秒
            interval_time: 轮询间隔时间，默认取 0.5秒
            return: 成功返回True 失败返回 False

            hwnd: window handle
            xpath: element path
            horizontal: horizontal percentage -1 does not scroll
            vertical: vertical percentage -1 does not scroll
            wait_time: waiting time, which is 5 seconds by default
            interval_time: the polling interval, which is 0.5 seconds by default
            return: Returns True successfully, and returns False if it fails
        """

        end_time = time.time() + wait_time
        while time.time() < end_time:
            response = self.SendData('setElementScroll', hwnd, xpath, horizontal, vertical)
            if response == "false":
                time.sleep(interval_time)
                continue
            else:
                return True
        return False

    def is_selected(self, hwnd: str, xpath: str, wait_time: float = 5, interval_time: float = 0.5) -> bool:
        """
            单/复选框是否选中
            Is the single/check box selected

            hwnd: 窗口句柄
            xpath: 元素路径
            wait_time: 等待时间， 默认取 5秒
            interval_time: 轮询间隔时间，默认取 0.5秒
            return:  成功返回True 失败返回 False

            Hwnd: window handle
            Xpath: element path
            Wait_time: waiting time, which is 5 seconds by default
            Interval_time: the polling interval, which is 0.5 seconds by default
            Return: Returns True successfully, and returns False if it fails
        """
        end_time = time.time() + wait_time
        while time.time() < end_time:
            response = self.SendData('isSelected', hwnd, xpath)
            if response == "false":
                time.sleep(interval_time)
                continue
            else:
                return True
        return False

    def close_window(self, hwnd: str, xpath: str) -> bool:
        """
            关闭窗口
            Close the window

            hwnd: 窗口句柄
            xpath: 元素路径
            return:  成功返回True 失败返回 False

            hwnd: window handle
            xpath: element path
            return: Returns True successfully, and returns False if it fails
        """
        return "true" in self.SendData('closeWindow', hwnd, xpath) 

    def set_element_state(self, hwnd: str, xpath: str, state: str) -> bool:
        """
            设置窗口状态
            Set window state

            hwnd: 窗口句柄
            xpath: 元素路径
            state: 0正常 1最大化 2 最小化
            return:  成功返回True 失败返回 False

            hwnd: window handle
            xpath: element path
            state: 0 Normal 1 Maximize 2 Minimize
            return: Returns True successfully, and returns False if it fails
        """
        return "true" in self.SendData('setWindowState', hwnd, xpath, state)
    
    def get_elements(self, hwnd) -> json:
        """
            获取可见区域内的所有元素信息
            Get information of all elements in the visible area

            hwnd: 窗口句柄
            return: 成功返回数组json格式的元素信息，失败返回null

            hwnd: window handle
            return: element information in json format of array is returned successfully, and null is returned if it fails
        """
        response = self.SendData("getElements", hwnd)
        if response == "null":
            return None
        return json.loads(response)