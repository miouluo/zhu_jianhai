import numpy as np

#数组的索引
arr1 = np.array([2,5.6,0.33,0.61,0.09])
print(arr1)
#一维数组单个元素索引
print(arr1[0])    #从左往右，取元素
print(arr1[-5])   #从右往左，取元素
print(arr1[0],arr1.dtype)

#一维数组多个元素的索引（切片）
print(arr1[2:3])
print(arr1[2:4])
#返回为一个数组，而不是元素，且取值是左闭右开区间

res1 = arr1[2]
res2 = arr1[2:3]
print(res1,res1.shape)   #输出为（）表示为0维数组
print(res2,res2.shape)

#一维数组逻辑索引
arr2 = np.array([2.86,1.56,5.66,3.85])
index = arr2 > 3     #取列表里大于2的数，返还给index
print(arr2[index])

arr3 = np.arange(1,10).reshape([3,3])#规定行和列，必须要刚好能放下？？？
print(arr3)
print(arr3[2,0])#取出单个元素
print(arr3[2,:])#取出某行
print(arr3[:,2])#取出某列
print(arr3[1:3,1:3])#取某一块
print(arr3[arr3[:,0]>5,:])#取出大于某一值的目标行，逻辑索引

n = 5
x = np.linspace(1,100,n)
y = np.linspace(1,70,n)
dist = np.zeros([n,n])
for i in range(n):
    for j in range(n):
        dist[i,j] = np.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)

print(dist)