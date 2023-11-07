import socket
import time
from threading import Thread

c = socket.socket()
c.connect(('localhost', 6000))
n = 0

while True:
    msg = input("please input:\r\n")
    c.send(msg.encode('utf8'))
    if msg == "bye": break

c.close()
