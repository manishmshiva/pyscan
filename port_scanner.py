#!/usr/env/python
# Port scanner using python
# Author: Manish Shivanandhan (www.manishmshiva.com)
# Date : 13-May-2020

import socket
import sys

# cli arguments
try:
    server = sys.argv[1]
except:
    print("Enter an ip as a command line argument")
    quit()
    

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# connect to a port and perform the scan
def port_scan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False

# Run a scan for all the important ports to see if they are open

for port in range(0,1024):
    if port_scan(port):
        print("Port ",port," is open.")
    else:
        print("Port ",port," is closed.")