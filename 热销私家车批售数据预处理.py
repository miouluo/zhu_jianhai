import numpy as np
import pandas as pd

# 导入数据
car = pd.read_excel('热销私家车批售数据2021年.xlsx')
print(car.head())

print(car.shape)  # 数据行列
print(car.isnull().sum())  # 查看缺失值，无缺失值
print(car.duplicated())  # 查看重复值，有重复值
carnew = car.drop_duplicates()  # 删除重复值
print(carnew.shape)  # 新的数据行列

# 修改异常值
# 在总部列中，数据大多都包含省份和城市，而小部分仅有城市
carnew = carnew.replace('北京', '北京-北京')
carnew = carnew.replace('天津', '天津-天津')
carnew = carnew.replace('上海', '上海-上海')
carnew = carnew.replace('重庆', '重庆-重庆')
print(carnew.head(10))  # 检查修改成果

# 新增两列总部省份和总部城市
carnew['总部省份'] = carnew['总部'].str[0:2]
carnew['总部城市'] = carnew['总部'].str[3:]
print(carnew.head())  # 检查列是否新增
