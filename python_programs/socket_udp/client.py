from socket import *  
  
HOST = '192.168.30.205'
PORT=9999  
  
s = socket(AF_INET,SOCK_DGRAM)  
s.connect((HOST,PORT))  
while True:  
    message = raw_input('send message:>>')  
    s.sendall(message)  
    data = s.recv(1024)  
    print data  
s.close()



