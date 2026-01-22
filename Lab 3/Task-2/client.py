import socket

PORT = 5060
FORMAT = "utf-8"
S_Device = socket.gethostname()
S_IP = socket.gethostbyname(S_Device)
S_addr = (S_IP, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(S_addr)

user = input("Please type a message: ")
client.send(user.encode(FORMAT))

s_response = client.recv(1024).decode(FORMAT)
print(f"Server says: {s_response}")

client.close()