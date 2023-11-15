# 下载文件的客户端
import socket,os
# 创建套接字
tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 连接IP地址和端口
tcp_client_socket.connect(('127.0.0.1',8080))
down_path = input('请输入文件路径：\n')
file_name = input('请输入文件名：\n')
all_path = os.path.join(down_path,file_name)
# 文件名编码
tcp_client_socket.send(all_path.encode())
# 判断文件是否存在
all_path = os.path.join(down_path,file_name)
try:
    all_files = os.listdir(down_path)
    if file_name in all_files:
        try:
            # 文件传输
            with open(os.getcwd()+'\\'+file_name,'wb')as file:
                while True:
                        #接收数据
                        file_data = tcp_client_socket.recv(1024)
                        # 数据长度不为0表示还有数据没有写入
                        if file_data:
                            file.write(file_data)
                            # 数据为0表示下载完成
                        else:
                            break
        # 下载出现异常时捕获异常
        except Exception as e:
            print("下载异常：", e)
        # 无异常则下载成功
        else:
            print(file_data,'下载成功')
        # 关闭客户端
        tcp_client_socket.close()
    else:
        print('指定文件不存在')
except FileExistsError as e:
    print('指定路径不存在')


