import requests
from bs4 import BeautifulSoup
from datetime import datetime
hd = {'user-agent': 'chrome'}


def get_one_article(article_url):
    r = requests.get(article_url, headers=hd)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text,'html.parser') # 指定解析器为html.parser
    title = soup.find('h1', class_='u-title')
    info = soup.find('span', class_='m-con-time')
    # 将时间字符串转换为datetime对象
    time_obj = datetime.strptime(info.get_text(), '%Y-%m-%d %H:%M')
    # 将datetime对象转换为指定格式的字符串
    time_str = time_obj.strftime('%Y-%m-%d')
    body = soup.find('div', class_='u-mainText')
    return {
        'title': title.get_text(),
        'info': time_str, # 修改时间格式
        'body': body.get_text()
    }
def get_article_urls(page_url, domain=''):
    r = requests.get(page_url, headers=hd)
    soup = BeautifulSoup(r.text)
    rtn = []
    all_divs = soup.find_all('p',class_="main_title")
    for div in all_divs:
        rtn.append(domain + div.a['href'])
    return rtn

def save_one_article(i, article):
    filename = str(i+1).zfill(2) + '.txt'
    f = open('../txt/' + filename, 'w',encoding='utf-8')
    f.write(article['title']+ '\n')
    f.write(article['info']+ '\n')
    f.write(article['body'])
    f.close()
    print('Saved article', i+1, ':', article['title'])
    print('Word count:', len(article['body']))

def save(articles):
    f = open('统计.csv', 'w',encoding='utf-8',errors='replace')
    f.write('编号,时间,字数,标题\n')
    for i in range(len(articles)):
        line = str(i+1) + ','#序号
        line += articles[i]['info'] + ',' #时间
        line += str(len(articles[i]['body'])) + ','#字数
        line += articles[i]['title'].strip()#标题
        f.write(line + '\n')
        save_one_article(i, articles[i])
    f.close()

prefix = 'https://guancha.gmw.cn/node_11273_'
page_urls = [prefix + str(i)+ '.htm' for i in range(2,12)]
article_urls = []

for page in page_urls:
    print('###', page)
    tmp = get_article_urls(page,'https://guancha.gmw.cn/')
    article_urls.extend(tmp)

articles = []
for url in article_urls:
    print('>>>', url)
    articles.append(get_one_article(url))

save(articles)