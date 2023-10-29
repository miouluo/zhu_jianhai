
d = {'Tom':"cat",'Jerry':"mouse"}  #dict具有很快的查找速度，但需要内存大
print (d['Tom'])

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print (d['Michael'])

#把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
d['Lisa']=100
print(d['Lisa'])

print('Thomas' in d)#用于检测一个dict里是否有这个key
print(d.get('Thomas',-1))#第二种检测是否有该key的办法“，”后面的数字可以不存在，默认返回none，也可也自己随意指定

#要删除一个key，用pop(key)方法，对应的value也会从dict中删除
d.pop('Bob')
print(d)
#print (d['Tom'])，程序报错，因为d被覆盖

'''list比较，dict有以下几个特点：

    1.查找和插入的速度极快，不会随着key的增加而变慢；
    2.需要占用大量的内存，内存浪费多。

而list相反：

    1.查找和插入的时间随着元素的增加而增加；
    2.占用空间小，浪费内存很少。

所以，dict是用空间来换取时间的一种方法。'''

#需要牢记的第一条就是dict的key必须是不可变对象

#key = [1, 2, 3]#这里的key是一个list
#d[key] = 'a list' 因此运行这里会报错

"Set"
s = set([1, 2, 3])             #创建的是一个list，打印结果只是告诉你里面有1、2、3这些元素
print(s)
s = set([1, 1, 2, 2, 3, 3])
print(s)                       #重复的元素被自动过滤
#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(5)
print(s)
#通过remove(key)方法可以删除元素
s.remove(3)
print(s)

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)#交集

print(s1 | s2)#并集
