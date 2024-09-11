def summa(*tal):
    return sum(tal)

totalt = summa(1,2,3,4)
print(totalt)

def foods(s, vegan=False):
    if vegan:
        print(f"soja{s}")
    else:
        print(s)

foods("mjölk")
foods("mjölk", True)
