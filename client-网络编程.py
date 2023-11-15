# 客户端
import socket
def main():
    client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect(('172.16.105.90',6789))
    while True:   #可以循环发送数据
        data=input('--------待处理数据--------')
        client_socket.send(data.encode('gb2312'))
        recv_info=client_socket.recv(1024).decode('gb2312')
        print('--------处理结果--------\n%s' %recv_info)
    server_socked.close()

if __name__ =='__main__':
    main()