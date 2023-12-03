import requests

d = {'msg': '我是水军'}
resp = requests.post('http://localhost:8080/', data=d)
print( resp.text )