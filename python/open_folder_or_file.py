# coding: utf-8
from tkinter import *
import os 
 
aie = Tk()
 
 
def form1():
    os.startfile("\\\\10.10.27.106\commun\z instal Logiciels") 
 
 
B1 = Button(aie, text='Form1', command=form1)
B1.pack()
aie.mainloop()