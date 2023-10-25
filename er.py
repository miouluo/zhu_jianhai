import requests
import json
import pandas as pd

if __name__ == "__main__":
    #  指定url
    url = 'https://www.renrenche.com/lurker/search/pc_select'
    #  UA伪装：将对应的请求User-Agent封装到字典中
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.3162 SLBChan/105'
    }
    #  指定POST请求的参数
    data = {
        'city': 'bj',  # 城市代码，北京为bj
        'brand': ' ',  # 品牌名称，可以为空
        'price': ' ',  # 价格区间，单位为万，可以为空
        'page': 1  # 页码，从1开始，可以为空
    }
    response = requests.post(url=url, headers=headers, data=data)
    response.raise_for_status()  # 检查响应状态码是否为200
    data = response.json()  # 获取JSON数据

    try:
        # 尝试执行的代码
        response = requests.post(url=url, headers=headers, data=data)
        response.raise_for_status()  # 检查响应状态码是否为200
        data = response.json()  # 获取JSON数据
    except Exception as e:
        # 发生异常时执行的代码
        print("出现异常：", e)
    else:
        # 未发生异常时执行的代码
        print("爬取数据成功！")

    finally:

        # 无论是否发生异常都执行的代码

        with open("，/issues.csv", "w", encoding="utf-8") as f:

            csv_file = "./issues.csv".DictWriter(f, fieldnames=["gravatar_id", "position", "number", "votes", "created_at",
                                                     "comments", "body", "title", "updated_at", "html_url", "user",
                                                     "labels", "state"], delimiter=",")

            csv_file.writeheader()  # 写入表头

            csv_file.writerows(data["issues"])  # 写入数据

            print("保存数据结束！")










'''        # 读取本地JSON格式数据，并转换为列表形式
        with open('二手车爬虫.json', encoding='utf-8') as f:
            data_list = json.load(f)

        # 提取所需数据，并保存为DataFrame格式
        with open("issues.csv", "w", encoding="utf-8") as f:
            data = [[d['brand'], d['price'], d['tag']] for d in data_list]
            df = pd.DataFrame(data, columns=['brand', 'price', 'tag'])
            df.to_csv('二手车爬虫.csv', index=False, encoding='utf-8')
            csv_file = csv.DictWriter(f, fieldnames=["gravatar_id", "position", "number", "votes", "created_at",
                                                     "comments", "body", "title", "updated_at", "html_url", "user",
                                                     "labels", "state"], delimiter=",")
            csv_file.writeheader()  # 写入表头
            csv_file.writerows(data["issues"])  # 写入数据
       # 保存为csv文件，不包含索引列，指定编码格式
        print(df)

    except Exception as e:
        print('出现异常：', e)
'''

