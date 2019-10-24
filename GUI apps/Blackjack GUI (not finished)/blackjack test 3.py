from tkinter import *

import random

aplicatie = Tk()

aplicatie.geometry('600x600')

pachet = []
for culoare in ['Inima rosie','inima Neagra','Romb','Trefla']:
    for numere in ['2']:#,'3','4','5','6','7','8','9','10','A','J','Q','K']:
        pachet.append(numere + ' de ' + culoare)

scor = 0
pozitie = 0

def imagine3(nume, label3, photo3):
    global pozitie
    #global photo3
    global image
    photo3 = PhotoImage(file=nume)
    label3 = Label(aplicatie, image = photo3)
    label3.grid(row = 1, column = pozitie)
    pozitie += 1

def v_carte():
    global pozitie
    global scor
    global photo3
    global photo4
    global photo5
    global photo6
    global photo7
    global photo8
    global photo9
    global photo10
    global photo11
    global photo12
    global photo13
    global photo14
    global photo15
    global photo16
    global photo17
    global photo18
    global photo19
    global photo20
    global photo5
    global photo6
    global photo3
    global photo4
    global photo5
    global photo6
    global photo3
    global photo4
    global photo5
    global photo6
    global photo3
    global photo4
    global photo5
    global photo6
    global photo3
    global photo4
    global photo5
    global photo6
    global photo3
    global photo4
    global photo5
    global photo6
    global photo3
    global photo4
    global photo5
    global photo6
    global photo3
    global photo4
    global photo5
    global photo6
    global photo3
    global photo4
    global photo5
    global photo6
    global photo3
    global photo4
    global photo5
    global photo6

    n3 = random.choice(pachet)
    print(n3)
    pozitie3 = pachet.index(n3)
    del pachet[pozitie3]
    for elem in n3:
        if elem == '2': 
            scor += 2
            for elem in n3:
                if elem == 'I':
                    #imagine3('card26.gif', 'l1', 'photo3')
                        photo3 = PhotoImage(file='card26.gif')
                        label3 = Label(aplicatie, image = photo3)
                        label3.grid(row = 1, column = pozitie)
                        pozitie += 1
                elif elem == 'N':
                    #imagine3('card39.gif', 'l1')
                        photo4 = PhotoImage(file='card39.gif')
                        label4 = Label(aplicatie, image = photo4)
                        label4.grid(row = 1, column = pozitie)
                        pozitie += 1
                elif elem == 'T':
                    #imagine3('card0.gif', 'l1')
                        photo5 = PhotoImage(file='card0.gif')
                        label5 = Label(aplicatie, image = photo5)
                        label5.grid(row = 1, column = pozitie)
                        pozitie += 1
                elif elem == 'R':
                    #imagine3('card13.gif', 'l1')
                        photo6 = PhotoImage(file='card13.gif')
                        label6 = Label(aplicatie, image = photo6)
                        label6.grid(row = 1, column = pozitie)
                        pozitie += 1




b1 = Button(aplicatie, text = 'VREAU CARTE!', height = 2, width = 20, command = v_carte)
b1.grid(row = 0, column = 1, pady = 15)

##for elem in n3:
##    if elem == '2': 
##        scor += 2
##        for elem in n3:
##            if elem == 'I':
##                imagine3('card26.gif', 'l1', 'p1')
##            elif elem == 'N':
##                imagine3('card39.gif', 'l2', 'p2')
##            elif elem == 'T':
##                imagine3('card0.gif', 'l3', 'p3')
##            elif elem == 'R':
##                imagine3('card13.gif', 'l4', 'p4')
    
aplicatie.mainloop()
