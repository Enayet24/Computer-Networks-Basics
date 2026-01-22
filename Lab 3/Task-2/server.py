import socket

PORT = 5060
FORMAT = "utf-8"
S_Device = socket.gethostname()
S_IP = socket.gethostbyname(S_Device)
S_addr = (S_IP, PORT)

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for v in text:
        if v in vowels:
            count += 1
    return count

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(S_addr)
server.listen()
print(f"Server is listening on {S_IP}:{PORT}")

while True:
    c_socket, c_addr = server.accept()
    print(f"\nConnected to {c_addr}")
    
    msg = c_socket.recv(1024).decode(FORMAT)
    print(f"Client says: {msg}")
    
    v_count = count_vowels(msg)
    
    if v_count == 0:
        response = "Not enough vowels"
    elif v_count <= 2:
        response = "Enough vowels I guess"
    else:
        response = "Too many vowels"
        
    
    c_socket.send(response.encode(FORMAT))
    c_socket.close()