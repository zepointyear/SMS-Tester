#!/usr/bin/env python
"""
#Use this to call the sms function
#It is for sending SMS using AT commands - version v3
"""
## The packges below must be installed in advance
## install python-setuptools
## install pyserial
 
import serial
import time
import sys

from TextMessage import TextMessage

sms = TextMessage( int(sys.argv[1]) )
sms.connectDevice()
sms.getSimNumber()
sms.storeMessageDaemon()
sms.disconnectDevice()


 
def main():
	pass
 
if __name__ == "__main__":
	main()
