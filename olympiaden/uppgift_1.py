a = int(input("första graden: "))
b = int(input("andra graden: "))
c = int(input("tredje graden: "))

if a > 90 or b > 90 or c > 90:
    print("trubbig triangel")
elif a < 90 and b < 90 and c < 90:
    print("spetsig triangel")
elif a == 90 or b == 90 or c == 90:
    print("rätvinkligt triangel")