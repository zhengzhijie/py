# -*- coding: utf-8 -*-
'''
Created on 2019年5月9日

@author: zzj
'''

print ("hello world!")

# 变量：避免使用大写字母
message = "Hello World!"
print(message)
##################################字串
# 大小写
print("it's a dog")
print('it is a "dog"')
# 存储时，统一存储为小写，使用时做相应的转化
name = "zheng zhijie"
print("title() " + name + " : " + name.title())
print("upper() " + name + " : " + name.upper())
print("lower() " + name + " : " + name.lower())

first_name = "zheng"
last_name = "zhijie"
full_name = first_name + " " + last_name
print("hello " + full_name.title() + "!")

print("1\tpython")
print("---\n\tPython\n\tC\n\tJava")

fav = "   Python   "
print(fav.rstrip().replace(' ', '-'))
print(fav.lstrip().replace(' ', '-'))
print(fav.strip().replace(' ', '-'))
print(fav.replace(' ', '-'))
fav = fav.rstrip()
print(fav.replace(' ', '-'))

##################################数字
# 整数            + - * / **(乘方) 空格不影响运算
# 除法, 去掉小数位
print 3 / 2
print 3.0 / 2
print 3.0 / 1.0
# 浮点数        注意：结果包含的小数位数可能不确定
print 0.2 + 0.1

# 数字不会隐式转换
# print "a " + 3 + " b"
print "a " + str(3) + " b"

##################################列表 []表示, 方便存储在程序运行期间可能变化的数据集
color = ['red', 'yellow', 'white']
print color
print color[0].title()
print color[-1]
color[0] = "redb"
color.append('black')
print color
color.insert(0, 'blue')
print color
del color[1]
print color
# 列表作为栈使用
print "使用pop删除末尾的元素 " + color.pop()
print "使用pop(0)删除第一个元素 " + color.pop(0)
print color
color.append("white")
print "remove前 " + str(color)
color.remove('white')
print "remove后" + str(color)

letter = ['s', 'a', 'd', 's', 'c', 'p']
print sorted(letter, reverse=True)
print letter
letter.sort()
print letter
letter.sort(reverse=True)
print letter
letter.reverse()
print "reverse 后 " + str(letter)
print "len=" + str(len(letter))

# 遍历列表
print "------------我是分割线--------------"
letter = letter[0:2]
for le in letter:
    print le + " is a letter"
    print le.title() + "再次打印"
print "------end"

print "-------------数字列表---------------------"
for value in range(1, 3):
    print value
values = list(range(1, 11))
squ = []
for val in values:
    squ.append(val ** 2)
print squ
print str(values) + " min: " + str(min(values)) + " max: " + str(max(values)) + " sum: " + str(sum(values))
values = list(range(0, 10, 2))
print values

print "列表解析 " + str([value ** 2 for value in range(1, 11)])

print "---------------切片------------------------"
values = range(1, 11)
print values[0:5]
print values[0:]
print "最后三个 " + str(values[-3:])
##################################################元组：不可变列表
print '-------------------------------列表 可变列表；不可变列表：元组 ()'
dimens = (100, 20)  # 矩阵
print dimens
print dimens[0]

for d in dimens:
    print d

###################################################if语句
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw' and len(car) == 3:
        print car.upper()
    elif car == 'subaru':
        print car.lower() + "-:audi-" + str(car == 'audi')
    else:
        print car
print '-----------------------------'

if 'audi' in cars:
    print "audi is exist"
if('audi1' not in cars):
    print "audi1 is not exist"

nul = []
if nul:
    print 'nul: ' + str(nul)
else:
    nul.append('1')
    print str(nul)

################################################字典 {}
alien = {'name':'zhangsan', 'age':18}
print alien['name']
print alien['age']
alien['class'] = 'class1'
print alien
print "--------------del alien['class']"
del alien['class']
print alien

fav_languages = {
    'zhangsan':'Java',
    'lisi':'C',
    'wangwu':'Python',
    'wanger':'Python'
}
print fav_languages
print("zhangsan's favorite language is " + 
      fav_languages['zhangsan'].title() + ".")

print '---------------------------------------------------'
user_0 = {
    'username':'zhengzhijie',
    'firstname':'zheng',
    'secondname':"zhijie"
    }

for k, v in user_0.items():
    print "k=" + k + ", v=" + v
for k in user_0.keys():
    print k.title()

print '---------------------------------------'
names = ['zhangsan', 'chen', 'lisi']
for name in names:
    if name in fav_languages.keys():
        print name + " is in fav_languages"
    elif name not in fav_languages.keys():
        print name + " is not in fav_languages"
    else:
        print name

print '---------------------------sorted keys-------------------------'
for name in sorted(fav_languages.keys()):
    print name
for name in sorted(fav_languages.values()):
    print name
print "-------------------------去重---------------------------"
for name in set(fav_languages.values()):
    print name

'''
嵌套：列表  字典 -- 在列表中嵌套字典，在字典中嵌套列表，在字典中嵌套字典
'''
print "-------------------------------------------------------嵌套"
alien_0 = {'color':'white', 'age':18}
alien_1 = {'color':'black', 'age':53}
alien_2 = {'color':'blue', 'age':198}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print alien
'''字典列表 or 在字典中存储列表（单键对应多值时）'''

'''
列表和字典的嵌套，层级不宜太多
'''

'''
用户输入和 while循环
两个问题：如何和用户交互 input(); 如何让程序持续运行while
input的区别 
    2中input(希望读取的是一个合法的表达式)， raw_input(所有输入看成字串)
  3中input默认接收的是str类型
'''
# msg = input("Tell me something, then I will repeat it back to you: ")
# print(msg)
# name = raw_input("Please input your name: ")
# print("hello " + name + "!")

# prompt = "Please input your age: "
# age = ""
# acitve = True
# while acitve:
#     age = raw_input(prompt)
#     if age == 'q':
#         acitve = False
#         break
#     age = int(age)
#     
#     if age % 2 == 0:
#         print str(age) + " is even"
#     else:
#         print str(age) + " is odd"
# print "game over\n"

print "--------------------------------"
'''
break、continue的使用
'''
for n in range(10):
    if n % 2 == 0:
        continue
    print n
##########################################################
'''
for and while
for循环是一种遍历列表的有效方式，但for循环中不应修改列表，这时while起到作用
'''

unconfirmed = ['a', 'b', 'c', 'a', 'b', 'c']
confirmed = []
while unconfirmed:
    check = unconfirmed.pop(0)
    confirmed.append(check)
print 'unconfirmed : ' + str(unconfirmed)
print 'confirmed : ' + str(confirmed)

while 'a' in confirmed:
    confirmed.remove('a')
print "remove a ---"
print 'unconfirmed : ' + str(unconfirmed)
print 'confirmed : ' + str(confirmed)

# responses = {}
# active = True
# while active:
#     name = raw_input('what is your name: ')
#     response = raw_input('what are you like: ')
#     responses[name] = response
#     repeat = raw_input('do? (yes/no)')
#     if repeat == 'no':
#         active = False
# print responses

########################################################函数
