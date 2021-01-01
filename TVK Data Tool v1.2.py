# pyinstaller --onefile -w 'TVK Data Tool v1.2.py'
# pyinstaller --onefile -w --icon=SG.ico 'TVK Data Tool v1.2.py'
# cd C:\SeqGen\Python\TVK
import xlrd
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import easygui
import tkinter as tk
import time
from tkinter import *
from tkinter import filedialog
from statistics import mean

root=tk.Tk()
root.geometry("430x150") # This is the windows size
p1 = PhotoImage(file = 'SG.png') 
# Setting icon of master window 
root.iconphoto(False, p1)
myFont = tk.font.Font(size=10)
L1 = Label(text="Choose the block type of your measurment")
L1.place(x=90, y=30)
L1['font'] = myFont

def button(arg):
    if arg==1:
        root.destroy()
        exec(open("TVK_single_v1.2.py").read())
    if arg==2:
        root.destroy()
        exec(open("TVK_dual_v1.2.py").read())
    if arg==3:
        root.destroy()
        # exec(compile(open("TVK_dual_384_v1.2.py", "rb").read(), "TVK_dual_384_v1.2.py", 'exec'))
        exec(open("TVK_dual_384_v1.2.py").read())
    
root.title("TVK Data Tool")
b1=tk.Button(root,text="Single",command=lambda:button(1))
b1['font'] = myFont
b2=tk.Button(root,text="Dual",command=lambda:button(2))
b2['font'] = myFont
b3=tk.Button(root,text="Dual 384",command=lambda:button(3))
b3['font'] = myFont
b1.pack()
b1.place(x=35, y=80, bordermode=OUTSIDE, height=40, width=100)
b2.pack()
b2.place(x=165, y=80, bordermode=OUTSIDE, height=40, width=100)
b3.pack()
b3.place(x=295, y=80, bordermode=OUTSIDE, height=40, width=100)
root.mainloop()