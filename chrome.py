import requests

hd = {'user-agent': 'chrome'}
resp = requests.get('https://www.seig.edu.cn/', headers=hd)
resp.encoding = 'utf-8'
print(resp.text)