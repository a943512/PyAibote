import re


class UrlRequest:
    """
        URL请求
        URL request
    """

    def url_request(self, url: str = "https://www.baidu.com", requestType: str = "GET", headers: str = "null", postData: str = "null") -> str:
        """
            获取请求地址html数据
            Get that html data of the request address

            url: 请求的地址 http://www.ai-bot.net
            requestType: 请求类型，GET或者POST
            headers: 可选参数，请求头
            postData: 可选参数，用作POST 提交的数据
            return: {Promise.<string>} 返回请求数据内容

            url: The requested address is http://www.ai-bot.net
            requestType: request type, GET or POST
            headers: optional parameter, request header
            postData: optional parameter, used as data submitted by post
            return: {Promise.<string>} returns the requested data content
        """
        response = self.SendData("urlRequest", url, requestType, headers, postData)
        if "/" in response:
            response = re.findall(r'/(.*)',response)[0]
        if response == "null":
            return None
        return response