from tkinter import *

import random

from tkinter import messagebox

aplicatie = Tk()

aplicatie.geometry('900x600')

aplicatie.title('Blackjack GUI -> Tu vs calculator.')

pachet = []
for culoare in ['Inima rosie','inima Neagra','Romb','Trefla']:
    for numere in ['2','3','4','5','6','7','8','9','10','A','J','Q','K']:
        pachet.append(numere + ' de ' + culoare)

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

def imagine2(nume):
    global pozitie
    global photo2
    global image
    photo2 = PhotoImage(file=nume)
    label2 = Label(aplicatie, image = photo2)
    label2.grid(row = 1, column = pozitie)
    pozitie += 1

def imagine3(nume):
    global pozitie
    global photo3
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
                

def v_carte1():
    global scor
    n3 = random.choice(pachet)
    print(n3)
    pozitie3 = pachet.index(n3)
    del pachet[pozitie3]
    for elem in n3:
        if elem == '2': 
            scor += 2
            for elem in n3:
                if elem == 'I':
                    imagine3('card26.gif')
                elif elem == 'N':
                    imagine3('card39.gif')
                elif elem == 'T':
                    imagine3('card0.gif')
                elif elem == 'R':
                    imagine3('card13.gif')
        elif elem == '3': 
            scor += 2
            for elem in n3:
                if elem == 'I':
                    imagine3('card27.gif')
                elif elem == 'N':
                    imagine3('card40.gif')
                elif elem == 'T':
                    imagine3('card1.gif')
                elif elem == 'R':
                    imagine3('card14.gif')
        elif elem == '4': 
            scor += 2
            for elem in n3:
                if elem == 'I':
                    imagine3('card28.gif')
                elif elem == 'N':
                    imagine3('card41.gif')
                elif elem == 'T':
                    imagine3('card2.gif')
                elif elem == 'R':
                    imagine3('card15.gif')
        elif elem == '5': 
            scor += 2
            for elem in n3:
                if elem == 'I':
                    imagine3('card29.gif')
                elif elem == 'N':
                    imagine3('card42.gif')
                elif elem == 'T':
                    imagine3('card3.gif')
                elif elem == 'R':
                    imagine3('card16.gif')
        elif elem == '6': 
            scor += 2
            for elem in n3:
                if elem == 'I':
                    imagine3('card30.gif')
                elif elem == 'N':
                    imagine3('card43.gif')
                elif elem == 'T':
                    imagine3('card4.gif')
                elif elem == 'R':
                    imagine3('card17.gif')
        elif elem == '7': 
            scor += 2
            for elem in n3:
                if elem == 'I':
                    imagine3('card31.gif')
                elif elem == 'N':
                    imagine3('card44.gif')
                elif elem == 'T':
                    imagine3('card5.gif')
                elif elem == 'R':
                    imagine3('card18.gif')
        elif elem == '8': 
            scor += 2
            for elem in n3:
                if elem == 'I':
                    imagine3('card32.gif')
                elif elem == 'N':
                    imagine3('card45.gif')
                elif elem == 'T':
                    imagine3('card6.gif')
                elif elem == 'R':
                    imagine3('card19.gif')
        elif elem == '9': 
            scor += 2
            for elem in n3:
                if elem == 'I':
                    imagine3('card33.gif')
                elif elem == 'N':
                    imagine3('card46.gif')
                elif elem == 'T':
                    imagine3('card7.gif')
                elif elem == 'R':
                    imagine3('card20.gif')
        elif elem == '10': 
            scor += 2
            for elem in n3:
                if elem == 'I':
                    imagine3('card34.gif')
                elif elem == 'N':
                    imagine3('card47.gif')
                elif elem == 'T':
                    imagine3('card8.gif')
                elif elem == 'R':
                    imagine3('card21.gif')
        elif elem == 'A': 
            scor += 2
            for elem in n3:
                if elem == 'I':
                    imagine3('card38.gif')
                elif elem == 'N':
                    imagine3('card51.gif')
                elif elem == 'T':
                    imagine3('card12.gif')
                elif elem == 'R':
                    imagine3('card25.gif')
        elif elem == 'J': 
            scor += 2
            for elem in n3:
                if elem == 'I':
                    imagine3('card35.gif')
                elif elem == 'N':
                    imagine3('card48.gif')
                elif elem == 'T':
                    imagine3('card9.gif')
                elif elem == 'R':
                    imagine3('card22.gif')
        elif elem == 'Q': 
            scor += 2
            for elem in n3:
                if elem == 'I':
                    imagine3('card36.gif')
                elif elem == 'N':
                    imagine3('card49.gif')
                elif elem == 'T':
                    imagine3('card10.gif')
                elif elem == 'R':
                    imagine3('card23.gif')
        elif elem == 'K': 
            scor += 2
            for elem in n3:
                if elem == 'I':
                    imagine3('card37.gif')
                elif elem == 'N':
                    imagine3('card50.gif')
                elif elem == 'T':
                    imagine3('card11.gif')
                elif elem == 'R':
                    imagine3('card24.gif')
    






n1 = random.choice(pachet)
print(n1)
pozitie1 = pachet.index(n1)
del pachet[pozitie1]

for elem in n1:
    if elem == '2': 
        scor += 2
        for elem in n1:
            if elem == 'I':
                imagine('card26.gif')
            elif elem == 'N':
                imagine('card39.gif')
            elif elem == 'T':
                imagine('card0.gif')
            elif elem == 'R':
                imagine('card13.gif')
    elif elem == '3': 
        scor += 2
        for elem in n1:
            if elem == 'I':
                imagine('card27.gif')
            elif elem == 'N':
                imagine('card40.gif')
            elif elem == 'T':
                imagine('card1.gif')
            elif elem == 'R':
                imagine('card14.gif')
    elif elem == '4': 
        scor += 2
        for elem in n1:
            if elem == 'I':
                imagine('card28.gif')
            elif elem == 'N':
                imagine('card41.gif')
            elif elem == 'T':
                imagine('card2.gif')
            elif elem == 'R':
                imagine('card15.gif')
    elif elem == '5': 
        scor += 2
        for elem in n1:
            if elem == 'I':
                imagine('card29.gif')
            elif elem == 'N':
                imagine('card42.gif')
            elif elem == 'T':
                imagine('card3.gif')
            elif elem == 'R':
                imagine('card16.gif')
    elif elem == '6': 
        scor += 2
        for elem in n1:
            if elem == 'I':
                imagine('card30.gif')
            elif elem == 'N':
                imagine('card43.gif')
            elif elem == 'T':
                imagine('card4.gif')
            elif elem == 'R':
                imagine('card17.gif')
    elif elem == '7': 
        scor += 2
        for elem in n1:
            if elem == 'I':
                imagine('card31.gif')
            elif elem == 'N':
                imagine('card44.gif')
            elif elem == 'T':
                imagine('card5.gif')
            elif elem == 'R':
                imagine('card18.gif')
    elif elem == '8': 
        scor += 2
        for elem in n1:
            if elem == 'I':
                imagine('card32.gif')
            elif elem == 'N':
                imagine('card45.gif')
            elif elem == 'T':
                imagine('card6.gif')
            elif elem == 'R':
                imagine('card19.gif')
    elif elem == '9': 
        scor += 2
        for elem in n1:
            if elem == 'I':
                imagine('card33.gif')
            elif elem == 'N':
                imagine('card46.gif')
            elif elem == 'T':
                imagine('card7.gif')
            elif elem == 'R':
                imagine('card20.gif')
    elif elem == '10': 
        scor += 2
        for elem in n1:
            if elem == 'I':
                imagine('card34.gif')
            elif elem == 'N':
                imagine('card47.gif')
            elif elem == 'T':
                imagine('card8.gif')
            elif elem == 'R':
                imagine('card21.gif')
    elif elem == 'A': 
        scor += 2
        for elem in n1:
            if elem == 'I':
                imagine('card38.gif')
            elif elem == 'N':
                imagine('card51.gif')
            elif elem == 'T':
                imagine('card12.gif')
            elif elem == 'R':
                imagine('card25.gif')
    elif elem == 'J': 
        scor += 2
        for elem in n1:
            if elem == 'I':
                imagine('card35.gif')
            elif elem == 'N':
                imagine('card48.gif')
            elif elem == 'T':
                imagine('card9.gif')
            elif elem == 'R':
                imagine('card22.gif')
    elif elem == 'Q': 
        scor += 2
        for elem in n1:
            if elem == 'I':
                imagine('card36.gif')
            elif elem == 'N':
                imagine('card49.gif')
            elif elem == 'T':
                imagine('card10.gif')
            elif elem == 'R':
                imagine('card23.gif')
    elif elem == 'K': 
        scor += 2
        for elem in n1:
            if elem == 'I':
                imagine('card37.gif')
            elif elem == 'N':
                imagine('card50.gif')
            elif elem == 'T':
                imagine('card11.gif')
            elif elem == 'R':
                imagine('card24.gif')

            

n2 = random.choice(pachet)
print(n2)
pozitie2 = pachet.index(n2)
del pachet[pozitie2]

for elem in n2:
    if elem == '2': 
        scor += 2
        for elem in n2:
            if elem == 'I':
                imagine2('card26.gif')
            elif elem == 'N':
                imagine2('card39.gif')
            elif elem == 'T':
                imagine2('card0.gif')
            elif elem == 'R':
                imagine2('card13.gif')
    elif elem == '3': 
        scor += 2
        for elem in n2:
            if elem == 'I':
                imagine2('card27.gif')
            elif elem == 'N':
                imagine2('card40.gif')
            elif elem == 'T':
                imagine2('card1.gif')
            elif elem == 'R':
                imagine2('card14.gif')
    elif elem == '4': 
        scor += 2
        for elem in n2:
            if elem == 'I':
                imagine2('card28.gif')
            elif elem == 'N':
                imagine2('card41.gif')
            elif elem == 'T':
                imagine2('card2.gif')
            elif elem == 'R':
                imagine2('card15.gif')
    elif elem == '5': 
        scor += 2
        for elem in n2:
            if elem == 'I':
                imagine2('card29.gif')
            elif elem == 'N':
                imagine2('card42.gif')
            elif elem == 'T':
                imagine2('card3.gif')
            elif elem == 'R':
                imagine2('card16.gif')
    elif elem == '6': 
        scor += 2
        for elem in n2:
            if elem == 'I':
                imagine2('card30.gif')
            elif elem == 'N':
                imagine2('card43.gif')
            elif elem == 'T':
                imagine2('card4.gif')
            elif elem == 'R':
                imagine2('card17.gif')
    elif elem == '7': 
        scor += 2
        for elem in n2:
            if elem == 'I':
                imagine2('card31.gif')
            elif elem == 'N':
                imagine2('card44.gif')
            elif elem == 'T':
                imagine2('card5.gif')
            elif elem == 'R':
                imagine2('card18.gif')
    elif elem == '8': 
        scor += 2
        for elem in n2:
            if elem == 'I':
                imagine2('card32.gif')
            elif elem == 'N':
                imagine2('card45.gif')
            elif elem == 'T':
                imagine2('card6.gif')
            elif elem == 'R':
                imagine2('card19.gif')
    elif elem == '9': 
        scor += 2
        for elem in n2:
            if elem == 'I':
                imagine2('card33.gif')
            elif elem == 'N':
                imagine2('card46.gif')
            elif elem == 'T':
                imagine2('card7.gif')
            elif elem == 'R':
                imagine2('card20.gif')
    elif elem == '10': 
        scor += 2
        for elem in n2:
            if elem == 'I':
                imagine2('card34.gif')
            elif elem == 'N':
                imagine2('card47.gif')
            elif elem == 'T':
                imagine2('card8.gif')
            elif elem == 'R':
                imagine2('card21.gif')
    elif elem == 'A': 
        scor += 2
        for elem in n2:
            if elem == 'I':
                imagine2('card38.gif')
            elif elem == 'N':
                imagine2('card51.gif')
            elif elem == 'T':
                imagine2('card12.gif')
            elif elem == 'R':
                imagine2('card25.gif')
    elif elem == 'J': 
        scor += 2
        for elem in n2:
            if elem == 'I':
                imagine2('card35.gif')
            elif elem == 'N':
                imagine2('card48.gif')
            elif elem == 'T':
                imagine2('card9.gif')
            elif elem == 'R':
                imagine2('card22.gif')
    elif elem == 'Q': 
        scor += 2
        for elem in n2:
            if elem == 'I':
                imagine2('card36.gif')
            elif elem == 'N':
                imagine2('card49.gif')
            elif elem == 'T':
                imagine2('card10.gif')
            elif elem == 'R':
                imagine2('card23.gif')
    elif elem == 'K': 
        scor += 2
        for elem in n2:
            if elem == 'I':
                imagine2('card37.gif')
            elif elem == 'N':
                imagine2('card50.gif')
            elif elem == 'T':
                imagine2('card11.gif')
            elif elem == 'R':
                imagine2('card24.gif')



mana_j1 = n1 + ',' + n2

scris = Label(aplicatie, text = 'TU: ', pady = 15)
scris.grid(row = 0)

b1 = Button(aplicatie, text = 'VREAU CARTE!', height = 2, width = 20, command = v_carte)
b1.grid(row = 0, column = 1, pady = 15)

b2 = Button(aplicatie, text = 'NU MAI VREAU CARTE!', height = 2, width = 20)
b2.grid(row = 0, column = 2, pady = 15)

scris2 = Label(aplicatie, text = '______________________________________________________________________________________________________________________________________________________________________________________________________________________')
scris2.grid(row = 2, columnspan =6)

scris3 = Label(aplicatie, text = 'CALCULATOR: ', pady = 15)
scris3.grid(row = 3)

aplicatie.mainloop()
