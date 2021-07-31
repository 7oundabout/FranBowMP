import socket
from _thread import *
import sys 
from settings import WIDTH, HEIGHT
from player import Player
import pickle
import linecache
print("Здравствуйте. Это клиент сервера.")

ip = input("Вы хотите ввести свой ip или хотите взять из файла? Напишите ip или file: ")

if ip == "ip":
	input_ip = input("Введите ip: ")
	server = ':'.join(input_ip.split(':')[:-1])
	port = int(':'.join(input_ip.split(':')[-1:]))

	save = input("Хотите сохранить ip? Напишите Y или N. ")

	if save.upper() == "Y":
		print("Ip был сохранён в ip-server.txt")
		data = '\n' + input_ip
		open('ip-server.txt', 'a').write(data)


	elif save.upper() == "N":
		print("Ip не был сохранён")
	
	
	else:
		print("Ошибка")
		sys.exit()


elif ip == "file":
	print("Хорошо, ip сервера будет взят с файла ip-server.txt")
	print("Выберите ip: ")

	f = open("ip-server.txt","r")
	listing = f.read()
	print(listing)
	choose = int(input())
	data = linecache.getline('ip-server.txt', choose)
	server = ':'.join(data.split(':')[:-1])
	port = int(':'.join(data.split(':')[-1:]))
	print("Ip вашего сервера: "+ data)
	f.close()

else:
	print("Ошибка")
	sys.exit()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((server, port))
except socket.error as e:
	str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

players = [Player(player_x = WIDTH // 2, player_y = HEIGHT // 2, player_direction = 0, player_detector = 0), Player(player_x = WIDTH // 2 - 20, player_y = HEIGHT // 2 -20, player_direction = 0, player_detector = 0)]

def threaded_client(conn, player):
	conn.send(pickle.dumps(players[player]))
	reply = ""
	while True:
		try:
			data = pickle.loads(conn.recv(2048))
			players[player] = data

			if not data:
				print("Disconnnected")
				break
			else:
				if player == 1:
					reply = players[0]
				else:
					reply = players[1]
#					print("Received: ", data)
#					print("Sending: ", reply)

			conn.sendall(pickle.dumps(reply))
		except:
			break
	print("Lost connection")
	conn.close()

currentPlayer = 0
while True:
	conn, addr = s.accept()
	print("Connected to:", addr)

	start_new_thread(threaded_client, (conn, currentPlayer))
	currentPlayer += 1