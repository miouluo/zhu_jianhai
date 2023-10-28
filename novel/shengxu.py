# -*- coding: gbk -*-


import requests
from bs4 import BeautifulSoup
import io
def get_novel_chapters():#chapters篇章 novel小说
    url = 'http://www.89wx.cc/35/35532/'
    r=requests.get(url)
    r.encoding="gbk"
    soup=BeautifulSoup(r.text,'html.parser')

    data=[]
    for dd in soup.find_all('dd'):
        link=dd.find("a")
        if not link:
            continue
        data.append(('http://www.89wx.cc%s'%link['href'],link.get_text()))
    return data

def get_chaper_content(url):
    r=requests.get(url)
    r.encoding='gbk'
    soup = BeautifulSoup(r.text.replace('&nbsp;',"").replace('大漠孤烟直，长河落日圆。Ω笔趣阁ＷｗＷ．ｂｉｑＵｗＵ．Ｃｃ','').replace('http://m.biquwu.cc','').replace('笔趣阁手机端',""), 'html.parser')#这行要好好看
    return soup.find("div",id='content').get_text()



novel_chapters=get_novel_chapters()
total_cnt=len(novel_chapters)
idx=0
with open("圣墟.txt", 'a+', encoding='GBK') as fout:
    for chapter in novel_chapters:
        idx += 1
        print(idx, '总章节为%s' % total_cnt)
        url, title = chapter
        fout.write(title + '\n' + get_chaper_content(url))
        print(get_chaper_content(url))