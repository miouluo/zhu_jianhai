import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
data = pd.read_excel('EducationData.xlsx', sheet_name='Foundational learning')
data.head()

#经济状况/国家


# 使用groupby来按'Countries and areas'和'Development regions'列分组，然后计算每个国家在不同经济状态下的总值
grouped_data = data.groupby(['Countries and areas', 'Development regions'])['Total'].sum().reset_index()

# 创建一个柱状图
plt.figure(figsize=(30, 8))
plt.grid(True, linestyle='--', alpha=0.7)
# 使用柱状图显示每个国家的总值，每个国家在不同经济状态下有不同的柱子
for region in grouped_data['Development regions'].unique():
    region_data = grouped_data[grouped_data['Development regions'] == region]
    plt.bar(region_data['Countries and areas'], region_data['Total'], label=region)

plt.xlabel('Countries and areas')
plt.ylabel('Total percentage')
plt.title('Total percentage by Country and Development Regions')
plt.xticks(rotation=90)
plt.legend(title='Development Regions')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#年龄/国家




# 使用groupby来按'Countries and areas'和'Age group'列分组，并计算每个国家在不同年龄段的总值
grouped_data = data.groupby(['Countries and areas', 'Age group'])['Total'].sum().unstack().reset_index()

# 创建一个柱状图
plt.figure(figsize=(25, 8))
plt.grid(True, linestyle='--', alpha=0.7)
# 使用柱状图显示每个国家在不同年龄段的总值
x = range(len(grouped_data['Countries and areas']))
x_ticks = [i for i in x]

for age_group in grouped_data.columns[1:]:
    plt.bar(x, grouped_data[age_group], label=age_group)

plt.xlabel('Countries and areas')
plt.ylabel('Total percentage')
plt.title('Total percentage by Countries and Age Groups')
plt.xticks(x, grouped_data['Countries and areas'], rotation=90)
plt.legend(title='Age group')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#性别/国家


# 使用groupby来按'Countries and areas'列分组，并计算每个国家在'Girls'和'Boys'列下的总值
grouped_data = data.groupby('Countries and areas')[['Girls', 'Boys']].sum().reset_index()

# 创建一个折线图
plt.figure(figsize=(25, 8))
plt.grid(True, linestyle='--', alpha=0.7)
# 绘制折线图，显示每个国家在'Girls'和'Boys'列下的总值
x = range(len(grouped_data))
x_ticks = [i for i in x]

plt.plot(x, grouped_data['Girls'], label='Girls', marker='o')
plt.plot(x, grouped_data['Boys'], label='Boys', marker='x')

plt.xlabel('Countries and areas')
plt.ylabel('Total percentage')
plt.title('Total percentage by Countries and Gender')
plt.xticks(x, grouped_data['Countries and areas'], rotation=90)
plt.legend(title='Gender')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#地区/国家


# 使用groupby来按'Countries and areas'列分组，并计算每个国家在'Urban'和'Rural'列下的总值
grouped_data = data.groupby('Countries and areas')[['Urban', 'Rural']].sum().reset_index()

# 创建一个折线图
plt.figure(figsize=(25, 8))
plt.grid(True, linestyle='--', alpha=0.7)
# 绘制折线图，显示每个国家在'Urban'和'Rural'列下的总值
x = range(len(grouped_data))
x_ticks = [i for i in x]

plt.plot(x, grouped_data['Urban'], label='Urban', marker='o')
plt.plot(x, grouped_data['Rural'], label='Rural', marker='x')

plt.xlabel('Countries and areas')
plt.ylabel('Total percentage')
plt.title('Total percentage by Countries and Urban/Rural')
plt.xticks(x, grouped_data['Countries and areas'], rotation=90)
plt.legend(title='Area Type')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


