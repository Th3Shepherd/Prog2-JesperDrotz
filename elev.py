class Elev:
    glad = False
    def __init__ (self, name, age, godkänd):
        self.name = name
        self.age = age
        if godkänd:
            self.glad = True
        
e1 = Elev("Johann", 21, True)

print(e1.name)
print(e1.age)
print(e1.glad)