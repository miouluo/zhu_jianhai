import requests
from bs4 import BeautifulSoup

hd = {'user-agent': 'chrome'}


def get_one_article(article_url):
    title = ''
    ''
    ''
    html = requests.get(article_url, headers=hd)
    # print(html.text)
    soup = BeautifulSoup(html.text, features='html.parser')
    titlenode = soup.find('div', class_='article-title')
    title = titlenode.getText()
    # print(titlenode)
    # title = titlenode.h4.string

    infonode = soup.find('div', class_='article-info text-muted').ul
    # print(infonode)
    info = infonode.getText()

    bodynode = soup.find('div', class_='article-body')
    body = bodynode.getText()
    # print(bodynode.text)

    return {
        'title': title,
        'info': info,
        'body': body}


url = 'https://news.seig.edu.cn/cms/8135.html'  # 测试文章1篇
article = get_one_article(url)
# print(article)


# 2
def get_article_urls(page_url, domain=''):
    """ 若文章url为相对地址，则需补上域名（domain） """
    html = requests.get(page_url, headers=hd)
    soup = BeautifulSoup(html.text, features='html.parser')
    medium = soup.find_all('div', class_='media')
    l = []
    for m in medium:
        # print(m.div.h3.a['href'])
        l.append(domain + m.div.h3.a['href'])
    # print(l)
    return l


def save(articles):
    for articles in article:
        f = open(articles['title'].replace('\n','') + '.txt', 'w', encoding='utf-8')
        f.write(articles['body'])
        f.close()
    print('保存文章篇数', len(articles))


url = 'https://news.seig.edu.cn/cms/news/1/p/%d.html'  # 测试第一页
article_urls = []
for i in range(1, 7):
    url2 = url % (i)
    article_urls.extend(get_article_urls(url2, 'https://news.seig.edu.cn'))
# print(article_urls)

# 3
article = []
for url in article_urls:
    article.append(get_one_article(url))

save(article)
