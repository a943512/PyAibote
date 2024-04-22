import re

class PopUpWindow:
    """
        点击alert警告框
        Click the alert warning box.
    """
    
    def click_alert(self, accept: bool, prompt_text: str = "") -> bool:
        """
            点击警告框
            Click the warning box

            accept: 确认或取消
            prompt_text: 可选参数，输入的警告框文本
            return: 布尔值

            accept: Confirm or cancel
            prompt_text: Optional parameter, warning box text entered.
            return: bool
        """
        return "true" in self.SendData("clickAlert", accept, prompt_text) 

    def get_alert_text(self) -> str:
        """
            获取警告框文本
            Get warning box text

            return: 警告框文本字符串
            return: Return: warning box text string
        """
        response = self.SendData("getAlertText")
        if response == "null":
            return None
        return response