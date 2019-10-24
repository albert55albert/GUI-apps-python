from tkinter import *
import random
from tkinter import messagebox

aplicatie = Tk()
aplicatie.geometry('392x350')
aplicatie.title('Spanzuratoarea cu litere.')

messagebox.showinfo('', 'Bine ai venit la Spanzuratoarea cu litere!! \n Apasa pe un buton a carui litera corespunzatoare crezi ca se afla in cuvant!')

cuvinte = ['mar', 'par', 'cais', 'prun', 'nuc']

cuvant = random.choice(cuvinte)
iesire = '_' * len(cuvant)
lista1 = list(cuvant)
mega = list(iesire)

incercari = len(cuvant) + 3

ghicite = []

def apasare(litera):
    global ghicire
    global incercari
    ghicire = litera
    scris2 = Label(aplicatie, text = incercari)
    scris2.grid(row = 8, columnspan = 8)
    if incercari > 0:
        if ghicire in cuvant:
            if ghicire not in ghicite:
                pozitie_ghicire = lista1.index(ghicire)
                mega[pozitie_ghicire] = ghicire
                ecran.delete(0, END)
                ecran.insert(0, mega)
                ghicite.append(ghicire)
                if lista1 == mega:
                    messagebox.showinfo('', 'Bravo ai ghicit cuvantul!')
                    aplicatie.destroy()
                elif incercari == -1 and lista1 != mega:
                    messagebox.showinfo('', 'Ai pierdut!')
                    aplicatie.destroy()
            else:
                messagebox.showinfo('', 'Ai introdus o litera pe care ai ghicit.o.')
        else:
            messagebox.showinfo('', 'Ai introdus o litera care nu se afla in cuvant.')
            ecran.delete(0, END)
            ecran.insert(0, mega)
            incercari = incercari-1
    else:
        messagebox.showinfo('', 'Ai pierdut!')
        aplicatie.destroy()

#--------------------------------------------------------------------# Crearea si afisarea butoanelor... .

scris = Label(aplicatie, text = 'Spanzuratoarea cu litere.')
scris.grid(row = 0, columnspan = 8)

ecran = Entry(aplicatie)
ecran.grid(row = 1, columnspan = 8, ipady = 17)


ecran.insert(0, mega) #trebuie sa fie sub ecran !

b1 = Button(aplicatie, text = 'A', height = 3, width = 5, command = lambda : apasare('a'))
b1.grid(row = 3, column = 0)

b2 = Button(aplicatie, text = 'B', height = 3, width = 5, command = lambda : apasare('b'))
b2.grid(row = 3, column = 1)

b3 = Button(aplicatie, text = 'C', height = 3, width = 5, command = lambda : apasare('c'))
b3.grid(row = 3, column = 2)

b4 = Button(aplicatie, text = 'D', height = 3, width = 5, command = lambda : apasare('d'))
b4.grid(row = 3, column = 3)

b5 = Button(aplicatie, text = 'E', height = 3, width = 5, command = lambda : apasare('e'))
b5.grid(row = 3, column = 4)

b6 = Button(aplicatie, text = 'F', height = 3, width = 5, command = lambda : apasare('f'))
b6.grid(row = 3, column = 5)

b7 = Button(aplicatie, text = 'G', height = 3, width = 5, command = lambda : apasare('g'))
b7.grid(row = 3, column = 6)

b8 = Button(aplicatie, text = 'H', height = 3, width = 5, command = lambda : apasare('h'))
b8.grid(row = 3, column = 7)

b9 = Button(aplicatie, text = 'I', height = 3, width = 5, command = lambda : apasare('i'))
b9.grid(row = 4, column = 0)

b10 = Button(aplicatie, text = 'J', height = 3, width = 5, command = lambda : apasare('j'))
b10.grid(row = 4, column = 1)

b11 = Button(aplicatie, text = 'K', height = 3, width = 5, command = lambda : apasare('k'))
b11.grid(row = 4, column = 2)

b12 = Button(aplicatie, text = 'L', height = 3, width = 5, command = lambda : apasare('l'))
b12.grid(row = 4, column = 3)

b13 = Button(aplicatie, text = 'M', height = 3, width = 5, command = lambda : apasare('m'))
b13.grid(row = 4, column = 4)

b14 = Button(aplicatie, text = 'N', height = 3, width = 5, command = lambda : apasare('n'))
b14.grid(row = 4, column = 5)

b15 = Button(aplicatie, text = 'O', height = 3, width = 5, command = lambda : apasare('o'))
b15.grid(row = 4, column = 6)

b16 = Button(aplicatie, text = 'P', height = 3, width = 5, command = lambda : apasare('p'))
b16.grid(row = 4, column = 7)

b17 = Button(aplicatie, text = 'Q', height = 3, width = 5, command = lambda : apasare('q'))
b17.grid(row = 5, column = 0)

b18 = Button(aplicatie, text = 'R', height = 3, width = 5, command = lambda : apasare('r'))
b18.grid(row = 5, column = 1)

b19 = Button(aplicatie, text = 'S', height = 3, width = 5, command = lambda : apasare('s'))
b19.grid(row = 5, column = 2)

b20 = Button(aplicatie, text = 'T', height = 3, width = 5, command = lambda : apasare('t'))
b20.grid(row = 5, column = 3)

b21 = Button(aplicatie, text = 'U', height = 3, width = 5, command = lambda : apasare('u'))
b21.grid(row = 5, column = 4)

b22 = Button(aplicatie, text = 'V', height = 3, width = 5, command = lambda : apasare('v'))
b22.grid(row = 5, column = 5)

b23 = Button(aplicatie, text = 'W', height = 3, width = 5, command = lambda : apasare('w'))
b23.grid(row = 5, column = 6)

b24 = Button(aplicatie, text = 'X', height = 3, width = 5, command = lambda : apasare('x'))
b24.grid(row = 5, column = 7)

b25 = Button(aplicatie, text = 'Y', height = 3, width = 5, command = lambda : apasare('y'))
b25.grid(row = 6)

b26 = Button(aplicatie, text = 'Z', height = 3, width = 5, command = lambda : apasare('z'))
b26.grid(row = 6, column = 1)

scris = Label(aplicatie, text = 'INCERCARI RAMASE:')
scris.grid(row = 7, columnspan = 8)

aplicatie.mainloop()