import re
import time

class MapFindingOperation:
    """
        找图功能
        Map finding function
    """
    def find_images(self, image_name: str, region: tuple = (0,0,0,0), algorithm: tuple = (0,0,0), similarity: float = 0.9, multi: int = 1, wait_time: float = 5, interval_time: float = 0.5) -> list:
        """
            寻找图片坐标，在当前屏幕中寻找给定图片中心点的坐标，返回坐标列表(如果想拿一个坐标取第一个坐标元祖即可)
            Find the coordinates of the picture, find the coordinates of the center point of a given picture in the current screen, and return to the coordinate list (if you want to take a coordinate and take the first coordinate ancestor)

            image_name: 图片名称（手机中）/storage/emulated/0/ 手机根目录
            region: 截图区域，默认全屏，``region = (起点x、起点y、终点x、终点y)``，得到一个矩形
            algorithm:
                处理屏幕截图所用的算法，默认原图，注意：给定图片处理时所用的算法，应该和此方法的算法一致；
                ``algorithm = (algorithm_type, threshold, max_val)``

                按元素顺序分别代表：
                0. ``algorithm_type`` 算法类型
                1. ``threshold`` 阈值
                2. ``max_val`` 最大值

                ``threshold`` 和 ``max_val`` 同为 255 时灰度处理.
                ``algorithm_type`` 算法类型说明:
                    0. ``THRESH_BINARY``      算法，当前点值大于阈值 `threshold` 时，取最大值 ``max_val``，否则设置为 0；
                    1. ``THRESH_BINARY_INV``  算法，当前点值大于阈值 `threshold` 时，设置为 0，否则设置为最大值 max_val；
                    2. ``THRESH_TOZERO``      算法，当前点值大于阈值 `threshold` 时，不改变，否则设置为 0；
                    3. ``THRESH_TOZERO_INV``  算法，当前点值大于阈值 ``threshold`` 时，设置为 0，否则不改变；
                    4. ``THRESH_TRUNC``       算法，当前点值大于阈值 ``threshold`` 时，设置为阈值 ``threshold``，否则不改变；
                    5. ``ADAPTIVE_THRESH_MEAN_C``      算法，自适应阈值；
                    6. ``ADAPTIVE_THRESH_GAUSSIAN_C``  算法，自适应阈值；
            similarity: 相似度，0-1 的浮点数，默认 0.9；
            multi: 目标数量，默认为 1，找到 1 个目标后立即结束；
            wait_time: 等待时间，默认取 self.wait_timeout
            interval_time: 轮询间隔时间，默认取 self.interval_timeout
            return: 坐标列表 或者 []

            image_name: image name (in mobile phone) /storage/emulated/0/ mobile phone root directory.
            region: screenshot area, full screen by default, `` region = (starting point x, starting point y, ending point x, ending point y) ```, and a rectangle is obtained.
            algorithm:
                The algorithm used to process screen shots defaults to the original image. Note: the algorithm used in the given image processing should be consistent with the algorithm of this method;

                ``algorithm = (algorithm_type, threshold, max_val)``

                Represents, respectively, in the order of elements:
                    0. ``algorithm_type ``` algorithm type
                    1. ``threshold ```` threshold
                    2. `` Max _ val```` Maximum value

                Gray processing when threshold and max_val are both 255
                `` algorithm _ type``` description of algorithm_type
                        0. ``` threshold _ binary``` algorithm, when the current point value is greater than the threshold value ` threshold `, the maximum value ``` max _ val```` is taken, otherwise it is set to 0
                        1. `` threshold _ binary _ inv``` algorithm, when the current point value is greater than the threshold value ` threshold `, set it to 0, otherwise set it to the maximum value max_val；
                        2. `` threshold _ tozero``` algorithm, when the current point value is greater than the threshold ` threshold', it will not be changed, otherwise it will be set to 0
                        3. `` threshold _ tozero _ inv``` algorithm, when the current point value is greater than the threshold value ``` threshold ```, it is set to 0, otherwise it will not change
                        4. `` threshold _ trunc``` algorithm, when the current point value is greater than the threshold value ``` threshold ```, it is set as the threshold value ``` threshold ```, otherwise it will not be changed
                        5. ``` Adaptive _ threshold _ mean _ c``` algorithm, adaptive threshold
                        6. ``` Adaptive _ Thresh _ Gaussian _ C``` algorithm, adaptive threshold
            similarity: similarity, floating point number of 0-1, default 0.9;
            multi: number of targets; the default value is 1, and it ends immediately after finding one target
            wait_time: the waiting time, which is self.wait_timeout by default
            interval_time: polling interval; self.interval_timeout is selected by default
            Return: list of coordinates or []
        """
        if not image_name.startswith("/storage/emulated/0/"):
            image_name = "/storage/emulated/0/" + image_name
    
        algorithm_type, threshold, max_val = algorithm
        if algorithm_type in (5, 6):
            threshold = 127
            max_val = 255
        end_time = time.time() + wait_time
        while time.time() < end_time:
            response = self.SendData("findImage", image_name, *region, similarity, algorithm_type, threshold, max_val, multi)
            if response == "-1.0|-1.0":
                time.sleep(interval_time)
            else:
                image_points = response.split("/")
                point_list = []
                for point_str in image_points:
                    x, y = point_str.split("|")
                    point_list.append((float(x),float(y)))
                return point_list
        return []

    def find_dynamic_image(self, interval_ti: int, region: tuple = (0,0,0,0), wait_time: float = 5, interval_time: float = 0.5) -> list:
        """
            找动态图，对比同一张图在不同时刻是否发生变化，返回坐标列表
            Find the dynamic diagram, compare whether the same diagram has changed at different times, and return the coordinate list

            interval_ti: 前后时刻的间隔时间，单位毫秒；
            region: 截图区域，默认全屏，``region = (起点x、起点y、终点x、终点y)``，得到一个矩形
            wait_time: 等待时间，默认取 5秒
            interval_time: 轮询间隔时间，默认取 0.5秒
            return: 坐标列表 或者 []

            interval_ti: the interval between the preceding and the following moments, in milliseconds
            region: screenshot area, full screen by default, `` region = (starting point x, starting point y, ending point x, ending point y) ```, and a rectangle is obtained
            wait_time: waiting time, which is 5 seconds by default
            interval_time: the polling interval, which is 0.5 seconds by default
            return: list of coordinates or []
        """
        end_time = time.time() + wait_time
        while time.time() < end_time:
            response = self.SendData("findAnimation", interval_ti, *region)
            if response == "-1.0|-1.0":
                time.sleep(interval_time)
            else:
                image_points = response.split("/")
                point_list = []
                for point_str in image_points:
                    x, y = point_str.split("|")
                    point_list.append((float(x), float(y)))
                return point_list
        return []






