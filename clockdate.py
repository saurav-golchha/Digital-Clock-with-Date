#Importing all required modules
from tkinter import *
from tkinter.ttk import *
from time import strftime
import datetime as dt

#creating tkinter window
root=Tk()
root.title("Digital Clock & Date")

#defining time function to display time on the Label
def time():
    str=StringVar()
    str=strftime('%H:%M:%S %p')
    l.config(text = str)
    l.after(1000, time)
l=Label(root,font=("calibri",40,"bold"), background="red", foreground="white")
l.pack(anchor='n')
time()

#defining day function to display date on the Label
def day():
    d=dt.date.today()
    d1=d.strftime("%d-%m-%Y")
    l1.config(text=d1)
l1=Label(root,font=("calibri",28,"bold"), background="blue", foreground="white")
l1.pack(anchor='s')
day()

mainloop()
