# -*- coding: UTF-8 -*-
import re
import time

import requests as t
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
index = 1
for page in range(1, 3):
    url = 'http://cpc.people.com.cn/GB/87228/index1.html'
    page_html = t.get(url, headers).text
    soup = BeautifulSoup(page_html, 'html.parser')
    de_ports = soup.select('.fl ul li a')
    for port in de_ports:
        de_href = port['href']
        if not de_href.startswith('http'):
            de_href = 'http://cpc.people.com.cn' + de_href
        print(f'抓取第：{index}篇文章：{de_href}')
        de_resp = t.get(de_href, headers)
        de_resp.encoding = 'gbk'
        de_html = de_resp.text
        soup_detail = BeautifulSoup(de_html, 'html.parser')
        title = re.findall('<h1.*?>(.*?)</h1>', de_html, re.S)[0].replace('&nbsp;', '')
        content = soup_detail.select(".show_text")[0].get_text().strip()
        if index < 10:
            num = '0' + str(index)
        else:
            num = index
        with open(f'txt/{num}.txt', 'w', encoding='utf-8') as fr:
            fr.write(f'{title}\n\n{content}')
        time.sleep(2)
        index += 1

