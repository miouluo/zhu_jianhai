import socket
s=socket.socket()
s.bind(("0.0.0.0",6000))
s.listen()
c,addr=s.accept()

while True:
    msg =input("please input:\r\n")
    c.send(msg.decode('utf8'))
    if msg=="bye":break

c.close()
s.close()