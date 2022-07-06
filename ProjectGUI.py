
from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import messagebox
import webbrowser
import os 
import sys 
pro = Tk()
pro.geometry('800x450+280+50') #geometry is for size 
pro.resizable(False,False) #we can't edit the size 
pro.title("SUMMER TRUCK") 
pro.iconbitmap("/Users/reemaalameer/Desktop/icon.ico")
title=Label(pro, text='ICE CREAM Truck System',fg='#FADCE4',bg= '#9DD2D8',font=('tajawal',16,'bold'))
title.pack(fill=X)


F1=Frame(pro,width=300, height=440,bg='#FFB5CC')
F1.place(x=500,y=24)


B1=Button(F1, text='MENU',width=26,fg='#9DD2D8',bg='#FFB5CC',font=('tajawal',16,'bold'))
B1.place(x=0,y=120)

B2=Button(F1, text='ICE CREAM',width=26,fg='#FFB5CC',bg='#FFB5CC',font=('tajawal',16,'bold'))
B2.place(x=0,y=150)

B3=Button(F1, text='DRINKS',width=26,fg='#FFB5CC',bg='#FFB5CC',font=('tajawal',16,'bold'))
B3.place(x=0,y=180)

B4=Button(F1, text='SNACKS',width=26,fg='#FFB5CC',bg='#FFB5CC',font=('tajawal',16,'bold'))
B4.place(x=0,y=210)
#frame2
F2=Frame(pro,width=570, height=120,bg='#FFB5CC')
F2.place(x=0,y=330)

L1=Label(F2, text='USERNAME',fg='#9DD2D8',bg='#FFB5CC',font=('tajawal',16,'bold'))
L1.place(x=290,y=25)

L2=Label(F2, text='PASSWORD',fg='#9DD2D8',bg='#FFB5CC',font=('tajawal',16,'bold'))
L2.place(x=290,y=70)

En1=Entry(F2, font=('tajawal',12),justify='center')
En1.place(x=110,y=26)

En2=Entry(F2, font=('tajawal',12),justify='center')
En2.place(x=110,y=71)

B=Button(F2,text='Sign in',fg='#FFB5CC',bg= '#9DD2D8',font=('tajawal',12),width=8,height=4)
B.place(x=6,y=27)

#person photo
photo1 =PhotoImage(file="/Users/reemaalameer/Desktop/person.png")
imo1 =Label(pro,image=photo1)
imo1.place(x=390,y=335,width=110,height=110)


#car photo
photo =PhotoImage(file="/Users/reemaalameer/Desktop/ice.png")
imo =Label(pro,image=photo)
imo.place(x=0,y=24,width=500,height=310)


pro.mainloop()#must be in end of program