# -*- coding: gbk -*-


import requests
from bs4 import BeautifulSoup
import io
def get_novel_chapters():#chaptersƪ�� novelС˵
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
    soup = BeautifulSoup(r.text.replace('&nbsp;',"").replace('��Į����ֱ����������Բ������Ȥ��ף��ף�����գ��գ��ã�','').replace('http://m.biquwu.cc','').replace('��Ȥ���ֻ���',""), 'html.parser')#����Ҫ�úÿ�
    return soup.find("div",id='content').get_text()



novel_chapters=get_novel_chapters()
total_cnt=len(novel_chapters)
idx=0
with open("ʥ��.txt", 'a+', encoding='GBK') as fout:
    for chapter in novel_chapters:
        idx += 1
        print(idx, '���½�Ϊ%s' % total_cnt)
        url, title = chapter
        fout.write(title + '\n' + get_chaper_content(url))
        print(get_chaper_content(url))