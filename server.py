import socket
import random
import pickle
from _thread import *
from game import Game

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "192.168.248.72"
port = 6666
try:
    sock.bind((server, port))
except socket.error as e:
    str(e)

sock.listen(2)  
print("server running. Waiting for connections...")

connected = set()
games = {}
idCount = 0

def threaded_client(conn, p, gameId):
    global idCount
    p=str(p)
    conn.send(p.encode())
    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()
            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(p, data)
                    conn.sendall(pickle.dumps(game))
                    i=1
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()


def create():
    y = [random.choice('roygbp') for _ in range(4)]
    check="".join(y)
    print(y)
    secret_code = str(check)
    print(secret_code)
    return secret_code


while True:
    conn, addr = sock.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
        secret_code=create()
        secret_code = str(secret_code)
        conn.send(secret_code.encode())
        print("player 1 sent")
    else:
        games[gameId].ready = True
        p = 1
        conn.send(secret_code.encode())
        print("player 2 sent")
    
    start_new_thread(threaded_client, (conn, p, gameId))
