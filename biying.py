import requests
import json
from lxml import etree

if __name__ == "__main__":
    # 指定url
    url = 'https://www.renrenche.com/buy'

    # UA伪装：将对应的请求User-Agent封装到字典中
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.3162 SLBChan/105'
    }

    # 使用requests库来获取网页源代码
    response = requests.get(url, headers=headers)
    content = response.text

    # 将网页源代码转换为json格式
    content_json = json.loads(content)

    # 数据下载到本地
    fp = open('二手车.json', 'w')
    fp.write(content_json)
    fp.close()

    # 使用lxml库来解析网页源代码
    tree = etree.HTML(content)

    # 获取想要的数据
    all_list = tree.xpath('//div[@class="row-fluid list-row js-car-list"]')
    print(all_list)
    for car_list in all_list:
        dan_car = car_list.xpath('.//div[@class="span6 list-item car-item"]')
        print(dan_car)
        for i in dan_car:
            brand = i.xpath('.//h3[@class="title"]/text()')
            print(brand)
            price = i.xpath('.//div[@class="price"]/text()')
            print(price)
