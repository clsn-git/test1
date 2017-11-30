#json

import json

l = [1,2,3]
# print(type(l))
# s =  json.dumps(l)  #类型改为字符串
# print(type(s))
# l2 = json.loads(s)  #类型改为列表
# print(type(l2))
#
#
# ls = {'tom':21,
#       'kali':22,
#       'tim':[123,'male']}
# print(type(ls))
# sls = json.dumps(ls)
# print(type(sls))
# ls2 = json.loads
# print(type(ls2))
#
#
#
# l = [1,23,{'jion':21}]
#
#
#

# import requests
# r = requests.get(url= 'http://www.houzhaoshun.cn')
# print(r.status_code )#获取返回状态
# print(r.text)
#
#
while True:
      ss = input("你想说点什么？")
      if ss == 'quit':
            print('再见！')
            break
      else:
            print('你好！')


# import json
# import requests
# s = requests.session()
# url = 'http://www.tuling123.com/openapi/api'
# da = {"key": "3011a9191c11007ff2cebc3c1760a381",
#       "info": '1'}
# data = json.dumps(da)
# r = s.post(url, data=data)
# j = r.text
# print(j)
# ls = json.loads(j)
# print(type(ls))
# print(ls)
# print(ls['text'])
