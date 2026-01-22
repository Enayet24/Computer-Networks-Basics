import socket
import threading

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

def handle_client(conn, addr):
    print(f"\n[NEW CONNECTION] {addr} connected.")
    
    try:
        msg = conn.recv(1024).decode(FORMAT)
        print(f"[{addr}] Message: {msg}")
        
        v_count = count_vowels(msg)
        
        if v_count == 0:
            response = "Not enough vowels"
        elif v_count <= 2:
            response = "Enough vowels I guess"
        else:
            response = "Too many vowels"
            
        conn.send(response.encode(FORMAT))
        print(f"[{addr}] Sent: {response}")
        
    finally:
        conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(S_addr)
server.listen()
print(f"Server is listening on {S_IP}:{PORT}")

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.daemon = True 
    thread.start()
    print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

