import socket

PORT = 5060
FORMAT = "utf-8"
S_Device = socket.gethostname()
S_IP = socket.gethostbyname(S_Device)
S_addr = (S_IP, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(S_addr)

hours_input = input("Enter total hours worked: ")

client.send(hours_input.encode(FORMAT))

salary_response = client.recv(1024).decode(FORMAT)
print(f"Total Salary: Tk {salary_response}")

client.close()