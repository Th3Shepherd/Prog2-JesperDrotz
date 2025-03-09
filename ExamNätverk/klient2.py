from socket import *


def connect_to_server():
    s = socket()
    host = "192.168.1.182"
    port = 12345
    s.connect((host, port))
    return s

conn = connect_to_server()

b = conn.recv(1024)
msg = b.decode('utf-16')
print(msg)

while True:
    msg = input("Skriv 'slå tärning' för att slå tärningen, eller 'quit' för att avsluta spelet: ")
    
    if msg.lower() == "quit":
        print("Tack för att du spelade!")
        break
    
    b = msg.encode("utf-16")
    conn.send(b)
    
    b = conn.recv(1024)
    msg = b.decode("utf-16")
    print(msg)

conn.close()
