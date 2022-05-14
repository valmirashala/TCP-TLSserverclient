import OpenSSL
import socket as soct
import sys 
import ssl
from pprint import pprint
import hashlib
import base64
from cryptography.fernet import Fernet

openssl = OpenSSL.crypto
certiFile=open("C:\\Users\\User\\certificate.crt").read()
keyFile=open("C:\\Users\\User\\private.key").read()


x509 = openssl.load_certificate(openssl.FILETYPE_PEM, certiFile)
print(x509.get_subject())


key=openssl.load_privatekey(openssl.FILETYPE_PEM, keyFile)


# server connection
try: 
	serverSocket = soct.socket() 
	print("Socket successfully created")
except soct.error as err: 
	print("Socket creation failed with error",err) 

serverPort = 8000
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(5)      
print("Socket is listening")
client, addr = serverSocket.accept() 