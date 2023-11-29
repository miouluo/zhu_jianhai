from lxml import etree

with open('data/html_doc.html') as f:
    html_doc = f.read()

# 使用lxml.etree + Xpath解析网页
dom = etree.HTML(html_doc)
dom.xpath('/html/head/title/text()')
dom.xpath('//title/text()')
dom.xpath('/html//titlea/text()')

dom.xpath('//body/p/a[1]/text()')
dom.xpath('//body/p/a[@id="link1"]/text()')
dom.xpath('//body/p/a[@id="link1"]/@href')      # 提取目标元素的属性值(@href表示是一个超链接)
dom.xpath('//body/p/a[@id="link1"]/@class')     # 提取目标元素的属性值(@class可以理解为一个标识，用来标识特定的标签。)

# 使用beautifulsoup + CSS Seletor解析网页
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'lxml')    # 解析网页数据，得到BeautifulSoup对象
# # 通过标签名获取元素
# soup.title
# soup.p
# soup.a

soup.select('html > head > title')        # 绝对路径写法
soup.select('body a')                     # 相对路径写法
soup.select('p > a:nth-child(1)')         # 在路径中添加元素序号信息
soup.select('p > a[id="link1"]')          # 在路径中添加元素属性信息

type(soup.select('p > a:nth-child(1)')[0])           # 查找提取出的元素的类型
soup.select('p > a:nth-child(1)')[0].text            # 提取目标元素的文本内容
soup.select('p > a:nth-child(1)')[0].get('href')     # 提取目标元素的属性值

soup.find_all('title')              # 查找所有的title标签
soup.find_all('a', id='link1')      # 查找id属性为link1的a标签
