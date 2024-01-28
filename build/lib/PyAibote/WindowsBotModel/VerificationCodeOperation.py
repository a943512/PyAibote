import base64
from urllib import request as request_lib, parse

class VerificationCodeOperation:
    """
        验证码操作
        Verification code operation
    """
    def get_captcha(file_path: str, username: str, password: str, soft_id: str, code_type: str,len_min: str = '0') -> dict:
        """
            识别验证码
            Identification verification code

            file_path: 图片文件路径
            username: 用户名
            password: 密码
            soft_id: 软件ID
            code_type: 图片类型 参考https://www.chaojiying.com/price.html
            len_min: 最小位数 默认0为不启用,图片类型为可变位长时可启用这个参数
            return: JSON
                err_no,(数值) 返回代码  为0 表示正常，错误代码 参考https://www.chaojiying.com/api-23.html
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
        file = open(file_path, mode="rb")
        file_data = file.read()
        file_base64 = base64.b64encode(file_data)
        file.close()
        url = "http://upload.chaojiying.net/Upload/Processing.php"
        data = {
            'user': username,
            'pass': password,
            'softid': soft_id,
            'codetype': code_type,
            'len_min': len_min,
            'file_base64': file_base64
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        parse_data = parse.urlencode(data).encode('utf8')
        req = request_lib.Request(url, parse_data, headers)
        response = request_lib.urlopen(req)
        result = response.read().decode()
        return json.loads(result)

    def error_captcha(username: str, password: str, soft_id: str, pic_id: str) -> dict:
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
        url = "http://upload.chaojiying.net/Upload/ReportError.php"
        data = {
            'user': username,
            'pass': password,
            'softid': soft_id,
            'id': pic_id,
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        parse_data = parse.urlencode(data).encode('utf8')
        req = request_lib.Request(url, parse_data, headers)
        response = request_lib.urlopen(req)
        result = response.read().decode()
        return json.loads(result)

    def score_captcha(username: str, password: str) -> dict:
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
        url = "http://upload.chaojiying.net/Upload/GetScore.php"
        data = {
            'user': username,
            'pass': password,
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        parse_data = parse.urlencode(data).encode('utf8')
        req = request_lib.Request(url, parse_data, headers)
        response = request_lib.urlopen(req)
        result = response.read().decode()
        return json.loads(result)
