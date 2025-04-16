import re
import json,requests

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

    def yolo_by_hwnd(self, hwnd: int, region: tuple = (0, 0, 0, 0), mode: bool = False) -> list:
        """
            yolo 根据窗口句柄目标检测
            Yolo target detection based on window handle

            hwnd: 窗口句柄
            region: (左上角x点, 左上角y点, 右下角 x点, 右下角 y点)
            mode: 操作模式，后台 True，前台 False。默认前台操作 
            return: 失败返回空[]，成功返回数组形式的识别结果。 0~3目标矩形位置  4目标类别  5置信度

            hwnd: Window handle
            region: (point X in the upper left corner, point Y in the upper left corner, point X in the lower right corner, point Y in the lower right corner)
            mode: Operation mode, background True, foreground False. Default foreground operation
            return: Failed to return empty [], successfully returned the recognition result in the form of array. 0~3 Target Rectangular Position 4 Target Category 5 Confidence
        """
        response = self.SendData("yoloByHwnd", hwnd, *region, mode)
        if response == "null":
            return []
        return json.loads(response)

    def yolo_by_file(self, file_path: str, region: tuple = (0, 0, 0, 0)) -> list:
        """
            yolo 根据图片进行目标检测
            Yolo carries out target detection according to the picture.

            file_path: 图片路径
            region: (左上角x点, 左上角y点, 右下角 x点, 右下角 y点)
            return:  失败返回空[]，成功返回数组形式的识别结果。 0~3目标矩形位置  4目标类别  5置信度

            file_path: Picture path
            region: (point X in the upper left corner, point Y in the upper left corner, point X in the lower right corner, point Y in the lower right corner)
            return:  Failed to return empty [], successfully returned the recognition result in the form of array. 0~3 Target Rectangular Position 4 Target Category 5 Confidence
        """
        response = self.SendData("yoloByFile", file_path, *region)
        if response == "null":
            return []
        return json.loads(response)

    def yolo_tool_by_file(self, tool_server_ip: str, tool_server_port: str, file_path: str, is_get_class_name: str = '0') -> dict:
        """
            yolo综合工具 根据图片进行目标检测
            Yolo integrated tools detect targets according to pictures

            tool_server_ip: 工具部署电脑的IP地址 本机部署就是 127.0.0.1, 公网写公网IP
            tool_server_port： 需要和工具上面填写的端口号一致
            file_path: 图片路径
            region: (左上角x点, 左上角y点, 右下角 x点, 右下角 y点)
            is_get_class_name： 获取pt模型中所有训练的类名 0：不获取  1：获取
            return:  失败返回空{}，成功返回数组形式的识别结果。 0~3目标矩形位置  4目标类别  5置信度

            tool_server_ip: the IP address of the tool deployment computer. The local deployment is 127.0.0.1, and the public network writes the public network IP.
            tool_server_port: it needs to be consistent with the port number filled in the tool.
            file_path: image path.
            region: (point X in the upper left corner, point Y in the upper left corner, point X in the lower right corner, point Y in the lower right corner)
            is_get_class_name: Get the class names of all trainings in pt model 0: Don't get 1: Get.
            return: failed to return an empty {}, and successfully returned the recognition result in the form of an array. 0~3 Target Rectangular Position 4 Target Category 5 Confidence
        """

        url = f'http://{tool_server_ip}:{tool_server_port}/pt_model_predict'

        with open(file_path, 'rb') as f:
            image_content = f.read()

        files = {'file': image_content}
        data = {'get_class_name': is_get_class_name}

        response = requests.post(url, files=files, data=data)
        if response.status_code == 200:
            data_json = json.loads(response.text)
            return data_json
        else:
            return {}