import socket 


with open('notes/wordlist.txt', 'r') as files:
    users = files.readlines() 

target = input("Target: ")

for user in users:
    user.strip("\n")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.connect((target, 25)) 
    sock.recv(1024) 
    sock.send(b"VRFY {user}\n") 
    smtp_result = sock.recv(1024) 
    sock.close() 
    
    if "252" in smtp_result:
        print(f"{user} -> Valid!")
    elif "550" in smtp_result:
        print(f"{user} -> Invalid User!")
    elif "503" in smtp_result:
        print("Server requires authentication.")
        break
    else:
        print("server response: ", smtp_result)