import requests
from bs4 import BeautifulSoup

hd = {'user-agent': 'chrome'}
url = 'https://news.seig.edu.cn/cms/news/1/p/1.html'
r = requests.get(url, headers=hd)
r.encoding = 'utf-8'

soup = BeautifulSoup(r.text,features='html.parser')
div0 = soup.find_all('div', class_='media-body')
# 遍历所有找到的div标签，并打印它们的文本内容
for div in div0:
    print(div.text)