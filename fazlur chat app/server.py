import time, socket, sys, threading
 
HEADER = 64
FORMAT = "utf-8"
new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
DISCONNECT_MESSAGE = "!DISCONNECT"
 
port = 8080
 
new_socket.bind((host_name, port))
print( "Binding successful!")
print("This is your IP: ", s_ip)
 
name = input('Enter name: ')
 
new_socket.listen(2) 
 
 
conn, add = new_socket.accept()
 
print("Received connection from ", add[0])
print('Connection Established. Connected From: ',add[0])
 
client = (conn.recv(1024)).decode()
print(client + ' has connected.')
 
def client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()
        

def start():
    new_socket.listen()
    print(f"[LISTENING] Server is listening on {new_socket}")
    while True:
        conn, addr = new_socket.accept()
        thread = threading.Thread(target=client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()