# name = input("请输入你的姓名")
# # age = input ('请输入你的年龄')
# # sex = input ('请输入你的性别')
# # print('hello',name,age,sex)
# print("hello,%s!"%name)
# print('hello,'+name+'!')
# print('%s'%name)

name = input("Name:")
age = input("Age:")
job = input("Job:")
hobbie = input("Hobbie:")
info1 = '''
------------ info of %s -----------
Name : %s
Age : %s
job : %s
Hobbie: %s
------------- end -----------------
''' % (name, name, age, job, hobbie)
print(info1)


info2 ='Name :'+name+'Age : '+age+'job : '+job+'Hobbie: '+hobbie
info2 ='Name :%s,Age :%s,job : %s,Hobbie: %s'\
      %(name,age,job,hobbie)
print(info2)