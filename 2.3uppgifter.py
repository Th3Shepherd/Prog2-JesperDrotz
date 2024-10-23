class landdjur:
    def __init__(self):
        self.miljö = "land"
    
    def moving(self):
        return "Rör sig på land!"
    
    
class havsdjur:
    def __init__(self):
        self.miljö = "hav"
    def moving(self):
        return "Rör sig i vatten!"

class däggdjur:
    def __init__(self):
        self.föder = "föder levande"

class Häst(landdjur, däggdjur):
    def __init__(self):
        landdjur.__init__(self)
        däggdjur.__init__(self)
        self.art = "Häst"
        

class val(havsdjur, däggdjur):
    def __init__(self):
        super().__init__(self)
        self.art = "Val"
        

class ödla(landdjur):
    def __init__(self):
        super().__init__(self)
        self.art = "Ödla"
        

