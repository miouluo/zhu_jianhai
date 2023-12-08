# 如何读取不同数据源

import pandas as pd

# 读取文本数据
data_txt = pd.read_csv('地址/文件名.txt', sep=' ')
data_csv = pd.read_csv('地址/文件名.csv', encoding='GBK', header=0)
#sep 设置分隔符、header 将某行数据作为列名称。有默认、engine 表示数据解析引擎，有中文时常用GBK。、names 接受列名称。

'''
读取Excel文件
data_excel = pd.read_excel('文件的位置/文件名称.xlsx', sheet_name='meal_order_detail2')
sheetname,设置读取的表名、header，将某行数据转化为列名称。
excel的存储
data_excel.to_excel('目标文件夹/存储的文件名称.xlsx', index=None, sheet_name='test1')
index=none在保存时可以去除存在于左边的编号。
'''

# DataFrame常用操作
import pandas as pd
#通过字典创造一个表格并查看其数据,每个字典对应一列
d={'people':['man','women','elder man','teen'],'high':[1.7,1.6,1.65,1.8],'weight':[140,90,70,100]}
df=pd.DataFrame(d,index=[1,2,3,4])
print(df)

#常用属性
'''values 元素
index 索引
columns 列名
dtypes 类型
size 元素个数
ndim 维度数
shape 数据形状（行列数目）
'''
print(df.values)
print(df.index)
print(df.shape)
print(df.dtypes)
print(df.columns)
print(df.ndim)

#访问数据框的元素
d={'people':['man','women','elder man','teen'],'high':[1.7,1.6,1.65,1.8],'weight':[140,90,70,100],'work':['teacher','mother','','']}
df=pd.DataFrame(d,index=[1,2,3,4])
print(df)
print(df['high'])#单列访问

print(df[['people','weight']])#多列数据访问
print(df.head(3))     # 访问某几行数据,head头几行
print(df.tail(3))    #tail末几行

print(df.iloc[0, 0])    # 按照行列顺序进行数据访问
print(df.iloc[0:3, 0])
print(df.iloc[:, 0])
print(df.iloc[0, :])
print(df.iloc[1:3, 1:3]) #是一个左开右闭区间

print(df.loc['1', 'people'])   # 按照行列名称进行数据访问
print(df.loc['1':'3', 'people'])
print(df.loc[:, 'people'])
print(df.loc['1', :])
print(df.loc[['2','3'], ['high', 'weight']])