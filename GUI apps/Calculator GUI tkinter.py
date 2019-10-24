from tkinter import *

from tkinter import messagebox

aplicatie = Tk()

aplicatie.geometry('268x334')

aplicatie.title('Calculator')

#------------------------------------# functii pt butoane

def clic(numar):
	actual = ecran.get() #ia de pe ecran ce este afisat
	ecran.delete(0, END)
	ecran.insert(0, str(actual) + str(numar)) #variabila actual este adunata cu nr coresp. butonului apasat

def plus():
	nr_1 = ecran.get() #tot sirul de numere este transformat intr-un singur numar 'complet'
	global nr__1
	global operatie
	operatie = 'adunare' #seteaza ca operatia sa fie ...
	nr__1 = int(nr_1) #transforma stringul in integer
	ecran.delete(0, END)

def minus():
	nr_1 = ecran.get() #tot sirul de numere este transformat intr-un singur numar 'complet'
	global nr__1
	global operatie
	operatie = 'scadere' #seteaza ca operatia sa fie ...
	nr__1 = int(nr_1) #transforma stringul in integer
	ecran.delete(0, END)

def inmultire():
	nr_1 = ecran.get() #tot sirul de numere este transformat intr-un singur numar 'complet'
	global nr__1
	global operatie
	operatie = 'inmultire' #seteaza ca operatia sa fie ...
	nr__1 = int(nr_1) #transforma stringul in integer
	ecran.delete(0, END)

def impartire():
	nr_1 = ecran.get() #tot sirul de numere este transformat intr-un singur numar 'complet'
	global nr__1
	global operatie
	operatie = 'impartire' #seteaza ca operatia sa fie ...
	nr__1 = int(nr_1) #transforma stringul in integer
	ecran.delete(0, END)

def egal():
	nr_2 = ecran.get() #dupa ce ai apasat egal ce este pe ecran intra in variabila nr_2
	nr__2 = int(nr_2)
	ecran.delete(0, END)

	if operatie == 'adunare':
		rezultat = nr__1 + nr__2 #se calculeaza suma
		ecran.insert(0, rezultat) #se arata suma pe ecran
	elif operatie == 'scadere':
		rezultat = nr__1 - nr__2
		ecran.insert(0, rezultat)
	elif operatie == 'inmultire':
		rezultat = nr__1 * nr__2
		ecran.insert(0, rezultat)
	elif operatie == 'impartire':
		rezultat = nr__1 / nr__2
		ecran.insert(0, rezultat)

def clear():
	ecran.delete(0, END)

#----------------------------------------# crearea butoanelor butoanelor

ecran = Entry(aplicatie)
b_plus = Button(aplicatie, text = '+', height = 4, width = 7, command = plus)
b1 = Button(aplicatie, text = '1', height = 4, width = 7, command = lambda : clic(1))
b2 = Button(aplicatie, text = '2', height = 4, width = 7, command = lambda : clic(2))
b3 = Button(aplicatie, text = '3', height = 4, width = 7, command = lambda : clic(3))
b_minus = Button(aplicatie, text = '-', height = 4, width = 7, command = minus)
b4 = Button(aplicatie, text = '4', height = 4, width = 7, command = lambda : clic(4))
b5 = Button(aplicatie, text = '5', height = 4, width = 7, command = lambda : clic(5))
b6 = Button(aplicatie, text = '6', height = 4, width = 7, command = lambda : clic(6))
b_inmultit = Button(aplicatie, text = '*', height = 4, width = 7, command = inmultire)
b7 = Button(aplicatie, text = '7', height = 4, width = 7, command = lambda : clic(7))
b8 = Button(aplicatie, text = '8', height = 4, width = 7, command = lambda : clic(8))
b9 = Button(aplicatie, text = '9', height = 4, width = 7, command = lambda : clic(9))
b_impartit = Button(aplicatie, text = '/', height = 4, width = 7, command = impartire)
b_egal = Button(aplicatie, text = '=', height = 4, width = 7, command = egal)
b_clear = Button(aplicatie, text = 'C', height = 4, width = 7, command = clear)
b_0 = Button(aplicatie, text = '0', height = 4, width = 7, command = lambda : clic(0))

#-----------------------------------------# aratarea butoanelor in fereastra

ecran.grid(row = 1, columnspan = 4, ipady = 17)
b_plus.grid(row = 2)
b1.grid(row = 2, column = 1)
b2.grid(row = 2, column = 2)
b3.grid(row = 2, column = 3)
b_minus.grid(row = 3)
b4.grid(row = 3, column = 1)
b5.grid(row = 3, column = 2)
b6.grid(row = 3, column = 3)
b_inmultit.grid(row = 4)
b7.grid(row = 4, column = 1)
b8.grid(row = 4, column = 2)
b9.grid(row = 4, column = 3)
b_impartit.grid(row = 5)
b_egal.grid(row = 5, column = 1)
b_clear.grid(row = 5, column = 2)
b_0.grid(row = 5, column = 3)


aplicatie.mainloop()