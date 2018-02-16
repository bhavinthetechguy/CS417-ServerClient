import socket
from time import *
import math
import sys

arr = sys.argv

if len(arr) <6:

    print "Not Enough parameters"
    exit(0)

#given in the parameter: IP and PORT
trans_type = arr[1].upper()
send_type = arr[2].lower()

port = int(arr[3])
IP = socket.gethostbyname(arr[4])
address = (IP,port)

#setting the right transport socket TCP or UDP
if trans_type == "TCP":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(address)
    server_socket.listen(1)
    client_socket, client_info = server_socket.accept()
    print "TCP CONNECTION CLIENT"

else:
    print "UDP CONNECTION CLIENT"
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(address)








#print "One Client Connected\nClient IP: " ,client_info[0]+"\nClient Port: ",client_info[1],"\n"
fragment = int(arr[5])
if fragment < 5:
    fragment +=5
num =0


if trans_type =="TCP":
    data = client_socket.recv(4)
    client_socket.send("ACK")
    print "send FILE ACK"

else:
     data, clientAddress = server_socket.recvfrom(fragment)
     server_socket.sendto("ACK",clientAddress)
     print "send FILE ACK"

bytes_read = 4
while True:
    if trans_type =="TCP":
        data = client_socket.recv(fragment)

        if send_type == "stop-and-wait":
            client_socket.send("ACK")

    else:
        
        data, clientAddress = server_socket.recvfrom(fragment)
        if send_type=="stop-and-wait":
            server_socket.sendto("ACK",clientAddress)
        

    print "recieved: ",len(data)
    num = num+1
    bytes_read += len(data)

    if data == "close":
         break;
        


    

server_socket.close()
print "Acknowledgement Protocol Used: ",trans_type
print "messages read: ",num
print "bytes read: ",(bytes_read)
