a=float(input("请输入你的身高（单位m）："))
b=float(input("请输入你的体重（kg）："))
c= b/(a)**2
if float(c)>23:
    print("你的bmi值是"+str(c)+"偏胖")
else:
    print("你的bmi值是" + str(c)+"正常")
