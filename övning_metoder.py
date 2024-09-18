def MyCountry(Country = "Sweden"):
    print("I am from " + Country)

MyCountry()
MyCountry("Norway")
MyCountry("England")

def Number(*number):
    print("I like the number " + number[0])
    
Number("0", "11", "20", "420", "50")
#funger bara om jag gör siffrorna strings!

def Name(**namn):
    print("Mitt namn är " + namn["Filippa"])

Name(Jacob = "Jacob Jacobsson", Bertil = "Bertil Warhammer", Filippa = "Filippa Bengtsson") 