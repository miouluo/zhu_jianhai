#任务实现
#1.建立一个字符串变量“Apple's unit price is 9 yuan."
ApplepriceString = "Apple's unit price is 9 yuan."
#2.提取出里面的数字9并赋值给新的变量
Appleprice = ApplepriceString[-7]
#3.查看新变量的数据类型。
type(Appleprice)
#4.将提取的数字9转换成整型（int）
Applepriceint = int(Appleprice)
#5.确认数据类型是否转换成功
type(Applepriceint)
#str为字符串，int为整型

#自我测试
print(Appleprice)
print(Applepriceint)