 import socket

from babandar import process

c=socket.socket()

c.connect(('192.168.6.176',6800))
pro=process()
Message=pro.isomaking()
print(Message)
#Message=input('enter your message here:')
c.send(bytes(Message,'utf-8'))

#02830200F23E448128E490000000000006000030191234567890123456458400000000000001200012111045389488711062501210000000060119010008155481180089457845415515548118                                                       000524                23001001001000047670000012300100111100007786000001000000


print(c.recv(1024).decode())
print(c.recv(1024).decode())
