import requests
from bs4 import BeautifulSoup

hd = {'user-agent': 'chrome'}
url = 'https://news.seig.edu.cn/cms/8135.html'
r = requests.get(url, headers=hd)
r.encoding = 'utf-8'

soup = BeautifulSoup(r.text,features='html.parser')
title = soup.find('div', class_='article-title')
info = soup.find('div', class_='article-info text-muted')
body = soup.find('div', class_='article-body')
print( title.get_text() )
print( info.get_text() )
print( body.get_text() )
