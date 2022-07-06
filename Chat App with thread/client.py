import socket

FORMAT = "utf-8"

HEADER = 64
PORT = 5050
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.56.1"

ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    message_length = len(message)
    send_length = str(message_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048). decode(FORMAT))


send("Hello World!")
input()
send("Hello Guyss!")
input()
send("Hy Everyone!")

send(DISCONNECT_MESSAGE)
