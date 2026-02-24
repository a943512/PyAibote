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
            Get the current page title

            return：当前页面标题 或 None
            return：current page title or None

        """
        response = self.SendData("getTitle")
        if response == "webdriver error":
            return None
        return response

    def enable_network(self, url: str, method: str) -> bool:
        """
            启用网络数据监听，此函数一般在goto、点击跳转等操作 前调用。可多次调用监听多个目标
            Enable network data monitoring. This function is generally called before operations such as goto and click jump
            Multiple calls can be made to monitor multiple targets

            url: 监听的url
            method: 监听的请求类型。'GET'或'POST'
            return: 总是返回 true

            url: url for listening
            method: the type of request to listen to. GET' or' POST'
            return: always returns true

        """
        return "true" in self.SendData("enableNetwork", url, method)

    def wait_network_data(self, timeout : int = 10) -> str:
        """
            等待获取网络数据，此函数必须在 goto、点击跳转等操作后立刻执行。执行完自动关闭 enableNetwork 设置的监听目标
            Waiting to obtain network data, this function must be executed immediately after goto, click jump and other operations
            After performing automatic shutdown of the listening target set by enableNetwork

            timeout: 等待超时,单位毫秒。默认10秒
            return: 成功返回json数组格式的数据，失败返回null

            timeout: Wait timeout, in milliseconds. Default 10 seconds
            return: data in jsons array format is returned successfully, and null is returned if it fails

        """
        return self.SendData("waitNetworkData", timeout*1000)




        