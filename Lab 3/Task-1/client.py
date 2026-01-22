import socket

PORT = 5060
FORMAT = "utf-8"
S_Device = socket.gethostname()
S_IP = socket.gethostbyname(S_Device)
S_addr = (S_IP, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(S_addr)

hostname = socket.gethostname()
c_ip = socket.gethostbyname(hostname)

message = f"Client IP: {c_ip}, Client Device Name: {hostname}"
client.send(message.encode(FORMAT))

client.close()