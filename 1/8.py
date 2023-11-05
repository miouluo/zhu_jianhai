#2 and 与（😊😊😒😊有一个不开心就返回不开心）只要任意一个条件没满足就视为没有完成
#3 or 或（😒😒😊😒有一个开心就返回开心）只要条件内任意一个条件完成就视为完成
#1 not 非
shopping_list =[]
shopping_list.append("键盘")
shopping_list.append("键帽")
shopping_list.remove("键帽")
shopping_list.append("电竞椅")
shopping_list[1]="硬盘"
print(shopping_list)
print(len(shopping_list))
print(shopping_list[0])

price =[799,1024,200,800]
max_price =max(price)
min_pirce =min(price)
sorted_price =sorted(price)
print(max_price)
print(min_pirce)
print(sorted_price)
#元组（）列表[]
query =input("请输入你要查询的流行语")
slang_dict ={"觉醒年代":"教材","yyds":"永远的神"}
slang_dict["双减"] ="教学"

if query in slang_dict:
    print("查询的词语"+query +"含义如下")
    print(slang_dict[query])
else:
    print("暂未收录")
    print("当前词条数为："+str(len(slang_dict))+"条")


