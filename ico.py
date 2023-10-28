import mmh3
import requests
response = requests.get('https://mmbiz.qpic.cn/sz_mmbiz_png/1tu2S7MNvia2ibA7kszBaWoaggzcJ2k4GW57IMtgV7LgXDWEHJjdLbUjTtibr7StBKWdwFDRxnnGvBQ5aFFZYB7Ag/640?wx_fmt=png')
favicon = response.content
hash = mmh3.hash(favicon)
print(hash)
