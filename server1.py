import socket

#服务器的IP地址和端口号
server_ip="172.16.71.39"
server_port=91

#创建TCP socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    client_socket.connect((server_ip,server_port))
    number=input()

    client_socket.send(number.encode())
    response=client_socket.recv(1024).decode()

    print("Answer:",response)
finally:
    client_socket.close()