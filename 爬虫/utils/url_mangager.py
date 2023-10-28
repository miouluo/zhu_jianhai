

class UrlManger( ):
    '''
    url管理器
    '''
    def __init__(self):
        self.new_urls=set()#没用过的,待爬取的url
        self.old_urls = set()#用过的，已经爬取过的url

    def add_new_url(self,url):
        if url is None or len(url)==0:# 长度为0或者没有东西的时候就不让他添加了
            return
        if url in self.new_urls or url in self.old_urls:# 判断是否获取了如果获取过了就不获取了
            return
        self.new_urls.add(url)#不在容器里然后获取
    def add_new_urls(self,urls):
        if urls is None or len(urls)==0:#看里面有没有带爬取的url
            return

        for url in urls:# 遍历循环获取url
            self.add_new_url(url)


    def get_url(self):#取出url
        if self.has_new_url():
            url=self.new_urls.pop()
            self.old_urls.add(url)
            return url
        else:
            return None
    def has_new_url(self):
        return len(self.new_urls)>0

