import itchat
import requests
import json
def talk(content):
    s = requests.session()
    url = 'http://www.tuling123.com/openapi/api'
    da = {"key": "3011a9191c11007ff2cebc3c1760a381",
          "info": content ,}
    data = json.dumps(da)
    r = s.post(url, data=data)
    j = eval(r.text)      #str——>dict
    code = j['code']
    try:
        if code == 100000:
            recontent = j['text']   #文本
        elif code == 200000:
            recontent = j['text']+j['url']   #链接
        else:
            recontent = False
    except:
        recontent = False
    return recontent
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    res = talk(msg.text)
    if res == False:
        return '对不起，听不懂你在说啥'
    else:
        return res


itchat.auto_login()
itchat.run()
