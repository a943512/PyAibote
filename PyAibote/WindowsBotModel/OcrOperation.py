import re
from ast import literal_eval


class OcrOperation:
    """
        OCR 操作
        OCR operation
    """

    # def init_ocr_server(self, ip: str, use_angle_model: bool = False, enable_gpu: bool = False, enable_tensorrt: bool = False) -> bool:
    #     """
    #         初始化 OCR 服务
    #         Initialize OCR service

    #         ip: ocr服务器IP，固定端口9527。当参数值为 "127.0.0.1"时 为本地DLL模式
    #         use_angle_model: 支持图像旋转
    #         enable_gpu: 启动GPU 模式。GPU 模式需要电脑安装 NVIDIA 驱动，并且到群文件下载对应 cuda 版本
    #         enable_tensorrt: 启动加速，仅 enable_gpu = True 时有效。图片太大可能会导致GPU内存不足。
    #         return: 总是返回true

    #         ip: ocr server IP, fixed port 9527. When the parameter value is "127.0.0.1", it is local DLL mode
    #         use_angle_model: supports image rotation
    #         enable_gpu: starts GPU mode. GPU mode requires the computer to install NVIDIA driver and download the corresponding cuda version from the group file
    #         enable_tensorrt: Enables acceleration, which is only valid when enable_gpu = True. Too large a picture may lead to insufficient GPU memory
    #         return: always returns true
    #     """
    #     return "true" in self.SendData("initOcr", ip, use_angle_model, enable_gpu, enable_tensorrt)

    def ocr_server_by_file(self, ocr_server_id: str, image_path: str, region: tuple = (0, 0, 0, 0), algorithm: tuple = (0, 0, 0)) -> list:
        """
            OCR 服务，通过 OCR 识别图片路径中的文字
            OCR service, which recognizes the characters in the image path through OCR

            ocr_server_id: ocr服务端IP，端口固定为9527
            image_path: 图片路径
            region: (左上角x点, 左上角y点, 右下角 x点, 右下角 y点)
            algorithm: (二值化算法类型, 阈值, 最大值)
            return: 失败返回null，成功返回列表形式的识别结果: [[[[317, 4], [348, 4], [348, 22], [317, 22]]]]

            ocr_server_id: the IP of the ocr server, and the port is fixed at 9527
            image_path: image path
            region: (point X in the upper left corner, point Y in the upper left corner, point X in the lower right corner, point Y in the lower right corner)
            algorithm: (Binary algorithm type, threshold, maximum)
            return: failed to return null, and successfully returned the recognition results in list form: [[[[317,4], [348,4], [348,22], [317,22]]]
        """
        algorithm_type, threshold, max_val = algorithm
        if algorithm_type in (5, 6):
            threshold = 127
            max_val = 255

        response = self.SendData("ocrByFile", ocr_server_id, image_path, *region, algorithm_type, threshold, max_val)
        if response == "null" or response == "":
            return []
        return literal_eval(response)

    def ocr_server_by_hwnd(self, ocr_server_id: str, hwnd: str, region: tuple = (0, 0, 0, 0), algorithm: tuple = (0, 0, 0), mode: bool = False) -> list:
        """
            OCR 服务，通过 OCR 识别窗口句柄中的文字
            OCR service, which recognizes the characters in the window handle through OCR
            
            ocr_server_id: ocr服务端IP，端口固定为9527
            hwnd: Window 句柄
            region: (左上角x点, 左上角y点, 右下角 x点, 右下角 y点)
            algorithm: (二值化算法类型, 阈值, 最大值)
            mode: 操作模式，后台 true，前台 false。默认前台操作   
            return: 失败返回null，成功返回列表形式的识别结果: [[[[317, 4], [348, 4], [348, 22], [317, 22]]]]

            ocr_server_id: the IP of the ocr server, and the port is fixed at 9527
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

        response = self.SendData("ocrByHwnd", ocr_server_id, hwnd, *region, algorithm_type, threshold, max_val, mode)
        if response == "null" or response == "":
            return []
        return literal_eval(response)

    def get_text(self, ocr_server_id: str, hwnd_or_image_path: str, region: tuple = (0, 0, 0, 0), algorithm: tuple = (0, 0, 0), mode: bool = False) -> list:
        """
            通过 OCR 识别窗口/图片中的文字，
            Recognize the characters in the window/picture through OCR, and return to the text list

            ocr_server_id: ocr服务端IP，端口固定为9527
            hwnd_or_image_path: 窗口句柄或者图片路径；
            region: 识别区域，默认全屏；
            threshold二值化图片, thresholdType算法类型：
                                                      0   THRESH_BINARY算法，当前点值大于阈值thresh时，取最大值maxva，否则设置为0
                                                      1   THRESH_BINARY_INV算法，当前点值大于阈值thresh时，设置为0，否则设置为最大值maxva
                                                      2   THRESH_TOZERO算法，当前点值大于阈值thresh时，不改变，否则设置为0
                                                      3   THRESH_TOZERO_INV算法，当前点值大于阈值thresh时，设置为0，否则不改变
                                                      4   THRESH_TRUNC算法，当前点值大于阈值thresh时，设置为阈值thresh，否则不改变
                                                      5   ADAPTIVE_THRESH_MEAN_C算法，自适应阈值
                                                      6   ADAPTIVE_THRESH_GAUSSIAN_C算法，自适应阈值
                                thresh阈值，maxval最大值，threshold默认保存原图。thresh和maxval同为255时灰度处理
            mode: 操作模式，后台 True，前台 False, 默认前台操作；
            return: 返回文字列表

            ocr_server_id: the IP of the ocr server, and the port is fixed at 9527
            hwnd_or_image_path: window handle or image path
            region: recognition region, full screen by default
            algorithm: the algorithm and parameters used to process the picture/screen, and the original picture is saved by default
            threshold binary image, thresholdType algorithm type:
                0 THRESH_BINARY algorithm, when the current point value is greater than the threshold thresh, take the maximum maxva, otherwise set to 0.
                1 THRESH_BINARY_INV algorithm, when the current point value is greater than the threshold thresh, set it to 0, otherwise set it to the maximum maxva.
                2 THRESH_TOZERO algorithm, when the current point value is greater than the threshold thresh, it will not change, otherwise it will be set to 0.
                3 THRESH_TOZERO_INV algorithm, when the current point value is greater than the threshold thresh, it is set to 0, otherwise it will not change.
                4 THRESH_TRUNC algorithm, when the current point value is greater than the threshold thresh, set it as the threshold thresh, otherwise it will not change.
                5 ADAPTIVE_THRESH_MEAN_C algorithm, adaptive threshold
                6 adaptive _ threshold _ Gaussian _ c algorithm, adaptive threshold.
                Threshold threshold, maxval maximum, threshold saves the original image by default. Gray processing when thresh and maxval are both 255.
            mode: operation mode, background True, foreground False, default foreground operation
            return: returns the text list
        """
        if hwnd_or_image_path.isdigit():
            text_info_list = self.ocr_server_by_hwnd(ocr_server_id, hwnd_or_image_path, region, algorithm, mode)
        else:
            text_info_list = self.ocr_server_by_file(ocr_server_id, hwnd_or_image_path, region, algorithm)

        return text_info_list

    def find_text(self, ocr_server_id: str, hwnd_or_image_path: str, text: str, region: tuple = (0, 0, 0, 0), algorithm: tuple = (0, 0, 0), mode: bool = False) -> list:
        """
            通过 OCR 识别窗口/图片中的文字
            Recognize the characters in the window/picture through OCR, and return the coordinate list

            ocr_server_id: ocr服务端IP，端口固定为9527
            hwnd_or_image_path: 句柄或者图片路径
            text: 要查找的文字
            region: 识别区域，默认全屏
            algorithm: 处理图片/屏幕所用算法和参数，默认保存原图
            threshold二值化图片, thresholdType算法类型：
                                                      0   THRESH_BINARY算法，当前点值大于阈值thresh时，取最大值maxva，否则设置为0
                                                      1   THRESH_BINARY_INV算法，当前点值大于阈值thresh时，设置为0，否则设置为最大值maxva
                                                      2   THRESH_TOZERO算法，当前点值大于阈值thresh时，不改变，否则设置为0
                                                      3   THRESH_TOZERO_INV算法，当前点值大于阈值thresh时，设置为0，否则不改变
                                                      4   THRESH_TRUNC算法，当前点值大于阈值thresh时，设置为阈值thresh，否则不改变
                                                      5   ADAPTIVE_THRESH_MEAN_C算法，自适应阈值
                                                      6   ADAPTIVE_THRESH_GAUSSIAN_C算法，自适应阈值
                                thresh阈值，maxval最大值，threshold默认保存原图。thresh和maxval同为255时灰度处理
            mode: 操作模式，后台 true，前台 false, 默认前台操作
            return: 文字坐标列表

            ocr_server_id: the IP of the ocr server, and the port is fixed at 9527
            hwnd_or_image_path: handle or image path
            text: the text to find
            region: recognition region, full screen by default
            algorithm: the algorithm and parameters used to process the picture/screen, and the original picture is saved by default
            threshold binary image, thresholdType algorithm type:
                0 THRESH_BINARY algorithm, when the current point value is greater than the threshold thresh, take the maximum maxva, otherwise set to 0.
                1 THRESH_BINARY_INV algorithm, when the current point value is greater than the threshold thresh, set it to 0, otherwise set it to the maximum maxva.
                2 THRESH_TOZERO algorithm, when the current point value is greater than the threshold thresh, it will not change, otherwise it will be set to 0.
                3 THRESH_TOZERO_INV algorithm, when the current point value is greater than the threshold thresh, it is set to 0, otherwise it will not change.
                4 THRESH_TRUNC algorithm, when the current point value is greater than the threshold thresh, set it as the threshold thresh, otherwise it will not change.
                5 ADAPTIVE_THRESH_MEAN_C algorithm, adaptive threshold
                6 adaptive _ threshold _ Gaussian _ c algorithm, adaptive threshold.
                Threshold threshold, maxval maximum, threshold saves the original image by default. Gray processing when thresh and maxval are both 255.
            mode: operation mode, background true, foreground false, default foreground operation
            return: list of text coordinates
        """

        if hwnd_or_image_path.isdigit():
            text_info_list = self.ocr_server_by_hwnd(ocr_server_id, hwnd_or_image_path, region, algorithm, mode)
        else:
            text_info_list = self.ocr_server_by_file(ocr_server_id, hwnd_or_image_path, region, algorithm)

        text_points = []
        for item in text_info_list:
            full_text = item["text"]
            if text in full_text:
                x1, y1, x2, y2 = item["box"]
                
                # 文本区域尺寸
                width = x2 - x1
                height = y2 - y1
                
                # 跳过空文本或无效 box
                if len(full_text) == 0 or width <= 0 or height <= 0:
                    continue
                
                # 等宽假设：每个字符宽度
                single_char_width = width / len(full_text)
                
                # 查找子串首次出现位置
                pos = full_text.find(text)
                if pos == -1:
                    continue  # 理论不会发生
                
                # 子串中心相对于 box 左上角的偏移
                sub_width = len(text) * single_char_width
                offset_x = pos * single_char_width + sub_width / 2
                offset_y = height / 2
                
                # 绝对坐标（加上 region 偏移）
                point_x = region[0] + x1 + offset_x
                point_y = region[1] + y1 + offset_y
                
                text_points.append((float(point_x), float(point_y)))
        
        return text_points