

class IframeOperation:
    """
        iframe 操作
        IframeOperation
    """

    def switch_to_frame(self, xpath) -> bool:
        """
            切换到指定 frame
            Switch to the specified frame

            xpath: xpath 路径
            return: 布尔值

            xpath: xpath path
            return: bool
        """
        return "true" in self.SendData("switchFrame", xpath)

    def switch_to_main_frame(self) -> bool:
        """
            切回主 frame
            Switch back to the main frame

            return: 布尔值
            return: bool

        """
        return "true" in self.SendData("switchMainFrame")