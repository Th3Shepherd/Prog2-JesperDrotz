class Media:
    def __init__(self, titel):
        self.titel = titel
class Bok(Media):
    def __init__(self, titel, antalSidor):
        super().__init__(titel)
        self.antalSidor = antalSidor
class Ljudspår(Media):
    def __init__(self, titel, speltid):
        super().__init__(titel)
        self.speltid = speltid
class Film(Ljudspår):
    def __init__(self, titel, speltid, upplösning):
        super().__init__(titel, speltid)
        self.upplösning = upplösning
x = Film("Warhammer", "2 timmar", "4k")
print(x.upplösning)

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
    
x = Student("Himmy", "Barack", 2035)
x.welcome()
