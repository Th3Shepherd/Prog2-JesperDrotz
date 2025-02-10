from socket import *
def connect_to_server():
    s = socket()                # Skapa ett socket-objekt
    # Ange IP-adress manuellt
    host = input("localhost")
    # t.ex. "localhost" om servern körs på samma dator som klienten
    port = 12345                # Servern körs på port 12345
    s.connect((host, port))     # Anslut till servern
    return s
s = connect_to_server()
b = s.recv(1024)            # Ta emot ett meddelande från servern
msg = b.decode("utf-16")    # Gör om meddelandet från bytekod till vanlig text
print(msg)
