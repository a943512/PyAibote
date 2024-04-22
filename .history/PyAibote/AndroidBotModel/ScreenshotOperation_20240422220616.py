import re

class ScreenshotOperation:
    """
        截图操作
        Screenshot operation
    """
    def __pull_file(self, *args) -> bytes:
        args_len = ""
        args_text = ""

        for argv in args:
            argv = str(argv)
            args_text += argv
            args_len += str(len(bytes(argv, 'utf8'))) + "/"
        data = (args_len.strip("/") + "\n" + args_text).encode("utf8")
        if len(data) > 10000:
            self.debug(rf"<-<- {data[:100]}......")
        else:
            self.debug(rf"<-<- {data}")
        self.request.sendall(data)
        response = self.request.recv(65535)
        if len(response) > 10000:
            self.debug(rf"<-<- {response[:100]}......")
        else:
            self.debug(rf"<-<- {response}")
        if response == b"":
            raise ConnectionAbortedError(f"{self.client_address[0]}:{self.client_address[1]} 客户端断开链接")
        data_length, data = response.split(b"/", 1)
        while int(data_length) > len(data):
            data += self.request.recv(65535)
        return data

    def save_screenshot(self, image_name: str, region: tuple = (0,0,0,0), algorithm: tuple = (0,0,0)) -> str:
        """
            保存截图，返回图片地址(手机中)或者 None
            Save the screenshot and return to the picture address (in the phone) or None

            image_name: 图片名称，保存在手机 /storage/emulated/0/ 路径下；
            region: 截图区域，默认全屏，``region = (起点x、起点y、终点x、终点y)``，得到一个矩形
            algorithm: 处理截图所用算法和参数，默认保存原图，
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
            return: 图片地址(手机中) 或者 None

            Image_name: the name of the picture, which is saved in the path of mobile phone /storage/emulated/0/
            Region: screenshot area, full screen by default, `` region = (starting point x, starting point y, ending point x, ending point y) ```, and a rectangle is obtained
            Algorithm: the algorithm and parameters used to process screenshots, and the original image is saved by default
            The algorithm used to process screen shots defaults to the original image. Note: the algorithm used in the given image processing should be consistent with the algorithm of this method
                ``algorithm = (algorithm_type, threshold, max_val)``

                Represents, respectively, in the order of elements:
                0. ``algorithm_type ``` algorithm type
                1. ``threshold ```` threshold
                2. `` Max _ val```` Maximum value

                Gray processing when threshold and max_val are both 255.
                `` algorithm _ type``` description of algorithm_type:
                0. ``` threshold _ binary``` algorithm, when the current point value is greater than the threshold value ` threshold `, the maximum value ``` max _ val```` is taken, otherwise it is set to 0;
                1. `` threshold _ binary _ inv``` algorithm, when the current point value is greater than the threshold value ` threshold `, set it to 0, otherwise set it to the maximum value max_val；;
                2. `` threshold _ tozero``` algorithm, when the current point value is greater than the threshold ` threshold', it will not be changed, otherwise it will be set to 0;
                3. `` threshold _ tozero _ inv``` algorithm, when the current point value is greater than the threshold value ``` threshold ```, it is set to 0, otherwise it will not change;
                4. `` threshold _ trunc``` algorithm, when the current point value is greater than the threshold value ``` threshold ```, it is set as the threshold value ``` threshold ```, otherwise it will not be changed;
                5. ``` Adaptive _ threshold _ mean _ c``` algorithm, adaptive threshold;
                6. ``` Adaptive _ Thresh _ Gaussian _ C``` algorithm, adaptive threshold;
            Return: picture address (in mobile phone) or None.
        """
        if not image_name.startswith("/storage/emulated/0/"):
            image_name = "/storage/emulated/0/" + image_name

        algorithm_type, threshold, max_val = algorithm
        if algorithm_type in (5, 6):
            threshold = 127
            max_val = 255

        response = self.SendData("saveScreenshot", image_name, *region, algorithm_type, threshold, max_val)
        if "true" in response:
            return image_name
        return None

    def save_element_screenshot(self, image_name: str, xpath: str) -> str:
        """
            保存元素截图
            Save element screenshot

            image_name: 图片名称，保存在手机 /storage/emulated/0/ 路径下
            xpath: xpath路径
            return: 图片地址(手机中)或者 None

            image_name: the name of the picture, which is saved in the path of mobile phone /storage/emulated/0/
            xpath: xpath path
            return: picture address (in mobile phone) or None
        """
        response = self.SendData("getElementRect", xpath)
        if response == "-1|-1|-1|-1":
             return None
        start_x, start_y, end_x, end_y = response.split("|")
        return self.save_screenshot(image_name, region=(start_x, start_y, end_x, end_y))

    def take_screenshot(self, region: tuple = (0,0,0,0), algorithm: tuple = (0,0,0), scale: float = 1.0) -> bytes:
        """
            保存截图，返回图像字节格式或者None, 此功能如果做投屏scale参数需要缩放3倍以上不然很慢

            region: 截图区域，默认全屏，``region = (起点x、起点y、终点x、终点y)``，得到一个矩形
            algorithm: 处理截图所用算法和参数，默认保存原图
                处理屏幕截图所用的算法，默认原图，注意：给定图片处理时所用的算法，应该和此方法的算法一致
                ``algorithm = (algorithm_type, threshold, max_val)``

                按元素顺序分别代表：
                0. ``algorithm_type`` 算法类型
                1. ``threshold`` 阈值
                2. ``max_val`` 最大值

                ``threshold`` 和 ``max_val`` 同为 255 时灰度处理
                ``algorithm_type`` 算法类型说明:
                    0. ``THRESH_BINARY``      算法，当前点值大于阈值 `threshold` 时，取最大值 ``max_val``，否则设置为 0
                    1. ``THRESH_BINARY_INV``  算法，当前点值大于阈值 `threshold` 时，设置为 0，否则设置为最大值 max_val
                    2. ``THRESH_TOZERO``      算法，当前点值大于阈值 `threshold` 时，不改变，否则设置为 0
                    3. ``THRESH_TOZERO_INV``  算法，当前点值大于阈值 ``threshold`` 时，设置为 0，否则不改变
                    4. ``THRESH_TRUNC``       算法，当前点值大于阈值 ``threshold`` 时，设置为阈值 ``threshold``，否则不改变
                    5. ``ADAPTIVE_THRESH_MEAN_C``      算法，自适应阈值；
                    6. ``ADAPTIVE_THRESH_GAUSSIAN_C``  算法，自适应阈值；

            scale: 图片缩放率，默认为 1.0，1.0 以下为缩小，1.0 以上为放大
            return: 图像字节格式或者"null"的字节格式
        """
        algorithm_type, threshold, max_val = algorithm
        if algorithm_type in (5, 6):
            threshold = 127
            max_val = 255

        response = self.__pull_file("takeScreenshot", *region, algorithm_type, threshold, max_val, scale)
        if b"null" in response:
            return None
        return response





