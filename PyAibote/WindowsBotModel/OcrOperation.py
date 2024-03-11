import re
from ast import literal_eval


class OcrOperation:
    """
        OCR 操作
        OCR operation
    """

    def init_ocr_server(self, ip: str, use_angle_model: bool = False, enable_gpu: bool = False, enable_tensorrt: bool = False) -> bool:
        """
            初始化 OCR 服务
            Initialize OCR service

            ip: ocr服务器IP，固定端口9527。当参数值为 "127.0.0.1"时 为本地DLL模式
            use_angle_model: 支持图像旋转
            enable_gpu: 启动GPU 模式。GPU 模式需要电脑安装 NVIDIA 驱动，并且到群文件下载对应 cuda 版本
            enable_tensorrt: 启动加速，仅 enable_gpu = True 时有效。图片太大可能会导致GPU内存不足。
            return: 总是返回true

            ip: ocr server IP, fixed port 9527. When the parameter value is "127.0.0.1", it is local DLL mode
            use_angle_model: supports image rotation
            enable_gpu: starts GPU mode. GPU mode requires the computer to install NVIDIA driver and download the corresponding cuda version from the group file
            enable_tensorrt: Enables acceleration, which is only valid when enable_gpu = True. Too large a picture may lead to insufficient GPU memory
            return: always returns true
        """
        return "true" in self.SendData("initOcr", ip, use_angle_model, enable_gpu, enable_tensorrt)

    def ocr_server_by_file(self, image_path: str, region: tuple = (0, 0, 0, 0), algorithm: tuple = (0, 0, 0)) -> list:
        """
            OCR 服务，通过 OCR 识别图片路径中的文字
            OCR service, which recognizes the characters in the image path through OCR

            image_path: 图片路径
            region: (左上角x点, 左上角y点, 右下角 x点, 右下角 y点)
            algorithm: (二值化算法类型, 阈值, 最大值)
            return: 失败返回null，成功返回列表形式的识别结果: [[[[317, 4], [348, 4], [348, 22], [317, 22]]]]

            image_path: image path
            region: (point X in the upper left corner, point Y in the upper left corner, point X in the lower right corner, point Y in the lower right corner)
            algorithm: (Binary algorithm type, threshold, maximum)
            return: failed to return null, and successfully returned the recognition results in list form: [[[[317,4], [348,4], [348,22], [317,22]]]
        """
        algorithm_type, threshold, max_val = algorithm
        if algorithm_type in (5, 6):
            threshold = 127
            max_val = 255

        response = self.SendData("ocrByFile", image_path, *region, algorithm_type, threshold, max_val)
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        if response == "null" or response == "":
            return []
        return literal_eval(response)

    def ocr_server_by_hwnd(self, hwnd: str, region: tuple = (0, 0, 0, 0), algorithm: tuple = (0, 0, 0), mode: bool = False) -> list:
        """
            OCR 服务，通过 OCR 识别窗口句柄中的文字
            OCR service, which recognizes the characters in the window handle through OCR

            hwnd: Window handle
            region: (左上角x点, 左上角y点, 右下角 x点, 右下角 y点)
            algorithm: (二值化算法类型, 阈值, 最大值)
            mode: 操作模式，后台 true，前台 false。默认前台操作   
            return: 失败返回null，成功返回列表形式的识别结果: [[[[317, 4], [348, 4], [348, 22], [317, 22]]]]

            image_path: image path
            region: (point X in the upper left corner, point Y in the upper left corner, point X in the lower right corner, point Y in the lower right corner)
            algorithm: (Binary algorithm type, threshold, maximum)
            mode: Operation mode, background true, foreground false. Default foreground operation
            return: failed to return null, and successfully returned the recognition results in list form: [[[[317,4], [348,4], [348,22], [317,22]]]
        """
        algorithm_type, threshold, max_val = algorithm
        if algorithm_type in (5, 6):
            threshold = 127
            max_val = 255

        response = self.SendData("ocrByHwnd", hwnd, *region, algorithm_type, threshold, max_val, mode)
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        if response == "null" or response == "":
            return []
        return literal_eval(response)

    def get_text(self, hwnd_or_image_path: str, region: tuple = (0, 0, 0, 0), algorithm: tuple = (0, 0, 0), mode: bool = False) -> list:
        """
            通过 OCR 识别窗口/图片中的文字，
            Recognize the characters in the window/picture through OCR, and return to the text list

            hwnd_or_image_path: 窗口句柄或者图片路径；
            region: 识别区域，默认全屏；
            algorithm: 处理图片/屏幕所用算法和参数，默认保存原图；
            mode: 操作模式，后台 True，前台 False, 默认前台操作；
            return: 返回文字列表

            hwnd_or_image_path: window handle or image path
            region: recognition region, full screen by default
            algorithm: the algorithm and parameters used to process the picture/screen, and the original picture is saved by default
            mode: operation mode, background True, foreground False, default foreground operation
            return: returns the text list
        """
        if hwnd_or_image_path.isdigit():
            text_info_list = self.ocr_server_by_hwnd(hwnd_or_image_path, region, algorithm, mode)
        else:
            text_info_list = self.ocr_server_by_file(hwnd_or_image_path, region, algorithm)

        text_list = []
        for text_info in text_info_list:
            text = text_info[-1][0]
            text_list.append(text)
        return text_list

    def find_text(self, hwnd_or_image_path: str, text: str, region: tuple = (0, 0, 0, 0), algorithm: tuple = (0, 0, 0), mode: bool = False) -> list:
        """
            通过 OCR 识别窗口/图片中的文字
            Recognize the characters in the window/picture through OCR, and return the coordinate list


            hwnd_or_image_path: 句柄或者图片路径
            text: 要查找的文字
            region: 识别区域，默认全屏
            algorithm: 处理图片/屏幕所用算法和参数，默认保存原图
            mode: 操作模式，后台 true，前台 false, 默认前台操作
            return: 文字坐标列表

            hwnd_or_image_path: handle or image path
            text: the text to find
            region: recognition region, full screen by default
            algorithm: the algorithm and parameters used to process the picture/screen, and the original picture is saved by default
            mode: operation mode, background true, foreground false, default foreground operation
            return: list of text coordinates
        """

        if hwnd_or_image_path.isdigit():
            text_info_list = self.ocr_server_by_hwnd(hwnd_or_image_path, region, algorithm, mode)
        else:
            text_info_list = self.ocr_server_by_file(hwnd_or_image_path, region, algorithm)

        text_points = []
        for text_info in text_info_list:
            if text in text_info[-1][0]:
                points, words_tuple = text_info

                left, _, right, _ = points

                start_x = left[0]
                start_y = left[1]

                end_x = right[0]
                end_y = right[1]

                width = end_x - start_x
                height = end_y - start_y
                words: str = words_tuple[0]

                single_word_width = width / len(words)
                pos = words.find(text)

                offset_x = single_word_width * (pos + len(text) / 2)
                offset_y = height / 2

                text_point = (
                    region[0] + start_x + offset_x,
                    region[1] + start_y + offset_y
                )
                text_points.append(text_point)
        return text_points