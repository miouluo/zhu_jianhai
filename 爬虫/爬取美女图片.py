# -*- coding: UTF-8 -*-
#上面那行很重要


'''
爬取图片，并且下载图片
url:https://pic.netbian.com/4kmeinv/

'''


#获取网页的源代码
import requests
from bs4 import BeautifulSoup
import re
import os.path







def craw_html(url):
      headers = {

            'Sec - Fetch - Dest':

                  'document',

            'Sec - Fetch - Mode':

                  'navigate',

            'Sec - Fetch - Site':

                  'cross - site',

      }
      resq = requests.get(url,headers=headers)
      resq.encoding='gbk'
      html = resq.text
      return html




def parse_and_download(html):
      soup = BeautifulSoup(html, 'html.parser')
      imgs = (soup.find('div', id='main')
              .find('div', class_='slist')
              .find('ul', class_='clearfix')
              .find_all('div', class_='pic')
              )
      for img in imgs:
            pattern = r'url\((.*?)\)'
            src = re.search(pattern, img['style'])
            filname = os.path.basename(src.group(1))
            with open(f"美女图片/{filname}", 'wb') as f:
                  resp_img = requests.get(src.group(1))#group（0）为全返回group(1)放回第一个
                  f.write(resp_img.content)







urls=['https://pic.netbian.top/4kmeinv/index.html']+[
      f'https://pic.netbian.top/4kmeinv/index_{i}.html'
      for i in range(2,11)
]
for url in urls:
      print("正在爬取%s"%url)
      html=craw_html(url)
      parse_and_download(html)
# from docx import Document
#
# # 创建一个Document对象
# document = Document()
#
# # 添加文本
# document.add_paragraph(html)
#
# # 保存文档
# document.save('example.docx')


