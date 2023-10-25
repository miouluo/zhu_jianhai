import urllib.request
import urllib.parse
import gzip
from io import BytesIO


# import requests
from bs4 import BeautifulSoup
from lxml import etree
# import json
if __name__ == "__main__":
    #  指定url
    url = 'https://www.renrenche.com/cn/ershouche/?plog_id=ef281edfe381a835e4a9f02045069aad'

    #  UA伪装：将对应的请求User-Agent封装到字典中
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.3162 SLBChan/105',
        'Cookie':
            'rrc_ip_province=%E5%B9%BF%E4%B8%9C; zhimai-page-list-banner=true; rrc_promo_two_years=rrc_promo_two_years; rls_uuid=AC4CEEE8-655F-4E98-9E98-26D033B7847B; _ga=GA1.2.1838419783.1685784978; rrc_ip_city_twohour=gz; rrc_ss=initiative; Hm_lvt_8d28aa8f3d4a777433a55c884bdca17e=1685784979,1686385460; rrc_rrc_session=vutct12fqs45s9d58dl6r6pl65; rrc_rrc_signed=s%2Cvutct12fqs45s9d58dl6r6pl65%2Cccd89559438bb026c6011d29952546b3; rrc_modified_city=true; rrc_record_city=cn; Hm_lvt_c8b7b107a7384eb2ad1c1e2cf8c62dbe=1685784979,1686385460,1686385705; rrc_session_city=cn; geo=%7B%22lat%22%3A%2223.4487150%22%2C%22lng%22%3A%22113.4866150%22%7D; acw_sc__v2=64843ae1158f9b986effdcf3d9561c99a0d06573; acw_tc=b65cfd3c16863874262622003e076e97529acfcf5a860cea8338d6da1003bf; new_visitor_uuid=6424f792f1e3698562a233d26b586ab5; rrc_fr=bing_seo; rrc_tg=fr%3Dbd_pz%26tg_aid%3D10113665; SERVERID=270971e3646d3ff60658e5f765b10009|1686387474|1686387430; _pzfxuvpc=1685784978387%7C3506690146135063279%7C8%7C1686387479282%7C3%7C1283145191387867926%7C5619861179107618938; Hm_lpvt_c8b7b107a7384eb2ad1c1e2cf8c62dbe=1686387479; ssxmod_itna=euDQD5iIkD8Sx0d7CDjg7xuCDynSDfxY5REU+3D/K4wDnqD=GFDK40EAgIwnm+ehinrpi=airCmp4jje3hfqiWcnHeDHxY=DUEorPdrDen=D5xGoDPxDeDADYoUDAqiOD7qDdjpkVUkDm4GWBqDgn4Gg4miD0ft9QLiD4qDB+rdDKqr9DGY63jtQvTqtoG=DjqrD/3eadG=3H6c49wTboiiaQqGy9PGuUMrg0eDHzLNleQ+e8iPIw0vq+YeFn7GqKEh4n0+K+GwinBd=S7e08OGXF3x=KE4AsXDDGRDoekDxD===; ssxmod_itna2=euDQD5iIkD8Sx0d7CDjg7xuCDynSDfxY5REU4G9bTKDBwYQx7pK62gx644KHGF8C79XxnjDWYr4unmC724=sbjujiDqoZy0KWgFdOAfhqfhYtvxyteMXkm1LEx22fciMy7XX5iljko7xrnEF4wZq=lp0Oota+krTGr/74kgy+HzPiHQwWKbv+C9aO1zKsq7czCf7E6+3IkKa=R8ahDESwqtIkF=YsV/B7M4nGFcr2u7a4oNeuV7jjqtA8FcFRV+6nH=uultqbx2ZuD3M75qnOvROTR9f8/hoMRHWypIuZ/gIsLHN=0ytXYPrgYrZE==0Emix+NjjiHli/PIHg+ZQPd+mG2QLjUGgPbhphnNwDPKoP4nhQDrNpq7mvxGqmxP5eKqiedPIOb5XQA+lNHQT+cT8SmGUEO85GUmUB+hU3mKKvKcpY3eOm07cuiDHiv+B5IccLSmK1c4B+H3XdoNVQLKm4DQIrKhP9DRjgDn4=biq0hCELKjklRkyBLRKhd9rtnRHdQei+KeQNYCsNC+2kxK7hvq+wQwMk4bDDFqD+aDxD==='
    }


    data = {

        'plog_id': 'ef281edfe381a835e4a9f02045069aad'

            }
    data = urllib.parse.urlencode(data)

#  请求对象的定制
    request = urllib.request.Request(url=url, headers=headers )

#  模拟浏览器访问数据
    response = urllib.request.urlopen(request)
    print(response)

#  获取网页源码
    h = response.read()
    buff = BytesIO(h)
    f = gzip.GzipFile(fileobj=buff)
    content = f.read().decode('utf-8')


    print(content)

#  数据下载到本地
    fp = open('二手车.json', 'w', encoding='utf-8')
    fp.write(content)
    with open('./二手车.html', 'w', encoding='utf-8') as fp:
        fp.write(content)


#  解析网页源码


    # x = BeautifulSoup(content, 'lxml')  # 使用 lxml 解析器作为底层解析引擎
    # print(x.prettify())  # 变成规整的 html 格式
    # # tree = etree.HTML(x.prettify())
    tree = etree.HTML(content)

    # / html / body / div[1] / div[3] / div / div[1] / div[2] / div[3]
#  获取想要的数据
    all_list = tree.xpath('/html/body/div[3]/div[3]/div/div/div[1]/ul')
    print(all_list)
    # for car_list in all_list:
    #     dan_car = car_list.xpath('/html/body/div[3]/div[3]/div/div/div[1]/ul/li[1]/a')
    #     print(dan_car)
    #     for i in dan_car:
    #         brand = dan_car.xpath('/html/body/div[1]/div[4]/div/div[1]/div[2]/div[3]/div[1]/a/div/h3/text()')
    #         print(brand)
    #         price = dan_car.xpath('/html/body/div[1]/div[4]/div/div[1]/div[2]/div[3]/div[1]/a/div/div[4]/div')
    #         print(price)

    # / html / body / div[1] / div[4] / div / div[1] / div[2] / div[3] / div[1] / a / div / div[4] / div
    # print(result)










    # page_text = requests.get(url=url, headers=headers)
    # # tree = etree.HTML(page_text)
    # print(page_text)
    # div_list = tree.xpath('/html/body/div[1]/div[4]/div/div[1]/div[2]/div[3]/text()')
    # # x = BeautifulSoup(page_text, 'lxml')  # 使用 lxml 解析器作为底层解析引擎
    # # print(x.prettify())  # 变成规整的 html 格式
    # # tree = etree.HTML(x.prettify())
    #
    # print(div_list)
    #
    #
    # # fp = open('二手车.txt', 'w', encoding='utf-8')
    # #
    # # for div in div_list:
    # #     brand = div.xpath('/html/body/div[1]/div[4]/div/div[1]/div[2]/div[3]/div[1]/a/div/h3/text()')[0]
    # #     print(brand)
    # #     fp.write(brand + '\n')
    # #     print(brand)
    #     # for div in brand:
    #
    #
    #
    # # print(page_text)
    # # with open('./爬虫.html', 'w', encoding='utf-8') as fp:
    # #     fp.write(page_text)
