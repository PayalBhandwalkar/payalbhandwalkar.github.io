from Tkinter import*
from Tkinter import ttk
import random
import Tkinter.messagebox
from datetime import datetime


class Customer:
    def __init__(self,roo):
        self.root = root
        self.root.title("Customer Billing system")
        self.root.geometry("1350x750+0+0")
        self.root.config(background="powder blue")

        ABC =Frame(self.root, bg="powder blue", bd=20 ,relif=RIDGE)
        ABC.grid()
        ABC1 =Frame(ABC,bd=14, width=1350,height=100,padx=10,relif=RIDGE,bg="powder blue")
        ABC1.grid(row=0,column=0,columnspan=4,sticky=W)
        ABC2 =Frame(ABC,bd=14, width=450,height=488,padx=10,relif=RIDGE,bg="cadet blue")
        ABC2.grid(row=1,column=0,sticky=W)
        ABC3 =Frame(ABC,bd=14, width=450,height=488,padx=10,relif=RIDGE,bg="powder blue")
        ABC3.grid(row=1,column=1,sticky=W)
        ABC4 =Frame(ABC,bd=14, width=460,height=488,padx=10,relif=RIDGE,bg="cadet blue")
        ABC4.grid(row=1,column=2,sticky=W)
        ABC5 =Frame(ABC4, bd=14, width=370,height=340,padx=10,relif=RIDGE,bg="cadet blue")
        ABC5.grid(row=0,column=0,sticky=W)
        ABC6 =Frame(ABC4, bd=14, width=370,height=120,padx=10,relif=RIDGE,bg="cadet blue")
        ABC6.grid(row=1,column=0,columnspan=4,sticky=W)

        Date1 = stringVar()
        Time1 = stringVar()
        Date1.set(time.strftime("%D/%m/%y"))
        Time1.set(time.strftime("%H:%M:%S"))

        self.lblTitle=Label(ABC1, textvariable=Date1,font=('arial',30,'bold'),
                    pady=9,bd=5,bg="cadet blue",fg="Cornsilk").grid(row=0,column=0)

        self.lblTitle=Label(ABC1, text="\tCustomer Billing Systems\t\t",font=('arial',30,'bold'),
                     pady=9,bd=5,bg="cadet blue",fg="Cornsilk",justify=CENTER).grid(row=0,column=1)
        
        self.lblTitle=Label(ABC1, textvariable=Time1,font=('arial',30,'bold'),
                     pady=9,bd=5,bg="cadet blue",fg="Cornsilk").grid(row=0,column=2)

 #=====================================================================================
   
#========================================================================================

#=========================================================================================
 if __name__ =='__main__':
     root = Tk() 
     application = Customer(root)  
     root.mainloop()


