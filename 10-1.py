# 类的继承
class Fruit:   #父类
    color = '绿色'         #类变量
    def __int__(self,age):
        self.age=age
        print('这个水果是？？？')
    def  yingyang(self,color):  #苹果自己的方法，方法重写
        sum=1
        for i in range(1,10):  #猴子吃桃
            sum=(sum+1)*2
        print('桃子总数：',sum)
        print('水果的颜色是：',color)
        print('我们已经丰收了水果。')

class Apple(Fruit):        #extends 继承
    color = '红色'
    def __int__(self):
        print('我是Apple。')
class Orange(Fruit):
    color = '橙色'
    def __int__(self):
        print('我是Orange。')
    def yingyang(self,color):  #金字塔
        n=6
        for i in range(1,7):
            for j in range(1,7-i):
                print(' ',end=' ')
            for k in range(1,2*i):
                print('*',end=' ')
            print()
print(Fruit.color)
app=Apple()
app.yingyang(app.color)

org=Orange()
org.yingyang(org.color)
