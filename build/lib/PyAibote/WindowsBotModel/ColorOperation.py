
import re
import time

class ColorOperation:
    """
        图色操作
        Color operation
    """
    def save_screenshot(self, hwnd: str, save_path: str, region: tuple = (0,0,0,0), algorithm: tuple = (0,0,0), mode: bool = False) -> bool:
        """
            截图
            screenshot

            hwnd: 窗口句柄
            save_path: 图片存储路径
            region: 截图区域，默认全屏，``region = (起点x、起点y、终点x、终点y)``，得到一个矩形
            algorithm:
                处理截图所用算法和参数，默认保存原图，
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

            mode: 操作模式，后台 true，前台 false, 默认前台操作
            return: "False"或者 "True"

            hwnd: window handle
            save_path: the image storage path.
            region: screenshot area, full screen by default, `` region = (starting point x, starting point y, ending point x, ending point y) ```, and a rectangle is obtained.
            algorithm:
                The algorithm and parameters used to process screenshots, the original image is saved by default,
                ``algorithm = (algorithm_type, threshold, max_val)``
                Represents, respectively, in the order of elements:
                0. ``algorithm_type ``` algorithm type
                1. ``threshold ```` threshold
                2. `` Max _ val```` Maximum value

                Gray processing when threshold and max_val are both 255.
                    `` algorithm _ type``` description of algorithm_type:
                        0. ``` threshold _ binary``` algorithm, when the current point value is greater than the threshold value ` threshold `, the maximum value ``` max _ val```` is taken, otherwise it is set to 0;
                        1. `` threshold _ binary _ inv``` algorithm, when the current point value is greater than the threshold value ` threshold `, it is set to 0, otherwise it is set to the maximum value max_val；;
                        2. `` threshold _ tozero``` algorithm, when the current point value is greater than the threshold ` threshold', it will not be changed, otherwise it will be set to 0;
                        3. `` threshold _ tozero _ inv``` algorithm, when the current point value is greater than the threshold ``` threshold ```, set it to 0, otherwise it will not change;
                        4. `` threshold _ trunc``` algorithm, when the current point value is greater than the threshold value ``` threshold ```, it is set as the threshold value ``` threshold ```, otherwise it will not be changed;
                        5. ``` Adaptive _ threshold _ mean _ c``` algorithm, adaptive threshold;
                        6. ``` Adaptive _ Thresh _ Gaussian _ C``` algorithm, adaptive threshold;

            mode: operation mode, background true, foreground false, default foreground operation.
            return: "False "or" True "
        """

        algorithm_type, threshold, max_val = algorithm
        if algorithm_type in (5, 6):
            threshold = 127
            max_val = 255

        return "true" in self.SendData("saveScreenshot", hwnd, save_path, *region, algorithm_type, threshold, max_val,mode)

    def get_color(self, hwnd: str, x: float, y: float, mode: bool = False) -> str:
        """
            获取指定坐标点的色值
            Gets the color value of the specified coordinate point and returns the color value string (#008577) or None

            hwnd: 窗口句柄
            x: x 坐标；
            y: y 坐标；
            mode: 操作模式，后台 True，前台 False, 默认前台操作
            return: 色值字符串(#008577)或者 None

            hwnd: Window handle
            x: x coordinate
            y: y coordinate
            mode: Operation mode, background True，前台, foreground False, default foreground operation.
            return: Color value string (#008577) or None
        """
        response = self.SendData("getColor", hwnd, x, y, mode)
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        if response == "null":
            return None
        return response

    def find_color(self, hwnd: str, color: str, sub_colors: tuple = (), region: tuple = (0, 0, 0, 0),similarity: float = 0.9, mode: bool = False, wait_time: float = 5, interval_time: float = 0.5)  -> tuple:
        """
            获取指定色值的坐标点，返回坐标或者 None
            Gets the coordinate point of the specified color value, and returns the coordinate or None

            hwnd: 窗口句柄
            color: 颜色字符串，必须以 # 开头，例如：#008577
            sub_colors: 辅助定位的其他颜色
            region: 在指定区域内找色，默认全屏
            similarity: 相似度，0-1 的浮点数，默认 0.9
            mode: 操作模式，后台 true，前台 false, 默认前台操作
            wait_time: 等待时间，默认取 self.wait_timeout
            interval_time: 轮询间隔时间，默认取 self.interval_timeout
            return: 成功返回{x:number, y:number} 失败返回None


            hwnd: window handle
            color: color string, which must start with #, for example: #008577
            sub_colors: other colors to assist positioning
            region: Find the color in the specified area, full screen by default
            similarity: similarity, floating point number of 0-1, default is 0.9
            mode: operation mode, background true, foreground false, default foreground operation
            wait_time: the waiting time, which is self.wait_timeout by default
            interval_time: polling interval; self.interval_timeout is selected by default
            return: returned {x:number, y:number} successfully, and returned None if failed
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
            response = self.SendData("findColor", hwnd, color, sub_colors_str, *region, similarity, mode)
            if "/" in response:
                response = re.findall(r'/(.*)',response)[0]
            if response == "-1.0|-1.0":
                time.sleep(interval_time)
            else:
                x, y = response.split("|")
                return (x,y)

        return None

    def compare_color(self, hwnd: str, main_x: float, main_y: float, color: str, sub_colors: tuple = (), region: tuple = (0, 0, 0, 0), similarity: float = 0.9, mode: bool = False) -> bool:
        """
            比较指定坐标点的颜色值
            Compare the color values of the specified coordinate points

            hwnd: 窗口句柄；
            main_x: 主颜色所在的X坐标；
            main_y: 主颜色所在的Y坐标；
            color: 颜色字符串，必须以 # 开头，例如：#008577；
            sub_colors: 辅助定位的其他颜色；
            region: 截图区域，默认全屏，``region = (起点x、起点y、终点x、终点y)``，得到一个矩形
            similarity: 相似度，0-1 的浮点数，默认 0.9；
            mode: 操作模式，后台 true，前台 false, 默认前台操作；
            return: True或者 False

            hwnd: window handle
            main_x: the x coordinate of the main color
            main_y: the y coordinate of the main color
            color: color string, which must start with #, for example: # 008577
            sub_colors: other colors to assist positioning
            region: screenshot area, full screen by default, `` region = (starting point x, starting point y, ending point x, ending point y) ```, and a rectangle is obtained
            similarity: similarity, floating point number of 0-1, default 0.9
            mode: operation mode, background true, foreground false, default foreground operation
            return: True or False
        """

        if sub_colors:
            sub_colors_str = ""
            for sub_color in sub_colors:
                offset_x, offset_y, color_str = sub_color
                sub_colors_str += f"{offset_x}/{offset_y}/{color_str}\n"
            sub_colors_str = sub_colors_str.strip()
        else:
            sub_colors_str = "null"
        return "true" in self.SendData("compareColor", hwnd, main_x, main_y, color, sub_colors_str, *region, similarity,mode)

    def extract_image_by_video(self, video_path: str, save_folder: str, jump_frame: int = 1) -> bool:
        """
            提取视频帧
            Extract video frames

            video_path: 视频路径
            save_folder: 提取的图片保存的文件夹目录
            jump_frame: 跳帧，默认为1 不跳帧
            return: True或者False

            video_path: Video path
            save_folder: The folder directory where the extracted pictures are saved
            jump_frame: Frame skipping, the default is 1, no frame skipping
            return: True or False
        """
        return "true" in self.SendData("extractImageByVideo", video_path, save_folder, jump_frame)

    def crop_image(self, image_path, save_path, left, top, rigth, bottom) -> bool:
        """
            裁剪图片
            Crop a picture

            image_path: 图片路径
            save_path: 裁剪后保存的图片路径
            left: 裁剪的左上角横坐标
            top: 裁剪的左上角纵坐标
            rigth: 裁剪的右下角横坐标
            bottom: 裁剪的右下角纵坐标
            return: True或者False

            image_path: image path
            save_path: the path of the saved picture after cropping
            left: abscissa of the upper left corner of the crop
            top: the ordinate of the upper left corner of the crop
            rigth: abscissa of the lower right corner of the crop
            bottom: ordinate of the lower right corner of the crop
            return: True or False
        """
        return "true" in self.SendData("cropImage", image_path, save_path, left, top, rigth, bottom) 

    def find_images(self, hwnd_or_big_image_path: str, image_path: str, region: tuple = (0, 0, 0, 0), algorithm: tuple = (0, 0, 0), similarity: float = 0.9, mode: bool = False, multi: int = 1, wait_time: float = 5, interval_time: float = 0.5) -> list:
        """
            寻找图片坐标，在当前屏幕中寻找给定图片中心点的坐标，返回坐标列表
            Find picture coordinates, find the coordinates of the center point of a given picture in the current screen, and return to the coordinate list

            hwnd_or_big_image_path: 窗口句柄或者图片路径；
            image_path: 图片的绝对路径；
            region: 从指定区域中找图，默认全屏；
            algorithm: 处理屏幕截图所用的算法，默认原图，注意：给定图片处理时所用的算法，应该和此方法的算法一致；
            similarity: 相似度，0-1 的浮点数，默认 0.9；
            mode: 操作模式，后台 true，前台 false, 默认前台操作；
            multi: 返回图片数量，默认1张；
            wait_time: 等待时间，默认取 self.wait_timeout；
            interval_time: 轮询间隔时间，默认取 self.interval_timeout；
            return: 成功返回 单坐标点[{x:number, y:number}]，多坐标点[{x1:number, y1:number}, {x2:number, y2:number}...] 失败返回空[]

            thresholdType算法类型：
                0   THRESH_BINARY算法，当前点值大于阈值thresh时，取最大值maxva，否则设置为0
                1   THRESH_BINARY_INV算法，当前点值大于阈值thresh时，设置为0，否则设置为最大值maxva
                2   THRESH_TOZERO算法，当前点值大于阈值thresh时，不改变，否则设置为0
                3   THRESH_TOZERO_INV算法，当前点值大于阈值thresh时，设置为0，否则不改变
                4   THRESH_TRUNC算法，当前点值大于阈值thresh时，设置为阈值thresh，否则不改变
                5   ADAPTIVE_THRESH_MEAN_C算法，自适应阈值
                6   ADAPTIVE_THRESH_GAUSSIAN_C算法，自适应阈值
                thresh阈值，maxval最大值，threshold默认保存原图。thresh和maxval同为255时灰度处理

            hwnd_or_big_image_path: window handle or image path;
            image_path: the absolute path of the picture;
            region: Find the map from the specified area, full screen by default;
            algorithm: the algorithm used to process screen shots, the original image by default. Note: the algorithm used in a given image processing should be consistent with the algorithm of this method;
            similarity: similarity, floating point number of 0-1, default 0.9;
            mode: operation mode, background true, foreground false, default foreground operation;
            multi: Returns the number of pictures, with 1 picture by default;
            wait_time: the waiting time, which defaults to self. wait _ timeout;
            interval_time: polling interval; self. interval _ timeout is selected by default;
            return: single coordinate point [{x:number, y:number}] was successfully returned, and multi-coordinate point [{x1: number, y1: number}, {x2: number, y2: number} ...] failed to return empty [].

            ThresholdType algorithm type:
                0 THRESH_BINARY algorithm, when the current point value is greater than the threshold thresh, take the maximum maxva, otherwise set to 0
                1 THRESH_BINARY_INV algorithm, when the current point value is greater than the threshold thresh, set it to 0, otherwise set it to the maximum maxva
                2 THRESH_TOZERO algorithm, when the current point value is greater than the threshold thresh, it will not change, otherwise it will be set to 0
                3 THRESH_TOZERO_INV algorithm, when the current point value is greater than the threshold thresh, it is set to 0, otherwise it will not change
                4 THRESH_TRUNC algorithm, when the current point value is greater than the threshold thresh, set it as the threshold thresh, otherwise it will not change
                5 ADAPTIVE_THRESH_MEAN_C algorithm, adaptive threshold
                6 adaptive _ threshold _ Gaussian _ c algorithm, adaptive threshold
                Threshold threshold, maxval maximum, threshold saves the original image by default. Gray processing when thresh and maxval are both 255
        """

        algorithm_type, threshold, max_val = algorithm
        if algorithm_type in (5, 6):
            threshold = 127
            max_val = 255

        end_time = time.time() + wait_time
        while time.time() < end_time:
            if hwnd_or_big_image_path.isdigit():
                response = self.SendData("findImage", hwnd_or_big_image_path, image_path, *region, similarity,
                                            algorithm_type,
                                            threshold, max_val, multi, mode)
            else:
                response = self.SendData("findImageByFile", hwnd_or_big_image_path, image_path, *region, similarity,
                                            algorithm_type,
                                            threshold, max_val, multi, mode)
            if "/" in response:
                response = re.findall(r'/(.*)',response)[0]
            if response in ["-1.0|-1.0", "-1|-1"]:
                time.sleep(interval_time)
                continue
            else:
                image_points = response.split("/")
                point_list = []
                for point_str in image_points:
                    x, y = point_str.split("|")
                    point_list.append((float(x), float(y)))
                return point_list
        return []

    def find_dynamic_image(self, hwnd: str, interval_ti: int, region: tuple = (0, 0, 0, 0), mode: bool = False, wait_time: float = 5, interval_time: float = 0.5) -> list:
        """
            找动态图，对比同一张图在不同时刻是否发生变化，返回坐标列表
            Find the dynamic diagram, compare whether the same diagram has changed at different times, and return the coordinate list

            hwnd: 窗口句柄
            interval_ti: 前后时刻的间隔时间，单位毫秒
            region: 在指定区域找图，默认全屏
            mode: 操作模式，后台 true，前台 false, 默认前台操作
            wait_time: 等待时间，默认取 self.wait_timeout
            interval_time: 轮询间隔时间，默认取 self.interval_timeout
            return: 成功返回 单坐标点[{x:number, y:number}]，多坐标点[{x1:number, y1:number}, {x2:number, y2:number}...] 失败返回空[]

            hwnd: window handle
            interval_ti: the interval between the preceding and the following moments, in milliseconds
            region: Find the map in the specified area, full screen by default
            mode: operation mode, background true, foreground false, default foreground operation
            wait_time: the waiting time, which is self.wait_timeout by default
            interval_time: polling interval; self.interval_timeout is selected by default
            return: single coordinate point [{x:number, y:number}] was successfully returned, and multi-coordinate point [{x1: number, y1: number}, {x2: number, y2: number} ...] failed to return empty []
        """

        end_time = time.time() + wait_time
        while time.time() < end_time:
            response = self.SendData("findAnimation", hwnd, interval_ti, *region, mode)
            if "/" in response:
                response = re.findall(r'/(.*)',response)[0]
            if response == "-1|-1":
                time.sleep(interval_time)
                continue
            else:
                image_points = response.split("/")
                point_list = []
                for point_str in image_points:
                    x, y = point_str.split("|")
                    point_list.append((float(x), float(y)))
                return point_list
        return []




