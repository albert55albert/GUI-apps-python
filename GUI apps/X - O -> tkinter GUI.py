from tkinter import *

from tkinter import messagebox

aplicatie = Tk()

aplicatie.geometry('282x252')

aplicatie.title('X - O')

#----------------------------------------------#

def verificare():
    if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':
        messagebox.showinfo('', 'X a castigat !')
        aplicatie.destroy()
    elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X':
        messagebox.showinfo('', 'X a castigat !')
        aplicatie.destroy()
    elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X':
        messagebox.showinfo('', 'X a castigat !')
        aplicatie.destroy()
    elif b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X':
        messagebox.showinfo('', 'X a castigat !')
        aplicatie.destroy()
    elif b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':
        messagebox.showinfo('', 'X a castigat !')
        aplicatie.destroy()
    elif b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X':
        messagebox.showinfo('', 'X a castigat !')
        aplicatie.destroy()
    elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X':
        messagebox.showinfo('', 'X a castigat !')
        aplicatie.destroy()
    elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X':
        messagebox.showinfo('', 'X a castigat !')
        aplicatie.destroy()
    elif b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O':
        messagebox.showinfo('', 'O a castigat !')
        aplicatie.destroy()
    elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O':
        messagebox.showinfo('', 'O a castigat !')
        aplicatie.destroy()
    elif b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O':
        messagebox.showinfo('', 'O a castigat !')
        aplicatie.destroy()
    elif b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O':
        messagebox.showinfo('', 'O a castigat !')
        aplicatie.destroy()
    elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O':
        messagebox.showinfo('', 'O a castigat !')
        aplicatie.destroy()
    elif b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O':
        messagebox.showinfo('', 'O a castigat !')
        aplicatie.destroy()
    elif b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O':
        messagebox.showinfo('', 'O a castigat !')
        aplicatie.destroy()
    elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O':
        messagebox.showinfo('', 'O a castigat !')
        aplicatie.destroy()
    elif variabila == 9:
        messagebox.showinfo('', 'Egal !')
        aplicatie.destroy()
  

#----------------------------------------------#

variabila = 0


#alta metoda pentru a verifica egalul este sa verifici textul din fiecare buton.
#daca in toate butoanele scrie ceva atunci este egal


rand = 1

def clic1():
    global rand
    global variabila
    if b1['text'] == '':
        if rand == 1:
            rand = 2
            b1['text'] = 'X'
            variabila += 1
            verificare()
        elif rand == 2:
            rand = 1
            b1['text'] = 'O'
            variabila += 1
            verificare()
            

def clic2():
    global rand
    global variabila
    if b2['text'] == '':
        if rand == 1:
            rand = 2
            b2['text'] = 'X'
            variabila += 1
            verificare()
        elif rand == 2:
            rand = 1
            b2['text'] = 'O'
            variabila += 1
            verificare()

def clic3():
    global rand
    global variabila
    if b3['text'] == '':
        if rand == 1:
            rand = 2
            b3['text'] = 'X'
            variabila += 1
            verificare()
        elif rand == 2:
            rand = 1
            b3['text'] = 'O'
            variabila += 1
            verificare()

def clic4():
    global rand
    global variabila
    if b4['text'] == '':
        if rand == 1:
            rand = 2
            b4['text'] = 'X'
            variabila += 1
            verificare()
        elif rand == 2:
            rand = 1
            b4['text'] = 'O'
            variabila += 1
            verificare()

def clic5():
    global rand
    global variabila
    if b5['text'] == '':
        if rand == 1:
            rand = 2
            b5['text'] = 'X'
            variabila += 1
            verificare()
        elif rand == 2:
            rand = 1
            b5['text'] = 'O'
            variabila += 1
            verificare()

def clic6():
    global rand
    global variabila
    if b6['text'] == '':
        if rand == 1:
            rand = 2
            b6['text'] = 'X'
            variabila += 1
            verificare()
        elif rand == 2:
            rand = 1
            b6['text'] = 'O'
            variabila += 1
            verificare()

def clic7():
    global rand
    global variabila
    if b7['text'] == '':
        if rand == 1:
            rand = 2
            b7['text'] = 'X'
            variabila += 1
            verificare()
        elif rand == 2:
            rand = 1
            b7['text'] = 'O'
            variabila += 1
            verificare()

def clic8():
    global rand
    global variabila
    if b8['text'] == '':
        if rand == 1:
            rand = 2
            b8['text'] = 'X'
            variabila += 1
            verificare()
        elif rand == 2:
            rand = 1
            b8['text'] = 'O'
            variabila += 1
            verificare()

def clic9():
    global rand
    global variabila
    if b9['text'] == '':
        if rand == 1:
            rand = 2
            b9['text'] = 'X'
            variabila += 1
            verificare()
        elif rand == 2:
            rand = 1
            b9['text'] = 'O'
            variabila += 1
            verificare()


        


#---------------------------------------------------#

b1 = Button(aplicatie, text = '', fg = 'green', height = 5, width = 10, command = clic1)
b2 = Button(aplicatie, text = '', fg = 'green', height = 5, width = 10, command = clic2)
b3 = Button(aplicatie, text = '', fg = 'green', height = 5, width = 10, command = clic3)
b4 = Button(aplicatie, text = '', fg = 'green', height = 5, width = 10, command = clic4)
b5 = Button(aplicatie, text = '', fg = 'green', height = 5, width = 10, command = clic5)
b6 = Button(aplicatie, text = '', fg = 'green', height = 5, width = 10, command = clic6)
b7 = Button(aplicatie, text = '', fg = 'green', height = 5, width = 10, command = clic7)
b8 = Button(aplicatie, text = '', fg = 'green', height = 5, width = 10, command = clic8)
b9 = Button(aplicatie, text = '', fg = 'green', height = 5, width = 10, command = clic9)

b1.grid(row = 1)
b2.grid(row = 1, column = 1)
b3.grid(row = 1, column = 2)
b4.grid(row = 2)
b5.grid(row = 2, column = 1)
b6.grid(row = 2, column = 2)
b7.grid(row = 3)
b8.grid(row = 3, column = 1)
b9.grid(row = 3, column = 2)

aplicatie.mainloop()
