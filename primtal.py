x = int(input("är det ett primtal?: "))

def är_primtal(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    if (n - 1) % 4 == 0 or (n - 3) % 4 == 0:
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    else:
        return False
        
    
    
print(är_primtal(x))

    