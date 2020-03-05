import requests

from wcb_project import settings


class YunPian:
    def __init__(self,apikey):
        self.post_url = "http://sms.yunpian.com/v2/sms/single_send.json"
        self.apikey = apikey

    def send_message(self,code,mobile):
        params= {
            "apikey":self.apikey,
            "text":f"【毛信宇test】您的验证码是{code}。如非本人操作，请忽略本短信",
            "mobile":mobile,
        }
        res = requests.post("http://sms.yunpian.com/v2/sms/single_send.json",params)
        return res

if __name__ == '__main__':
   y = YunPian(settings.APIKEY)
   y.send_message('123456','17852361975')

