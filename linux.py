import socket 
import os 
import threading
import pyfiglet


senderIP = input("Enter Your IP address: ")
senderPort = 1238

reciverIP = input("Enter Reciver IP address: ")
reciverPort = 9879

socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

socket.bind((senderIP,senderPort))
print(pyfiglet.figlet_format("UDP Chat Application", font = "digital" ))

def sendMsg():
        while True:		
                message = input()
                print("\n")
                if( message == 'bye' or message == 'exit'):    
                       message = 'Receiver is on Offline Mode.....!!!!'    
                       socket.sendto(message.encode(),(reciverIP,reciverPort))
                       os._exit(1)
                else:
                     socket.sendto(message.encode(),(reciverIP,reciverPort))
                    
def recvMsg():
        while True:
                message = socket.recvfrom(100)
                print("\n\t\t\t\t" + "Receiver -> " + ":" + message[0].decode())
               

sendMsg = threading.Thread(target=sendMsg)
recvMsg = threading.Thread(target=recvMsg)

 
sendMsg.start()
recvMsg.start()
