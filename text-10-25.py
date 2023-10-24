s = input('height(m):') # 输入现在的升高单位为m
x = input('weight:') # 输入现在的体重，单位为千克
height = float(s) # 将输入的字符串转变为浮点数
weight = float(x)
bim = weight/(height**2)
print(bim)
if bim<18.5:
    print("过轻")
elif bim<=25:
    print("正常")
elif bim<=28:
    print("过重")
elif bim<=32:
    print("肥胖")
else :
    print("高度肥胖")
