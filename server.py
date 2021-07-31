import socket
from _thread import *
import sys 
from settings import WIDTH, HEIGHT
from player import Player
import pickle

server = "25.89.203.122"
port = 4991

print("Здравсствуйте, вас приветствует NVORON production. Это клиент сервера.")

choose = input("Вы уверены, что хотите оставить ip адрес и порт:" + server + ":" + str(port) + " без изменений?\nНапишите yes или no (Y or N): ")

if choose.upper() == "Y" or choose.upper() == "YES":
	pass

elif choose.upper() == "N" or choose.upper() == "NO":
	ip = input("Вы хотите ввести свой ip или хотите взять из файла? Напишите ip или file: ")
	
	if ip == "ip":
		server = input("Введите ip:")
		port = int(input("Введите порт:"))
	
	elif ip == "file":
		print("Хорошо, ip сервера будет взят с файла ip-server.txt")
		file = open('ip-server.txt', 'r')
		data = file.read()
		server = ':'.join(data.split(':')[:-1])
		port = int(':'.join(data.split(':')[-1:]))
		print("Ip, к которому вы хотите присоединиться: "+data)
	
	else:
		print("Ошибка")
		sys.exit()

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