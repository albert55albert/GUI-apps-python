from tkinter import *

aplicatie = Tk()



##photo1 = PhotoImage(file="card26.gif")
##label = Label(a, image = photo1)
##label.grid(row = 1)
##
##photo1 = PhotoImage(file="card27.gif")
##label = Label(a, image = photo1)
##label.grid(row = 1, column = 90)
scor = 0
pozitie = 0
def imagine(nume):
    global pozitie
    global photo1
    global image
    photo1 = PhotoImage(file=nume)
    label = Label(aplicatie, image = photo1)
    label.grid(row = 1, column = pozitie)
    pozitie += 1

mana_j1 = '2I'

for elem in mana_j1:
    if elem == '2': 
        scor += 2
        for elem in mana_j1:
            if elem == 'I':
                imagine('card26.gif')
            elif elem == 'N':
                imagine('card39.gif')
            elif elem == 'T':
                imagine('card0.gif')
            elif elem == 'R':
                imagine('card13.gif')

aplicatie.mainloop()
