
import requests
import json
url='https://maimai.cn/sdk/web/content/get_list'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31',
    'Sec-Fetch-Site': 'same-origin',
    'Cookie': 'seid=s1695041686511; guid=Gx4EGBkEGB8ZBBMeVhMcGR8cEh9WGxkEHx4aGAQaBB0bGwVNTm8KHBkEHRkfBUNYS0xLeQoaBBoEGgQdGxsFT0dFWEJpCgNFQUlPbQpPQUNGCgZmZ35iYQIKHBkEHRkfBV5DYUhPfU9GWlprCgMeHFIKER4cREN9ChEaBBobCn5kClldRU5EQ30CChoEHwVLRkZDUEVn; AGL_USER_ID=fc6d5dad-1c53-4161-a737-91c18cabf710; _buuid=4b247f8f-9fe1-40f2-ba40-f1dfddf988a1; browser_fingerprint=856409F6; maimai_pc_login_show_tooltip=1; gdxidpyhxdE=3bS0Y0WbLNyGN9QpTbdUZfBJ9%2BVpyfJpqgudgsRpURs8WkZu9oZsalm9ijWoSs4YDMQiSocoqYQWT3ZsNB8T9OQ%5CA91BVM%5Cozq1rw3HEo%2BSpjoVPkWcfrKOiy4mDT7ceb2h0LaZQIMpDvyL1myIcIIzd6CofQuw26170qv%5C4ysCSBM7r%3A1695042630053; YD00198168557789%3AWM_NI=iewY9IJk1PxkGOJ17hNj8qWjj59NjRcKgH3ujLiF3Wx%2BaiEYLyrRr5H%2FGX2th1v8w94qm0oVqN4bjyMCkm%2FjL8Gyc%2Fm4ukzGWTUWy8RCUG%2BBT35RTFmGoZpDMfVTqsCrTEk%3D; YD00198168557789%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eeb1d87ca590c09af14fa8b08eb7c14e839a9e82d167a8a78aaff85fa3889cd9cd2af0fea7c3b92aabbbb9babc438ab5ffb1fb61859186d2b6648eb6f892d662aaebf7afe95aa195a9a9b27faa94a7a7b25dbcf5af8ac85390a7beb3f13f8cf189b9b180acefbad9f633f8afa3d1ee5eb392fc83e9738f9da58eae6290e8899ae225afecbb8cf94d958c9bb8fc34929d9ba8aa4a98edfbb3d74eaf99a1bbf3508fba9ab5f47981ae9ca6ea37e2a3; YD00198168557789%3AWM_TID=wG2rBisJOhdBVBFBBQbV2djEd%2FUOWC4J; u=240075687; u.sig=r7rVUax5zMwnlReN5bK8vPV9OPI; access_token=1.57bbe5d4431aecb69121f4a5ad609e4a; access_token.sig=Mni1kczvzWC9XqCAHaK73YHLOx8; u=240075687; u.sig=r7rVUax5zMwnlReN5bK8vPV9OPI; access_token=1.57bbe5d4431aecb69121f4a5ad609e4a; access_token.sig=Mni1kczvzWC9XqCAHaK73YHLOx8; channel=www; channel.sig=tNJvAmArXf-qy3NgrB7afdGlanM; maimai_version=4.0.0; maimai_version.sig=kbniK4IntVXmJq6Vmvk3iHsSv-Y; session=eyJzZWNyZXQiOiJHbFk4NTFMd3d2eWxHdWlTNXd2aUJWb04iLCJ1IjoiMjQwMDc1Njg3IiwiX2V4cGlyZSI6MTY5NTEyODUwMTI1NCwiX21heEFnZSI6ODY0MDAwMDB9; session.sig=uSPRVcMTq2tnb8TNzW6BH6ATY5M; csrftoken=IPpULoEo-y3CXq6WhPGJ64845COBtoqE7CfE',
    'X-Csrf-Token': 'IPpULoEo-y3CXq6WhPGJ64845COBtoqE7CfE'

}


def craw_page(page_number):
    # ctrl_alt l
    params = {
        'api': 'gossip/v3/square',
        'u': '240075687',
        'page': 1,
        'before_id': 0

    }
    resp = requests.get(url, params=params, headers=headers)
    # print(resp.status_code)
    data = json.loads(resp.text)
    datas = []
    for text in data['list']:
        datas.append(text['text'])
    return datas



with open('脉脉爬取结果.txt','w',encoding='utf-8') as f:
        for page in range(0, 11):
            print('craw page', page)
            datas = craw_page(page)
            f.write("\n".join(datas) + '\n')

