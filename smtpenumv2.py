#!/usr/bin/python import socket

import socket
import sys
import re

file = open('users.txt')
# To read lines in python script you should use the readliness.
for linha in file.readlines():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((sys.argv[1],587))
	s.send("VRFY "+linha)
	result = s.recv(1024)
	if re.search('252',result):
		print "Usuario encontrado: "+result.strip('252 2.0.0')
	else:
		print "Resultado sem identificar usuarios\r\n" +result 
