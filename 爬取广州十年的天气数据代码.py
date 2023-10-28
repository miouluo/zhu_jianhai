import requests
import pandas as pd
import html5lib
import lxml
from io import StringIO
url='https://tianqi.2345.com/Pc/GetHistory'

headers={
'User-Agent': '''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76'''
,'Sec-Fetch-Site': 'same-origin'
}

def craw_table(year,month):

    '''提供年份和月份爬取对应的表格数据'''

    params = {
        "areaInfo[areaId]": 59287,
        "areaInfo[areaType]": 2,
        'date[year]': year,
        'date[month]': month
    }
    resp = requests.get(url, headers=headers, params=params)  # 因为在原文中也是用get
    date = resp.json()['data']#他就是有一点像表格th是列名td是值
    print(date)
    html_string = StringIO(date)
    df = pd.read_html(html_string)[0]#df=pd.read_html(data)[0]不能这样用了要改
    #pd.read_html只针对table标签，如果没有就没有用
    #<tr>每一行行数，<td>表格里面的内容，<th>表格的标题,就两个数据组成一个好的表格
    print(df)
    return df

df_list=[]
for year in range(2011,2023):
    for month in range(1,13):
        print('爬取：%s,%s'%(year,month))
        df = craw_table(year, month)
        df_list.append(df)

print(df_list)
pd.concat(df_list).to_excel("广州12年的天气情况数据.xlsx",index=False)#要openpyxl进行作用了