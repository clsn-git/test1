#平方
# l =[1,2,3,4,5]
# for ss in l:
#     print(ss**2)
#

#打印偶数
# l = list(range(101))
# for a in l:
#     if a%2 == 0:
#         print(a)

#切片打印
# l = list(range(101))
# print(l[::3])

# l1 = range(100)
# l2 = list(range(100))
# print(l1)
# print(l2)
 #i  ...item

# l = range(1,100,2)
# print(l)
# for a in l:
#     print(a)

# int str list 布尔值 tuple(元组)

# l = ['a','b','c','5','6']
# for i in l :
#     print(i)
# #len(l) 第2:
# for i in range(len(l)):
#     print(l[i])

#元组   数据类型  不可修改
# tuple
# t1 = (1,2,3,4)
# t2 = (2,)
# print(t1[1])
# print(t1)
# print(t2)

#元组不可变
# t = ('a','b','c','d',[1,2,3],4)
# t2 = (1,2,3,(4,5,6))
# print(id(t[4]))
# print(t)
# t[4].append('hello')
# print(t)
# print(t[4])
# print(id(t[4]))
# print(t2)
# print(id(t2[4]))


# l = [['你好',2015,'male'],
#      ['再见',2016,'female'],
#      ['好的',2017,'male'],
#      ['厂长',2018,'male'],
#      ['好吧',2020,'female']]
# for l_item in l :
#     print(l_item)
#     print(l_item[0])
#     if l_item[0] == '好的':
#         print('年份：',l_item[1])
#         print('性别：',l_item[2])

# dict(字典)

#key:value key：不可变、唯一
#字典是无序的

'''
# d = {'张三':[18,'female'],
#      '李四':[19,'male'],
#      '王五':[20,'female'],
#      '赵六':[21,'male'],
#      '马六':[27,'male'],
# }

# for i in d:
#      if i.startswith('张'):  #开头
#           print(i,d[i])
#      if i.endswith('六'):   #结尾
#           print(i,d[i][0])
#


# print(d)
# print(d['张三'])
# print(d['李四'][1])
# print(d.get('王五'))
# print(d.get('赵'))   #友好
# print(d.keys())
# for i in d.keys():
#      print(i,d[i])
# # # print(d.values())
# # # for i in d.values():
# # #      print(i)
# for i in d:
#      print(i)
#
# #语法糖
# for k in d.items():
#      print(k)
#
#
#     s = '张三'
#    print(s.startswith('张'))

# d['周董'] = 'male'  #向字典添加
# print(d)
# d['周董'] = [20,'male'] #修改
# print(d)
# d['张三'] = [20,'female'] #修改
# print(d)
# # for k in d :
# #      print(k)
# print(d.pop('李四')) #删除
# print(d.pop('周董')) #删除
# print(d)
# print(len(d))   #len计数
#
'''


###集合###
#去重、无序、确定性
#1、去重；2、关系运算
# s = {1,2,3,4,7,6,75,3,4,6,8}
# print( s )
#
# l = [1,6,8,9,4,2,3,6,1,3,9]
# new_l = []
# for i in l:
#      if i not in new_l:
#           new_l.append(i)
# print(new_l)
# s=set(l) #去重
# print(list(s)) #转为列表

#关系运算
ll = {454,545,8,63,4,3,1}
lw = {8,55,96,3,1,25,454}
# print(ll&lw) #交集
# print(ll.intersection(lw))
# print(ll|lw) #并集
# print(ll.union(lw))
# print(ll-lw) #补集
# print(ll.difference(lw))
#
# ll.add(123456) #添加
# print(ll)
# ll.remove(454) #删除
# print(ll)
# print(ll.pop())#删除
# print(ll)
# ll.discard(3) #删除
# print(ll)
# ll.clear()  #清空
# print(ll)