mood_index=int(input("心情指数：90"))
if mood_index>=68:
    print("今晚可以打游戏")
else:
    print("不打游戏")


#BMI=体重/（身高**2）
user_weight= float(input("请输入你的体重："))
user_height= float(input("请输入你的身高："))
user_BMI= user_weight /(user_height)**2
print("你的BMI值为："+str(user_BMI))
if user_BMI <=18.5:
    print("偏瘦")
elif 18.5< user_BMI <= 25:
    print("正常")
elif 25 <user_BMI <= 30:
    print("偏胖")
else:
    print("肥胖")

