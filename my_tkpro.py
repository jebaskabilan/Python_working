from tkinter import *
from PIL import ImageTk, Image
import os

class application:

    def __init__(self,root):
        self.root=root
        self.my_frame()
        self.my_home()
        self.my_new()
        self.my_search()
        self.my_delete()
        

    def my_frame(self):
        #set title window
        self.root.title("Product")
        #set pixel
        self.root.geometry("800x400")
        #create frame
        self.f1 = Frame(self.root,height=802,width=800,bg='sky blue',highlightbackground="black",highlightthickness=1)       #Right Frame
        self.f1.place(x=800,y=0)
        self.f3 = Frame(self.root,height=802,width=800,bg='sky blue',highlightbackground="gray",highlightthickness=1)       #L sub Frame - button
        self.f3.place(x=200,y=30)

        self.f2=Frame(self.root,height=700,width=200,bg='blue',highlightbackground="gray",highlightthickness=1)
        self.f2.place(x=0,y=0)

    def my_home(self):
        self.img1=ImageTk.PhotoImage(Image.open("homelogo007.png"))
        b1=Button(self.f2,image=self.img1,bd=0,cursor="hand2",compound="left",command=self.my_home,relief=SUNKEN,bg='blue')
        b1.place(x=30,y=0)

    def my_newfun(self):
        #labels
        self.id=Label(self.f3,text=" Id ",font=("Helvetica",10,"bold"))
        self.name=Label(self.f3,text=" Name ",font=("Helvetica",10,"bold"))
        self.subid=Label(self.f3,text=" Sub Id ",font=("Helvetica",10,"bold"))
        self.mrp=Label(self.f3,text=" MRP ",font=("Helvetica",10,"bold"))
        self.unit=Label(self.f3,text=" Unit ",font=("Helvetica",10,"bold"))
        self.uom=Label(self.f3,text=" Uom ",font=("Helvetica",10,"bold"))
        self.rate=Label(self.f3,text=" Rate  ",font=("Helvetica",10,"bold"))
        self.tax=Label(self.f3,text=" Tax ",font=("Helvetica",10,"bold"))
        #Labels Layout
        self.id.grid(row=0,column=0,padx=10,pady=10)
        self.name.grid(row=1,column=0,padx=10,pady=10)
        self.subid.grid(row=2,column=0,padx=10,pady=10)
        self.mrp.grid(row=3,column=0,padx=10,pady=10)
        self.unit.grid(row=4,column=0,padx=10,pady=10)
        self.uom.grid(row=5,column=0,padx=10,pady=10)
        self.rate.grid(row=6,column=0,padx=10,pady=10)
        self.tax.grid(row=7,column=0,padx=10,pady=10)
        #Entries
        self.e1=Entry(self.f3,font=("15"),width=10,justify="center",fg="#1c1c1b",highlightbackground="black",highlightthickness=1)
        self.e2=Entry(self.f3,font=("15"),width=10,justify="center",fg="#1c1c1b",highlightbackground="black",highlightthickness=1)
        self.e3=Entry(self.f3,font=("15"),width=10,justify="center",fg="#1c1c1b",highlightbackground="black",highlightthickness=1)
        self.e4=Entry(self.f3,font=("15"),width=10,justify="center",fg="#1c1c1b",highlightbackground="black",highlightthickness=1)
        self.e5=Entry(self.f3,font=("15"),width=10,justify="center",fg="#1c1c1b",highlightbackground="black",highlightthickness=1)
        self.e6=Entry(self.f3,font=("15"),width=10,justify="center",fg="#1c1c1b",highlightbackground="black",highlightthickness=1)
        self.e7=Entry(self.f3,font=("15"),width=10,justify="center",fg="#1c1c1b",highlightbackground="black",highlightthickness=1)
        self.e8=Entry(self.f3,font=("15"),width=10,justify="center",fg="#1c1c1b",highlightbackground="black",highlightthickness=1)


    def my_new(self):    
        self.img2=ImageTk.PhotoImage(Image.open("ins1.png"))
        b2=Button(self.f2,text="New",image=self.img2,bd=0,cursor="hand2",compound="left",command=self.my_newfun,relief=SUNKEN,bg='blue')
        b2.place(x=30,y=150)
            
    def my_search(self):
        self.img3=ImageTk.PhotoImage(Image.open("vw.png"))
        b3=Button(self.f2,text="Search",image=self.img3,bd=0,cursor="hand2",compound="left",command=self.my_search,relief=SUNKEN,bg='blue')
        b3.place(x=30,y=250)

    def my_delete(self):
        self.img4=ImageTk.PhotoImage(Image.open("del.png"))
        b4=Button(self.f2,text="Delete",image=self.img4,bd=0,cursor="hand2",compound="left",command=self.my_delete,relief=SUNKEN,bg='blue')
        b4.place(x=30,y=350)
        

   
        
    



root=Tk()



app=application(root)
root.mainloop()