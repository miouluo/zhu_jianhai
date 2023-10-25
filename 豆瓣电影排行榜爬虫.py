# # 导包
# import urllib.request
# from lxml import etree
# import urllib.parse
#
#
# #（1）请求对象定制
# url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'
#
# headers = {
# 'User-Agent':
#             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.3162 SLBChan/105'
# }
#
# data = {
#     'type': 5,
#     'start': 0,
#     'limit': 20
# }
# data = urllib.parse.urlencode(data)
#
# request = urllib.request.Request(url=url, headers=headers)
#
# # (2)模拟浏览器访问数据
# response = urllib.request.urlopen(request)
#
# # （3）获取网页内源码
# content = response.read().decode('utf-8')
# print(content)
#
# # (4)下载数据到本地
# # fp = open('豆瓣电影.json', 'w', encoding='utf-8')
# # fp.write(content)
#
# # https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20
# # https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=40&limit=20
#
# # (5)数据解析
# tree = etree.HTML(content)
# # all_list = tree.xpath('//div[@id="wrapper"]/@class')
# # print(all_list)




# import requests
# from lxml import etree
# if __name__ == "__main__":
#     #  指定url
#     url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'
#     #  发起请求
#     #  get方法会返回一个响应对象
#
#     headers = {
#          'User-Agent':
#                     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.3162 SLBChan/105',
#         'Cookie':'ll="118281"; bid=Rfk-m0KxM1U; _pk_id.100001.4cf6=132dc2f52115643f.1686377984.; __yadk_uid=2kj3oECs8MGzQVqAdQWdzcMM98GOV4le; _vwo_uuid_v2=D69D690B6EABC08F6995A648D92027D30|78192d79f301de50d065965b2ceee0db; _pk_ref.100001.4cf6=["","",1686469387,"https://www.baidu.com/link?url=rt94w5-zvp22NFQJUQbAwdUH-uVNmPz_HqRkXxjZ-pgEco5cF-M1YXOiF_959klJ&wd=&eqid=8ff5149b000aa5490000000664857b06"]; _pk_ses.100001.4cf6=1; __utma=30149280.742110040.1686377984.1686377984.1686469387.2; __utmc=30149280; __utmz=30149280.1686469387.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt_douban=1; __utma=223695111.1537790935.1686377984.1686377984.1686469387.2; __utmb=223695111.0.10.1686469387; __utmc=223695111; __utmz=223695111.1686469387.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap_v=0,6.0; __utmb=30149280.4.10.1686469387',
#         'Referer':'https://movie.douban.com/typerank?type_name=动作&type=5&interval_id=100:90&action='
#
#     }
#
#     # data = {
#     #     'type': 5,
#     #     'start': 0,
#     #     'limit': 20
#     #
#     # }
#
#     proxy = {
#         "HTTP": "113.120.35.77:9999"
#     }
#
#     response = requests.get(url, headers=headers)
#     content = response.content.decode('utf8')
#     print(content)
    #  获取响应数据，text返回的是字符串形式的响应数据

    # page_text = response.text
    # print(page_text)
    # #  持久化存储
    # with open('./豆瓣电影爬虫.html', 'w', encoding='utf-8') as fp:
    #     fp.write(page_text)
    # with open('./豆瓣电影爬虫.txt', 'w', encoding='utf-8') as fp:
    #     fp.write(page_text)
    # print('爬取数据结束！！！')


import requests
from lxml import etree
#定义一个url
url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'
#定义一个头部
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "Referer":"https://movie.douban.com/review/best/?start=20",
    "Cookie":"ll=118281; bid=h5hVz7E908E; _pk_ref.100001.4cf6=["","",1655549995,https://www.baidu.com/link?url=6JA9-A-UT3kmslX1Ba5uTP2ZYOLHmmA9PsrC5wL1jnnlh0NxqHIX_duGygp6L8-s&wd=&eqid=9ba511430012e32d0000000662adb02b]; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1783311154.1655549995.1655549995.1655549995.1; __utmb=30149280.0.10.1655549995; __utmc=30149280; __utmz=30149280.1655549995.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1788219700.1655549995.1655549995.1655549995.1; __utmb=223695111.0.10.1655549995; __utmc=223695111; __utmz=223695111.1655549995.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _vwo_uuid_v2=D1CD456F0E8FE8A66FBF130658580BCE6|629c6a8d6b9ce186d81787184b86d404; __gads=ID=2ef2f716a3d59195-22875af88bd4003e:T=1655550007:RT=1655550007:S=ALNI_MZPD3xEG2yNN99WaOfilT8OdmAtYg; __gpi=UID=000006c02ac13c6e:T=1655550007:RT=1655550007:S=ALNI_MYEIqaIj00OYre8AgD_7aPFcsURhA; __yadk_uid=LscrIQgH4pHqE8iyUxrlIAsdt5WChbAx; _pk_id.100001.4cf6=212115cbe8a26728.1655549995.1.1655550276.1655549995."
}
#定义一个ip
proxy={
    "HTTP":"113.120.35.77:9999"
}


