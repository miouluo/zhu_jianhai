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