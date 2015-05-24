__author__ = 'Alexander'
from socket import *

serverHost = 'localhost'
serverPort = 50007

massage = raw_input("Enter line: ")

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

sockobj.send(massage)
data = sockobj.recv(1024)
print 'Client received ', data
sockobj.close()
