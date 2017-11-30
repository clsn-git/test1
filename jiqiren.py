import json
import requests
def send(neirong):  #形式参数
    s = requests.session()
    url = 'http://www.tuling123.com/openapi/api'
    da = {"key": "3011a9191c11007ff2cebc3c1760a381",
          "info": neirong}
    data = json.dumps(da)
    r = s.post(url, data=data)
    j = r.text
    ls = json.loads(j)
    print(ls['text'])


while True:
    sr = input('请输入')
    if sr == 'q':
        break
    else:
        send(sr)
