class Weapon:
    def __init__(self, weight, fire, price, resistance):
        self.weight = weight
        self.fire = fire
        self.price = price
        self.resistance = resistance


class Tank(Weapon):
    def __init__(self, weight, fire, price, resistance, oil, speed, health):
        super(). __init__(weight, fire, price, resistance)
        self.oil = oil
        self.speed = speed
        self.health = health

    def BeHit(self, a):

        print('对象受到火力的打击为：', format(a))
        self.health = self.health - a / self.resistance

    def ShowState(self):

        print('显示受打击后对象的状态为：')

        print(self.weight, self.fire, self.price, self.resistance, self.health, end='')
# 打印重载，用print函数输出对象的属性

    def __str__(self):
        return f'初始值：重量为{self.weight},火力{self.fire},价格{self.price},抗打击力{self.resistance},健康程度{self.health}'


A = Tank(2000, 800, 500000, 600, 0, 0, 100)
print(A)
A.BeHit(20000)
A.ShowState()
# print(A.ShowState())
