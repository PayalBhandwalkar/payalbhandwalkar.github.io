from tkinter import *

window=Tk()
window.geometry("700x500")

def calculate():
    aalo_paratha=e1.get()
    samosa=e2.get()
    fried_rice=e3.get()
    pani_puri=e4.get()
    vada_pav=e5.get()
    Tea=e6.get()
    print(type(tea))
    total=(int(aalo_paratha)*30),(int(samosa)*12),(int(fried_rice)*40),(int(pani_puri)*20),
           (int(vada_pav)*15),(int(Tea)*10)
    label16=Label(window,text="total",font="times 28 bold")
    label16.place(x=100,y=360)


label8=Label(window,text="BILLING SYSTEM",font="times 30 bold")
label8.place(x=550,y=70)

#---------------------menu selection----------------------------------

label1=Label(window,text="MENU",font="times 28 bold")
label1.place(x=550,y=70)

label2=Label(window,text="aalo paratha          Rs 30",font="times 28 bold")
label2.place(x=550,y=70)

label3=Label(window,text="samosa                Rs 12",font="times 28 bold")
label3.place(x=550,y=70)

label4=Label(window,text="pani puri             Rs 20",font="times 28 bold")
label4.place(x=550,y=70)

label5=Label(window,text="fried rice            Rs 40",font="times 28 bold")
label5.place(x=550,y=70)

label6=Label(window,text="vada pav              Rs 15",font="times 28 bold")
label6.place(x=550,y=70)

label7=Label(window,text="Tea                   Rs 10",font="times 28 bold")
label7.place(x=550,y=70)

#-----------------billing section----------------------------------

label9=Label(window,text="select the items",font="times 20 bold")
label9.place(x=70,y=70)

label10=Label(window,text="aalo paratha",font="times 18 bold")
label10.place(x=20,y=120)

e1=Entry(window)
e1.place(x=20,y=150)

label11=Label(window,text="samosa",font="times 18 bold")
label11.place(x=20,y=120)

e2=Entry(window)
e2.place(x=20,y=150)

label12=Label(window,text="pani puri",font="times 18 bold")
label12.place(x=20,y=120)

e3=Entry(window)
e3.place(x=20,y=150)

label13=Label(window,text="fried rice",font="times 18 bold")
label13.place(x=20,y=120)

e4=Entry(window)
e4.place(x=20,y=150)

label14=Label(window,text="vada pav",font="times 18 bold")
label14.place(x=20,y=120)

e5=Entry(window)
e5.place(x=20,y=150)

label15=Label(window,text="Tea",font="times 18 bold")
label15.place(x=20,y=120)

e6=Entry(window)
e6.place(x=20,y=150)


b2=Button(window,text= 'bill',width=20,command=calculate)
b2.place(x=100,y=300)



window.mainloop()
