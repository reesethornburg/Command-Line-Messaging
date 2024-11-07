import socket
import threading
import sys

def outgoingMessage(client):
    try:
        while True:
            message = input("Enter message to send: ")
            if message == "/quit":
                print('Client closed.')
                client.send(message.encode('utf-8'))
                break
            else: client.send(message.encode('utf-8'))
    except:
        print("[Error] error occured in outgoingMessage()")

def incomingMessage(client):
    while True:
        try:
            message= client.recv(1024).decode('utf-8')
            if message:
                print(f"\nMessage received from server: {message}")
                print("Enter message to send: ")
            else: break
        except:
            print("Error occured in incomingMessage()")
            break



def client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if len(sys.argv) != 3:
        if len(sys.argv) < 3:
            print("[Error] Not enough arguments passed.")
            return
        if len(sys.argv) > 3:
            print("[Error] Too many arguments passed.")
            return
    else:
        servIP = sys.argv[1]
        servPort = int(sys.argv[2])

    client.connect((servIP, servPort))
    senderThread = threading.Thread(target=outgoingMessage, args=(client,))
    receiverThread = threading.Thread(target=incomingMessage, args=(client,))
    senderThread.start()
    receiverThread.start()
    senderThread.join()
    receiverThread.join()
    client.close()

client()
