import socket

# Accept an integer from the keyboard
client_number = int(input('ENTER INTEGER BETWEEN 1 and 100: '))

client_name = input('ENTER CLIENT NAME :')
message = f'{client_name},{client_number}'
serverAddress = '10.5.215.244'
portNumber = 54345
# Create socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((serverAddress, portNumber))

client_socket.send(message.encode())

# Receive data from the server
messageFromServer = client_socket.recv(1024).decode()

print(messageFromServer)

