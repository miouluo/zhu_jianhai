# 通信客户端
from socket import *
hostname='LAPTOP-KIN6VNBT'   # 主机或者IP地址
port = 8088
clientsock = socket(AF_INET,SOCK_STREAM)   # 创建套字节socket
clientsock.connect((hostname,port))   #连接主机和端口
message = input('Enter something Please:')  #提示信息
clientsock.send(message.encode())   #发送
uppermess = clientsock.recv(1024).decode()   #接收
print('信息发送：'+uppermess)