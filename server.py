import socket
import threading
import sys


def broadcast(message, clientList, sender):
    try:
        for i in clientList:
            if i == sender:
                pass
            else:
                i.send(message.encode('utf-8'))
    except:
        print("[Error] Error occured in broadcast().")
        sender.close()

def takeClient(client, clientList):
    clientList.append(client)
    while True:
        try:
            if clientList == []:
                print("No more clients.")
                break
            message = client.recv(1024).decode('utf-8')
            if message:
                if message == '/quit':
                    print(f"{client} disconnected.")
                    break
                print(f"received message: {message}")
                broadcast(message, clientList, client)
            else:
                break
        except:
            print("[Error] Error occured in 'takeClient()'.")
            break
    clientList.remove(client)
    client.close()

def server():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servIP = "localhost"
    if len(sys.argv) != 2:
        if len(sys.argv) > 2:
            print("[Error] Too many arguments.")
            return
        if len(sys.argv) < 2:
            print("[Error] Not enough arguments.")
            return
    else:
        servPort = int(sys.argv[1])
    serv.bind((servIP, servPort))
    serv.listen(3)
    print("Listening for client.")
    clientList = []
    try:
        while True:
            clientSock, clientAddr = serv.accept()
            print(f"Connection established with {clientSock} at {clientAddr}")
            thread = threading.Thread(target=takeClient, args=(clientSock,clientList,))
            thread.start()
    except:
        print("[error] Error occured in server()")
        serv.close()

server()
