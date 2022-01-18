import socket
from _thread import *
import sys 
from settings import WIDTH, HEIGHT
from player import Player
import pickle

server = "192.168.1.80"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((server, port))
except socket.error as e:
	str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

players = [[WIDTH // 2 - 30, HEIGHT // 2 - 30, False, False, 0, 1, 0], [WIDTH // 2 - 30, HEIGHT // 2 - 30, False, False, 0, 2, 1]]

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
