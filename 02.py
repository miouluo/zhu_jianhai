# 本周专业课学习内容
class student:
    def __init__(self,sno,sname):
        self.sno=sno
        self.sname=sname

class Card:
    def __init__(self,money):
        self.money=money

    def cunqian(self,x):
        return x+self.money

    def shuaka(self,y):
        return self.money-y

class StuCard(student,Card):
    pass
c=StuCard("01","小李")
c=Card(50)
print(c.cunqian(10))
print(c.shuaka(20))
print(isinstance(c,student))
print(isinstance(c,Card))