from tkinter import *
from random import *
root=Tk()
root.geometry('400x400')
root.title('dices')
#imports tkinter and configs the window
label=Label(root , text='resultados')
label.grid(column=3 , row=0)
#cretes the labels to show the 'results' word
resposta=(0)
#define the variable resposta
lista4=[1,2,3,4]
lista6=[1,2,3,4,5,6]
lista8=[1,2,3,4,5,6,7,8]
lista10=[1,2,3,4,5,6,7,8,9,10]
lista12=[1,2,3,4,5,6,7,8,9,10,11,12]
lista20=[1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20]
#creates the lists for the dice numbers
def froll ():
    global resposta
    blank=Label(root , text='    ')
    blank.grid(column=3 , row=1)
    results=Label(root , text=resposta)
    results.grid(column=3 , row=1)
#creates te function to the dice rolling button
def f4 ():
    global resposta
    resposta=(choice(lista4))
def f6 ():
    global resposta
    resposta=(choice(lista6))
def f8 ():
    global resposta
    resposta=(choice(lista8))
def f10 ():
    global resposta
    resposta=(choice(lista10))
def f12 ():
    global resposta
    resposta=(choice(lista12))
def f20 ():
    global resposta
    resposta=(choice(lista20))
#creates the functions for the dice seletion buttons 
d4=Button(root , text='D4' , command=f4)
d4.grid(column=0 , row=0)
d6=Button(root , text='D6' , command=f6)
d6.grid(column=1 , row=0)
d8=Button(root , text='D8' , command=f8)
d8.grid(column=2 , row=0)
d10=Button(root , text='D10' , command=f10)
d10.grid(column=0 , row=1)
d12=Button(root , text='D12' , command=f12)
d12.grid(column=1 , row=1)
d20=Button(root , text='D20' , command=f20)
d20.grid(column=2 , row=1)
#creates and places the buttons for dice selection
roll=Button(root , text='roll dices' , command=froll)
roll.grid(column=0 , row=2)
#creates the button that roll the dices
