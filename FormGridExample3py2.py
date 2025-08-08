import Tkinter as tk
import copy

from PyStdVector import My1DArray
 
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
            MyNameText="bL"+str(LineN)+"C"+str(ColN)
            MyText="B"+str(LineN)+str(ColN)+" Name="+MyNameText
            #MyNameText="SL"+str(LineN)+"C"+str(ColN)#so err: widget name starts with uppercase letter
            if LineN==active.L and ColN==active.C:
                #CurLineCell=gui.Label(master=f, text=MyText, relief=tk.SUNKEN, background="blue")
                CurLineCell=gui.Label(master=f, name=MyNameText, text=MyText, relief=tk.SUNKEN)
            else:
                CurLineCell=gui.Label(master=f, name=MyNameText, text=MyText, relief=tk.RIDGE)
            CurLineCell.pack(side=gui.LEFT)
        #f.pack()#also works

class TableGridView:
    #
    def __init__(self, mstr, gui, contentSize, headerSize, activeRows, Align_Left1Top2Bottom3Right4=0, DfltWidth=40):
        self.gui=gui
        self.cntColFrames=[]
        self.cntCols=[]
        self.cellsOfContent=[]
        self.cellsOfLoCH=[]
        self.cellsOfCoLH=[]
        self.widthArray=[]
        self.QLines=contentSize.L
        self.QColumns=contentSize.C
        self.QLineHeaders=headerSize.L
        self.QColumnHeaders=headerSize.C
        self.ActiveLineN=activeRows.L
        self.ActiveColN=activeRows.C
        #
        #self.widthArray=copy.deepcopy(widthArray)
        for i in range(1, self.QColumns+1):
            self.widthArray.append(DfltWidth)
        #self.widthArray=copy.deepcopy(widthArray)
        #
        self.tableViewMainFrame=gui.Frame(master=mstr)#ja, inot fa it ine
        if Align_Left1Top2Bottom3Right4==1:
            self.tableViewMainFrame.pack(side=gui.LEFT)
        elif Align_Left1Top2Bottom3Right4==2:
            self.tableViewMainFrame.pack(side=gui.TOP)
        elif Align_Left1Top2Bottom3Right4==3:
            self.tableViewMainFrame.pack(side=gui.BOTTOM)
        elif Align_Left1Top2Bottom3Right4==3:
            self.tableViewMainFrame.pack(side=gui.RIGHT)
        else:
            self.tableViewMainFrame.pack()                       
        if self.QLineHeaders>0 and self.QColumnHeaders>0:
            self.cornerFrame=gui.Frame(master=self.tableViewMainFrame)
            self.cornerFrame.pack(side=gui.LEFT)
            self.colHeaderFrame=gui.Frame(master=self.tableViewMainFrame)
            self.colHeaderFrame.pack(side=gui.LEFT)
            self.lineHeaderFrame=gui.Frame(master=self.tableViewMainFrame)
            self.lineHeaderFrame.pack(side=gui.BOTTOM)
            self.contentFrame=gui.Frame(master=self.tableViewMainFrame)
            self.contentFrame.pack(side=gui.RIGHT)
        elif self.QLineHeaders==0 and self.QColumnHeaders>0:
            #self.cornerFrame=gui.Frame(master=tableViewMainFrame)
            #self.cornerFrame.pack(side=gui.LEFT)
            self.colHeaderFrame=gui.Frame(master=self.tableViewMainFrame)
            self.colHeaderFrame.pack()
            #self.lineHeaderFrame=gui.Frame(master=tableViewMainFrame)
            #self.lineHeaderFrame.pack(side=gui.BOTTOM)
            self.contentFrame=gui.Frame(master=self.tableViewMainFrame)
            self.contentFrame.pack()
        elif self.QLineHeaders>0 and self.QColumnHeaders==0:
            #self.cornerFrame=gui.Frame(master=tableViewMainFrame)
            #self.cornerFrame.pack(side=gui.LEFT)
            #self.colHeaderFrame=gui.Frame(master=tableViewMainFrame)
            #self.colHeaderFrame.pack()
            self.lineHeaderFrame=gui.Frame(master=self.tableViewMainFrame)
            self.lineHeaderFrame.pack()
            self.contentFrame=gui.Frame(master=self.tableViewMainFrame)
            self.contentFrame.pack(side=gui.LEFT)
        else: #self.QLineHeaders==0 and self.QColumnHeaders==0:
            self.contentFrame=gui.Frame(master=self.tableViewMainFrame)
            self.contentFrame.pack()
        #
        self.Show()
    #            
    def Show(self):
        #curCntColFrame
        #curCntCol
        #curCntCell
        if self.QLineHeaders>0:
            #NOp
            zero=0
        if self.QColumnHeaders>0:
            #NOp
            zero=0
        #content cells
        curCntCol=[]
        #curCntColFrame=self.gui.Frame(master=self.contentFrame)#ce wa error
        for ColN in range(1, self.QColumns+1):
            curCntColFrame=self.gui.Frame(master=self.contentFrame)
            for LineN in range(1,self.QLines+1):
                MyNameText="cellContL"+str(LineN)+"C"+str(ColN)
                MyText="BL"+str(LineN)+"C"+str(ColN)+MyNameText
                if LineN==self.ActiveLineN and ColN==self.ActiveColN:
                    curCntCell=self.gui.Label(master=curCntColFrame, name=MyNameText, text=MyText, relief=tk.SUNKEN, width=self.widthArray[ColN-1])
                else:
                    curCntCell=self.gui.Label(master=curCntColFrame, name=MyNameText, text=MyText, relief=tk.RIDGE, width=self.widthArray[ColN-1])
                curCntCell.pack()
                #
                self.cntColFrames.append(curCntColFrame)
                #self.cntCols.append(curCntCell)
                curCntCol.append(curCntCell)
            #
            curCntColFrame.pack(side=self.gui.LEFT)
            #
            self.cntCols.append(curCntCol)
        #self
            
    #
    def getQLines(self):
        return self.QLines
    # 
    def getQColumns(self):
        return self.QColumns
    #
    #
    def getCurLineN(self):
        return self.ActiveLineN
    # 
    def getCurColumnN(self):
        return self.ActiveColN
    # 
    def SetCurLineN(self, N):
        if N>=1 and N<=self.QLines:
            self.ActiveLineN=N
    # 
    def SetCurColumnN(self, N):
        if N>=1 and N<=self.QColumns:
            self.ActiveColN=N
    #
    def SetCurRows(self, activeRows):
        if activeRows.C>=1 and activeRows.L>=1 and activeRows.L<=self.QLines and activeRows.C<=self.QColumns:
            self.ActiveColN=activeRows.C
            self.ActiveLinelN=activeRows.L
    #
    def GetCurRows(self):
        r=TableSize(self.ActiveLineN.L, self.ActiveColN)
        return r
    #
    def SetCurFirstCell(self):
        self.ActiveLineN=1
        self.ActiveColN=1
    #
    def SetCurLastCell(self):
        self.ActiveLineN=self.QLines
        self.ActiveColN=self.QColumns
    #
    def SetCurFirstLine(self):
        self.ActiveLineN=1
    #
    def SetCurLastLine(self):
        self.ActiveLineN=self.QLines
    #
    def SetCurFirstColumn(self):
        self.ActiveColeN=1
    #
    def SetCurLastColumn(self):
        self.ActiveColN=self.QColumns    
    
 
frame_a = tk.Frame(master=window,  relief=tk.RIDGE)
frame_b = tk.Frame(master=window, relief=tk.GROOVE)
frame_c = tk.Frame(master=window)
 
label_a = tk.Label(master=frame_a, text="I'm in Frame A", relief=tk.SUNKEN)
label_a.pack()
 
#label_b = tk.Label(master=frame_b, text="I'm in Frame B", relief=tk.RIDGE)
#label_b.pack()


size=TableSize(4,4)
ActiveCell=TableSize(1,1)
ActiveCell=TableSize(2,2)
headerSize=TableSize(1,1)

Align_Left1Top2Bottom3Right4=0
DfltWidth=10

#def __init__(self, mstr,   gui, contentSize, headerSize, activeRows, Align_Left1Top2Bottom3Right4=0, DfltWidth=40)
#
grid =    TableGridView(frame_b, tk,        size, headerSize, ActiveCell, Align_Left1Top2Bottom3Right4,   DfltWidth)
#

#tbl=TableGrid(frame_b,tk, size)#also works
#
#ShowGrid(frame_b,tk, size, ActiveCell)
#
grid.Show()
#

label_c = tk.Label(master=frame_c, text="I'm in Frame C", relief=tk.GROOVE)
label_c.pack()
 
#frame_a.pack(side=LEFT, expand=YES, fill=X)
#frame_b.pack(expand=YES, fill=BOTH)
#frame_c.pack(side=BOTTOM,  relief=tk.SUNKEN, expand=YES, fill=X)
frame_a.pack(expand=tk.YES, fill=tk.X)
frame_b.pack(expand=tk.YES, fill=tk.BOTH)
frame_c.pack(expand=tk.YES, fill=tk.X)

label_c.config(relief=tk.SUNKEN)
 
window.mainloop()



