import re
import time


class ElementOperation:
    """
        元素操作
        Element operation
    """
    
    def get_element_rect(self, xpath: str, wait_time: float = 5, interval_time: float = 0.5) -> tuple:
        """
            获取元素位置，返回元素区域左上角和右下角坐标
            Gets the position of the element and returns the coordinates of the upper left corner and the lower right corner of the element area

            xpath: xpath 路径
            wait_time: 等待时间，默认取 5秒
            interval_time: 轮询间隔时间，默认取 0.5秒
            return: x,y坐标 或者 空()

            xpath: xpath path
            wait_time: waiting time, which is 5 seconds by default
            interval_time: the polling interval, which is 0.5 seconds by default
            return: x,y coordinates or empty ()
        """

        end_time = time.time() + wait_time
        while time.time() < end_time:
            response = self.SendData("getElementRect", xpath)

            if response == "-1|-1|-1|-1":
                time.sleep(interval_time)
            else:
                start_x, start_y, end_x, end_y = response.split("|")
                return ((float(end_x)+float(start_x))/2,(float(end_y)+float(start_y))/2)

        return ()

    def press_release_by_ele(self, xpath, duration: float, wait_time: float = 5, interval_time: float = 0.5) -> bool:
        """
            按压元素并释放
            Press the element and release.

            xpath: 要按压的元素
            duration: 按压时长，单位秒
            wait_time: 查找元素的最长等待时间 默认5秒
            interval_time: 查找元素的轮询间隔时间 默认0.5
            return: Ture 或者 False

            xpath: the element to press
            duration: duration of pressing, in seconds
            wait_time: The longest waiting time for finding an element defaults to 5 seconds
            interval_time: The polling interval of the lookup element defaults to 0.5
            return: Ture or False
        """
        response = self.get_element_rect(xpath, wait_time=wait_time, interval_time=interval_time)
        if response:
            return self.press_release(response, duration)
        else:
            return False

    def get_element_desc(self, xpath: str, wait_time: float = 5, interval_time: float = 0.5) -> str:
        """
            获取元素描述
            Get element description

            xpath: xpath 路径
            wait_time: 等待时间，默认取 5秒
            interval_time: 轮询间隔时间，默认取 
            return: 元素描述字符串

            xpath: xpath path
            wait_time: the waiting time, which is self.wait_timeout by default to 5 seconds
            interval_time: polling interval; self.interval_timeout is selected by default to 0.5
            return: element description string 
        """

        end_time = time.time() + wait_time
        while time.time() < end_time:
            response = self.SendData("getElementDescription", xpath)

            if response == "null":
                time.sleep(interval_time)
            else:
                return response
        return None

    def get_element_text(self, xpath: str, wait_time: float = 5, interval_time: float = 0.5) -> str:
        """
            获取元素文本
            Get element text

            xpath: xpath 路径
            wait_time: 等待时间，默认取 5秒
            interval_time: 轮询间隔时间，默认取 0.5秒
            return: 元素文本

            xpath: xpath path
            wait_time: waiting time, which is 5 seconds by default.
            interval_time: the polling interval, which is 0.5 seconds by default.
            return: element text
        """

        end_time = time.time() + wait_time
        while time.time() < end_time:
            response = self.SendData("getElementText", xpath)

            if response == "null":
                time.sleep(interval_time)
            else:
                return response
        return None

    def set_element_text(self, xpath: str, text: str, wait_time: float = 5, interval_time: float = 0.5) -> bool:
        """
            设置元素文本
            Set element text

            xpath: 元素路径
            text: 设置的文本
            wait_time: 等待时间，默认取 self.wait_timeout
            interval_time: 轮询间隔时间，默认取 self.interval_timeout
            return:  成功返回True 失败返回False

            xpath: element path
            text: the text of the setting
            wait_time: the waiting time, which is self.wait_timeout by default
            interval_time: polling interval; self.interval_timeout is selected by default
            return: Returns True successfully, and returns False if it fails
        """
  
        end_time = time.time() + wait_time
        while time.time() < end_time:
            response = self.SendData("setElementText", xpath, text)
            if "false" in response or "null" in response:
                time.sleep(interval_time)
            else:
                return True
        return False

    def click_element(self, xpath: str, wait_time: float = 5, interval_time: float = 0.5) -> bool:
        """
            点击元素
            Click element

            xpath: 元素路径
            wait_time: 等待时间，默认取 5秒
            interval_time: 轮询间隔时间，默认取 0.5秒
            return: 成功返回True 失败返回False

            xpath: element path
            wait_time: waiting time, which is 5 seconds by default
            interval_time: the polling interval, which is 0.5 seconds by default
            return: Returns True successfully, and returns False if it fails
        """

        end_time = time.time() + wait_time
        while time.time() < end_time:
            response = self.SendData("clickElement", xpath)
            if "false" in response or "null" in response:
                time.sleep(interval_time)
            else:
                return True
        return False

    def click_any_elements(self, xpath_list: list, wait_time: float = 5, interval_time: float = 0.5) -> bool:
        """
            遍历点击列表中的元素，直到任意一个元素返回 True
            Traverse the elements in the click list until any element returns True

            xpath_list: xpath 列表
            wait_time: 等待时间，默认取 5秒
            interval_time: 轮询间隔时间，默认取 0.5秒
            return: 成功返回True 失败返回False

            xpath_list: xpath list
            wait_time: waiting time, which is 5 seconds by default
            interval_time: the polling interval, which is 0.5 seconds by default
            return: Returns True successfully, and returns False if it fails
        """

        end_time = time.time() + wait_time
        while time.time() < end_time:
            for xpath in xpath_list:
                result = self.click_element(xpath, wait_time, interval_time)
                if result:
                    return True
            time.sleep(interval_time)

        return False

    def scroll_element(self, xpath: str, direction: int = 0) -> bool:
        """
            滚动元素，0 向上滑动，1 向下滑动

            xpath: xpath 路径
            direction: 滚动方向，0 向上滑动，1 向下滑动
            return: 成功返回True 失败返回False
        """
        return "true" in self.SendData("scrollElement", xpath, direction) 

    def element_exists(self, xpath: str, wait_time: float = 5, interval_time: float = 0.5) -> bool:
        """
            元素是否存在
            Does the element exist

            xpath: xpath 路径
            wait_time: 等待时间，默认取 self.wait_timeout
            interval_time: 轮询间隔时间，默认取 self.interval_timeout
            return: 成功返回True 失败返回False

            xpath: xpath path
            wait_time: the waiting time, which is self.wait_timeout by default
            interval_time: polling interval; self.interval_timeout is selected by default
            return: Returns True successfully, and returns False if it fails
        """
        end_time = time.time() + wait_time
        while time.time() < end_time:
            response = self.SendData("existsElement", xpath) 
            if "false" in response or "null" in response:
                time.sleep(interval_time)
            else:
                return True
        return False

    def any_elements_exists(self, xpath_list: list, wait_time: float = 5, interval_time: float = 0.5) -> bool:
        """
            遍历列表中的元素
            Traverse the elements in the list

            xpath_list: xpath 列表
            wait_time: 等待时间，默认取 self.wait_timeout
            interval_time: 轮询间隔时间，默认取 self.interval_timeout
            return: 任意一个元素存在就返回 True 否则就是为False

            xpath_list: xpath list
            wait_time: the waiting time, which is self.wait_timeout by default
            interval_time: polling interval; self.interval_timeout is selected by default
            return: If any element exists, it will return True, otherwise it will be False
        """

        end_time = time.time() + wait_time
        while time.time() < end_time:
            for xpath in xpath_list:
                result = self.element_exists(xpath, wait_time, interval_time)
                if result:
                    return result
            time.sleep(interval_time)
        return result

    def element_is_selected(self, xpath: str) -> bool:
        """
            判断元素是否选中
            Determine whether the element is selected

            xpath: xpath 路径
            return: 成功返回True 失败返回False

            xpath: xpath path
            return: Returns True successfully, and returns False if it fails
        """
        return  "true" in self.SendData("isSelectedElement", xpath) 

    def click_element_by_slide(self, xpath, distance: int = 1000, duration: float = 0.5, direction: int = 1,count: int = 999, end_flag_xpath: str = None, wait_time: float = 600,interval_time: float = 0.5) -> bool:
        """
            滑动列表，查找并点击指定元素
            Slide the list, find and click the specified element.

            xpath: xpath路径
            distance: 滑动距离，默认 1000
            duration: 滑动时间，默认 0.5 秒
            direction: 滑动方向，默认为 1； 1=上滑，2=下滑
            count: 滑动次数
            end_flag_xpath: 结束标志 xpath，无标志不检测此标志
            wait_time: 等待时间，默认 10 分钟
            interval_time: 轮询间隔时间，默认 0.5 秒
            return: 成功返回True 失败返回False

            Xpath: xpath path
            Distance: sliding distance; default is 1000
            Duration: sliding time, 0.5 seconds by default
            Direction: sliding direction, which defaults to 1; 1= slide up, 2= slide down
            Count: number of slides
            End_flag_xpath: end the flag xpath, if there is no flag, this flag will not be detected
            Wait_time: waiting time, 10 minutes by default
            Interval_time: the polling interval, which is 0.5 seconds by default
            return:  Returns True successfully, and returns False if it fails
        """

        if direction == 1:
            _end_point = (500, 300)
            _start_point = (500, _end_point[1] + distance)
        elif direction == 2:
            _start_point = (500, 300)
            _end_point = (500, _start_point[1] + distance)

        end_time = time.time() + wait_time
        current_count = 0
        while time.time() < end_time and current_count < count:
            current_count += 1

            if self.click_element(xpath, wait_time=1, interval_time=0.5):
                return True

            if end_flag_xpath and self.element_exists(end_flag_xpath, wait_time=1, interval_time=0.5):
                return False

            self.swipe(_start_point, _end_point, duration)
            time.sleep(interval_time)

        return False


