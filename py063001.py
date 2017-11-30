#三元换算符
# a = 15
# b = 12

# if a>b:
#     print(a)
# else:
#     print(b)
#
# c = a if a>b else b
# print(c)

# print(a if a%b==0 else False)
#
# print(a/3 if a%3==0 else False)
#
# print(a if a%3==0 and a%5==0 else False)


# sr = input("请输入")
# # print('Hello' if sr == '' else sr)
# l=[0,1,2,3,4,5,6,7,8,9,10]
# print(l[2::2] if sr=="0" else l[1::2])

# sr = input("请输入")
# ss = int(sr)
# print(list(range(2,ss+1,2)) if ss%2 == 0 else list(range(1,ss+1,1)))

#用户输入一个值
#如果值为空，就输出'hello'
#否则输出用户输入的内容

# a = input('请输入一个值：')
# print('hello' if not a else a)
# print('hello' if a=='' else a)

# a = ''
# l = [1]
# print(bool(l))
# not False == True


# l=[0,1,2,3,4,5,6,7,8,9,10]
# a = input('请输入:')
# print(l[2::2] if a=="0" else l[1::2])


# l=[0,1,2,3,4,5,6,7,8,9,10]
# # # new_l = []
# # # for i in l :
# # #     i = i+1
# # #     new_l.append(i)
# # # print(new_l)
# #
# # print([i+1 for i in l])
# print(i%3 for i in l)
#
# print([True if i%2==0 else False for i in l])

# l = ['Tom','Jack','Eva',]
# for i in l:
#     print('hello',i)
#
# print(['hello,'+i for i in l ])
# {'name':'','sex':''}

#
# l = [
#      {'name':'Tom','sex':'male'},
#      {'name':'Jack','sex':'male'},
#      {'name':'Eva','sex':'famale'},
# ]
# # print([i['name'] for i in l])
#
# for i in l:
#     print(i)
#
# # print(l.count('male'))  #count 计数
#
#
# print([i['sex'] for i in l].count('famale'))



# l = [2,5,6,7,9,3,1,5,6,48,8,3,1,6,4]
# print(sorted(l))   #排序
# print(max(l))
# print(min(l))


# l = ['电脑','自行车','雨伞']
# # for i in l:
# #     print(i)
# for  i in enumerate(l,1):      #加标号
#     print(i[0],i[1])
#

print(eval('2-(2+3*6)//2'))

eval("print(eval('1+1'))")





