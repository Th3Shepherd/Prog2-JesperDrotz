from socket import *
def connect_to_server():
    s = socket()                # Skapa ett socket-objekt
    # Ange IP-adress manuellt
    host = input("10.32.34.239")
    # t.ex. "localhost" om servern körs på samma dator som klienten
    port = 12345                # Servern körs på port 12345
    s.connect((host, port))     # Anslut till servern
    return s
s = connect_to_server()
# Ta emot ett meddelande från servern
b = s.recv(1024)
msg = b.decode("utf-16")    # Gör om meddelandet från bytekod till vanlig text
print(msg)
# Skicka ett eget meddelande till servern
msg = input("Skriv något till servern:")
b = msg.encode("utf-16")
s.send(b)
s.close()