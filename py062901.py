#函数  def

# def mail(who,used):
#     # print(who,'连接服务器')
#     # print(who,'发送邮件')
#     # print(who,'断开连接')
#     print(who,'出问题了','占有率:',used)
# cpu = 0.8
# disk = 0.92
# cache = 0.88
# if cpu > 0.8:
#     mail('cpu',cpu)  #位置参数
# if disk > 0.8:
#     mail('disk',disk)
# if cache > 0.8:
#     mail('cache',cache)
#

def mail():
    print('你好!')

mail()
print(mail)


# def mail(who,used):
#     print(who,'出问题了','占有率:',used)
#     return True, '成功'   #函数返回值
# re  = mail('cpu',0.85)
# print(re[0],re[1])

#
# def mail(who,used):
#     print(who,'出问题了','占有率:',used)
#     '成功'   #return None 默认
# re1  = mail('cpu',0.85)
# print(re1)


# def stu_info(name,sex='male'):   #默认参数
#     print(name,sex)
# stu_info('建生')
# stu_info('张优')
# stu_info('卢玉','famale')
# stu_info(sex='male',name='微博')


#动态传参

# def func(a,c,*b,**d):  #*b  接收参数 ：语法
#     # print(a)
#     # print(c)
#     print(b)
#     print(d)
# # func(123,45,561,'hello',22, name = 'ling',ling='kong',py = 'none')
# l = ['abc','def']
# ln = {'python':255,
#       'linux':18,
# }
# func('123','456','789',*l,'445',**ln)

#面向过程、面向函数、面向对象


