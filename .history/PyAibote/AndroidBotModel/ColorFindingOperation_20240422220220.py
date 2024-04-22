import re
import time

class ColorFindingOperation:
    """
        色值相关
        Color value correlation
    """

    def get_color(self, point: tuple) -> str:
        """
            获取指定坐标点的色值
            Gets the color value of the specified coordinate point.

            point: x, y坐标点
            return: 色值字符串(例如: #008577)或者 None

            point: x, y coordinate point
            return: color value string (for example: #008577) or None
        """
        response = self.SendData("getColor", point[0], point[1])
        if response == "null":
            return None
        return response

    def find_color(self, color: str, sub_colors: list = [], region: tuple = (0,0,0,0), similarity: float = 0.9, wait_time: float = 5, interval_time: float = 0.5) -> tuple:
        """
            获取指定色值的坐标点，返回坐标或者 None
            Gets the coordinate point of the specified color value, and returns the coordinate or None

            color: 颜色字符串，必须以 # 开头，例如：#008577；
            sub_colors: 辅助定位的其他颜色 (偏移x、偏移y、颜色字符串)
            region: 截图区域，默认全屏，``region = (起点x、起点y、终点x、终点y)``，得到一个矩形
            similarity: 相似度，0-1 的浮点数，默认 0.9；
            wait_time: 等待时间，默认取 5秒
            interval_time: 轮询间隔时间，默认取 0.5秒
            return: 坐标或者 ()

            color: color string, which must start with #, for example: # 008577
            sub_colors: other colors (offset x, offset y, color string) to assist positioning
            region: screenshot area, full screen by default, `` region = (starting point x, starting point y, ending point x, ending point y) ```, and a rectangle is obtained
            similarity: similarity, floating point number of 0-1, default 0.9
            wait_time: waiting time, which is 5 seconds by default
            interval_time: the polling interval, which is 0.5 seconds by default
            return: coordinates or ()
        """
        if sub_colors:
            sub_colors_str = ""
            for sub_color in sub_colors:
                offset_x, offset_y, color_str = sub_color
                sub_colors_str += f"{offset_x}/{offset_y}/{color_str}\n"
            sub_colors_str = sub_colors_str.strip()
        else:
            sub_colors_str = "null"
        end_time = time.time() + wait_time
        while time.time() < end_time:
            response = self.SendData("findColor", color, sub_colors_str, *region, similarity)
            if "/" in response:
                response = re.findall(r'/(.*)',response)[0]
            if response == "-1.0|-1.0":
                time.sleep(interval_time)
            else:
                x, y = response.split("|")
                return (x, y)
        return ()





