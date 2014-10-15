#WindyBrew by Will Simm, Catalyst Project, Lancaster University w.simm@lancs.ac.uk
#see readme.md

import pusherclient
import time
import json
import math
import os
global pusher
global socket


def connect_handler(data):
	#this will obviously depend on your data feed
    channel = pusher.subscribe('windTurbine')
    channel.bind('power', process)


#turn on socket
def socket_on():
	global socket
	if (socket == 0):
		os.system('sudo python /home/pi/raspberry-strogonanoff/src/strogonanoff_sender.py --channel 1 --button 3 --gpio 0 on')
        	print ('socket on')
		socket = 1
	else:
		print ('socket already on')

#turn it off
def socket_off():
	global socket
	if (socket == 1):
		os.system('sudo python /home/pi/raspberry-strogonanoff/src/strogonanoff_sender.py --channel 1 --button 3 --gpio 0 off')
        	print ('socket off')
		socket = 0
	else:
		print ('socket already off')

#decode the json from pusher
def process(power):
	decoded = json.loads(power)
	#print ('power')
	#print (decoded['power']) 

	#here is the threshold for turning socket on or off
	if (float(decoded['power']) >= 25):
		socket_on()
	else:
		socket_off()


#set this path to where you down;loaded strogonoff's socket control script - https://github.com/dmcg/raspberry-strogonanoff
os.system('sudo python /home/pi/raspberry-strogonanoff/src/strogonanoff_sender.py --channel 1 --button 3 --gpio 0 off')
print ('socket off')
socket = 0

#setup your pusher connection here
pusher = pusherclient.Pusher('<api key>')
pusher.connection.bind('pusher:connection_established', connect_handler)
pusher.connect()


while True:
    time.sleep(1)

