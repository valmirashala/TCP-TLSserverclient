import socket as soct
import ssl
from cryptography.fernet import Fernet
import base64
import sys
import hashlib

def sendMessage(message,socket):
	socket.send(message)  


def connectToServer(IP, Port):                   
	try:
		#print("a")
		clientSocket = soct.socket()
		clientSocket.connect((IP,Port)) 
		
	except ConnectionRefusedError:
		print("Lidhja deshtoi!")
		clientSocket = None
	return clientSocket

message=""
serverIP = '127.0.0.1'
serverPort = 8000
socket = connectToServer(serverIP, serverPort)
while True and message.lower()!="end":
	
	if not socket:
		sys.exit()