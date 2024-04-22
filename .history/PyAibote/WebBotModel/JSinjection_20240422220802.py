import re


class JSinjection:
    """
        JS 注入
        JS injection
    """

    def execute_script(self, script: str) -> str:
        """
            注入执行 JS
            Injection execution JS

            script: 要执行的 JS 代码
            return: 假如注入代码有返回值，则返回此值，否则返回 None

            script: JS code to be executed
            return: If the injection code has a return value, this value is returned, otherwise None is returned
            
            示例：
            Examples:
                result = execute_script('(()=>alert(123))()')
        """
        response = self.SendData("executeScript", script)
        if response == "null":
            return None
        return response



