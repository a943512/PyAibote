import re


class OcrCorrelation:
    """
        OCR 文字识别
        optical character recognition
    """
    def _parsing_ocr_data(self, ocr_server_id: str = "127.0.0.1", region: tuple = (0,0,0,0), algorithm: tuple = (0,0,0), scale: float = 1.0)-> list:
        """
            OCR 文字服务，识别屏幕中的文字
            OCR text service, which recognizes the text on the screen

            ocr_server_id: ocr服务端IP，端口固定为9527。当参数值为 "127.0.0.1"时，则使用手机内置的ocr识别
            region 指定区域 [10, 20, 100, 200]，region默认全屏
            algorithm: threshold二值化图片 (algorithm_type: 算法类型, threshold: 默认保存原图。thresh和maxval同为255时灰度处理 , max_val: 最大值)
                                                0   THRESH_BINARY算法，当前点值大于阈值thresh时，取最大值maxva，否则设置为0
                                                1   THRESH_BINARY_INV算法，当前点值大于阈值thresh时，设置为0，否则设置为最大值maxva
                                                2   THRESH_TOZERO算法，当前点值大于阈值thresh时，不改变，否则设置为0
                                                3   THRESH_TOZERO_INV 算法，当前点值大于阈值thresh时，设置为0，否则不改变
                                                4   THRESH_TRUNC算法，当前点值大于阈值thresh时，设置为阈值thresh，否则不改变
                                                5   ADAPTIVE_THRESH_MEAN_C算法，自适应阈值
                                                6   ADAPTIVE_THRESH_GAUSSIAN_C 算法，自适应阈值
            scale: 图片缩放率, 默认为 1.0 原大小。大于1.0放大，小于1.0缩小，不能为负数。
            return:  失败返回None，成功返回手机屏幕上的文字

            ocr_server_id: the IP of the ocr server, and the port is fixed at 9527. When the parameter value is "127.0.0.1", the built-in ocr of the mobile phone is used for recognition.
            region specifies the area [10, 20, 100, 200], and the region defaults to full screen
            algorithm: threshold binary image (algorithm_type: algorithm type, threshold: the original image is saved by default. Gray processing when thresh and maxval are both 255, max_val: maximum)
                0 THRESH_BINARY algorithm, when the current point value is greater than the threshold thresh, take the maximum maxva, otherwise set to 0
                1 THRESH_BINARY_INV algorithm, when the current point value is greater than the threshold thresh, set it to 0, otherwise set it to the maximum maxva
                2 THRESH_TOZERO algorithm, when the current point value is greater than the threshold thresh, it will not change, otherwise it will be set to 0
                3 THRESH_TOZERO_INV algorithm, when the current point value is greater than the threshold thresh, it is set to 0, otherwise it will not change
                4 THRESH_TRUNC algorithm, when the current point value is greater than the threshold thresh, set it as the threshold thresh, otherwise it will not change
                5 ADAPTIVE_THRESH_MEAN_C algorithm, adaptive threshold
                6 ADAPTIVE_THRESH_GAUSSIAN_C algorithm, adaptive threshold
            scale: the image scaling rate, which defaults to 1.0 original size. Magnification greater than 1.0 and reduction less than 1.0 cannot be negative
            return: return to None in case of failure, and successfully return the text on the mobile phone screen

        """

        algorithm_type, threshold, max_val = algorithm
        if algorithm_type in (5, 6):
            threshold = 127
            max_val = 255
        response = self.SendData("ocr", ocr_server_id, *region, algorithm_type, threshold, max_val, scale)
        if response == "null" or response == "":
            return []
        return eval(response)

    # def init_ocr_server(self, ip: str="127.0.0.1", useAngleModel:bool = False, enableGPU:bool =False, enableTensorrt:bool=False) -> bool:
    #     """
    #         初始化 OCR 服务
    #         Initialize OCR service
            
    #         ip: ocr服务IP或域名。端口固定 9527。当参数值为 "127.0.0.1"时，则使用手机内置的ocr识别，不必打开ppocr.exe服务端 默认值为 "127.0.0.1
    #         options: 可选参数，{useAngleModel:boolean, enableGPU:boolean, enableTensorrt:boolean}  仅外部OCR ocrServer ppocr.exe有效
    #             useAngleModel:   支持图像旋转。 默认False
    #             enableGPU:       启动GPU 模式。默认False 。GPU模式需要电脑安装NVIDIA驱动，并且到群文件下载对应cuda版本
    #             enableTensorrt : 启动加速，仅 enableGPU = true 时有效，默认False 。图片太大可能会导致GPU内存不足
    #         return: True 或者 False

    #         ip: ocr service IP or domain name. Port fixed 9527. When the parameter value is "127.0.0.1", the built-in ocr recognition of the mobile phone is used, and the default value is "127.0.0.1" without opening the ppocr.exe server
    #         options: optional parameter, {useanglemodel: Boolean, EnableGPU: Boolean, EnableTensort: Boolean} Only external OCR OCR Server ppocr.exe is valid.
    #             useAngleModel: supports image rotation. Default False
    #             enableGPU: start GPU mode. Default is False. GPU mode requires the computer to install NVIDIA driver and download the corresponding cuda version from the group file
    #             enableTensorrt: Starts acceleration, which is valid only when enableGPU = true, and the default is False. Too large a picture may lead to insufficient GPU memory
    #         return: True or False
    #     """
    #     return "true" in self.SendData("initOcr", ip,useAngleModel, enableGPU, enableTensorrt) 

    def get_text(self, ocr_server_id: str = "127.0.0.1", region: tuple = (0,0,0,0), algorithm: tuple = (0,0,0), scale: float = 1.0) -> list:
        """
            通过 OCR 识别屏幕中的文字，返回文字列表

            ocr_server_id: ocr服务端IP，端口固定为9527。当参数值为 "127.0.0.1"时，则使用手机内置的ocr识别
            region: 识别区域，默认全屏；
            algorithm: 处理图片/屏幕所用算法和参数，默认保存原图；
            threshold二值化图片, thresholdType算法类型：
                                                      0   THRESH_BINARY算法，当前点值大于阈值thresh时，取最大值maxva，否则设置为0
                                                      1   THRESH_BINARY_INV算法，当前点值大于阈值thresh时，设置为0，否则设置为最大值maxva
                                                      2   THRESH_TOZERO算法，当前点值大于阈值thresh时，不改变，否则设置为0
                                                      3   THRESH_TOZERO_INV算法，当前点值大于阈值thresh时，设置为0，否则不改变
                                                      4   THRESH_TRUNC算法，当前点值大于阈值thresh时，设置为阈值thresh，否则不改变
                                                      5   ADAPTIVE_THRESH_MEAN_C算法，自适应阈值
                                                      6   ADAPTIVE_THRESH_GAUSSIAN_C算法，自适应阈值
                                thresh阈值，maxval最大值，threshold默认保存原图。thresh和maxval同为255时灰度处理
            scale: 图片缩放率，默认为 1.0，1.0 以下为缩小，1.0 以上为放大
            return: 文字列表

            ocr_server_id: the IP of the ocr server, and the port is fixed at 9527. When the parameter value is "127.0.0.1", the built-in ocr of the mobile phone is used for recognition.
            region: recognition region, full screen by default;
            algorithm: the algorithm and parameters used to process the picture/screen, and the original picture is saved by default
            threshold binary image, thresholdType algorithm type:
                0 THRESH_BINARY algorithm, when the current point value is greater than the threshold thresh, take the maximum maxva, otherwise set to 0.
                1 THRESH_BINARY_INV algorithm, when the current point value is greater than the threshold thresh, set it to 0, otherwise set it to the maximum maxva.
                2 THRESH_TOZERO algorithm, when the current point value is greater than the threshold thresh, it will not change, otherwise it will be set to 0.
                3 THRESH_TOZERO_INV algorithm, when the current point value is greater than the threshold thresh, it is set to 0, otherwise it will not change.
                4 THRESH_TRUNC algorithm, when the current point value is greater than the threshold thresh, set it as the threshold thresh, otherwise it will not change.
                5 ADAPTIVE_THRESH_MEAN_C algorithm, adaptive threshold
                6 adaptive _ threshold _ Gaussian _ c algorithm, adaptive threshold.
            scale: the zoom rate of the picture, which is 1.0 by default; below 1.0, it means zooming out; above 1.0, it means zooming in
            return: text list
        """
        
        text_info_list = self._parsing_ocr_data(ocr_server_id, region, algorithm, scale)
        return text_info_list

    def find_text(self, ocr_server_id: str, text: str, region: tuple = (0,0,0,0), algorithm: tuple = (0,0,0), scale: float = 1.0) -> tuple:
        """
            查找文字所在的坐标，返回坐标列表（坐标是文本区域中心位置）
            Find the coordinates of the text and return a list of coordinates (coordinates are the center of the text area)

            ocr_server_id: ocr服务端IP，端口固定为9527。当参数值为 "127.0.0.1"时，则使用手机内置的ocr识别
            text: 要查找的文字；
            region: 识别区域，默认全屏；
            algorithm: 处理图片/屏幕所用算法和参数，默认保存原图；
            scale: 图片缩放率，默认为 1.0，1.0 以下为缩小，1.0 以上为放大；
            return: 坐标列表（坐标是文本区域中心位置）,找不到返回空列表 []

            ocr_server_id: the IP of the ocr server, and the port is fixed at 9527. When the parameter value is "127.0.0.1", the built-in ocr of the mobile phone is used for recognition.
            text: the text to find
            region: recognition region, full screen by default
            algorithm: the algorithm and parameters used to process the picture/screen, and the original picture is saved by default
            scale: the zoom rate of the picture, which is 1.0 by default; below 1.0, it is reduced; above 1.0, it is enlarged
            return: list of coordinates (coordinates are the center position of the text area), and the return empty list [] cannot be found
        """

        text_info_list = self._parsing_ocr_data(ocr_server_id, region, algorithm, scale)
        if text_info_list ==[]:
            return text_info_list

        default_tuple = ()
        for item in text_info_list:
            full_text = item["text"]
            if text in full_text:
                x1, y1, x2, y2 = item["box"]
        
                total_width = x2 - x1
                total_height = y2 - y1
                
                if len(full_text) == 0:
                    continue
                char_width = total_width / len(full_text)
                
                pos = full_text.find(text)
                if pos == -1:
                    continue  
                
                sub_text_width = len(text) * char_width
                offset_x = pos * char_width + sub_text_width / 2
                offset_y = total_height / 2
                
                abs_x = region[0] + x1 + offset_x
                abs_y = region[1] + y1 + offset_y
                
                scaled_x = abs_x / scale
                scaled_y = abs_y / scale
    
                return (float(scaled_x), float(scaled_y))
        return default_tuple