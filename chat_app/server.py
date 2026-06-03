import socket

# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind IP and Port
server.bind(("localhost", 9999))

# Listen for client
server.listen(1)

print("Waiting for connection...")

client_socket, address = server.accept()

print("Connected to:", address)

while True:

    # Receive message from client
    message = client_socket.recv(1024).decode()

    if message.lower() == "exit":
        print("Chat ended")
        break

    print("Client:", message)

    # Send reply
    reply = input("You: ")

    client_socket.send(reply.encode())

client_socket.close()
server.close()