#radio_terminal --rx-socket "tcp://127.0.0.1:55555" --tx-socket "tcp://127.0.0.1:44444" --hwid 0102 --raw

#!/usr/bin/env python
import sys
import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:5555")   
socket.setsockopt_string(zmq.SUBSCRIBE, "")
print("running...")
state = False

while True:
	msg = socket.recv()
	if msg:
		state = True
		print(f"{state}\nReceived: {msg}")
	time.sleep(0.5)
	state = False
	print(f"{state}")

	#Verified sync word: '11010011100100011101001110010001'
