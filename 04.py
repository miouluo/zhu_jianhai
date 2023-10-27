import pandas as pd
import numpy as np
#第三章 pandas统计分析基础

#实训1
#使用read_csv函数读取音乐行业收入信息表
housedata = pd.read_csv('./某地区房屋销售数据.csv', encoding='gbk')
print(housedata.head(5))
#查看数据的维度、形状以及所有特征的名称
print('某地区房屋销售信息表的维度为: ',housedata.ndim)
print('某地区房屋销售信息表的形状为:',housedata.shape)
print('某地区房屋销售信息表的列名为:\n ',housedata.columns)
#对房屋类型为单身公寓的数据进行索引等操作
unit1 = housedata.loc[housedata['房屋类型'] == 'unit']
print('对房屋类型为单身公寓的数据进行索引',unit1)
unit2 = housedata.iloc[(housedata["房屋类型"] == 'unit').values]
print('对房屋类型为单身公寓的数据进行索引',unit2)


#实训2
housedata = pd.read_csv('./某地区房屋销售数据.csv', sep=',', encoding='gbk')
# 输出转换前的原始date列的类型
print('进行转换前date的类型为：', housedata['房屋出售时间'].dtypes)
# 使用to_datetime函数将data列的数据类型转换成标准时间类型
housedata['房屋出售时间'] = pd.to_datetime(housedata['房屋出售时间'])
print('进行转换后date的类型为：', housedata['房屋出售时间'].dtypes)
#使用mean、max、min、mode函数分别计算该地区房屋价格的均值、最大值、最小值和众数
print('最小时间为：', pd.Timestamp.min)  # 查询计算机中最早的时间信息
print('最大时间为：', pd.Timestamp.max)  # 查询计算机中最晚的时间信息
# 计算价格均值
price_mean = housedata['房屋价格'].mean()
print('该地区房屋价格的均值为：', price_mean)
# 计算价格众数
price_mode = housedata['房屋价格'].mode()[0]  # 注意，众数可能有多个，这里只返回第一个众数
print('该地区房屋价格的众数为：', price_mode)
#使用quantile函数计算该地区房屋价格的分位数
q1 = housedata['房屋价格'].quantile(0.25)  # 计算第一四分位数（25% 分位数）
q2 = housedata['房屋价格'].quantile(0.5)   # 计算中位数（50% 分位数）
q3 = housedata['房屋价格'].quantile(0.75)  # 计算第三四分位数（75% 分位数）
print('该地区房屋价格的第一四分位数为：', q1)
print('该地区房屋价格的中位数为：', q2)
print('该地区房屋价格的第三四分位数为：', q3)
#使用describe()方法计算房屋价格数据的非空值数目、均值等统计量
# 计算价格数据的描述性统计量
price_stats = housedata['房屋价格'].describe()
print(price_stats)


#实训3
housedata = pd.read_csv('./某地区房屋销售数据.csv', sep=',', encoding='gbk')
#使用apply()方法生成new_postcode特征
# 定义生成 new_postcode 的函数
def generate_new_postcode(row):
    # 获取原始 postcode 值
    postcode = str(row['地区邮编'])
    # 在原始 postcode 值前添加 'New_' 前缀
    new_postcode = 'New_' + postcode
    return new_postcode
# 使用 apply() 方法生成 new_postcode 特征
housedata['new_postcode'] = housedata.apply(generate_new_postcode, axis=1)
# 打印数据集
print(housedata)
#使用agg()方法和count函数计算出每个地区的房屋售出总数
result = housedata.groupby('地区邮编').agg(total_sold=('地区邮编', 'count'))
print(result)
#使用groupby()方法对房屋类型propertyType进行分组，并对新地区邮编new_postcode进行分组后赋值给新的数据框housesalel
housesalel = housedata.groupby(['房屋类型','new_postcode'])
for (房屋类型, new_postcode), group in housesalel:
    print("Property Type: ", 房屋类型)
    print("New Postcode: ", new_postcode)
    print("Number of Sales: ", len(group))
#使用transform()聚合方法和mean函数计算housesalel中房屋价格的均值
housesalel = pd.DataFrame({
    '房屋类型': ['house','unit'],
    'new_postcode': ['New_2600','New_2601'],
    '房屋价格': ['825000','790000']
})
# 计算每个区域的房屋价格均值
mean_prices = housesalel.groupby('new_postcode')['房屋价格'].transform('mean')
# 将计算结果赋给新的列
housesalel['房屋价格均值'] = mean_prices
print(housesalel)


#实训4
#使用pivot_table函数创建数据透视表
housedata = pd.read_csv('./某地区房屋销售数据.csv', sep=',', encoding='gbk')
housedataPivot = pd.pivot_table(housedata[[
      '地区邮编', '房屋价格', '房屋类型']],
      index='地区邮编')
print('以地区邮编作为分组键创建的订单透视表为：\n', housedataPivot.head())
#使用crosstab函数创建数据交叉表
housedataCross = pd.crosstab(index=housedata['地区邮编'],
      columns=housedata['房屋类型'],
      values=housedata['房屋价格'], aggfunc = np.sum)
print('以地区邮编和房屋类型为分组键value_actual为值的透视表前5行4列为：\n',
      housedataCross.iloc[:5, :4])