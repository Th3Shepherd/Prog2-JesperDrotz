from socket import *
from _thread import *
import random

def start_server():         # Samma som i förra exemplet
    s = socket()
    host = "localhost"
    port = 12345
    s.bind((host, port))
    s.listen()
    return s

def threaded_client(connection, player_number, other_player_conn):   
    msg = f"Spelare {player_number}, välkommen till tärningsspelet!"
    connection.send(msg.encode("utf-16"))
    
    game_over = False
    target_score = 20
    current_score = 0
    
    while not game_over:
        data = connection.recv(1024)
        if not data:
            break
        msg = data.decode("utf-16")
        
        if msg.lower() == "slå tärning":
            roll = random.randint(1, 6)
            current_score += roll
            if current_score >= target_score:
                msg = f"Du slog {roll}. Din totalpoäng är {current_score}. Du har vunnit!"
                game_over = True
            else:
                msg = f"Du slog {roll}. Din totalpoäng är {current_score}. Det är nu nästa spelares tur!"
            
            other_player_conn.send(f"Spelare {player_number} slog {roll}. Totalt: {current_score}".encode("utf-16"))
        
        else:
            msg = "För att slå tärningen, skriv 'slå tärning'."
        
        connection.send(msg.encode("utf-16"))
    
    connection.send("Spelet är slut. Tack för att du spelade!".encode("utf-16"))
    connection.close()

s = start_server()
print("Servern är igång och väntar på spelare...")

ThreadCount = 0
connections = []  

while len(connections) < 2:
    conn, address = s.accept()
    print(f"En ny spelare anslöt: {address[0]}:{str(address[1])}")
    connections.append(conn)
    ThreadCount += 1
    print(f"Spelare #{ThreadCount} ansluten!")

print("Båda spelarna är anslutna. Spelet börjar!")
start_new_thread(threaded_client, (connections[0], 1, connections[1])) 
start_new_thread(threaded_client, (connections[1], 2, connections[0]))