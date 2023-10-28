import requests
from bs4 import BeautifulSoup
def get_novel_chapters():#chapters篇章 novel小说
    url = 'http://www.89wx.cc/26/26547/'
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
    soup = BeautifulSoup(r.text.replace('&nbsp;',"").replace('http://m.biquwu.cc','').replace('笔趣阁手机端',""), 'html.parser')#这行要好好看
    return soup.find("div",id='content').get_text()



novel_chapters=get_novel_chapters()
total_cnt=len(novel_chapters)
idx=0
for chapter in novel_chapters:
    idx+=1
    print(idx,'总章节为%s'%total_cnt)
    url, title=chapter
    with open("极品帝王小说 %s.txt"%title,'w',encoding='GBK') as fout:#要看
        fout.flush()
        fout.write(title + '\n' + get_chaper_content(url))
        print(get_chaper_content(url))