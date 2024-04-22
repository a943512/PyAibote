import re
import json


class YoloService:
    """
        Yolo 目标检测
        Yolo target detection
    """

    def init_yolo_server(self, ip: str, model_path: str , classes_path:str) -> bool:
        """
            初始化 yolo 服务
            Initialize yolo service

            ip: yolo 服务 IP 或域名，端口固定9528
            model_path: 模型路径比如：  "d:/yolov8n.onnx"
            classes_path 种类路径，CPU模式需要此参数比如： "d:/classes.txt"
            return: True 或者 False

            ip: yolo service IP or domain name, with fixed port 9528
            model_path: model path, such as "d:/yolov8n.onnx"
            classes_path path, which is required for CPU mode, such as "d:/classes.txt"
            return: True or False
        """
        return "true" in self.SendData("initYolo", ip, model_path, classes_path) 

    def yolo(self, scale: float = 1.0) -> list:
        """
            yolo 目标检测
            Yolo target detection

            scale: 图片缩放率, 默认为 1.0 原大小。大于 1.0 放大，小于 1.0 缩小，不能为负数。
            return: 失败返回[]，成功返回数组形式的识别结果， 0~3目标矩形位置  4目标类别  5置信度

            scale: the image scaling rate, which defaults to 1.0 original size. Magnification greater than 1.0 and reduction less than 1.0 cannot be negative
            return: failed to return [], successfully returned the recognition result in the form of array, 0~3 target rectangle position 4 target category 5 confidence
        """
        response = self.SendData("yolo", scale)
        if response == "null":
            return []
        return json.loads(response)
