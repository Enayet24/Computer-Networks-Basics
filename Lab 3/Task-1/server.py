import socket

PORT = 5060
FORMAT = "utf-8"
S_Device = socket.gethostname()
S_IP = socket.gethostbyname(S_Device)
S_addr = (S_IP, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(S_addr)

server.listen()
print(f"Server is listening on {S_IP}:{PORT}")

while True:
    c_socket, c_addr = server.accept()
    print(f"Connection accepted from {c_addr}")

    msg = c_socket.recv(1024).decode(FORMAT)
    print(f"Received Client Information : {msg}")
    
    c_socket.close()
