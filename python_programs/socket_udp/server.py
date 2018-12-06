from socket import *  
  
HOST = '192.168.30.205'
PORT = 9999  
  
s = socket(AF_INET,SOCK_DGRAM)  
s.bind((HOST,PORT))  
print '...waiting for message..'  
while True:  
    data,address = s.recvfrom(1024)  
    print data,address  
    s.sendto('this is from the UDP server: %s' % (data),address)  
s.close()

