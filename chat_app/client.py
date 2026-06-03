import socket

# Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect(("localhost", 9999))

while True:

    # Send message
    message = input("You: ")

    client.send(message.encode())

    if message.lower() == "exit":
        break

    # Receive reply
    reply = client.recv(1024).decode()

    print("Server:", reply)

client.close()