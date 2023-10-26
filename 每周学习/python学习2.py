#创建字符串
string1 = 'python1'
string2 = "python2"
string3 = '''123
hanser
毛怪
456'''
print(string3)
#字符串的基本操作
string1 + string2   #合并字符串
string1 * 3         #复制字符串
int('9')            #将字符串转换为数值

#字符串的索引及字符操作
print(string1)
string1[0]          #正序索引，序号从0开始
string1[-7]         #逆序索引，序号从-1开始

string1[1:3]        #字符串的切片操作，切片时左闭右开
string1[:3]
string1[3:]