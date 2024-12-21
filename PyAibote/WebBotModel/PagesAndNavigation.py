import re


class PagesNavigation:
    """
        页面和导航功能模块
        Page and navigation function module
    """

    def goto(self, url: str) -> bool:
        """
            跳转页面
            Jump page

            url: 网址
            return: 布尔值

            url: website address
            return: bool
        """
        return "true" in self.SendData("goto", url)

    def new_page(self, url: str) -> bool:
        """
            新建 Tab 并跳转页面
            Create a new Tab and jump to the page

            url: 网址
            return: 布尔值

            url: website address
            return: bool
        """
        return "true" in self.SendData("newPage", url)

    def back(self) -> bool:
        """
            后退
            go back

            return: 布尔值
            return: bool
        """
        return "true" in self.SendData("back")

    def forward(self) -> bool:
        """
            前进
            go move

            return: 布尔值
            return: bool
        """
        return "true" in self.SendData("forward")

    def refresh(self) -> bool:
        """
            刷新
            refresh

            return: 布尔值
            return: bool
        """
        return "true" in self.SendData("refresh")

    def get_current_page_id(self) -> str:
        """
            获取当前页面 ID
            Get the current page ID

            return: 字符串, 找不到页面则返回None
            return: str or None if not found Page
        """
        response = self.SendData("getCurPageId")
        if response == "null":
            return None
        return response

    def get_all_page_id(self) -> list:
        """
            获取所有页面 ID
            Get all page ids

            return: 所有页面ID，找不到则返回空列表[]
            return: all page ID, or an empty list [] if it is not found
        """
        response = self.SendData("getAllPageId")
        if response == "null":
            return []
        return response.split("|")
    
    def switch_to_page(self, page_id: str) -> bool:
        """
            切换到指定页面
            Switch to the specified page

            page_id: 你要切换的页面ID
            return: 布尔值

            page_id: ID of the page you want to switch.
            return: bool
        """
        return "true" in self.SendData("switchPage", page_id)

    def close_current_page(self) -> bool:
        """
            关闭当前页面
            Close the current page

            return: 布尔值
            return: bool
        """
        return "true" in self.SendData("closePage")

    def get_current_url(self) -> str:
        """
            获取当前页面 URL
            Get URL of current page

            return: 当前页面URL 或 None
            return: URL of current page or None
        """
        response = self.SendData("getCurrentUrl")
        if response == "webdriver error":
            return None
        response = re.findall(r'(http.*)',response)
        if response:
            return response[0]
        else:
            return None

    def get_current_title(self) -> str:
        """
            获取当前页面标题

            return：当前页面标题 或 None
            return：current page title or None

        """
        response = self.SendData("getTitle")
        if response == "webdriver error":
            return None
        return response








        