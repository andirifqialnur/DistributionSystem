import socket
import select
import threading

HEADER_LENGTH = 64
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 2706
ADDR = (SERVER, PORT)
FORMAT = "utf-8"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((SERVER, PORT))
server_socket.listen()

sockets_list = [server_socket]

clients = {}


def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)

        if not len(message_header):
            return False

        message_length = int(message_header.decode(FORMAT).strip())
        return {"header": message_header, "data": client_socket.recv(message_length)}

    except:
        pass


def handle_client():
    # -------------------------
    read_sockets, _, = select.select(sockets_list, [], sockets_list)

    if read_sockets == server_socket:
        client_socket, client_address = server_socket.accept()

        user = receive_message(client_socket)
        sockets_list.append(client_socket)
        clients[client_socket] = user

        print(
            f"Accepted new connection from {client_address[0]}:{client_address[1]} username:{user['data'].decode(FORMAT)}")

    else:
        message = receive_message(read_sockets)

        if message is False:
            print(
                f"Closed Connection From {clients[read_sockets]['data'].decode(FORMAT)}")
            sockets_list.remove(read_sockets)
            del clients[read_sockets]

            user = clients[read_sockets]
            print(
                f"Received message from {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")

            if clients != read_sockets:
                clients.send(user['header'] + user['data'] + message['data'])

            # exception_sockets = sockets_list.remove(read_sockets)
            # del clients[read_sockets]
# ...............................................
    # def start():
    #     server.listen()
    #     print(f"[LISTENING] Server is Listening {SERVER}")

    #     while True:
    #         conn, addr = server.accept()
    #         thread = threading.Thread(target=handle_client, args=(conn, addr))
    #         thread.start()

    #         print(f"[ACTIVE CONNECTIONS] {threading.activeCount() + 1}")

    print(f"[LISTENING] Server is Listening {SERVER}")


while True:
    conn, addr = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=())
    thread.start()

    print(f"Received message from {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")
    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() + 1}")
