
import requests
import json
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.cnblogs.com/AggSite/AggSitePostList"

headers={

    # (":authority": "www.cnblogs.com",
    # ":method": "POST",
    # ":path": "/AggSite/AggSitePostList",
    # ":scheme": "https",)
    # "Accept": "text/plain, */*; q=0.01",
    # "Accept-Encoding": "gzip, deflate, br",
    # "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    # "Content-Length": "141",
    "Content-Type": "application/json; charset=UTF-8",
    # "Cookie": '_ga=GA1.1.512943656.1690267876; _pbjs_userid_consent_data=3524755945110770; cto_bundle=f7ue1l9rQ0NBNzRxV2poZVpRSWNGTWlTQnZra0FUbkFuZEs2Y0dDZlZDak5ZUW54cUdMak1jcUk4TzElMkZRN2NxYmo1N3NtVDZRT2xWc1A5NXo3bHBQUCUyRlBHS2w0dGdqTXc4T1R2b3V5Y1N3TWlkSkllM0JpRFN6TjcyT1hsVW5JRmo5cWlEJTJGbkdBWURwTzAzd2NGTll4bHhoZFElM0QlM0Q; __gads=ID=9b4d0a7bffb507e3":"T=1690267889":"RT=1695126899":"S=ALNI_Mb_YinIcg3mz4h4szkBfU5h43hGKw; __gpi=UID=00000c23ea92204b":"T=1690267889":"RT=1695126899":"S=ALNI_Mar-loCECqWmYsna8de1o0oSnfLVA; .AspNetCore.Antiforgery.b8-pDmTq1XM=CfDJ8Eg9kra6YURKsOjJwROiT4tZ4kdHVhQgAawKLZXP0la2G5B4TqfMLWmMQ3Q1b2Qewn2Lg62svMbP0Ms7Gzgy-V5eH29KftA3Mhf9hCc8kLSR4L7gxNLplJcIriiWO_Ucfl4L0E68n1X8nfdswEOj80w; _ga_M95P3TTWJZ=GS1.1.1695126900.7.1.1695127181.0.0.0',
    # "Origin": "https://www.cnblogs.com",
    # "Referer": "https://www.cnblogs.com/",
    # "Sec-Ch-Ua": '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    # "Sec-Ch-Ua-Mobile": "?0",
    # "Sec-Ch-Ua-Platform": '"Windows"',
    # "Sec-Fetch-Dest": "empty",
    # "Sec-Fetch-Mode": "cors",
    # "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31"
    # "X-Requested-With": "XMLHttpRequest"
}
#负载页
def craw_page(page_index):
    datas = {
        "CategoryType": "SiteHome",
        "ParentCategoryId": 0,
        "CategoryId": 808,
        "PageIndex": page_index,
        "TotalPostCount": 4000,
        "ItemListActionName": "AggSitePostList"
    }
    resp = requests.post(url, json.dumps(datas), headers=headers)
    return resp.text


def parse_data(html):
    soup = BeautifulSoup(html, "html.parser")
    articles = soup.find_all('article', class_='post-item')
    datas = []
    for article in articles:
        title = article.find('a', class_="post-item-title").get_text()
        href = article.find('a', class_="post-item-title")['href']
        author = article.find('a', class_="post-item-author").get_text()
        icon_digg = 0
        icon_comment = 0
        icon_views = 0
        for a in article.find_all('a'):
            if 'icon_digg' in str(a):
                icon_digg = a.find("span").get_text()
            if 'icon_comment' in str(a):
                icon_comment = a.find("span").get_text()
            if 'icon_views' in str(a):
                icon_views = a.find("span").get_text()
        datas.append([title, href, author, icon_digg, icon_comment, icon_views])
    return datas

all_datas=[]
for page in range(200):
    print('正在爬取%s页'%page)
    html = craw_page(page)
    datas = parse_data(html)
    all_datas.extend(datas)
df=pd.DataFrame(all_datas,columns=['title', 'href', 'author', 'icon_digg', 'icon_comment', 'icon_views'])
df.to_excel('博客园评价200页.xlsx',index=False)