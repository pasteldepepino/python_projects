from tkinter import *
from random import *
import os
root=Tk()
root.geometry('228x300')
root.title('clicker')
root.resizable(width=False, height=False)
points=0
bght1=(0)
def btn1f ():
    global points
    points=points+1
    lb1=Label(root , text=points)
    lb1.grid(column=0 , row=1)
    print(points)
def btn3f ():
    global points , bght1
    if points >= 200:
        if bght1 == 0:
            points=points-200
            lb1=Label(root , text=points)
            lb1.grid(column=0 , row=1)
            def btn12f ():
                global points
                points=points+2
                lb1=Label(root , text=points)
                lb1.grid(column=0 , row=1)
                print(points)
        else:
            print('powerup already bought')
            root3=Toplevel()
            root3.resizable(width=False, height=False)
            lbalrdbght=Label(root3 , text='powerup already bought!')
            lbalrdbght.grid(column=0 , row=0)
        bght1=1
        btn1=Button(root , text='click here!' , command=btn12f)
        btn1.grid(column=0 , row=0)
    elif points < 200:
        if bght1 == 1:
            root3=Toplevel()
            root3.resizable(width=False, height=False)
            lbalrdbght=Label(root3 , text='powerup already bought!')
            lbalrdbght.grid(column=0 , row=0)
        else:
            print('ERROR: NOT ENUGH POINTS. YOU HAVE {}, AND 200 ARE REQUIRED' .format(points))
            root3=Toplevel()
            root3.resizable(width=False, height=False)
            lberro=Label(root3 , text='ERROR: NOT ENUGH POINTS. YOU HAVE {}, AND 200 ARE REQUIRED' .format(points))
            lberro.grid(column=0 , row=0)
def btn2f ():
    root2 = Toplevel()
    root2.geometry ('402x571')
    root2.title('store')
    root2.resizable(width=False, height=False)
    moneypath=os.path.join('money.png')
    money=PhotoImage(file=moneypath)
    lbmon=Label(root2, image=money)
    lbmon.place(x=0 , y=0)
    lbp=Label(root2 , text='|product|')
    lbp.grid(column=0 , row=0)
    lbpr=Label(root2 , text='|price|')
    lbpr.grid(column=1 , row=0)
    btn3=Button(root2 , text='2 pontos / click' , command=btn3f)
    btn3.grid(column=0 , row=1)
    lbfirstpowup=Label(root2 , text='200')
    lbfirstpowup.grid(column=1 , row=1)
    root2.mainloop()
btn1=Button(root , text='click here!' , command=btn1f)
btn1.grid(column=0 , row=0)
btn2=Button(root , text='store' , command=btn2f)
btn2.grid(column=0 , row=2)
image1path=os.path.join('botao.png')
image=PhotoImage(file=image1path)
labelo=Label(root , image=image)
labelo.grid(column=0 , row=3)
root.mainloop()
