import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime

hd = {'user-agent': 'chrome'}


# 读取标题、时间、正文
def get_one_article(article_url):
    r = requests.get(article_url, headers=hd)
    # r.encoding = 'utf-8'  # 乱码
    r.encoding = 'gbk'
    soup = BeautifulSoup(r.text)

    title = soup.find('h1', id='articleTitle')
    info = soup.find('span', id='articleTime')
    info = str(info)

    # 对获取的时间进行处理
    match = re.search(r'\d{4}年\d{1,2}月\d{1,2}日', info)
    if match:
        extracted_date = match.group()
    info = datetime.strptime(extracted_date, '%Y年%m月%d日').strftime('%Y-%m-%d')
    body = soup.find('div', class_='TRS_Editor')

    return {
        'title': title.get_text(),
        'info': info,
        'body': body.get_text()
    }


##测试是否能提取到标题、时间和正文内容
# url = 'http://www.ce.cn/xwzx/shgj/gdxw/202311/23/t20231123_38803060.shtml'
# get_one_article(url)


# 获取对应页码下的所有访问链接
# 一个页面下有 40 个 链接
def get_article_urls(page_url, domain=''):
    ''' 若文章url为相对地址，则需补上域名（domain） '''
    r = requests.get(page_url, headers=hd)
    soup = BeautifulSoup(r.text)
    rtn = []
    all_div = soup.find_all('span', class_='f1')
    for div in all_div:
        rtn.append(domain + div.a['href'])
    return rtn


def save_one_article(i, article):
    f = open('txt/' + str(i) + '.txt', 'w', encoding='utf-8')
    f.write(article['title'])
    f.write(article['info'])
    f.write(article['body'])
    f.close()


def save(articles):
    ''' 可保存于txt、excel或数据库中 '''
    f = open('统计.csv', 'w', encoding='gbk')
    f.write('编号,时间,字数,标题\n')
    for i in range(len(articles)):
        line = str(i) + ','  # 编号
        line += articles[i]['info'] + ','  # 时间
        line += str(len(articles[i]['body'])) + ','  # 字数
        line += articles[i]['title'].strip()  # 标题
        f.write(line + '\n')
        save_one_article(i, articles[i])
    f.close()


prefix = 'http://www.ce.cn/xwzx/shgj/gdxw/index_'
# 爬取25 页耗时较久，测试时建议 range(1, 3)
page_urls = [prefix + str(i) + '.shtml' for i in range(1, 3)]
article_urls = []  # 解析得，所有文章的 url 列表
for page in page_urls:
    print('###', page)
    tmp = get_article_urls(page, 'http://www.ce.cn/xwzx/shgj/gdxw/')
    article_urls.extend(tmp)

articles = []  # 爬取得，所有文章title、info、body
for url in article_urls:
    print('>>>', url)
    articles.append(get_one_article(url))

save(articles)