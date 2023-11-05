import numpy as np
# 数组的索引
arr1 = np.array([0.3, 0.78, 0.24, 5, 3.2])
print(arr1)

# 一维数组的单个元素的索引
print(arr1[0])
print(arr1[-5])

# 一维数组的多个元素的索引（切片）
print(arr1[1:3])
print(arr1[-4:-2])

res1 = arr1[3]
res2 = arr1[3:4]
print(res1, res1.shape)
print(res2, res2.shape)

# 逻辑型索引
arr2 = np.array([2.3, 1.8, 4.5])
print(arr2)
print(arr2[[False, False, True]])#不常用
index = arr2 > 2
print(index)
print(arr2[index])

# 逻辑型索引
arr2 = np.array([2.3, 1.8, 4.5])
print(arr2)
print(arr2[[False, False, True]])#不常用
index = arr2 > 2
print(index)
print(arr2[index])

# 修改数组中的元素
arr3 = np.arange(1, 13).reshape([3, 4])
print(arr3)
arr3[0, 0] = 15
print(arr3)