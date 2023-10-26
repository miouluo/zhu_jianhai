#match的初步使用
'''
s = input('height(m):') # 输入现在的升高单位为m
x = input('weight:') # 输入现在的体重，单位为千克
height = float(s) # 将输入的字符串转变为浮点数
weight = float(x)
bim = weight/(height**2)
match bim :
    case x if x < 18.5:
        print(f'过轻:bim={x}')
    case x if x <=25 :
        print('正常:bim=')
    case x if x <=28 :
        print(f'过重:bim={x}')
    case x if x <=32:
        print(f'肥胖：bim={x}')
    case x if x >32:
        print(f'高度肥胖:bim={x}')'''

#循环的理解与初体验
#for...in循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:  #将names中每个字符串依次赋值给name，并且每赋值一次就打印一次
    print(name)

sum = 0
a=list(range(51))
print(a)
for x in range(51):
 sum=sum+x
print(sum)
#while循环,只要条件满足，就不断循环，条件不满足时退出循环。
A=0
X=100
while X>0:
    A=A+X
    X=X-2
print(A)
