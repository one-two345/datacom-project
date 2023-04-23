import socket
import random
# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind(('', 54345))

# Listen for incoming connections
server_socket.listen(5)

print('Server is ready to receive connections...')

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()

    print(f'Connection from {client_address}')

    # Receive data from the client
    data = client_socket.recv(1024).decode()
    
    # Extract client's name and number from the received data
    client_name, client_number = data.split(',')
    client_number = int(client_number)
    if not 1<=client_number<=100:
        client_socket.shutdown(5)
    # Generate server's name and server-chosen number
    server_name = 'Server of shambel'
    server_number = random.randint(1, 100) 
    
    total = client_number + server_number
    
    print("Server Name: ", server_name, "\n client Name: ", client_name, "\n server No.: ", server_number,
        "\n client No. : ", client_number, "\n Sum: ", total)
    # Prepare the response message
    response = f'Client: {client_name}\nServer: {server_name}\nClient Number: {client_number}\nServer Number: {server_number}\nSum: {total}'
    
    # Send the response back to the client
    client_socket.send(response.encode())
