import requests
import json
import traceback 

class ChatGenerative:
    """
        对接第三方ChatGPT模型
        Docking third-party ChatGPT model
    """

    def wen_xin_bot(self,api_key:str, secret_key:str, content:str) -> dict:
        """
            文心一言ChatGPT模型
            ERNIE Bot ChatGPT model

            api_key: 文心一言签发的api_key, 获取地址：https://console.bce.baidu.com/
            secret_key ：文心一言签发的秘钥
            content: 你想问的问题
            return: 字典

            api_key: api_key issued by ERNIE Bot, obtained at https://console.bce.baidu.com/
            secret_key: the secret key issued by ERNIE Bot.
            content: the question you want to ask
            return: dictionary
        """

        def get_access_token():
            """
                使用 AK，SK 生成鉴权签名（Access Token）
                :return: access_token，或是None(如果错误)
            """
            url = "https://aip.baidubce.com/oauth/2.0/token"
            params = {"grant_type": "client_credentials", "client_id": api_key, "client_secret": secret_key}
            return str(requests.post(url, params=params).json().get("access_token"))


        try:
            url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token=" + get_access_token()
            payload = json.dumps({
                "messages": [
                    {
                        "role": "user",
                        "content": content
                    }
                ],
                "disable_search": False,
                "enable_citation": False
            })
            headers = {
                'Content-Type': 'application/json'
            }
            
            response = requests.request("POST", url, headers=headers, data=payload)
            response = json.loads(response.text)
        except Exception as e:
            return {"err":traceback.format_exc()}
        return response

