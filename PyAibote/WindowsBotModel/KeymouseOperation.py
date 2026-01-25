

class KeymouseOperation:
    """
        键鼠操作
        Keymouse operation
    """

    def move_mouse(self, hwnd: str, x: float, y: float, mode: bool = False, ele_hwnd: str = "0") -> bool:
        """
            移动鼠标

            hwnd: 当前窗口句柄
            x: 横坐标
            y: 纵坐标
            mode: 操作模式，后台 True，前台 False, 默认前台操作
            ele_hwnd: 元素句柄，如果 mode=True 且目标控件有单独的句柄，则需要通过 get_element_window 获得元素句柄，指定 ele_hwnd 的值(极少应用窗口由父窗口响应消息，则无需指定)
            return: 总是返回True

            hwnd: Current window handle
            x: abscissa
            y: ordinate
            mode: Operation mode, background True, foreground False, default foreground operation
            ele_hwnd: Element handle, if mode=True and the target control has a separate handle, you need to get the element handle through get_element_window, and specify the value of ele_hwnd (it is unnecessary to specify if the application window is rarely responded to by the parent window)
            return: Always returns True
        """
        return "true" in self.SendData("moveMouse", hwnd, x, y, mode, ele_hwnd)

    def move_mouse_relative(self, hwnd: str, x: float, y: float, mode: bool = False) -> bool:
        """
            移动鼠标(相对坐标)
            Move the mouse (relative coordinates)

            hwnd: 当前窗口句柄
            x: 相对横坐标
            y: 相对纵坐标
            mode: 操作模式，后台 True，前台 False, 默认前台操作
            return: 总是返回True

            hwnd: Current window handle
            x: Relative abscissa
            y: Relative ordinate
            mode: Operation mode, background True, foreground False, default foreground operation
            return: Always returns True
        """
        return "true" in self.SendData("moveMouseRelative", hwnd, x, y, mode)

    def scroll_mouse(self, hwnd: str, x: float, y: float, count: int, mode: bool = False) -> bool:
        """
            滚动鼠标
            Scroll mouse

            hwnd: 当前窗口句柄
            x: 横坐标
            y: 纵坐标
            count: 鼠标滚动次数, 负数下滚鼠标, 正数上滚鼠标
            mode: 操作模式，后台 True，前台 False, 默认前台操作
            return: 总是返回True

            hwnd: Current window handle
            x: abscissa
            y: ordinate
            count: The number of mouse scrolling, negative scrolling down, positive scrolling up
            mode: Operation mode, background True, foreground False, default foreground operation
            return: Always returns True
        """
        return "true" in self.SendData("rollMouse", hwnd, x, y, count, mode)

    def click_mouse(self, hwnd: str, x: float, y: float, typ: int, mode: bool = False, ele_hwnd: str = "0") -> bool:
        """
            鼠标点击
            Mouse click

            hwnd: 当前窗口句柄
            x: 横坐标
            y: 纵坐标
            typ: 点击类型，单击左键:1 单击右键:2 按下左键:3 弹起左键:4 按下右键:5 弹起右键:6 双击左键:7 双击右键:8
            mode: 操作模式，后台 true，前台 false, 默认前台操作
            ele_hwnd: 元素句柄，如果 mode=True 且目标控件有单独的句柄，则需要通过 get_element_window 获得元素句柄，指定 ele_hwnd 的值(极少应用窗口由父窗口响应消息，则无需指定);
            return: 总是返回True

            hwnd: Current window handle
            x: abscissa
            y: ordinate
            typ: Click type, click left key: 1 Right key: 2 Press left key: 3 Pop up left key: 4 Press right key: 5 Pop up right key: 6 Double click left key: 7 Double click right key: 8
            mode: Operation mode, background True, foreground False, default foreground operation
            ele_hwnd: Element handle, if mode=True and the target control has a separate handle, you need to get the element handle through get_element_window, and specify the value of ele_hwnd (it is unnecessary to specify if the application window is rarely responded to by the parent window)
            return: Always returns True
        """
        return "true" in self.SendData("clickMouse", hwnd, x, y, typ, mode, ele_hwnd) 

    def send_keys(self, text: str) -> bool:
        """
            输入文本
            Input text

            text: 输入的文本
            return: 总是返回True

            text: Entered text
            return: Always returns True
        """
        return "true" in self.SendData("sendKeys", text) 

    def send_keys_by_hwnd(self, hwnd: str, text: str) -> bool:
        """
            后台输入文本(杀毒软件可能会拦截)
            Enter text in the background (antivirus software may intercept it)

            hwnd: 窗口句柄
            text: 输入的文本
            return: 总是返回True

            hwnd: Window handle
            text: Entered text
            return: Always returns True
        """
        return "true" in self.SendData("sendKeysByHwnd", hwnd, text)

    def send_vk(self, vk: int, typ: int) -> bool:
        """
            输入虚拟键值(VK)
            Enter the virtual key value (VK)

            vk: VK键值  按键对照表: https://blog.csdn.net/qq_42372031/article/details/105178789
            typ: 输入类型，按下弹起:1 按下:2 弹起:3
            return: 总是返回True

            vk: VK key value key table: https://blog.csdn.net/qq_42372031/article/details/105178789
            typ: Enter the type, press and pop up: 1 press: 2 pop up: 3
            return: Always returns True
        """
        return "true" in self.SendData("sendVk", vk, typ)

    def send_vk_by_hwnd(self, hwnd: str, vk: int, typ: int) -> bool:
        """
            后台输入虚拟键值(VK)
            Background input virtual key value (VK)

            hwnd: 窗口句柄
            vk: VK键值
            typ: 输入类型，按下弹起:1 按下:2 弹起:3
            return: 总是返回True

            hwnd: Window handle
            vk: VK key value
            typ: Enter the type, press and pop up: 1 press: 2 pop up: 3
            return: Always returns True
        """
        return "true" in self.SendData("sendVkByHwnd", hwnd, vk, typ)




