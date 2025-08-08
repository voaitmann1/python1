from FormGridGUI_py2 import *

frame_a = tk.Frame(master=window,  relief=tk.RIDGE)
frame_b = tk.Frame(master=window)
frame_c = tk.Frame(master=window, relief=tk.GROOVE)
 
label_a = tk.Label(master=frame_a, text="I'm in Frame A", relief=tk.SUNKEN)
label_a.pack()
 
size=TableSize(4,4)
ActiveCell=TableSize(1,1)
ActiveCell=TableSize(2,2)
headerSize=TableSize(1,1)

Align_Left1Top2Bottom3Right4=0
DfltWidth=20
rowOrder_LC0_CL1=0 #rowOrder_LC0_CL1=1
sourceOrder_LC0_CL1=0
contentSize=TableSize(len(dataSource),len(dataSource[0]))

grid =    TableView(frame_b, tk,        TableSize(len(dataSource),len(dataSource[0])), headerSize, ActiveCell, Align_Left1Top2Bottom3Right4,   DfltWidth, rowOrder_LC0_CL1, dataSource, sourceOrder_LC0_CL1)

label_c = tk.Label(master=frame_c, text="I'm in Frame C", relief=tk.GROOVE)
label_c.pack()
 
#frame_a.pack(side=LEFT, expand=YES, fill=X)
#frame_b.pack(expand=YES, fill=BOTH)
#frame_c.pack(side=BOTTOM,  relief=tk.SUNKEN, expand=YES, fill=X)
frame_a.pack(expand=tk.YES, fill=tk.X)
frame_b.pack(expand=tk.YES, fill=tk.BOTH)
frame_c.pack(expand=tk.YES, fill=tk.X)

label_c.config(relief=tk.SUNKEN)

#grid.grid.ShowConsole()
 
window.mainloop()
