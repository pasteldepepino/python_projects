from tkinter import *
root = Tk()
root.geometry('200x100')
root.title('Login')
#import the library and creates the tkinter window
lbusername=Label(root , text='username')
lbusername.grid(column=0 , row=0)
entusername=Entry(root)
entusername.grid(column=1 , row=0)
lbpassword=Label(root , text='password')
lbpassword.grid(column=0 , row=1)
entpassword=Entry(root)
entpassword.grid(column=1 , row=1)
#creates the labels and the entrys    
def functsignup ():
    root2=Toplevel()
    root2.geometry('200x100')
    root2.title('Sign-up')
    lbname=Label(root2 , text='name')
    lbname.grid(column=0 , row=0)
    entname=Entry(root2)
    entname.grid(column=1 , row=0)
    lbusername2=Label(root2 , text='username')
    lbusername2.grid(column=0 , row=1)
    entusername2=Entry(root2)
    entusername2.grid(column=1 , row=1)
    lbpassword2=Label(root2 , text='password')
    lbpassword2.grid(column=0 , row=2)
    entpassword2=Entry(root2)
    entpassword2.grid(column=1 , row=2)
    def btnsignup ():
        global name,username,password
        name=(entname.get())
        username=(entusername2.get())
        password=(entpassword2.get())
        entname.delete(0,END)
        entusername2.delete(0,END)
        entpassword2.delete(0,END)
        root2.geometry('430x100')
        lbanswer=Label(root2 , text='sing-in sucessfull, now close this window and login on the previous')
        lbanswer.grid(column=1 , row=3)
    btnsignup=Button(root2 , text='sign-up' , command=btnsignup)
    btnsignup.grid(column=0 , row=3)
    root2.mainloop()
def btnlogin ():
    global username,password,name
    if entusername.get()==username:
        if entpassword.get()==password:
            root3=Toplevel()
            lbsucess=Label(root3 , text='login sucessfull! welcome!')
            lbsucess.grid(column=0 , row=0)
            root3.mainloop()
    else:
        entusername.delete(0,END)
        entpassword.delete(0,END)
        entusername.insert(END,'incorrect')
        entpassword.insert(END,'incorrect')
#creates the functions for the buttons
login=Button(root , text='Login' , command=btnlogin)
login.grid(column=0 , row=3)
signup=Button(root , text='Sign-up' , command=functsignup)
signup.grid(column=1 , row=3)
#creates the buttons
root.mainloop()
