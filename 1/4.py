hello_world ='hello world' #变量名无需提前声明
print (hello_world)


'''print (hello_world)

'''

机器学习=['决策树','神经网络','聚类分析']
for i in 机器学习:
    print(i)
    print('hello world')

#创建字符串
string1='python1'
string2='python2'
string3='''
python3
python4
'''
print(string3)

#字符串基本操作
string1+string2 #合并字符串
string1 * 3 #复制字符串
int('9')    #将字符串转换成数值

#字符串索引及切片操作
print(string1)
string1[0]  #正序索引，序号从0开始
string1[-6]  #逆序索引，序号从-1开始
string1[1]

string1[1:3] #字符串的切片操作，切片时左闭右开
string1[:3]  #从开头到3前
string1[3:]  #从3开始

#任务实现
#1.创建一个字符串常量“Apple's unit price is 9 yuan.”。
applePricestring="Apple's unit price is 9 yuan."
#2.提取出里面的数字9并赋值给新的变量。
applePrice = applePricestring[-7]
#3.查看新变量的数据类型。
type(applePrice)
#4.将提取的数字9转成整型（int）。
applePriceInt = int(applePrice)
#5.确认数据类型是否转换成功。
type(applePriceInt)


#给定圆的半径，计算圆的周长和面积
pi = 3.14
r = 3
C = 2 * pi * r
S = pi * r ** 2

#给定周长，计算圆的半径和面积
C = 5
r = C / (2 * pi)
S = pi * r ** 2

#给定圆的面积，计算圆的半径和周长
S = 5
r = (S / pi)** 0.5
C = 2 * pi * r






