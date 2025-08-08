import tkinter as tk
 
window = tk.Tk()

#QLines=5
#QColumns=4
#LineHeaders=1
#ColumnHeaders=1
#ActiveLineN=2
#ActiveColumnN=2


class TableSize:
    def __init__(self, L=1, C=1):
        self.L=L
        self.C=C

class TableGrid:
    def __init__(self, mstr, gui, size):
        for LineIndex in range(0,size.L+1):
            #frames[LineIndex]=f
            #del CurLineCells[:]
            f=gui.Frame(master=mstr)
            for ColIndex in range(0,size.C+1):
                #CurLineCells[LineIndex, ColIndex]=gui.Label(master=frames[LineIndex], text="B"+str(LineIndex+1)+str(ColIndex+1), relief=tk.RIDGE)
                MyText="B"+str(LineIndex+1)+str(ColIndex+1)
                #CurLineCells[ColIndex]=gui.Label(master=frames[LineIndex], text=MyText, relief=tk.RIDGE)
                CurLineCell=gui.Label(master=f, text=MyText, relief=tk.RIDGE)
                CurLineCell.pack(side=gui.LEFT)
            #CurLineCells[LineIndex, ColIndex].pack(side=GUI.LEFT)
            f.pack()

def ShowGrid(mstr, gui, size, active):
    for LineN in range(1,size.L+1):
        f=gui.Frame(master=mstr)
        f.pack()# even so S'possible!
        for ColN in range(1,size.C+1):
            MyText="B"+str(LineN)+str(ColN)
            if LineN==active.L and ColN==active.C:
                #CurLineCell=gui.Label(master=f, text=MyText, relief=tk.SUNKEN, background="blue")
                CurLineCell=gui.Label(master=f, text=MyText, relief=tk.SUNKEN)
            else:
                CurLineCell=gui.Label(master=f, text=MyText, relief=tk.RIDGE)
            CurLineCell.pack(side=gui.LEFT)
        #f.pack()#also works
        
 
frame_a = tk.Frame(master=window,  relief=tk.RIDGE)
frame_b = tk.Frame(master=window, relief=tk.GROOVE, )
frame_c = tk.Frame(master=window)
 
label_a = tk.Label(master=frame_a, text="I'm in Frame A", relief=tk.SUNKEN)
label_a.pack()
 
#label_b = tk.Label(master=frame_b, text="I'm in Frame B", relief=tk.RIDGE)
#label_b.pack()
#
#tbl=Table2x2(frame_b)

size=TableSize(3,3)
ActiveCell=TableSize(1,1)
ActiveCell=TableSize(1,1)

#tbl=TableGrid(frame_b,tk, size)#also works
ShowGrid(frame_b,tk, size, ActiveCell)

label_c = tk.Label(master=frame_c, text="I'm in Frame B", relief=tk.GROOVE)
label_c.pack()
 
#frame_a.pack(side=LEFT, expand=YES, fill=X)
#frame_b.pack(expand=YES, fill=BOTH)
#frame_c.pack(side=BOTTOM,  relief=tk.SUNKEN, expand=YES, fill=X)
frame_a.pack(expand=tk.YES, fill=tk.X)
frame_b.pack(expand=tk.YES, fill=tk.BOTH)
frame_c.pack(expand=tk.YES, fill=tk.X)
 
window.mainloop()



