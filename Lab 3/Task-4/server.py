import socket

PORT = 5060
FORMAT = "utf-8"
S_Device = socket.gethostname()
S_IP = socket.gethostbyname(S_Device)
S_addr = (S_IP, PORT)

def calc_salary(hrs):
    if hrs <= 40:
        return hrs * 200
    else:
        return 8000 + (hrs - 40) * 300

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(S_addr)
server.listen()
print(f"Server is listening on {S_IP}:{PORT}")

while True:
    client_socket, client_addr = server.accept()
    print(f"\nConnected to {client_addr}")
    
    try:
        msg = client_socket.recv(1024).decode(FORMAT)
        hrs_worked = float(msg)
        print(f"Client worked: {hrs_worked} hours")
    
        salary = calc_salary(hrs_worked)
        
        
        response = f"{salary}"
        client_socket.send(response.encode(FORMAT))
        print(f"Sent salary: Tk {salary}")
        
    finally:
        client_socket.close()