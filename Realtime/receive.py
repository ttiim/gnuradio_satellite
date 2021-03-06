#Timothy Wriglesworth
#ALEASAT Mission
#ORCASAT Mission
#University of British Columbia


#>python3 receive.py

# to find block implementations look at:
#https://github.com/daniestevez/gr-satellites/find/maint-3.8

import sys
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.2:5559")   
socket.setsockopt_string(zmq.SUBSCRIBE, '')
print("running..")

while True:
	string = socket.recv()
	print(f"Received: {string}")

	#Verified sync word: '11010011100100011101001110010001'


# 00110101001011100011010100101110

# 00110101001011100011010100101110


# 11010011
# 10010001


# 11010011100100011101001110010001