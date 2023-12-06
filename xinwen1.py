import requests
import os
from bs4 import BeautifulSoup
import csv
import re
import threading
import queue
from lxml import etree
from concurrent.futures import ThreadPoolExecutor

hd = {'user-agent': 'chrome'}


def get_one_article(article_url):
    r = requests.get(article_url, headers=hd)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    text = etree.HTML(r.text)
    title1 = soup.find('li', class_='left left-main')
    title=soup.find('h3')
    info = text.xpath('.//div[@class="time fix"]/span//text()')[0:1]
    # info = soup.find('div', class_='time fix')
    body = soup.find('div', class_='content all-txt')

    return {
        'title': title.get_text() if title else '',
        'info': info[0] if info else '',
        'body': body.get_text() if body else ''}


def get_article_urls(page_url, domain=''):
    r = requests.get(page_url, headers=hd)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')

    rtn = []
    all_div = soup.find_all('div', class_='right fn')
    for div in all_div:
        rtn.append(domain + div.h4.a['href'])

    return rtn


def save_one_article(i, article):
    folder_path = r'G:\大二上学期\python\作业\课设\2240512122万佳佳\txt'
    if i<10:
        f = open(os.path.join(folder_path, '0'+str(i+1) + '.txt'), 'w', encoding='utf-8')
        f.write(article['title'])
        f.write(article['info'])
        f.write(article['body'])
        f.close()
    else:
        f = open(os.path.join(folder_path, str(i+1) + '.txt'), 'w', encoding='utf-8')
        f.write(article['title'])
        f.write(article['info'])
        f.write(article['body'])
        f.close()

    print('第', i+1, '篇文章', len(article['body']))
    print('字数', article['title'])

    return len(article['body'])


def save(articles):
    folder_path = r'G:\大二上学期\python\作业\课设\2240512122万佳佳\src'
    csv_path = os.path.join(folder_path, '统计.csv')

    with open(csv_path, 'w', encoding='utf-8', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['编号', '时间', '字数', '标题'])

        for i, article in enumerate(articles):
            word_count = save_one_article(i, article)
            if i<9:
                csv_writer.writerow(['0'+str(i+1), article['info'].strip(), word_count, article['title'].strip()])
            else:
                csv_writer.writerow([i+1, article['info'].strip(), word_count, article['title'].strip()])



prefix = 'https://www.guancha.cn/economy/2023_11_27_7171'
page_urls = [prefix + str(i) + '.shtml' for i in range(42, 44)]

article_urls = []

for page in page_urls:
    print('###', page)
    tmp = get_article_urls(page, 'https://www.guancha.cn/')
    article_urls.extend(tmp)

print(tmp)
articles = []

for url in article_urls:
    print('>>>', url)
    articles.append(get_one_article(url))

save(articles)
