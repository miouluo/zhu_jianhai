#client
import socket
from threading import Thread
from multi import Sender, Receiver

c = socket.socket()
c.connect(('localhost', 9999))

t1 = Sender(c)
t1.start()
t2 = Receiver(c)
t2.start()
#server
from threading import Thread


class Sender(Thread):
    def __init__(self, socket):
        super().__init__()
        self.socket = socket

    def run(self):
        while True:
            s = input()
            self.socket.send(s.encode('gb2312'))


class Receiver(Thread):
    def __init__(self, socket):
        super().__init__()
        self.socket = socket

    def run(self):
        while True:
            s = self.socket.recv(1024)
            print('[对方]', s.decode('gb2312'))