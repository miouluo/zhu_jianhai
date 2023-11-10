# 通信服务器
from socket import *
serverSock = socket(AF_INET,SOCK_STREAM)   # IPv4来通信，类型是TCP
serverSock.bind(('LAPTOP-KIN6VNBT',8088))   #主机地址一个，元组
serverSock.listen(1024)  # 监听
print('服务器准备接受信息：')

connectSock,address = serverSock.accept()  #创建连接对象
message = connectSock.recv(1024).decode()   # 接受
print('从客户端接受信息：')
modifmess = message.upper().encode()   # 接受信息后进行处理
connectSock.send(modifmess)