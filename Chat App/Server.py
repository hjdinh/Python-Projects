import socket
import threading

host = socket.gethostbyname(socket.gethostname())   # host server ip (private IP)
port = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # define constants (internet, TCP)
server.bind((host, port))   # bind host and port to socket

server.listen()     # listen for incoming connection, can define how many connections we accept

clients = []
usernames = []

def broadcast(message):     # broadcast message in terminal
    for client in clients:
        client.send(message)

def handle(client):     # handle individual connections to client
    while True:
        try:
            message = client.recv(1024).decode("utf-8")     # receive message from client
            print(f"{usernames[clients.index(client)]} says {message}")
            broadcast(message)      # broadcast to clients connected
        except:         # if client disconnects, remove them from client and usernames list
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            usernames.remove(username)
            break

def receive():
    while True:
        client, address = server.accept()       # accept connection, return client and server address
        print(f"Connected with {str(address)}.")
        
        client.send("USER".encode("utf-8"))     # send keyword to signal client that we're requesting the username
        username = client.recv(1024).decode("utf-8")    # receive username 

        clients.append(client)
        usernames.append(username)

        print(f"Username of client is {username}")
        broadcast(f"{username} has connected to the server.\n".encode("utf-8"))     # call broadcast method
        client.send("Connected to the server".encode("utf-8"))

        thread = threading.Thread(target=handle, args=(client,))    # execute handle method simultaneously 
        thread.start()

print("Server running...")
receive()