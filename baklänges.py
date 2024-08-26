text = input("Skriv text som ska skrivas baklänges här: ")

reverse_text = text[::-1]
# det är tomt i text[:0<--:-1] så att det tar hela strängen 
print("Här är din baklängda text:", reverse_text)