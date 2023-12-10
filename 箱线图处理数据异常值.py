import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_excel('文件的地址/文件名.xlsx',sheet_name='选择你要的表格，没有选择可以不填，有默认')
#箱线图判断异常值
data2=data['表中的列名称']          #提取表格中需要分析的列，可以同时分析多个列
data3=data['Female']
data4=data['Male']
Tdata=[data2,data3,data4]        #将三列数据放在一起
plt.boxplot(Tdata,labels=["Total","Female","Male"])   #labels 表的名称，有三张图就得有三个表名称
plt.show()

#定义一个函数，处理异常值
def replace(x):
    import  numpy as np
    QU = x.quantile(0.75)
    QL = x.quantile(0.25)
    IQR = QU-QL
    x[(x > (QU + 1.5*IQR)) | (x < (QL-1.5*IQR))] =np.nan
    return x

#将异常值变为空值
replace(data['Total'])
replace(data['Female'])
replace(data['Male'])