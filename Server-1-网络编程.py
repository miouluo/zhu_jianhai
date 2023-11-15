#功能：单进程非阻塞并发服务器
import socket
def main():
    server_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #创建SOCKET
    server_sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)   #重复使用绑定信息
    local_addr=('',6789)
    server_sock.bind(local_addr)   #绑定IP及端口
    server_sock.listen(3)
    server_sock.setblocking(False)   #服务器套接字server——socket设置为非阻塞
    cleint_address_list=[]
    while True:
        try:
            new_socket,cleint_address=server_sock.accept()   #等待新用户来
        except:
            pass
        else:
            print('一个新客户端到来了 %s'%str(cleint_address))
            new_socket.setblocking(False)   #将新用户设置成阻塞
            cleint_address_list.append((new_socket,cleint_address))   #本次建立连接后添加到已连接客户列表中去
        for cleint_sock,cleint_address in cleint_address_list:
            try:
                recv_info=cleint_sock.recv(1024).decode('gb2312')
            except:
                pass
            else:
                if len(recv_info)>0:
                    # 数据处理
                    print('待处理数据：%s'%recv_info)
                    data=recv_info.upper()
                    cleint_sock.send(data.encode('gb2312'))
                    print('处理结果: %s'%data)
                else:
                    cleint_sock.close()
                    cleint_address_list.remove(cleint_sock,cleint_address)
                    print('%s 已断开连接'%str(cleint_address))
    server_socket.close()

if __name__=='__main__':
    main()