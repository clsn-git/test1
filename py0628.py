# 内存
# a='123'
# print(id(a))

# a="hello"
# b=a
# print(id(a),id(b))
# a="5"
# print(id(a),id(b))

#数字  从 -5 到 256 常用
# s1 = "hello world"
# s2 = "hello world"
# print(id(s1),id(s2))

# 身份运算
# a = 10
# b = 10
# print(a is b)
# print(a is not b )

# print(oct(8),bin(2),hex(16))


# print(abs(-5))# 绝对值
#
# a,b = divmod(7,4)
# print(a,b)
'''
# a="   user   "
# print(a.strip())#去空格
# print(a.lstrip())#左
# print(a.rstrip())#又

# a="***user###"
# print(a.strip('*''#'))#去字符'''

#字符串索引
# a='username'
# print(a[-8])
# print(a[0])
# #切片 顾头不顾尾
# print(a[0:8:3])
# print(a[:4])
# print(a[4:])
# print(len(a))#字符串长度 len(）

# b="hello,world"
# c,d = b.split(",")#分割 split()
# print(c)
# print(d)

#替换方法
# b = 'hello,abc'
# a =  b.replace('abc','hzs')
# print(a)
# print(b)

#list 列表
#添加 append insert
list1 = ['aaa','vbc','saa','sas']
print(list1[0])#取值,列表有序
list1.append('侯召顺') #添加
print(list1)
list1.insert(0,'狗剩') #添加
print(list1)
list1[2]= "金克丝"  #修改
print(list1)
list1.remove('sas') #删除
print(list1)
name = list1.pop()  #删除最后一个
print(name)
print(list1)
print(list1.index('侯召顺'))  #查找
print(len(list1))

#list2 = ['aaa','vbc','saa','sas','hzs']
# print(list2[0:3])
# print(list2[-3:])
# print(list2[-1::-1])
# print('hzs' in list2)

#list3 = ['aaa','vbc','saa','sas','hzs']
# name = input("请输入姓名:")
# if name not in list3:
#     list3.append(name)
# else:
#     print('已存在')
# print(list3)

#循环输出
# list4 = ['aaa','vbc','saa','sas','hzs']
# for lianxi in  list4:
#     print(lianxi)
#     if lianxi == "sas":
#         break

"""pass"""

list5 = ['aaa','vbc','saa','sas','hzs']
for lianxi in  list5:
    if lianxi == "vbc":
        continue
    print(lianxi)






