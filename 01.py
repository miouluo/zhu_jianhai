# 这周专业课上的学习
class Fraction:
    def __init__(self,x,y):
        self.a, self.b = x,y

# 加分
    def __add__(self,other):
        fenzi = self.a * other .b + self.b * other.a  # 分子
        fenmu = self.b * other .b  # 分母
        return Fraction(fenzi, fenmu)

# 乘法
    def __mul__(self,other):
        return Fraction(self.a*other.a,self.b*other .b)


# 减法
    def __sub__(self,other):
        return Fraction(self.a * other.b - self * other.a,self.b * other .b)

#输出格式
    def __str__(self):
        return str(self.a) + "/" + str(self.b)

a = Fraction( 1,2)
b = Fraction( 1,3)
print(a - b)
