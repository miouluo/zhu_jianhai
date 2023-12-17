import requests
from bs4 import BeautifulSoup

hd = {'user-agent': 'chrome'}


# 网页为新华网时政页面

def get_one_article(article_url):
    html = requests.get(article_url, headers=hd)
    soup = BeautifulSoup(html.text, features='html.parser')
    titlenode = soup.find('span', class_='title')
    title = titlenode.getText()

    timenode = soup.find('div', class_='header-time left')
    time = timenode.getText()

    bodynode = soup.find('div', class_='main-left')
    body = bodynode.getText()

    return {
        'title': title,
        'time': time,
        'body': body}


# url = 'http://www.news.cn/politics/2023-12/17/c_1130031441.htm'  # 测试文章1篇
# article = get_one_article(url)
# print(article)


def get_article_urls(page_url):
    html = requests.get(page_url, headers=hd)
    soup = BeautifulSoup(html.text, features='html.parser')
    medium = soup.find_all('div', class_='tit')[:36]
    l = []
    for m in medium:
        # print(m.span.a['href'])
        l.append(m.a['href'])
    return l


url = 'http://www.news.cn/politics/index.html'
articles = get_article_urls(url)
print(articles)

def save(article):
    for idx, url in enumerate(articles, start=1):
        file_path = 'D:\python\big\txt'
        f = open(f"{file_path}{idx:02d}.txt", 'w', encoding='utf-8')
        f.write(f"标题: {article['title']}\n")
        f.write(f"时间: {article['time'].strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"\n{article['body']}")
        f.close()
    print('保存文章篇数', len(articles))


article = []
for url in articles:
    article.append(get_one_article(url))

save(article)
