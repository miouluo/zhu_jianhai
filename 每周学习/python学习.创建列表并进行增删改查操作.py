#创建列表
all_in_list = [0.25,'hello',True,[2.3,2.5]]
list_example = list('ABCD')
#列表中每个元素都是可变的;每个元素都有序，每个元素对应一个位置；列表可以容纳任何对象
print(all_in_list)

#列表的索引及切片
print(all_in_list)
all_in_list[1]      #索引操作
all_in_list[-3]

all_in_list[0:3]    #切片操作
all_in_list[-4:-1]
all_in_list[:3]
all_in_list[:]
all_in_list[0:1]    #注意，切片操作返回的职会保留原来的数据结构
all_in_list[0]

#为列表新增元素
print(all_in_list)
all_in_list.append(0.78)     #append是将元素增加到列表末尾
all_in_list.append([1,2])
all_in_list.extend([1,2])    #append与extend的区别一个将整体插入末尾，一个将元素逐个插入末尾
all_in_list.insert(1,'world')   #在指定位置插入相应元素
[1,2] + [3,4]       #两个列表元素相合并形成一个新的列表

#删除列表中的元素
print(all_in_list)
all_in_list.remove('hello')    #删除列表中的指定元素
del all_in_list[0:2]           #删除列表中多个元素
del all_in_list                #删除列表本身

#修改列表中的元素
all_in_list[0] = 125           #通过赋值来修改列表中的元素

#列表常用方法补充
#count 统计某个元素在列表中的次数
#index 从列表中找出某个值第一个匹配项的索引位置
#pop 移除列表中的一个元素（默认最后一个元素），并返回该元素的值
#remove 移除列表中某个值的第一个匹配项