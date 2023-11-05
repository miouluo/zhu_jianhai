#range(5,10,2)5是起始值，10是结束值，2是步长(默认1)
for i in range(5,10):
    print(i) #只会输出5-9
# 算出1到100的累加值
total = 0
for i in range(1,101):
    total =total + i
print(total)

print("hello,求平均值")
total =0
count =0

user_input = input("请输入数字（完成所有数字输入后，请输入q终止程序）:")
while user_input !="q":
    num =float(user_input)
    total += num
    count += 1
    user_input = input("请输入数字（完成所有数字输入后，请输入q终止程序）:")
if count == 0:
    result =0
else:
    result =total /count
print("平均值为"+str(result))
def calculate_BMI(weight,height):
    BMI = weight /height ** 2
    if BMI <= 18.5:
        category ="偏瘦"
    elif BMI <= 25:
        category ="正常"
    elif BMI <= 30:
        category ="偏胖"
    else:
        category ="肥胖"
    print(f"BMI分类为：{category}")
    return BMI
result =calculate_BMI(1.8,70)
print(result)