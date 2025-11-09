
import json,requests


class YoloService:
    """
        Yolo 目标检测
        Yolo target detection
    """

    # def init_yolo_server(self, ip: str, model_path: str , classes_path:str) -> bool:
    #     """
    #         初始化 yolo 服务
    #         Initialize yolo service

    #         ip: yolo 服务 IP 或域名，端口固定9528
    #         model_path: 模型路径比如：  "d:/yolov8n.onnx"
    #         classes_path 种类路径，CPU模式需要此参数比如： "d:/classes.txt"
    #         return: True 或者 False

    #         ip: yolo service IP or domain name, with fixed port 9528
    #         model_path: model path, such as "d:/yolov8n.onnx"
    #         classes_path path, which is required for CPU mode, such as "d:/classes.txt"
    #         return: True or False
    #     """
    #     return "true" in self.SendData("initYolo", ip, model_path, classes_path) 

    def yolo(self, ocr_server_id: str, region: tuple = (0,0,0,0), scale: float = 1.0) -> list:
        """
            yolo 目标检测
            Yolo target detection

            ocr_server_id: yolo服务端IP，端口固定为9528
            scale: 图片缩放率, 默认为 1.0 原大小。大于 1.0 放大，小于 1.0 缩小，不能为负数。
            region: 识别区域，默认全屏
            return: 失败返回[]，成功返回数组形式的识别结果， 0~3目标矩形位置  4目标类别  5置信度

            ocr_server_id: Yolo server IP, the port is fixed at 9528
            scale: the image scaling rate, which defaults to 1.0 original size. Magnification greater than 1.0 and reduction less than 1.0 cannot be negative
            region: Recognition area, default full screen
            return: failed to return [], successfully returned the recognition result in the form of array, 0~3 target rectangle position 4 target category 5 confidence
        """
        response = self.SendData("yolo", ocr_server_id, *region, scale)
        if response == "null" or response == "":
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