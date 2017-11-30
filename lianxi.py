# # num=input('请输入数字：')
# # print (type(num))  #(type())查看类型
# # if  int(num)%2 == 0: #强制转换int()类型
# #     print("偶数")
# # else:
# #     print("奇数")
#
# num = input("请输入分数：")
# a= int(num)
# if a>100 or a<0:
#     print('不合法的分数')
# elif a >=90:
#     print("A")
# elif a>=80:
#     print("B")
# elif a>=60:
#     print("C")
# else:
#     print("D")



import requests
import json

def talk(content):
    s = requests.session()
    url = 'http://www.tuling123.com/openapi/api'
    da = {"key":"3011a9191c11007ff2cebc3c1760a381",
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
        elif code == 302000:
            recontent = j['text']+j['list'][0]['info']+j['list'][0]['detailurl']  #新闻
        elif code == 308000:
            recontent = j['text']+j['list'][0]['info']+j['list'][0]['detailurl']  #菜谱
        else:
            recontent = False
    except:
        recontent = False
    return recontent


def main():
    print('''请开始和我聊天吧，直接按回车退出''')
    while True:
        ask = input("你  ： ")
        if ask == "":
            break
        else:
            res = talk(ask)
            if res == False:
                print('对不起，我听不懂你说的话')
            else:
                print("聊天小秘书： ", res)

if __name__ == '__main__':
    main()
