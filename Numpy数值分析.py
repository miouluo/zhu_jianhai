import numpy as np

arr1 = np.array([0.3,0.5,4.2])#一维列表
arr2 = np.array([[1,2,3],[5,6,1]])
print(arr1)
print(arr2)
print(type(arr1))
#查看数组的基础属性
print(arr1.shape)
print(arr1.ndim)
print(arr1.dtype)
print(arr2.shape)
print(arr2.dtype)
print(arr2.ndim)

#初识数组的特点
list1 = [0.3,0.5,4.2]
arr1 = np.array ([0.3,0.5,4.2])
print(arr1**2)
#print(list1**2) 会报错
print([i**2 for i in list1])#更麻烦，代码更长，反应时间更长
#创建常用数组
arr3= np.arange(0,10)#创建等差数组、默认公差为1
arr4 = np.arange(15)#同样可以创建等差数组，默认从0开始
arr5 = np.arange(0,20,2)#(开始的数、结束的数(该数不会被取到)、公差)
print(arr3)
print(arr4)
print(arr5)
#help(np.arange) 可以知道函数的使用办法
arr6 = np.linspace(0,2,11)#(起点、终点、数的个数)生成等差数列
print(arr6)
arr7 = np.zeros([4,4])#生成全0的数组（几层，几列，几行）
print(arr7)

#数组的数据类型及其转变
arr8 = np.array([4,8,6],dtype=np.float32)#在定义数组的时候该数据类型
arr8[1]=6.6                 #替换数据
print(arr8)
print(np.int32(arr8))       #在后续中更改数据类型

#生成随机数
print(np.random.random(8))  #生成无规定的8个随机数
print(np.random.rand(2,2))
print(np.random.randn(4,2,4))
