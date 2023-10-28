x=input('请输入一个三位自然数')
x=int(x)
a=x//100
b=x//10%10
c=x%10
print("a,b,c")

#三角形求边
import math
x=input("输入两边长及夹角")
a,b,theta=map(float,x.split())
c=math.sqrt(a**2+b**-2*a*b*math.cos(theta*math.pi/180)
print("c=",c)