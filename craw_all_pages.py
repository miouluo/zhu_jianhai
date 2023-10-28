import re

from utils import url_mangager
import requests
from bs4 import BeautifulSoup

root_url='http://www.crazyant.net'

urls=url_mangager.UrlManger()#类的调取
urls.add_new_url(root_url)

fout=open('craw_all_pages.txt', 'w',encoding='UTF-8')#文本的写入
while urls.has_new_url():
    curr_url = urls.get_url()#获取url
    r=requests.get(curr_url,timeout=3)
    if r.status_code!=200:#不对的话就就报错而且跳过
        print(curr_url,'error')
        continue
    soup=BeautifulSoup(r.text,"html.parser")#使用'html.parser'解析器给r.text返回一个Beautiful Soup对象方便接下来的操作
    title=soup.title.string#soup是Beautiful Soup对象 title是html中的<title>的标签，string是获取标签中的文本内容

    fout.write('%s\t%s\n'%(curr_url,title))
    print('success:%s\t%s'%(curr_url,title))

    fout.flush()

    links=soup.find_all('a')#

    for link in links:
        href=link.get("href")#获取HTML文档里面的href属性的值
        if href is None:
            continue
        pattern=r'^http://www.crazyant.net/\d+.html$'
        if re.match(pattern,href):#match匹配函数
            urls.add_new_url(href)

fout.close()