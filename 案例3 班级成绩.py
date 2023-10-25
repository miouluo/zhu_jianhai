# 1、导包。读取数据
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
import seaborn as sns

df=pd.read_csv("score.csv",sep = ",")  # sep 分隔符 用逗号隔开
print('There are ',len(df.columns),'columns')
for c in df.columns:
    sys.stdout.write(str(c)+',')
# stout.write 可以在命令行窗口写入，输出变量
# str（c） 强制转换为字符串，以逗号间隔开

# 2、重命名变量，查看数据信息
# rename 重命名
df = df.rename(columns={'Chance of Admit ':'Chance of Admit'})
print(df.info())

# 3、查看数据集前5行和后5行
print(df.head())
print(df.tail()) # tail() 输出后5行
print(df.head(6))
print(df.tail(6))

# 4、绘制相关系数矩阵热图
fig,ax=plt.subplots(figsize=(10,10))
sns.heatmap(df.corr(),ax=ax,annot=True,linewidths=0.05,fmt='2f',cmap='magma')
print(df.corr())
plt.show()
# heatmap 话热图
# corr 求相关系数的值（矩阵）
# fmt 保留2位小数
# magma 一种配色方案

# 5、是否做过科学研究
print("Not Having Research:",len(df[df.Research == 0]))
print("Having Research:",len(df[df.Research == 1]))

# 6、是否做过科学研究绘图可视化
y = np.array([len(df[df.Research == 0]),len(df[df.Research == 1])])
x = np.arange(2)
plt.bar(x,y)
plt.title("Research Experience")
plt.xlabel("Canditates")
plt.ylabel("Frequency")
plt.xticks(x,("Not having research","Having research"))
plt.show()
# bar 画柱状图

# 7、统计托福成绩情况
y = np.array([df['TOEFL Score'].min(),df['TOEFL Score'].mean(),df['TOEFL Score'].max()])
x = np.arange(3)
plt.bar(x,y)
plt.title('TOEFL Score')
plt.xlabel('Level')
plt.ylabel('TOEFL Score')
plt.xticks(x,('Worst','Average','Best'))
plt.show()

# 8、绘制 GRE 成绩直方图
df['GRE Score'].plot(kind='hist',bins=200,figsize=(6,6))
plt.title('GRE Score')
plt.xlabel('GRE Score')
plt.ylabel('Frequency')
plt.show()
# kind类型
# hist直方图

# 9、绘制学校排名与 CGPA 的散点图
plt.scatter(df['University Rating'],df['CGPA'])
# plt.scatter(df['CGPA'],df['University Rating'])
plt.title('CGPA Scores for University ratings')
plt.xlabel('University Rating')
plt.ylabel('CGPA')
plt.show()

# 10、绘制 GRE 与 CGPA 散点图
plt.scatter(df['GRE Score'],df['CGPA'])
plt.title('CGPA for GRE Scores')
plt.xlabel('GRE Score')
plt.ylabel('CGPA')
plt.show()

# 11、绘制 GRE 与 托福成绩的散点图（CGPA >=8.5）
df[df['CGPA']>=8.5].plot(kind='scatter',x='GRE Score',y='TOEFL Score',color='red')
plt.xlabel('GRE Score')
plt.ylabel('TOEFL Score')
plt.title('CGPA >= 8.5')
plt.grid(True)
plt.show()

# 12、绘制申请人数与大学排名柱状图（录取概率 > 75%）
s = df[df['Chance of Admit'] >= 0.75]['University Rating'].value_counts().head(5)
plt.title('University Ratings of Candidates with an 75% acceptance chance')
s.plot(kind='bar',figsize=(10,10),cmap='Pastel1')
plt.xlabel('University Rating')
plt.ylabel('Candidates')
plt.show()

# 13、绘制 SOP 与 CGPA 成绩的散点图
plt.scatter(df['CGPA'],df['SOP'])
plt.xlabel('CGPA')
plt.ylabel('SOP')
plt.title('SOP for CGPA')
plt.show()

# 14、绘制 SOP 与 GRE 成绩的散点图
plt.scatter(df['GRE Score'],df['SOP'])
plt.xlabel('GRE Score')
plt.ylabel('SOP')
plt.title('SOP for GRE Score')
plt.show()