import requests

url="http://tipdm.com/"  #爬取的目标网址
rq=requests.get(url)    #生成http请求


with open("tmp/web_data.txt",'w',encoding="utf-8") as f:  #以写的形式打开一个文件
    f.write(rq.text)  #将rq的结果写入文件中
print("响应状态码",rq.status_code)
print("编码",rq.encoding)
print("实体",rq.text)
print("请求头",rq.headers)