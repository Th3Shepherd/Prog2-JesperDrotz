hpoints = 0
tpoints = 0

x = input("Skriv ner här: ")

for points in x:
    if points == "H":
        hpoints += 1
    elif points == "T":
        tpoints += 1

if hpoints > tpoints and hpoints - tpoints >= 2 and hpoints >= 11:
    hpoints = 0
    tpoints = 0
    print(hpoints, tpoints)
elif tpoints > hpoints and tpoints - hpoints >= 2 and tpoints >= 11:
    hpoints = 0
    tpoints = 0
    print(hpoints, tpoints)
else:
    print(hpoints, tpoints)