import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
#设置中文编码和负号的正常显示
plt.rcParams['font.family']='Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False


# 每月订单数量的折线图
data1=df[df['price']>0].groupby('Month')['order_id'].nunique()
plt.figure(figsize=(16,10))
plt.plot(data1, color='g')
plt.xlabel('月份')
plt.ylabel('订单数量')
plt.title('每月订单数量')
for x,y in enumerate(data1):
    plt.text(x+0.75,y+2000,y)
    plt.plot(data1,color='r',linestyle=':',linewidth=1.2,marker='*',markersize=7)
    plt.plot(data1)
plt.show()

#不同省份成交金额的水平柱状图
chengjiao_price=df[df['price']>0].groupby('local')['price'].sum()
chengjiao_price
plt.figure(figsize=(12,8))
chengjiao_price.sort_values(ascending=True).plot.barh()
plt.xlabel('成交金额')
plt.ylabel('省份')
plt.title('不同省份成交金额')
plt.show()


#不同省份用户男女人数对比簇状柱形图
number_man=df[(df['price']>0)&(df['sex']=='男')].groupby('local')['sex'].count()
number_woman=df[(df['price']>0)&(df['sex']=='女')].groupby('local')['sex'].count()
cities = df['local'].value_counts( ).index
plt.figure(figsize=(13, 4))
x = np.arange(len(cities))  # x轴刻度标签位置
width = 0.25  # 柱子的宽度
# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
# x - width/2，x + width/2即每组数据在x轴上的位置
plt.bar(x - width/2, number_man, width, label='男')
plt.bar(x + width/2, number_woman, width, label='女')
plt.ylabel('人数')
plt.title('不同省份用户男女人数对比簇状柱形图')
# x轴刻度标签位置不进行计算
plt.xticks(x,labels=cities)
plt.legend()# 图列
plt.show()
