import pandas as pd
import requests
from lxml import etree
import json
if __name__ == "__main__":
    #  指定url
    url = 'https://www.renrenche.com/cn/ershouche/?'
    #  UA伪装：将对应的请求User-Agent封装到字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.3162 SLBChan/105',
        'Cookie':'rrc_modified_city=true; rrc_promo_two_years=rrc_promo_two_years; _ga=GA1.2.1192557248.1685783021; rls_uuid=8520A271-B815-4514-9E40-4230F3CA5C72; Hm_lvt_8adc6db2eb7f152a6f951aa53bc890f9=1685783021,1685795499,1685800065; rrc_modified_city=true; rrc_ip_province=广东; rrc_login_phone=19120018547; rrc_login_token=8568cd11d26b70630474ea310c68c9ef; rrc_userid=2744088431; Hm_lvt_8d28aa8f3d4a777433a55c884bdca17e=1685851860,1685889408,1685954000,1686054655; new_visitor_uuid=9d48a9f15007fbb757ef2704d5aca2f2; rrc_record_city=cn; zhimai-page-list-banner=true; acw_tc=3ccdc14f16864673850141944e101fb86d1acd878911f4b6bc8de7b3524086; rrc_rrc_session=rvgusub138pb6m4iu4shv7hv56; rrc_rrc_signed=s,rvgusub138pb6m4iu4shv7hv56,fc459890bc719a1d3b023f52299c5630; rrc_fr=bd_pz; rrc_tg=fr=bd_pz&tg_aid=10113665; rrc_ss=initiative; rrc_session_city=cn; Hm_lvt_c8b7b107a7384eb2ad1c1e2cf8c62dbe=1686054655,1686381767,1686392489,1686467391; acw_sc__v2=6485733f161e1bb18a02e048173c6c941bbffeb1; SERVERID=16b08e25ce34c915f4c1511ea20e3105|1686467428|1686467394; acw_sc__v3=648573c6cb07b82088f1b5b09971266a6163e561; _pzfxuvpc=1685783021236|1392355257146443240|63|1686467559372|12|9315760247594864975|1709812907538097126; _pzfxsvpc=1709812907538097126|1686467390932|5|https://www.baidu.com/other.php?sc.0f00000gBrgDLroP9YqY-iTiWBJs7-G9fEIfGvSXGjV5Dmaq1JkjuY-4ljyagJeUX8vTOqYNLJFTC8r3QQiVQDdvgygy2HC1xhBeTQQMMrPc7etyyqCj1g1Uq0xxVuGDp2hPF4YRi4Ji9PFdHfpHaiEZtECCrvubb4vx31yQbr4cgoKadC7B1fM9K8dmIpc5Uc3ZGg-1btVpxmyfT0yG40RRc5Tq.7D_NR2Ar5Od663rj6tGbkHFB9JiBjEohmE84TxjdCp8NMDkguggklXMTGyAp7BEubtU0.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqznEczerd0ZN1ugFxIZ-suHYs0A7bgLw4TARqnsKLULFb5TWQzn81VfKzmLmqn0KdThkxpyfqnHRYn1cdPWbsr0KVINqGujYkPHDkPjckr0KVgv-b5HDznj03nWnk0AdYTAkxpyfqnHnzn1f0TZuxpyfqn0KGuAnqiD4a0ZKGujYY0APGujY3P0KWThnqn1c4Pjb&dt=1686467381&wd=%E4%BA%BA%E4%BA%BA%E8%BD%A6&tpl=tpl_13234_31406_0&l=1543256908&ai=0_0_1_0&us=linkVersion%3D1%26compPath%3D10036.0-10032.0%26label%3D%25E4%25B8%25BB%25E6%25A0%2587%25E9%25A2%2598%26linkType%3D%26linkText%3D%25E4%25BA%25BA%25E4%25BA%25BA%25E8%25BD%25A6%25E4%25BA%258C%25E6%2589%258B%25E8%25BD%25A6%25EF%25BC%258C%25E5%258D%2596%25E8%25BD%25A6%25E4%25BE%25BF%25E6%258D%25B7%25E7%259C%2581%25E5%25BF%2583%25EF%25BC%258C%25E4%25B9%25B0%25E8%25BD%25A6%25E6%2594%25BE%25E5%25BF%2583%25E9%259D%25A0%25E8%25B0%25B1; Hm_lpvt_c8b7b107a7384eb2ad1c1e2cf8c62dbe=1686467559; ssxmod_itna=QqjxBDgD0Dy7i=D8zDX+G7Ayqob7NhHNYWPq8Dl=bxA5D8D6DQeGTW2rK3WDRAnMh4qQboecPK=bhGG+a3dULBTzrADB3DEx06xZniG4GGfxBYDQxAYDGDDPDo2PD1D3qDkD7h6CMy1qGWDm4sDYvFDQHGe4DFc2IOP4i7DDyd8x07YRKDeEahchgCq0gPH0KD9hYDsZ0f30KpjSf4M2oEIKuDHDGd30MP3nMHNChGE7KDXpQDv1ywRhoXXc5z4STeEnualnwxFAZY3BWe=E2PKQ0qVme3ZnqqsAn9amx7OADDiPjZ8YD===; ssxmod_itna2=QqjxBDgD0Dy7i=D8zDX+G7Ayqob7NhHNYWPqD6hKhCOD0ybe03H7uNeqoXqu3uYnMyQDRlfY2YXUAmor7DxnbutXmIeBrjeybqBwLeYtBSqvbOiQCScHaLZfxybrGztiKH6qlRcdDx9z1ZHTD6eax+Thm2YauGBPoZ7mT9ekDtqHafObr9nwpaHvi/ym/GA1k/yWnGBCLtfW/0Kj/jarwoc7kY5E+IEWnB5aGbqIThfwvZEIUzarF9yFfbMs0fIAfSonnjk=0YjI=6cOh4=1s=wAfuISYIaEu9BlDoeHDo8ljPNUcYsb8bmiwh4RsYnwtnxa74vx4F7=tbsQ4eXHxqHxrmND4Krwpmvy8+/nmRIHjlhBG5EB5EnAum5ABKH+cmbb5gRFio=nuQT40K5DxSDv5M8oSAoi15oqSgQEceylfcdTxDKT4QDqZANNixyS4H347cNqAowALKgLBDxD7=DYI4eD'
     }

    data = {

        'plog_id': '87b54a4858a44e72f5d59ae7e061f510'

    }
    response = requests.get(url=url,params=data, headers=headers)
    content = response.text
    print(content)
    #  发起请求
    #  get方法会返回一个响应对象
    #  数据解析
    # tree = etree.HTML(content)
    # #  存储div标签对象
    # div_list = tree.xpath('/html/body/div[1]/div[3]/div/div[1]/div[2]/div[3]')
    # fp = open('二手车.txt', 'w', encoding='utf-8')
    #
    # for div in div_list:
    #     brand = div.xpath('/html/body/div[1]/div[4]/div/div[1]/div[2]/div[3]/div[1]/a/div/h3/text()')[0]
    #     print(brand)
    #     fp.write(brand + '\n')
    #
    # print(content)
    #     #  持久化存储
    #
    # with open('./二手车爬虫.html', 'w', encoding='utf-8') as fp:
    #     fp.write(contnent)
'''    response = requests.post(url=url, headers=headers)

    list_data = response.json()
    fp = open('二手车爬虫.json', 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)
    print('爬取数据结束！！！')
    data_str = open('二手车爬虫.json').read()
    data_list = json.loads(data_str)
    ## d['title']中的'title'是自己json格式文件里面的names
    data = [[d['brand'], d['price'], d['tag']] for d in data_list]
    df_2 = pd.DataFrame(data, columns=['brand', 'price', 'tag'])
    df_2.head()
'''
#    from pandas.io.json import json_normalize
#    data = open("二手车爬虫.json", encoding="utf-8").read()
#    data_list = json.loads(data)
#    df = json_normalize(data_list)
#    print(df)

#    df = pd.read_json("二手车爬虫.json", encoding='utf-8', orient='records')
#    print(df)

    #  获取响应数据，text返回的是字符串形式的响应数据





