import math
def getarea(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return s

    else:
        return 0.0


if __name__ == '__main__':
    a = eval(input('请输入三角形的第一条边：'))
    b = eval(input('请输入三角形的第二条边：'))
    c = eval(input('请输入三角形的第三条边：'))
    area = getarea(a, b, c)
    print('三角形的面积是：', area)
