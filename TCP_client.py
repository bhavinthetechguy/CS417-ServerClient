'''import socket


serverName = ''
serverPort = 12000
#addresses of the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('', serverPort))
#making socket and handshaking with the server

sentence = input("Input lowercase sentence:")
s.send(sentence)
#taking input and sending it to the server socket

modifiedSentence = clientSocket.recv(1024)
print ('From Server:', modifiedSentence)
#recieving message and printing it

clientSocket.close()

'''
import socket
from time import *
import math
import sys


arr = sys.argv

if len(arr) <6 :
    print "Not enought parameters"
    exit(0)

#given in the parameter: IP and PORT
trans_type = arr[1].upper()
send_type = arr[2].lower()

port = int(arr[3])
IP = socket.gethostbyname(arr[4])
address = (IP,port)

#setting the right transport socket TCP or UDP
if trans_type == "TCP":
    client_socket = socket.socket()
    client_socket.connect(address)
    print "TCP CONNECTION CLIENT"

else:
    print "UDP CONNECTION CLIENT"
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    

#given in the parameters
fragment = int(arr[5])
string = ""
string = string.center(fragment,"*")

#2 to the power of 30
total_size = 2 ** 30


if trans_type =="TCP":
    sent = client_socket.send(bytes(total_size))
    reply = client_socket.recv(fragment)
    print "Recieved ACK"

else:
    sent = client_socket.sendto(bytes(total_size),address)
    sender_socket, aa = client_socket.recvfrom(fragment)
    print "Recieved ACK"

bytes_sent = 4
num= 0

start_time = time()

if send_type == "stop-and-wait":
    print "STOP AND WAIT"
    while total_size>0:

        
        #TCP is reliable data transport protocol, thus we use send instead of sento
        if trans_type =="TCP":
            
            sent = client_socket.send(string)
            reply = client_socket.recv(5)
            

        else:
            
            sent = client_socket.sendto(string,address)
            sender_socket, aa = client_socket.recvfrom(fragment)

        
        print "bytes sent: ",sent

        if (sent !=fragment):
            print "Could Not send the right amount of packet"
            exit(0)
        
        total_size -=sent
        bytes_sent += sent
        num = num+1

        if (total_size < fragment):
            string = ""
            string = string.center(total_size, "*")
            fragment = len(string)        

else:
    print "PURE STREAMING"
    while total_size >0:

         #TCP is reliable data transport protocol, thus we use send instead of sento
        if trans_type =="TCP":
            
            sent = client_socket.send(string)

        else:
            sent = client_socket.sendto(string,address)

        print "bytes sent: ",sent

        if (sent!=fragment):
            print "Could Not send the right amount of packet"
            exit(0)
        total_size -=sent
        bytes_sent += sent
        num = num+1

        if (total_size < fragment):
            string = ""
            string = string.center(total_size, "*")
            fragment = len(string)
        

      

if trans_type =="TCP":
    
    client_socket.send("close")
else:
    client_socket.sendto("close",address)


client_socket.close()

print "Number of messages sent: ",(num+1)
print "Number of bytes sent: ", (bytes_sent + 5)
print "Total Transmit time: ",time()-start_time

