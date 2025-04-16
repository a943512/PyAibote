import re
import json


class ElementOperation:
    """
        元素操作 
        Element operation
    """

    def is_displayed(self, xpath: str) -> bool:
        """
            元素是否可见
            Is the element visible

            xpath: xpath 路径
            return: 布尔值

            xpath: xpath path
            return: bool
        """
        return "true" in self.SendData("isDisplayed", xpath)

    def is_available(self, xpath: str) -> bool:
        """
            判断元素是否可用
            Determines whether an element is available.

            xpath: xpath 路径
            return: 布尔值

            xpath: xpath path
            return: bool
        """
        return "true" in self.SendData("isEnabled", xpath)

    def is_selected(self, xpath: str) -> bool:
        """
            元素是否已选中
            Whether the element is selected

            xpath: xpath 路径
            return: 布尔值

            xpath: xpath path
            return: bool
        """

        return "true" in self.SendData("isSelected", xpath)

    def get_element_outer_html(self, xpath: str) -> str:
        """
            获取元素的HTML包含对象本身以及所有子节点
            Gets the HTML of the element including the object itself and all child nodes

            xpath: xpath 路径
            return: HTML 带标签格式文本

            xpath: xpath path
            return: HTML tagged text
        """
        response = self.SendData("getElementOuterHTML", xpath)
        if response == "null":
            return None
        return response

    def get_element_inner_html(self, xpath: str) -> str:
        """
            获取元素的HTML所有子节点不包含对象本身
            Gets the HTML of the element. All child nodes do not contain the object itself

            xpath: xpath 路径
            return: HTML 带标签格式文本

            xpath: xpath path
            return: HTML tagged text
        """
        response = self.SendData("getElementInnerHTML", xpath)
        if response == "null":
            return None
        return response

    def get_element_text(self, xpath: str) -> str:
        """
            获取元素文本
            Get element text

            xpath: 元素的 xpath 路径
            return: 元素文本字符串或 None

            xpath: xpath path of the element
            return: element text string or None
        """
        response = self.SendData("getElementText", xpath)
        if "null" in response:
            return None
        return response

    def get_element_attr(self, xpath: str, attr_name: str) -> str:
        """
            获取元素HTML属性
            Gets the HTML attribute of the element

            xpath: xpath 路径
            attr_name: 属性名称
            return: 字符串

            xpath: xpath path
            attr_name: attribute name
            return: string
        """
        response = self.SendData("getElementAttribute", xpath, attr_name)
        if response == "null":
            return None
        return response

    def get_element_value(self, xpath: str) -> str:
        """
            获取input编辑框中的值
            Gets the value in the input edit box

            xpath: input输入框中的xpath路径
            return: 成功返回input输入框的值失败返回None

            xpath: XPath path in the input input box
            return: returns the value of the input input box successfully, and returns None if it fails
        """

        command =   """(function () {\
            let element = document.evaluate('"""
            
        command2 = """', document).iterateNext();\
            if(element == null)\
                return null;\
            else\
                return element.value;\
            })()"""
        command3 = command+xpath+command2
        response = self.execute_script(command3)
        if response == "None":
            return None
        return response

    def click_element(self, xpath: str) -> bool:
        """
            点击元素
            Click element

            xpath: 元素的 xpath 路径
            return: 布尔值

            xpath:  xpath path of the element
            return: Boolean value
        """
        return "true" in self.SendData("clickElement", xpath)

    def clear_element(self, xpath: str) -> bool:
        """
            清除元素值
            Clear element value

            xpath: xpath 路径
            return: 布尔值

            xpath: xpath path
            return: bool
        """
        return "true" in self.SendData("clearElement", xpath)

    def set_element_focus(self, xpath: str) -> bool:
        """
            设置元素焦点
            Set element focus

            xpath: xpath 路径
            return: 布尔值

            xpath: xpath path
            return: bool
        """
        return "true" in self.SendData("setElementFocus", xpath)

    def send_keys(self, xpath: str, value: str) -> bool:
        """
            用于模拟键盘输入，输入的字符会往后叠加；如果元素不能设置焦点，应先 click_mouse 点击元素获得焦点后再输入
            Used to simulate keyboard input, and the input characters will be superimposed later; If the element can't set the focus, click_mouse to get the focus before entering

            xpath: 元素 xpath 路径
            value: 输入的内容
            return: 布尔值

            xpath: xpath path of element
            value: the content entered
            return: Boolean value
        """
        return "true" in self.SendData("sendKeys", xpath, value)

    def set_element_value(self, xpath: str, value: str) -> bool:
        """
            设置元素值 (与send_keys原理一样不同的是set_element_value不会往后叠加字符)
            Set the element value (the same difference as the principle of send_keys is that set_element_value does not superimpose characters later)

            xpath: 元素 xpath 路径
            value: 设置的内容
            return: 布尔值

            xpath: xpath path of element
            value: the content of the setting
            return: Boolean value
        """
        return "true" in self.SendData("setElementValue", xpath, value)

    def send_vk(self, vk: str) -> bool:
        """
            发送Vk虚拟键码, 按键对照表: http://www.atoolbox.net/Tool.php?Id=815
            Send Vk virtual key code Key comparison table

            vk: 输入内容
            return: 布尔值

            vk: input content   http://www.atoolbox.net/Tool.php?Id=815
            return: Boolean value.
        """
        return "true" in self.SendData("sendVk", vk)

    def set_element_attr(self, xpath: str, attr_name: str, attr_value: str) -> bool:
        """
            设置元素属性
            Set element properties

            xpath: 元素 xpath 路径
            attr_name: 属性名称
            attr_value: 属性值
            return: 布尔值

            xpath: xpath path of element
            attr_name: attribute name
            attr_value: attribute value
            return: Boolean value
        """
        return "true" in self.SendData("setElementAttribute", xpath, attr_name, attr_value)

    def upload_file_by_element(self, xpath: str, file_path: str) -> bool:
        """
            通过元素上传文件
            Upload files through elements

            xpath:  元素 xpath 路径
            file_path: 文件路径
            return: 布尔值

            xpath: xpath path of element
            file_path: file path
            return: bool
        """
        return "true" in self.SendData("uploadFile", xpath, file_path)

    def get_element_rect(self, xpath: str) -> tuple:
        """
            获取元素矩形坐标
            Get rectangular coordinates of elements

            xpath: xpath 路径
            return: 元素矩形坐标或None

            xpath: xpath path
            return: Element rectangular coordinates or None
        """
        response = self.SendData("getElementRect", xpath)
        if response == "null":
            return None
        Coordinate = json.loads(response)
        L = Coordinate.get("left")
        R = Coordinate.get("right")

        T = Coordinate.get("top")
        B = Coordinate.get("bottom")
        response = (L+(R-L)/2, T+(B-T)/2)
        return response

    def save_screenshot(self, xpath: str = None, path: str = 'PyAibote.png') -> str:
        """
            截图，返回 PNG 格式的 base64, 保存图片时尽量不要把浏览器开全屏会出现异常抛错情况
            Screenshot, return to base64 in PNG format

            xpath: 元素路径，如果指定该参数则截取元素图片
            path: 生成图片路径，如果不设置路径则默认在当前目录生成名为PyAibote.png图片,如果设置为空值则不生成图片
            return: PNG 格式的 base64 的字符串或 None

            xpath: the path of the element. If this parameter is specified, the image of the element will be clipped
            path: Generate the image path. If not specified, the image named PyAibote.png will be generated in the current directory by default
            return: string of base64 in PNG format or None
        """
        if xpath is None:
            response = self.SendData("takeScreenshot")
        else:
            response = self.SendData("takeScreenshot", xpath)
        if response == "null":
            return None
        if path:
            self.SaveBase64Png(response,path)
        return response

    def show_xpath(self) -> bool:
        """
            显示元素xpath路径，页面加载完毕再调用。
            调用此函数后，可在页面移动鼠标会显示元素区域。移动并按下ctrl键，会在浏览器控制台打印相对xpath 和 绝对xpath路径
            ifrmae 内的元素，需要先调用 switchFrame 切入进去，再调用showXpath函数

            return: 总是True

            Displays the xpath path of the element, and then calls it after the page is loaded.
            After calling this function, you can move the mouse on the page to display the element area. 
            Moving and pressing the ctrl key will print the relative xpath and absolute xpath paths on the browser console.
            Elements in ifrmae need to be cut in by calling switchFrame first, and then calling the showXpath function.

            return: always True
        """
        return "true" in self.SendData("showXpath")