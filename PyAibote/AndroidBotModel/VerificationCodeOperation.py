import re,json


class VerificationCodeOperation:
    """
        验证码
        Verification Code
    """
    def get_captcha(self, file_path: str, username: str, password: str, soft_id: str, code_type: str, len_min: str = '0') -> dict:
        """
            识别验证码
            Identification verification code

            file_path: 图片文件路径
            username: 用户名
            password: 密码
            soft_id: 软件ID
            code_type: 图片类型 参考 https://www.chaojiying.com/price.html
            len_min: 最小位数 默认0为不启用,图片类型为可变位长时可启用这个参数
            return: JSON
                err_no,(数值) 返回代码  为0 表示正常，错误代码 参考 https://www.chaojiying.com/api-23.html
                err_str,(字符串) 中文描述的返回信息 
                pic_id,(字符串) 图片标识号，或图片id号
                pic_str,(字符串) 识别出的结果
                md5,(字符串) md5校验值,用来校验此条数据返回是否真实有效

            file_path: the path of the picture file
            username: user name
            password: password
            soft_id: software id
            code_type: the picture type refers to https://www.chaojiying.com/price.html
            len_min: The minimum number of digits is not enabled by default, and this parameter can be enabled when the picture type is variable bit length
            return: JSON
                err_no, (numerical value) The return code is 0, which means normal, and the error code refers to https://www.chaojiying.com/api-23.html
                err_str, (string) the return information described in Chinese
                pic_id, (string) picture identification number, or picture ID number
                pic_str, (string) the result of recognition
                md5, (string) md5 check value, which is used to check whether this data return is true and valid
        """
        if not file_path.startswith("/storage/emulated/0/"):
            file_path = "/storage/emulated/0/" + file_path

        response = self.SendData("getCaptcha", file_path, username, password, soft_id, code_type, len_min)
        return json.loads(response)

    def error_captcha(self, username: str, password: str, soft_id: str, pic_id: str) -> dict:
        """
            识别报错返分
            Identify and report errors and return points

            username: 用户名
            password: 密码
            soft_id: 软件ID
            pic_id: 图片ID 对应 getCaptcha返回值的pic_id 字段
            return: JSON
                err_no,(数值) 返回代码
                err_str,(字符串) 中文描述的返回信息

            username: user name
            password: password
            soft_id: software id
            pic_id: the picture id corresponds to the pic_id field of getCaptcha return value
            return: JSON
                err_no, (numeric) return code
                err_str, (string) the return information described in Chinese
        """
        response = self.SendData("errorCaptcha", username, password, soft_id, pic_id)
        return json.loads(response)

    def score_captcha(self, username: str, password: str) -> dict:
        """
            查询验证码剩余题分
            Query the remaining questions of verification code

            username: 用户名
            password: 密码
            return: JSON
                err_no,(数值) 返回代码
                err_str,(字符串) 中文描述的返回信息
                tifen,(数值) 题分
                tifen_lock,(数值) 锁定题分

            username: user name
            password: password
            return: JSON
                err_no, (numeric) return code
                err_str, (string) the return information described in Chinese
                tifen, (numerical) score
                tifen_lock, (numerical value) locks the score
        """
        response = self.SendData("scoreCaptcha", username, password)
        return json.loads(response)


