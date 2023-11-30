import socket
from threading import Thread
from multi import Sender,Receiver

s = socket.socket()
s.bind(('localhost', 9999))
s.listen(0)

print("I'm reader!")
c,addr=s.accept()
print("client from:"+str(addr))

t1=Sender(c)
t1.start()
t2.Receiver(c)
t2.start()