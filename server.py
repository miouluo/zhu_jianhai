import socket
serversocket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('0.0.0.0', 9999))
serversocket.listen(0)
print("服务器已启动")
clientsocket,addr = serversocket.accept()
print("l收到请求:%s" % str (addr))
msg ='Hello,你好 \r\n '
clientsocket.send(msg.encode ( 'gb2312'))
clientsocket.close()