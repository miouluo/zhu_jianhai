import socket
from threading import Thread
from multi import Sender,Receiver
c = socket.socket()

c.connect(('localhost', 9999))

t1=Sender(c)
t1.start()
t2.Receiver(c)
t2.start()

#c.close()