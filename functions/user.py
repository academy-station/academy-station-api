import requests


def getOpenID(js_code: str):
    APPID = "wx9de26bbb01981e49"
    SECRET = "54adc06ceff85b66f4332f367d21c168"

    res = requests.get(f"https://api.weixin.qq.com/sns/jscode2session?"
                       f"appid={APPID}&secret={SECRET}&js_code={js_code}"
                       f"&grant_type=authorization_code")
    return res.json()

