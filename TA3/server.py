import socket
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()

clients = []

print("Server has started...")

def clientThread(conn, addr):
    conn.send("Welcome to this chatroom!".encode('utf-8'))

    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            if message:
                print("Message from client: ", message)
                # Broadcast the message by calling the broadcast function
                
        except:
            continue

# Define broadcast function that takes two parameters message and connection


    # Loop through each client in clients
    
        # Check if client does not matches the connection
        
            # Add try block
            
                # Send the message to client
                
            # Add except block    
            
                # Print Error while sending to connection
                

while True:
    conn, addr = server.accept()
    
    print("New Client Connected", addr[0])
    clients.append(conn)
    
    new_thread = Thread(target= clientThread,args=(conn, addr))
    new_thread.start()
