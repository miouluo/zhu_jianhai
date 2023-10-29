#调用函数

help(hex)   #通过help了解一个函数的作用,hex将整数转换为16进制数
n1 = 255
n2 = 1000
h=hex
print(h(n1),h(n2))
#升级,将任意输入的十进制整数转换为16进制
'''
s=input("十进制(整数):")
s=int(s)
s=h(s)
print("对应的16进制为：",s)


abs  求数据绝对值，只能接收单个数据
max  能接收多个数据并返回最大值
int  转为整数
float转为浮点数
str  转为字符串
'''

 #定义函数
 #可以用def+函数名+（参数值）+:然后在缩进区域编写函数
def my_abs(x):     #定义属于自己的绝对值函数
    if x>= 0:
        return x
    else:
        return -x

print(my_abs(-100))