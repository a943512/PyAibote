import re
import json

class CookiesOperation:
    """
         Cookies操作
         CookiesOperation
    """

    def get_cookies(self, url: str) -> list:
        """
            获取指定 url 的 Cookies
            Get Cookies for the specified url

            url: url 字符串
            return: 布尔值

            url: url string
            return: bool
        """
        response = self.SendData("getCookies", url)
        if "/" in response:
            response = response.replace("\n","").replace("\t","")
  
        if response == "null":
            return None
        return json.loads(response)

    def get_all_cookies(self) -> list:
        """
             获取浏览器所有的Cookies
            Get all the Cookies

            return: 列表格式的 cookies
            return: cookies in list format
        """
        response = self.SendData("getAllCookies")
        if "/" in response:
            response = response.replace("\n","").replace("\t","")
            response = re.findall(r'/(.*)',response)[0]
        if response == "null":
            return None
        return json.loads(response)

    def set_cookies(self, url: str, name: str, value: str, options: dict = None) -> bool:
        """
            设置指定 url 的 Cookies
            Set Cookies for the specified url

            url: 要设置 Cookie 的域
            name: Cookie 名
            value: Cookie 值
            options: 其他属性
            return: 布尔值

            url: The domain to set the Cookie
            name: Cookie name
            value: Cookie value
            options: Other attributes
            return: bool
        """
        default_options = {
            "domain": "",
            "path": "",
            "secure": False,
            "httpOnly": False,
            "sameSite": "",
            "expires": 0,
            "priority": "",
            "sameParty": False,
            "sourceScheme": "",
            "sourcePort": 0,
            "partitionKey": "",
        }
        if options:
            default_options.update(options)
        return "true" in self.SendData("setCookie", name, value, url, *default_options.values())

    def delete_cookies(self, name: str, url: str = "", domain: str = "", path: str = "") -> bool:
        """
            删除指定 Cookie
            Delete the specified Cookie

            name: 要删除的 Cookie 的名称
            url: 删除所有匹配 url 和 name 的 Cookie
            domain: 删除所有匹配 domain 和 name 的 Cookie
            path: 删除所有匹配 path 和 name 的 Cookie
            return: 布尔值

            name: The name of the Cookie to delete
            url: Delete all Cookie that match url and name
            domain: Delete all Cookie matching domain and name
            path: Delete all Cookie matching path and name
            return: bool

        """
        return "true" in self.SendData("deleteCookies", name, url, domain, path)

    def delete_all_cookies(self) -> bool:
        """
            删除所有 Cookie
            Delete all Cookie

            return: 布尔值
            return: bool
        """
        return "true" in self.SendData("deleteAllCookies")

    def clear_cache(self) -> bool:
        """
            清除缓存
            Clear cache

            return: 布尔值
            return: bool
        """
        return "true" in self.SendData("clearCache") 





