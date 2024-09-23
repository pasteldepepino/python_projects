from tkinter import *
#import modules
root=Tk()
root.title('calculadora')
root.geometry('500x400')
#set window configs
op=0
n1=0
var=StringVar()
box=Entry(root , textvariable=var)
box.grid(column=4 , row=0)
#set text box config
def funct0 ():
    box.insert(END , 0)
def funct1 ():
    box.insert(END , 1)
def funct2 ():
    box.insert(END , 2)
def funct3 ():
    box.insert(END , 3)
def funct4 ():
    box.insert(END , 4)
def funct5 ():
    box.insert(END , 5)
def funct6 ():
    box.insert(END , 6)
def funct7 ():
    box.insert(END , 7)
def funct8 ():
    box.insert(END , 8)
def funct9 ():
    box.insert(END , 9)
#set functions for number buttons
def functx ():
    global op,n1
    op=1
    n1=float(box.get())
    box.delete(0, END)
def functI ():
    global op,n1
    op=2
    n1=float(box.get())
    box.delete(0, END)
def functX ():
    global op,n1
    op=3
    n1=float(box.get())
    box.delete(0, END)
def functO ():
    global op,n1
    op=4
    n1=float(box.get())
    box.delete(0, END)
#set functions for operation buttons
def functC ():
    global n1,n2
    box.delete(0, END)
    n1=float(0)
    n2=float(0)
def functH ():
    global op,n1
    n2=float(box.get())
    n=float(n2)
    box.delete(0, END)
    if op == 1:
        box.insert(END , float(n1*n))
    elif op == 2:
        box.insert(END , float(n1-n))
    elif op == 3:
        box.insert(END , float(n1+n2))
    elif op == 4:
        box.insert(END , float(n1/n))
#set functions for = and C buttons
button0=Button(root , text=0 , command=funct0)
button0.grid(column=0 , row=2)     
button1=Button(root , text=1 , command=funct1)
button1.grid(column=1 , row=2)
button2=Button(root , text=2, command=funct2)
button2.grid(column=2 , row=2)
button3=Button(root , text=3 , command=funct3)
button3.grid(column=0 , row=3)
button4=Button(root , text=4 , command=funct4)
button4.grid(column=1 , row=3)
button5=Button(root , text=5 , command=funct5)
button5.grid(column=2 , row=3)
button6=Button(root , text=6 , command=funct6)
button6.grid(column=0 , row=4)
button7=Button(root , text=7 , command=funct7)
button7.grid(column=1 , row=4)
button8=Button(root , text=8 , command=funct8)
button8.grid(column=2 , row=4)
button9=Button(root , text=9 , command=funct9)
button9.grid(column=0 , row=5)
#create and config number buttons
buttonx=Button(root , text='x' , command=functx)
buttonx.grid(column=0 , row=6)
buttonI=Button(root , text='-' , command=functI)
buttonI.grid(column=1 , row=6)
buttonX=Button(root , text='+' , command=functX)
buttonX.grid(column=2 , row=6)
buttonO=Button(root , text='/' , command=functO)
buttonO.grid(column=3 , row=6)
#create and config operation buttons
buttonC=Button(root , text='C' , command=functC)
buttonC.grid(column=0 , row=7)
buttonH=Button(root , text='=' , command=functH)
buttonH.grid(column=1 , row=7)
#create and config C and = buttons
root.mainloop()
