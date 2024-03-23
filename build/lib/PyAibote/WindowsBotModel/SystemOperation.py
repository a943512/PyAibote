import re


class SystemOperation:
    """
        系统操作
        system operation
    """

    def set_clipboard_text(self, text: str) -> bool:
        """
            设置剪切板内容
            Set the clipboard contents

            text: 要设置的内容
            return: 成功返回True 失败返回 False

            text: what to set
            return: Returns True successfully, and returns False if it fails
        """
        return "true" in self.SendData("setClipboardText", text)

    def get_clipboard_text(self) -> str:
        """
            获取剪切板内容
            Get the clipboard content

            return: 剪切板内容
            return: Shear board content
        """
        response = self.SendData("getClipboardText")
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        return  response

    def start_process(self, cmd: str, show_window=True, is_wait=False) -> bool:
        """
            启动指定程序
            Start the specified program

            cmd: 命令
            show_window: 是否显示窗口，默认显示
            is_wait: 是否等待程序结束， 默认不等待
            return: 成功返回True 失败返回 False

            cmd: command
            show_window: whether to display the window or not; it is displayed by default
            is_wait: whether to wait for the program to end; by default, it does not wait
            return: Returns True successfully, and returns False if it fails
        """
        return "true" in self.SendData("startProcess", cmd, show_window, is_wait)

    def execute_command(self, command: str, wait_timeout: int = 3) -> str:
        """
            执行cmd命令
            Execute cmd command

            command: cmd命令，不能含 "cmd"字串
            wait_timeout: 可选参数，等待结果返回超时，单位毫秒，默认3秒
            return: cmd执行结果

            Command: cmd command, which cannot contain "cmd" string.
            Wait_timeout: optional parameter, waiting for the result to return timeout, in milliseconds, the default is 300 milliseconds.
            Return: cmd execution result
        """
        return  self.SendData("executeCommand", command, wait_timeout*1000)


