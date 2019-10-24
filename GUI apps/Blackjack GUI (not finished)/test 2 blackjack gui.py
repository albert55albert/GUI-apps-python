from tkinter import *

aplicatie = Tk()




scor = 0
pozitie = 0

def imagine(nume):
    global photo1
    global image
    global pozitie
    photo1 = PhotoImage(file=nume)
    label = Label(aplicatie, image = photo1)
    label.grid(row = 1, column = pozitie)
    pozitie += 1



def verificare(mana_j1):
    global pozitie
    global photo1
    global image
    global scor
    #global mana_j1
    for elem in mana_j1:
        if elem == '2': 
            scor += 2
            for elem in mana_j1:
                if elem == 'N':
                    imagine('card39.gif')
                    print(pozitie)
                elif elem == 'I':
                    photo1 = PhotoImage(file="card26.gif")
                    label1 = Label(aplicatie, image = photo1)
                    label1.grid(row = 1, column = pozitie)
                    pozitie += 1
                    print(pozitie)
                elif elem == 'T':
                    photo1 = PhotoImage(file="card0.gif")
                    label1 = Label(aplicatie, image = photo1)
                    label1.grid(row = 1, column = pozitie)
                    pozitie += 1
                    print(pozitie)
                elif elem == 'R':
                    photo1 = PhotoImage(file="card13.gif")
                    label1 = Label(aplicatie, image = photo1)
                    label1.grid(row = 1, column = pozitie)
                    pozitie += 1
                    print(pozitie)


def verificare2(mana_j):
    global pozitie
    global photo2
    global image
    global scor
    #global mana_j1
    for elem in mana_j:
        if elem == '2': 
            scor += 2
            for elem in mana_j:
                if elem == 'N':
                    photo2 = PhotoImage(file="card39.gif")
                    label2 = Label(aplicatie, image = photo2)
                    label2.grid(row = 1, column = pozitie)
                    pozitie += 1
                    print(pozitie)
                elif elem == 'I':
                    photo2 = PhotoImage(file="card26.gif")
                    label2 = Label(aplicatie, image = photo2)
                    label2.grid(row = 1, column = pozitie)
                    pozitie += 1
                    print(pozitie)
                elif elem == 'T':
                    photo2 = PhotoImage(file="card0.gif")
                    label2 = Label(aplicatie, image = photo2)
                    label2.grid(row = 1, column = pozitie)
                    pozitie += 1
                    print(pozitie)
                elif elem == 'R':
                    photo2 = PhotoImage(file="card13.gif")
                    label2 = Label(aplicatie, image = photo2)
                    label2.grid(row = 1, column = pozitie)
                    pozitie += 1
                    print(pozitie)


mana_j11 = '2I'

mana_j12 = '2N'

verificare(mana_j12)
#verificare2(mana_j12)



aplicatie.mainloop()
