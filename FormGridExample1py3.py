#from Tkinter import *
##colors = [‘red’, ‘green’, ‘orange’, ‘white’, ‘yellow’, ‘blue’]
#colors = ['red', 'green', 'orange', 'white', 'yellow', 'blue']
#r = 0
#Button(text='Submit1', width=12).grid(row=0,column=0)
#Button(text='Submit1', width=12).grid(row=0,column=0)
##Button(text='Submit1', width=12).grid(row=0,column=0).grid(row=0,column=0)#NoneType obj ha no ttr grid
##Button(text='Submit1', width=12).grid(row=0,column=1).grid(row=0,column=0)
#Label(text='NearButton',  width=25).grid(row=r, column=1)
#for c in colors:
#    Label(text=c, relief=RIDGE, width=25).grid(row=r+1, column=0)
#    Entry(bg=c, relief=SUNKEN, width=50).grid(row=r+1, column=1)
#    Label(text="", relief=RIDGE, width=10).grid(row=r+1, column=2)
#    r += 1
#mainloop()
#from Tkinter import *
from tkinter import *
from tkinter import ttk
colors = ['red', 'green', 'orange', 'white', 'yellow', 'blue']
r=0
QInterfacelines=4
QDataLines=len(colors)
QAllLines=QInterfacelines+QDataLines
QInterfaceCols=4
QDataCols=1
if QInterfaceCols>QDataCols+1:
    MaxQCols=QInterfaceCols
else:
    MaxQCols=QDataCols+1
Label(text='Data:',  width=25).grid(row=0, column=0)
#Entry( relief=SUNKEN, width=50).grid(row=1, column=0)
Label(text='Source:',  width=25).grid(row=2, column=0)
#Entry( relief=SUNKEN, width=50).grid(row=3, column=0)
fontExample = ("Courier", 16, "bold")
comboExample = ttk.Combobox(
                            #app, 
                            values=[
                                    "January", 
                                    "February",
                                    "March",
                                    "April"],
                            font = fontExample)
#comboExample = ttk.Combobox(values=[
#                                    "January", 
#                                    "February",
#                                    "March",
#                                    "April"],
#                            font = fontExample).grid(row=3, column=0)
# ^ works gut
comboExample = ttk.Combobox(values=[
                                    "January", 
                                    "February",
                                    "March",
                                    "April"],
                            font = fontExample)
#comboExample = Combobox(values=[
#                                    "January", 
#                                    "February",
#                                    "March",
#                                    "April"],
#                            font = fontExample)
comboExample.grid(row=3, column=0)
comboExample.current(1)
comboExample1 = ttk.Combobox(values=colors,
                            font = fontExample)
#comboExample1 = Combobox(values=colors,
#                            font = fontExample)
comboExample1.grid(row=1, column=0)
comboExample1.current(1)
#
Button(text='AddLine', width=12).grid(row=0,column=1)
Button(text='InsLine', width=12).grid(row=1,column=1)
Button(text='DelLine', width=12).grid(row=2,column=1)
Label(text='',  width=25).grid(row=3, column=1)
#
Button(text='AddCol', width=12).grid(row=0,column=2)
Button(text='InsCole', width=12).grid(row=1,column=2)
Button(text='DelCol', width=12).grid(row=2,column=2)
Label(text='',  width=25).grid(row=3, column=2)
#
Button(text='AddBoth', width=12).grid(row=0,column=3)
Button(text='InsBothe', width=12).grid(row=1,column=3)
Button(text='DelBoth', width=12).grid(row=2,column=3)
Label(text='',  width=25).grid(row=3, column=3)
#
r=1
for c in colors:
    Label(text=c, relief=RIDGE, width=25).grid(row=r+QInterfacelines-1, column=0)
    Entry(bg=c, relief=SUNKEN, width=50).grid(row=r+QInterfacelines-1, column=1)
    Label(text="", relief=RIDGE, width=10).grid(row=r+QInterfacelines-1, column=2)
    r += 1
mainloop()

