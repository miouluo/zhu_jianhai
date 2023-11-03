import socket
clientsocket= socket.socket (socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect ( ( '172.16.71.39', 91) )
msg = clientsocket.recv (50)
number=input("请输入一个小数:")
clientsocket.send(number.encode())
response=clientsocket.recv(1024).decode()
print("Answer:",response)

clientsocket.close ()
