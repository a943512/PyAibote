import re
import json

class Control:
    """
        控件操作
        Control operation
    """
    def create_text_view(self, _id: int, text: str, coordinate: tuple = (400,500), width: int = 400, height: int = 60) -> bool:
        """
            创建文本框控件
            Create a text box control

            _id:  控件ID，不可与其他控件重复
            text:  控件文本
            coordinate   默认 (400,500)
            width:  控件宽度，默认 400
            height:  控件高度，默认 60
            return: True或者False

            _id: control id, which cannot be duplicated with other controls
            text: control text
            coordinate default (400,500)
            width: the width of the control, which is 400 by default
            height: control height, 60 by default
            return: True or False
        """
        return "true" in self.SendData("createTextView", _id, text, coordinate[0], coordinate[1], width, height)

    def create_edit_view(self, _id: int, text: str, coordinate: tuple = (400,500), width: int = 400, height: int = 150) -> bool:
        """
            创建编辑框控件
            Create an edit box control

            _id:  控件ID，不可与其他控件重复
            text:  控件文本
            coordinate: x,y坐标 默认 (400,500)
            width:  控件宽度，默认 400
            height:  控件高度，默认 150
            return: True或者False

            _id: control id, which cannot be duplicated with other controls
            text: control text
            coordinate: x,y coordinates default (400,500)
            width: the width of the control, which is 400 by default
            height: control height, default is 150
            return: True or False
        """
        return "true" in self.SendData("createEditText", _id, text, coordinate[0], coordinate[1], width, height) 

    def create_check_box(self, _id: int, text: str, coordinate: tuple = (400,500), width: int = 400, height: int = 60,is_select: bool = False) -> bool:
        """
            创建复选框控件
            Create a check box control

            _id:  控件ID，不可与其他控件重复
            text:  控件文本
            coordinate:  x,y坐标 默认 (400,500)
            width:  控件宽度，默认 400
            height:  控件高度，默认 60
            is_select:  是否勾选，默认 False
            return: True或者False

            _id: control id, which cannot be duplicated with other controls
            text: control text
            coordinate: x,y coordinates default (400,500)
            width: the width of the control, which is 400 by default
            height: control height, default is 60
            is_select: whether it is checked or not; the default value is False
            return: True or False
        """
        return "true" in self.SendData("createCheckBox", _id, text, coordinate[0], coordinate[1], width, height, is_select) 

    def create_list_text(self, _id: int, hint_text: str, list_text: list, coordinate: tuple = (400,500), width: int = 400, height: int = 400) -> bool:
        """
            创建ListText控件
            Create ListText control

            _id:  控件ID，不可与其他控件重复
            hint_text:  提示文本
            list_text:  列表文本
            coordinate: x,y坐标 默认 (400,500)
            width:  控件宽度
            height:  控件高度
            return: True或者False

            _ID: control id, which cannot be duplicated with other controls
            Hint_text: prompt text
            List_text: list text
            Coordinate: x,y coordinates default (400,500)
            Width: control width
            Height: control height
            Return: True or False
        """
        return "true" in self.SendData("createListText", _id, hint_text, coordinate[0], coordinate[1], width, height, list_text) 

    def create_web_view(self, _id: int, url: str, coordinate: tuple = (-1,-1), controlsize: tuple = (-1,-1)) -> bool:
        """
            创建WebView控件(直接会打开浏览器进入页面)
            Create a WebView control (which will directly open the browser to enter the page)

            _id: 控件ID，不可与其他控件重复
            url: 加载的链接
            coordinate: 控件在屏幕上 x 坐标，值为 -1 时自动填充宽高
            controlsize: 控件宽,高度，值为 -1 时自动填充宽高
            return: True或者False

            _id: control id, which cannot be duplicated with other controls
            url: loaded link
            coordinate: the x coordinate of the control on the screen, and the width and height are automatically filled when the value is -1
            controlsize: the width and height of the control. When the value is -1, the width and height will be automatically filled
            return: True or False
        """
        return "true" in self.SendData("createWebView", _id, url, coordinate[0], coordinate[1], controlsize[0], controlsize[1]) 

    def get_script_params(self) -> dict:
        """
            获取脚本配置参数(等待用户提交控件数据)
            Get script configuration parameters (wait for the user to submit control data)

            return: 用户提交的控件数据
            return: control data submitted by the user.
        """
        response = self.SendData("getScriptParam")
        if response == "null":
            return None
        try:
            params = json.loads(response)
        except Exception as e:
            return {}
        return params

    def clear_script_widget(self) -> bool:
        """
            清除脚本控件
            Clear script control

            return: True或者False
            return: True or False
        """
        return "true" in self.SendData("clearScriptControl") 























