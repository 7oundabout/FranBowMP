import socket
from _thread import *
import sys 
from settings import WIDTH, HEIGHT
import pickle
from levels import *

server = "192.168.1.172"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((server, port))
except socket.error as e:
	str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

players = [[WIDTH // 2 - 30, HEIGHT // 2 - 30, False, False, 0, 1, 0, None, levels_map], [WIDTH // 2 - 30, HEIGHT // 2 - 30, False, False, 0, 2, 1, None, levels_map]]

first_one = True
second_one = True

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
				if players[player][7] == None:
					pass
				else:
					packageInput(players[player][7])
					players[player][7] = None
					players[0][8] = levels_map
					players[1][8] = levels_map

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

def packageInput(data_player):
	if data_player != None:
		if data_player[0] == False:
			character = list(levels_map[data_player[1]][data_player[2]]) 
			character[data_player[3]] = "1"
			"".join(character)
			levels_map[data_player[1]][data_player[2]] = character

		elif data_player[0] == True:
			character = list(levels_map[data_player[1]][data_player[2]]) 
			character[data_player[3]] = "-"
			"".join(character)
			levels_map[data_player[1]][data_player[2]] = character

currentPlayer = 0
while True:
	conn, addr = s.accept()
	print("Connected to:", addr)

	start_new_thread(threaded_client, (conn, currentPlayer))
	currentPlayer += 1
