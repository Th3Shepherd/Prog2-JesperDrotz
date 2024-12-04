from tkinter import *
root = Tk()
b = Button(root, text ="Tryck mig!")
def click_handler(self):			# skapa en "callback"-funktion
    print("Någon klickade på knappen!")
b.bind("<Button-1>", click_handler)	# knyt funktionen till händelse
b.pack()
root.mainloop()
