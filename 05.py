import pandas as pd
import numpy as np
#第四章 使用pandas进行数据预处理

#实训1
#利用read_excel函数读取healthcare-dataset-stroke.xlsx表
healthdata1=pd.read_excel('./healthcare-dataset-stroke.xlsx')
print(healthdata1.head(5))
#利用read_excel函数读取healthcare-dataset-age_abs.xlsx表
healthdata2=pd.read_excel('./healthcare-dataset-age_abs.xlsx')
print(healthdata2.head(5))
#查看两表的数据量
stroke_rows, stroke_cols = healthdata1.shape
age_abs_rows, age_abs_cols = healthdata2.shape
print("healthcare-dataset-stroke.xlsx 表的数据量：{} 行, {} 列".format(stroke_rows, stroke_cols))
print("healthcare-dataset-age_abs.xlsx 表的数据量：{} 行, {} 列".format(age_abs_rows, age_abs_cols))
#以编号作为主键进行外连接(合并2个表格）
# 读取第一个表格
df1 = pd.read_excel('./healthcare-dataset-stroke.xlsx')
# 读取第二个表格
df2 = pd.read_excel('./healthcare-dataset-age_abs.xlsx')
# 执行外连接操作
result= pd.merge(df1, df2, on='编号', how='outer')
#查看数据是否合并成功
print(result)


#实训2
#获取年龄特征
print(result[['编号', '年龄']])
#利用for循环获取年龄特征中的数值，并用if-else语句判断年龄数值是否为异常值
# 获取年龄列的数值并进行异常值判断
for age in result['年龄']:
    # 将年龄值转换为整数
    age_int = int(age)
    # 判断年龄是否为小数或者超出正常范围
    if age % 1 != 0 or age < 0 or age > 120:
        print(f"异常年龄：{age}")
    else:
        print(f"正常年龄：{age}")
#若年龄数值为异常值，则删除异常值
# 删除年龄列中的异常值
result = result[(result['年龄'] % 1 == 0) & (result['年龄'] >= 0) & (result['年龄'] <= 120).reset_index(drop=True)]
# 输出删除异常值后的结果
print(result)


#实训3
#获取年龄特征
print(result[['编号', '年龄']])
#使用等宽发离散化对年龄特征进行离散化
age_cut = pd.cut(result['年龄'], 5)
print('离散化后5条记录年龄分布为：\n', age_cut.value_counts())