import re

class ScreenProjectionOperation:
    """
        投屏操作
        Screen projection operation
    """

    def get_group_id(self) -> str:
        """
            获取投屏组号
            Get the projection group number

            return: 组号
            return: group number
        """
        response = self.SendData("getGroup")
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        return response

    def get_identifier(self) -> str:
        """
            获取投屏编号
            Get the projection number

            return: 编号
            return: number
        """
        response =  self.SendData("getIdentifier")
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        return response

    def get_title(self) -> str:
        """
            获取投屏标题
            Get the title of the projection screen

            return: 标题
            return: title
        """
        response = self.SendData("getTitle")
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        return response


