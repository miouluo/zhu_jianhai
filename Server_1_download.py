# 下载文件的服务器端
import socket
import os,sys
# 创建tcp服务器端socket
tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定端口
tcp_server_socket.bind(('',8080))
# 设置监听，把服务器端socket由主动套接字改成被动套接字，只能接收客户端的请求
tcp_server_socket.listen(128)
while True:
    # 接收客户端信息
    client_socket,client_ip = tcp_server_socket.accept()
    print('客户端：',client_ip,'连接')
    # 接收下载信息
    file_name_data = client_socket.recv(1024)
    # 解析下载信息
    file_name = file_name_data.decode()
    # 判断文件是否存在
    try:
        with open(file_name,'rb') as file:
            while True:
                # 读取文件数据
                file_data =file.read(1024)
                # 数据长度不为0表示还有数据没有写入
                if file_data:
                    client_socket.send(file_data)
                    # 数据为0表示传输完成
                else:
                    print(file_name,'传输完成')
                    break
    except Exception as e:
        print("传输异常：",e)
    # 关闭客户端连接
    client_socket.close()

