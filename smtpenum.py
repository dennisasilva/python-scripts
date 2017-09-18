#!/usr/bin/python import socket

import socket
import sys

if len(sys.argv) != 3:
	print "Usage: smtpenum.py <ip adress OR hostname> <username>" 
	sys.exit(0)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1],587))
banner = s.recv(1024)
print banner

s.send("VRFY "+sys.argv[2]+"\r\n")
result = s.recv(1024)
print result
