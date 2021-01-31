import socket
from time import sleep

#from babandar import process

class kita:
    def dogra(self,ip,port,die):
        c = socket.socket()
        port=int(port)

        c.connect((ip, port))
        # pro=process()
        # Message=pro.isomaking()
        # print(Message)
        # Message=input('enter your message here:')
        Message=die
        print(Message)

        c.send(bytes(Message, 'utf-8'))
        print(c.recv(2024).decode())

        #sleep(1)




        # func=pro.isomaking()

        # 02830200F23E448128E490000000000006000030191234567890123456458400000000000001200012111045389488711062501210000000060119010008155481180089457845415515548118                                                       000524                23001001001000047670000012300100111100007786000001000000





