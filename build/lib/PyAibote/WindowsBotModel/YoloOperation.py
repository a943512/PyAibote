import re
import json

class YoloOperation:
    """
        yolo目标检测
        Yolo target detection
    """

    def init_yolo_server(self, ip: str, model_path: str = "d:/yolov8n.onnx", classesp_path: str = "d:/classes.txt") -> bool:
        """
            初始化 yolo 服务
            Yolo Operation

            ip: OCR 服务 IP 或域名，端口固定9528
            model_path: 模型路径
            classesp_path: 种类路径，CPU模式需要此参数
            return: 成功返回 True，失败返回False

            ip: OCR service IP or domain name, with fixed port 9528
            model_path: model path
            classesp_path: class path, which is required for CPU mode
            return: Returns True on success and False on failure
        """
        return "true" in self.SendData("initYolo", ip, model_path, classesp_path)

    def yolo_by_hwnd(self, hwnd: int, mode: bool = False) -> list:
        """
            yolo 根据窗口句柄目标检测
            Yolo target detection based on window handle

            hwnd: 窗口句柄
            mode: 操作模式，后台 True，前台 False。默认前台操作 
            return: 失败返回空[]，成功返回数组形式的识别结果。 0~3目标矩形位置  4目标类别  5置信度

            hwnd: Window handle
            mode: Operation mode, background True, foreground False. Default foreground operation
            return: Failed to return empty [], successfully returned the recognition result in the form of array. 0~3 Target Rectangular Position 4 Target Category 5 Confidence
        """
        response = self.SendData("yoloByHwnd", hwnd, mode)
        if response == "null":
            return []
        return json.loads(response)

    def yolo_by_file(self, file_path: str, mode: bool = False) -> list:
        """
            yolo 根据图片进行目标检测
            Yolo carries out target detection according to the picture.

            file_path: 图片路径
            mode: 操作模式，后台 True，前台 False。默认前台操作 
            return:  失败返回空[]，成功返回数组形式的识别结果。 0~3目标矩形位置  4目标类别  5置信度

            file_path: Picture path
            mode: Operation mode, background True, foreground False. Default foreground operation
            return:  Failed to return empty [], successfully returned the recognition result in the form of array. 0~3 Target Rectangular Position 4 Target Category 5 Confidence
        """
        response = self.SendData("yoloByFile", file_path, mode)
        if response == "null":
            return []
        return json.loads(response)
