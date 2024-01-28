

class KeymouseOperation:
    """
        鼠标键盘操作
        Mouse and keyboard operation
    """

    def click_mouse_by_element(self, xpath: str, typ: int) -> bool:
        """
            根据元素位置点击鼠标(元素中心点)

            xpath: 元素 xpath 路径
            typ: 点击类型，单击左键:1 单击右键:2 按下左键:3 弹起左键:4 按下右键:5 弹起右键:6 双击左键:7
            return: 布尔值

            xpath: Element xpath path
            typ: Click type, click left key: 1 Right click: 2 Press left key: 3 Pop up left key: 4 Press right key: 5 Pop up right key: 6 Double click left key: 7
            return: bool
        """
        return "true" in self.SendData("clickMouseByXpath", xpath, typ)

    def move_to_element(self, xpath: str) -> bool:
        """
            移动鼠标到元素位置(元素中心点)
            Move the mouse to the element position (element center point)

            xpath: 元素 xpath 路径
            return: 布尔值

            xpath: Element xpath path
            return: bool
        """
        return "true" in self.SendData("moveMouseByXpath", xpath)

    def scroll_mouse_by_element(self, xpath: str, offset_x: float, offset_y: float) -> bool:
        """
            根据元素位置滚动鼠标
            Scroll the mouse according to the element position.

            xpath: 元素路径
            offset_x: 水平滚动条移动的距离
            offset_y: 垂直滚动条移动的距离
            return: 布尔值

            xpath: xpath path
            offset_x: The distance the horizontal scroll bar moves
            offset_y: Distance the vertical scroll bar moves.
            return: bool
        """
        return "true" in self.SendData("wheelMouseByXpath", offset_x, offset_y, xpath)

    def click_mouse(self, point: tuple, typ: int) -> bool:
        """
            点击鼠标
            click the mouse

            point: 坐标点
            typ: 点击类型，单击左键:1 单击右键:2 按下左键:3 弹起左键:4 按下右键:5 弹起右键:6 双击左键:7
            return: 布尔值

            point: coordinate point
            typ: Click type, click left key: 1 Click right key: 2 Press left key: 3 Pop up left key: 4 Press right key: 5 Pop up right key: 6 Double click left key: 7
            return: Boolean value
        """
        return "true" in self.SendData("clickMouse", point[0], point[1], typ) 

    def move_mouse(self, point: tuple) -> bool:
        """
            移动鼠标
            Move the mouse

            point: 坐标点
            return: 布尔值

            point: coordinate point
            return: Boolean value
        """
        return "true" in self.SendData("moveMouse", point[0], point[1])

    def scroll_mouse(self, point: tuple = (0,0) ,offset_x: float = 0, offset_y: float = 100) -> bool:
        """
            滚动鼠标
            Scroll mouse

            point 鼠标x, y坐标位置
            offset_x: 水平滚动条移动的距离
            offset_y: 垂直滚动条移动的距离
            return: 布尔值

            point mouse x, y coordinate position
            offset_x: the distance that the horizontal scroll bar moves
            offset_y: the distance that the vertical scroll bar moves
            return: Boolean value
        """
        return "true" in self.SendData("wheelMouse", offset_x, offset_y, point[0], point[1])