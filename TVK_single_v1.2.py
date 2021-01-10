# For converting .py to .exe
# pyinstaller --onefile -w 'TVK Data Tool v1.1.py'  
# pyinstaller --onefile --icon=SG.ico --clean TVK Data Tool_v1.py
## v2.0: for dual channels 
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
import os

timestr = time.strftime("%m%d%Y-%I%M%S%p")
file_path_TNU=0
############################ GUI calling files ####################
root=tk.Tk()
# root.geometry("450x350")
p1 = PhotoImage(file = 'SG.png') 
# Setting icon of master window 
root.iconphoto(False, p1) 
myFont = tk.font.Font(size=10)
L1 = Label(text="85\N{DEGREE SIGN}C")
#L1.place(x=25, y=100)
L1.grid(row=2,column=2)
L2 = Label(text="45\N{DEGREE SIGN}C")
#L2.place(x=25, y=200)
L2.grid(row=3,column=2)
L3 = Label(text="TNU")
L3.grid(row=4,column=2)
global ent1, ent2, ent3
ent1=tk.Entry(root,font=10)
ent1.grid(row=2,column=3)
ent1['font'] = myFont
ent2=tk.Entry(root,font=10)
ent2.grid(row=3,column=3)
ent2['font'] = myFont
ent3=tk.Entry(root,font=10)
ent3.grid(row=4,column=3)
ent3['font'] = myFont

def browsefunc_85():
    global file_path_85
    filename =tk.filedialog.askopenfilename()
    ent1.insert(tk.END, filename) # add this
    file_path_85 = filename
def browsefunc_45():
    global file_path_45
    filename =tk.filedialog.askopenfilename()
    ent2.insert(tk.END, filename) # add this
    file_path_45 = filename
def browsefunc_TNU():
    global file_path_TNU
    filename =tk.filedialog.askopenfilename()
    ent3.insert(tk.END, filename) # add this
    file_path_TNU = filename

root.title("TVK Data Tool")
b1=tk.Button(root,text="Browse",command=browsefunc_85)
b1.grid(row=2,column=6)
b1['font'] = myFont
b2=tk.Button(root,text="Browse",font=4,command=browsefunc_45)
b2.grid(row=3,column=6)
b2['font'] = myFont
b3=tk.Button(root,text="Browse",command=browsefunc_TNU)
b3.grid(row=4,column=6)
b3['font'] = myFont
button = tk.Button(root,text="Next",command=root.destroy) 
button.grid(row=5,column=3)
button['font'] = myFont

root.mainloop()
############### Main data process #########################
global f, TNU_94, TNU_60, fig, ax
d = os.path.dirname(__file__) # directory of script
folder = os.path.join(d, 'Log')
file_name = "Temparature Log"+timestr+".txt"
file = os.path.join(folder, file_name)
try:
    os.makedirs(folder)
except OSError:
    pass
f= open(file,"w+") # .txt file for the output # .txt file for the output
# Fixing bug of non importing data
try:
    file_path_45
except NameError:
    file_path_45 = None
    print("45 degree data was not input")
    sys.exit()
try:
    file_path_85
except NameError:
    file_path_85 = None
    print("85 degree data was not input")
    sys.exit()

# Data input
df_85 = xlrd.open_workbook(file_path_85) # Calling data from 85
df_45 = xlrd.open_workbook(file_path_45) # Calling data from 45
# Data processing
xl_85 = df_85.sheet_by_index(0)
xl_45 = df_45.sheet_by_index(0)

# pre-condition setting
time_delay = 170
t = int(time_delay/2)+1

####################### 85/45 Temp Ver ##########################
# 85
def Temp_Ver_85(xl_85,t):
    for i in range(7,xl_85.nrows):
        if xl_85.cell_value(i, 1)>84:
            if abs(xl_85.cell_value(i, 1)-xl_85.cell_value(i+1, 1))<0.5:
                temp_85 = xl_85.row_values(i+t)
                return temp_85
# 45
def Temp_Ver_45(xl_45,t):
    for i in range(7,xl_45.nrows):
        if xl_45.cell_value(i, 1)<46 and 44<xl_45.cell_value(i,1):
            if abs(xl_45.cell_value(i, 1)-xl_45.cell_value(i+1, 1)<0.5):
                temp_45 = xl_45.row_values(i+t)
                return temp_45

####################### TNU #####################################
def TNU_94(xl_TNU,t_TNU,n):
    trigger =0 # set a trigger for finishing the while loop
    for i in range(n,xl_TNU.nrows):
        if i+40/2 > xl_TNU.nrows: 
            trigger = 1
            temp_TNU_94 = xl_TNU.row_values(i)
            n_out = i
            return temp_TNU_94, n_out, trigger
        else:
            if xl_TNU.cell_value(i, 1)>93:
                if abs(xl_TNU.cell_value(i, 1)-xl_TNU.cell_value(i+1, 1))<0.5:
                    temp_TNU_94 = xl_TNU.row_values(i+t_TNU)
                    n_out = i+t_TNU
                    return temp_TNU_94, n_out, trigger


def TNU_60(xl_TNU,t_TNU,n):
    trigger = 0
    for i in range(n,xl_TNU.nrows):
        if i+40/2 > xl_TNU.nrows:
            trigger = 1
            temp_TNU_60 = xl_TNU.row_values(i)
            n_out = i
            return temp_TNU_60, n_out, trigger
        else:
            if xl_TNU.cell_value(i, 1)<61 and 59<xl_TNU.cell_value(i, 1):
                if abs(xl_TNU.cell_value(i, 1)-xl_TNU.cell_value(i+1, 1))<0.5:
                    temp_TNU_60 = xl_TNU.row_values(i+t_TNU)
                    n_out = i+t_TNU
                    return temp_TNU_60, n_out, trigger

def TNU_function(file_path_TNU):
    # time for TNU
    time_delay_TNU = 30
    t_TNU = int(time_delay_TNU/2)+1
    # TNU data
    df_TNU = xlrd.open_workbook(file_path_TNU) # Calling data from 85
    xl_TNU = df_TNU.sheet_by_index(0)
    # TNU
    TNU_Data = []
    temp_94, n_out, trigger = TNU_94(xl_TNU,t_TNU,7)
    temp_Ave_94 = mean(temp_94[1:8])
    temp_TNU_94 = (max(temp_94[1:8])-min(temp_94[1:8]))/2
    temp_94.insert(1,temp_Ave_94)
    temp_94.insert(2,temp_TNU_94)
    TNU_Data.append(temp_94)
    f.write("TNU: \n")
    f.write("%s \n" % str(temp_94))
    while trigger==0:
        temp_60, n_out, trigger = TNU_60(xl_TNU,t_TNU,n_out)
        temp_Ave_60 = mean(temp_60[1:8])
        temp_TNU_60 = (max(temp_60[1:8])-min(temp_60[1:8]))/2
        temp_60.insert(1,temp_Ave_60)
        temp_60.insert(2,temp_TNU_60)
        if temp_Ave_60<61 and temp_Ave_60>59:
            TNU_Data.append(temp_60)
            f.write("%s \n" % str(temp_60))
        if trigger!=0:
            break
        temp_94, n_out, trigger = TNU_94(xl_TNU,t_TNU,n_out)
        temp_Ave_94 = mean(temp_94[1:8])
        temp_TNU_94 = (max(temp_94[1:8])-min(temp_94[1:8]))/2
        temp_94.insert(1,temp_Ave_94)
        temp_94.insert(2,temp_TNU_94)
        if temp_Ave_94>93:
            TNU_Data.append(temp_94)
            f.write("%s \n" % str(temp_94))
    f.close() 
    # Plot the TNU Data Table
    fig.patch.set_visible(False)
    ax[1].axis('off')
    ax[1].axis('tight')
    # Set the index and colums name
    mylist = ["94\N{DEGREE SIGN}C set point","60\N{DEGREE SIGN}C set point"]
    mylist1 = ["Average","TNU","Probe1 (A12)","Probe2 (H12)","Probe3 (C9)","Probe4 (F9)","Probe5 (C4)","Probe6 (F4)","Probe7 (A1)","Probe8 (H1)","Heated Cover"]
    if len(TNU_Data)>14:
        df = pd.DataFrame({"94":TNU_Data[12][1:12],"60":TNU_Data[13][1:12]},index = mylist1)
        df1 = df.round(2) # df round down to 2
        ax[1].table(cellText=df1.values, rowLabels = mylist1, colLabels=mylist, cellLoc ='center', loc='center')
        fig.tight_layout()
        ax[1].set_title('TNU Data Table')
    else:
        if (len(TNU_Data) %2) == 0:
            df = pd.DataFrame({"94":TNU_Data[len(TNU_Data)-2][1:12],"60":TNU_Data[len(TNU_Data)-1][1:12]},index = mylist1)
            df1 = df.round(2) # df round down to 2
            ax[1].table(cellText=df1.values, rowLabels = mylist1, colLabels=mylist, cellLoc ='center', loc='center')
            fig.tight_layout()
            ax[1].set_title('TNU Data Table')
        else:
            df = pd.DataFrame({"94":TNU_Data[len(TNU_Data)-1][1:12],"60":TNU_Data[len(TNU_Data)-2][1:12]},index = mylist1)
            df1 = df.round(2) # df round down to 2
            ax[1].table(cellText=df1.values, rowLabels = mylist1, colLabels=mylist, cellLoc ='center', loc='center')
            fig.tight_layout()
            ax[1].set_title('TNU Data Table')

################################### main writing to file  ###########################
# 85
temp_85 = Temp_Ver_85(xl_85,t)
temp_Ave_85 = mean(temp_85[1:8])
temp_TNU_85 = (max(temp_85[1:8])-min(temp_85[1:8]))/2
temp_85.insert(1,temp_Ave_85)
temp_85.insert(2,temp_TNU_85)
f.write("85C temp. ver: \n")
f.write("%s \n" % str(temp_85))
# 45
temp_45 = Temp_Ver_45(xl_45,t)
temp_Ave_45 = mean(temp_45[1:8])
temp_TNU_45 = (max(temp_45[1:8])-min(temp_45[1:8]))/2
temp_45.insert(1,temp_Ave_45)
temp_45.insert(2,temp_TNU_45)
f.write("45C temp. ver: \n")
f.write("%s \n" % str(temp_45))

# Plot the Data Table
fig, ax = plt.subplots(2, figsize=(6, 6))
fig.patch.set_visible(False)
ax[0].axis('off')
ax[0].axis('tight')
# Set the index and colums name
mylist = ["85\N{DEGREE SIGN}C set point","45\N{DEGREE SIGN}C set point"]
mylist1 = ["Average","TNU","Probe1 (A12)","Probe2 (H12)","Probe3 (C9)","Probe4 (F9)","Probe5 (C4)","Probe6 (F4)","Probe7 (A1)","Probe8 (H1)"]

df = pd.DataFrame({"85":temp_85[1:11],"45":temp_45[1:11]},index = mylist1)
df1 = df.round(2) # df round down to 2

ax[0].table(cellText=df1.values, rowLabels = mylist1, colLabels=mylist, cellLoc ='center', loc='center')
ax[0].set_title('Temperature Calibration Verification Data Table')
fig.tight_layout()

## Doing this for temperature verification without importing TNU data
if file_path_TNU != 0:
    TNU_function(file_path_TNU)
else:
    f.close()
    img = mpimg.imread("SG1.png")
    ax[1].imshow(img)
    ax[1].axis('off')
    
plt.show()
