import socket
# import Thread


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000
nickname = input("Choose your nickname: ")

client.connect((ip_address, port))
print("Connected with the server...")

# Create write() function

    # Create infinite loop
    
        # indent following lines to be part of the while loop
        # Send nickname and user input as message
        
        


message = client.recv(2048).decode('utf-8')
print("Message from server: ", message)   

# Create a thread write_thread that runs receive function

# Start thr write_thread
