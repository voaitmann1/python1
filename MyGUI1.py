from Tkinter import *
import locale
# -*- coding: cp1251 -*-
#setlocale(LC_ALL,'')
#setlocale(cp1251)
locale.setlocale(locale.LC_ALL, '')# ne shouts ma ne works
 
root = Tk()

clicks = 0
 
 
def click_button(): #event handler button click
    global clicks
    clicks += 1
    root.title("Clicks {}".format(clicks))


root.title("Графическая программа на Python")
#root.title("GUI program on Python")
root.geometry("400x300+300+250")#widthxheight +X+Y

#btn = Button(text="Hello")
#btn.pack()
btn = Button(text="Hello",          # its text
             background="#555",     # background
             foreground="#ccc",     # text color
             padx="20",             # padding x from borders to contents
             pady="8",              # padding x from borders to contents
             font="16" ,             # font height
             command=click_button   # ref to function - event handler
             )
btn.pack()
 
root.mainloop() 