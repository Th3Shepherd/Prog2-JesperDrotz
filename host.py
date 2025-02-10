from socket import *
def start_server():
    s = socket()            # Skapa ett socket-objekt
    host = "10.32.34.239"      # som körs på den egna datorn
    port = 12345            # på port 12345.
    s.bind((host, port))    # Konfigurera socket-objektet.
    s.listen()              # Vänta på att klient ansluter.
    return s
s = start_server()
while True:
    print("Servern är igång på port 12345! Väntar på att en klient ska ansluta...")
    conn, addr = s.accept()     # När en klient ansluter
    print("En klient anslöt från adressen", addr)
    # Skicka meddelande från servern
    msg = "Servern säger hej till klienten! Hur mår du idag?"
    b = msg.encode("utf-16")    # Gör om meddelandet till bytekod
    conn.send(b)                # Skicka meddelandet till klienten
    print("Väntar på meddelande från klienten...")
    # Ta emot ett meddelande från klienten
    b = conn.recv(1024)
    msg = b.decode("utf-16")    # Gör om från bytekod till vanlig text
    print(msg)
    # Stäng anslutningen till klienten
    conn.close()