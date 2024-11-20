pear = int(input("Hur många päron har Axel sålt: ")) 
apple = int(input("Hur många äpplen har Petra sålt"))

pearprice = 13
appleprice = 7

pearcost = 13 * pear
applecost = 7 * apple

if(pearcost > applecost):
    print("Axel")
elif pearcost < applecost:
    print("Petra")
else:
    print("lika")
    

