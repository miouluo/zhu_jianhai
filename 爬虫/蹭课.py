import  requests

headers={'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'
         ,'Sec - Fetch - Site': 'same - origin'
         }

def get_htmltext(url):
    try:
        r=requests.get(url,headers,timeout=30)
        r.raise_for_status()#状态
        r.encoding=r.apparent_encoding#自动判断编码
        return r.text#响应内容字符串形式
    except:
        return '异常'

def saveHTMLToFile(html, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
        print("文件保存成功")
    except Exception as e:
        print("文件保存失败:", e)


if __name__=="__main__":
    url = "http://www.taobao.com"
    html = get_htmltext(url)
    saveHTMLToFile(html, "taobao.html")