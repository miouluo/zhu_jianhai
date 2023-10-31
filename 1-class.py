#功能：定义类与对象
class Stu:
    study= 0
    a =12
    b =20
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age
        self.__jin =3000   #私有属性
    def study(self):
            sum=0
            for i in range(1, 101):
                sum=sum+i
            print('偶数之和是：',sum)
    def p__jin(selfself):
        print('结果是：',s1.__jin)

    def __eat(self):     # 私有成员方法前有两条下划线__
        a=10
        b=20
        if a>b:
            print('a=',a)
        else:
            print('b=',b)

s1=Stu('小爱',202520101,19)
print('小爱的名字：',s1.name,'小爱的学号是：',s1.id,'小爱的年龄是：',s1.age)
s1.age=18
s1.name='花花'
s1.id=202020
print('小爱的名字：',s1.name,'小爱的学号是：',s1.id,'小爱的年龄是：',s1.age)
s1.study()    #调用方法
s1.p__jin()
print(Stu.a+s1.b)      #类属性：可以被对象和类进行调用
s1._Stu__eat()   # 调用私有的成员方法