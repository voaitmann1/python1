import Tkinter as tk
import ttk
import copy
#from tableController2 import *
from TableController2 import *
#from  TableController2 import *#copied filename
from TableInfoClasses import *


items_ChoosingCell=[
                              "Content cell", 
                              "Line of Col Header Cell",
                              "Col of Line Header Cell",
                              "Lines General Name",
                              "Columns General Name",
                              "Table Name",
                              "DB Field Name",
                              "DB Table Name",
                              "Joined Table Name",
                              "Joined Content Field Name",
                              "Joined Key Field Name",
                              "Cell Items",
                              "Field Items"
                            ]
items_ChoosingAction=[
                              "Focus at Cell",
                              "Compress Displayed",
                              "Expand Displayed",
                              "Shift Displayed",
                              "Rows Moving" , 
                              "Cells Moving",
                              "Rows Ins or Add",
                              "Rows Del",
                              "Rows Size",
                              "Text Size",
                              "Text in Cell"
                            ]
items_ChoosingInfo=[
                              "Cells Items",
                              "Representation in Table",
                              "Representation in Text",
                              "Ussage Policy",
                              "DB Table data",
                              "DB Fields data",
                              "Cells Types"
                            ]


#class TableSize:
#    def __init__(self, L=1, C=1):
#        if isinstance(L, int) and isinstance(C, int):
#            self.L=L
#            self.C=C
#        elif isinstance(L, list) and len(L)==2 and isinstance(L[1-1], int) and isinstance(L[2-1], int):
#            self.L=L[1-1]
#            self.C=L[2-1]
#    def ShowConsole(self):
#        print("L="+str(self.L)+" C="+str(self.C))#
#
#    def CorrectActiveCellNByShownRowsNs(self, RowsNsLims):
#        if self.L<RowsNsLims.L1:
#            self.L=RowsNsLims.L1
#        if self.L>RowsNsLims.L2:
#            self.L=RowsNsLims.L2
#        if self.C<RowsNsLims.C1:
#            self.C=RowsNsLims.C1
#        if self.C>RowsNsLims.C2:
#            self.C=RowsNsLims.C2
#
#class TRowsNsLims:
#    def __init__(self, L1=1, C1=1, L2=0, C2=0, tblSize=0):
#        self.L1=L1
#        self.C1=C1
#        if L1<1:
#            self.L1=1
#        if C1<1:
#            self.C1=1
#        if isinstance(tblSize, TableSize):
#            if L2==0 or L2<L1 or L2>tblSize.L:
#                self.L2=tblSize.L
#            else:
#                self.L2=L2
#            if C2==0 or C2<C1 or C2>tblSize.C:
#                self.C2=tblSize.C
#            else:
#                self.C2=C2
#        else:
#            self.L2=L1
#            self.C2=C1
#
#    def ContentGridLineNByTableLineN(self, TableLineN):
#        return TableLineN-self.L1+1
#
#    def TableLineNByContentGridLineN(self, GridLineN):
#        return GridLineN+self.L1-1#
#
#    def ContentGridColNByTableColN(self, TableColN):
#        return TableColN-self.L1+1
#
#    def TableColNByContentGridColN(self, GridColN):
#        return GridColN+self.L1-1
#
#    def Correct(self, tblSize=0):
#        if isinstance(tblSize, TableSize):
#            if self.L2>tblSize.L:#so if 0
#                self.L2=tblSize.L
#            if self.C2>tblSize.C:#so if 0
#                self.C2=tblSize.C
#        if self.L1>self.L2:
#            self.L1=self.L2
#        if self.C1>self.C2:
#            self.C1=self.C2
#        if self.L1<1:
#            self.L1=1
#        if self.C1<1:
#            self.C1=1
#
#    def AddNextLine(self, tblSize=0):
#        if not (isinstance(tblSize, TableSize) and self.L2>=tblSize.L):
#            self.L2=self.L2+1
#        self.Correct(tblSize)
#
#    def AddPrevLine(self, tblSize=0):
#        if self.L1>1:
#            self.L1=self.L1-1
#        self.Correct(tblSize)
#
#    def AddNextColumn(self, tblSize=0):
#        if not (isinstance(tblSize, TableSize) and self.C2>=tblSize.C):
#            self.C2=self.C2+1
#        self.Correct(tblSize)
#
#    def AddPrevColumn(self, tblSize=0):
#        if self.C1>1:
#            self.C1=self.C1-1
#        self.Correct(tblSize)
#
#    def DelNextLine(self, tblSize=0):
#        if not (self.L2<=self.L1):
#            self.L2=self.L2-1
#        self.Correct(tblSize)
#
#    def DelPrevLine(self, tblSize=0):
#        if not(self.L1>=self.L2):
#            self.L1=self.L1+1
#        self.Correct(tblSize)
#
#    def DelNextColumn(self, tblSize=0):
#        if not(self.C2<=self.C1):
#            self.C2=self.C2-1
#        self.Correct(tblSize)
#
#    def DelPrevColumn(self, tblSize=0):
#        if not(self.C1>=self.C2):
#            self.C1=self.C1+1
#        self.Correct(tblSize)
#
#    def ShiftLinesToNext(self, tblSize=0):
#        if not (isinstance(tblSize, TableSize) and self.L2>=tblSize.L):
#            self.L2=self.L2+1
#            self.L1=self.L1+1
#        self.Correct(tblSize)
#
#    def ShiftLinesToPrev(self, tblSize=0):
#        if self.L1>1:
#            self.L1=self.L1-1
#            self.L1=self.L1-1
#        self.Correct(tblSize)
#
#    def ShiftColumnsToNext(self, tblSize=0):
#        if not (isinstance(tblSize, TableSize) and self.C2>=tblSize.C):
#            self.C2=self.C2+1
#            self.C1=self.C1+1
#        self.Correct(tblSize)
#
#    def ShiftColumnsToPrev(self, tblSize=0):
#        if self.C1>1:
#            self.C1=self.C1-1
#            self.C2=self.C2-1
#        self.Correct(tblSize)
#
#    def SetFirst(self):
#        self.L1=1
#        self.C1=1
#        self.L2=self.L1
#        self.C2=self.C1
#        #self.Correct(tblSize)
#
#    def SetFull(self, tblSize=0):
#        self.SetFirst()
#        if isinstance(tblSize, TableSize):
#            self.L2=tblSize.L
#            self.C2=tblSize.C
#        self.Correct(tblSize)
#            

#class TableCell:
#    def __init__(self, mstr, gui, coords, outerText, partOf_LC0_CL1, isActive=0):
#        self.Name=self.SetCoords(coords)
#        self.cell=gui.Label(master=mstr, name=Name, text=outerText)
#        if partOf_LC0_CL1==0:
#            self.cell.pack(side=gui.LEFT)
#        else:
#            self.cell.pack()
#    def getLineN(self):
#        Name=self.cell["name"]
#        LPart=Name[6-1,10]
#        N=int(LPart)
#        return N
#    def getColN(self):
#        Name=self.cell["name"]
#        CPart=Name[10-1,14]
#        N=int(CPart)
#        return N
#    def SetCoords(coords):
#        Name="contL"
#        if coords.L<10:
#            Name=Name+"000"
#        elif  coords.L<100:
#           Name=Name+"00"
#        elif coords.L<1000:
#            Name=Name+"0"
#        Name=Name+str(coords.L)
#        Name=Name+"C"
#        if coords.C<10:
#            Name=Name+"000"
#        elif  coords.C<100:
#            Name=Name+"00"
#        elif coords.C<1000:
#            Name=Name+"0"
#        Name=Name+str(coords.C)
#        return Name
        

#class TableGrid:
#    def __init__(self, mstr, gui, size):
#        for LineIndex in range(0,size.L+1):
#            #frames[LineIndex]=f
#            #del CurLineCells[:]
#            f=gui.Frame(master=mstr)
#            for ColIndex in range(0,size.C+1):
#                #CurLineCells[LineIndex, ColIndex]=gui.Label(master=frames[LineIndex], text="B"+str(LineIndex+1)+str(ColIndex+1), relief=tk.RIDGE)
#                MyText="B"+str(LineIndex+1)+str(ColIndex+1)
#                #CurLineCells[ColIndex]=gui.Label(master=frames[LineIndex], text=MyText, relief=tk.RIDGE)
#                CurLineCell=gui.Label(master=f, text=MyText, relief=tk.RIDGE)
#                CurLineCell.pack(side=gui.LEFT)
#            #CurLineCells[LineIndex, ColIndex].pack(side=GUI.LEFT)
#            f.pack()

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
    def __init__(self, mstr, gui, curTable, tblInf, GuiControls, rowsNsLimsToDispl, activeRows=0, DfltWidth=40, tblView=0):
        self.gui=gui
        self.tblView=tblView
        #self.rowOrder_LC0_CL1=rowOrder_LC0_CL1
        self.cntRowFrames=[]
        self.cntRows=[]
        self.cellsOfContent=[]
        self.cellsOfLoCH=[]
        self.cellsOfCoLH=[]
        self.widthArray=[]
        #
        vsh=1
        #
        if isinstance(tblInf, TableInfo1) and  isinstance(tblInf.ussagePolicy, TableUssagePolicy):
            self.ussagePolicy=copy.deepcopy(tblInf.ussagePolicy)
        else:
            self.ussagePolicy=TableUssagePolicy()
        if isinstance(tblInf, TableInfo1) and  isinstance(tblInf.repr, TableRepr):
            self.repr=copy.deepcopy(tblInf.repr)
            if vsh==1:
                print("repr accepted")
        else:
            self.repr=TableRepr()# if ne ecri ce - error: TableGridView has no attr repr
            if vsh==1:
                print("repr - created, ob nil given")
            self.repr.SetAsSimple()
            #self.repr.SetAsSimpleNumerated(1,1,1,1,1,1)
        if vsh==1:
            self.repr.ShowToConsole()
            print("")
        self.GuiControls=TableGUIControls()
        if isinstance(GuiControls, TableGUIControls):
            self.GuiControls=copy.deepcopy(GuiControls)
        else:
            self.GuiControls=TableGUIControls()
        #
        self.sourceOrder_LC0_CL1=curTable.GetStructRowOrderLC0CL1()
        self.contentSize=TableSize()
        self.contentSize.L=curTable.GetQLines()
        self.contentSize.C=curTable.GetQColumns()
        self. headerSize=TableSize()
        self.activeRows=TableSize()
        self.activeRows.L=1
        self.activeRows.C=1
        if activeRows!=[] and activeRows!=0:
            self.activeRows=copy.deepcopy(activeRows)
        #self.activeRows.CorrectActiveCellNByShownRowsNs(self.)#further
        if self.repr.GetIfLineOfColHeaderToShow()!=0 or curTable.GetIf_LineOfColHeaderExists()!=0:
           self. headerSize.C=1
        else:
           self. headerSize.C=0
        if self.repr.GetIfColOfLineHeaderToShow()!=0 or curTable.GetIf_ColOfLineHeaderExists()!=0:
           self. headerSize.L=1
        else:
           self. headerSize.L=0    
        #
        self.table=curTable#ja so, link
        print("Grid constructor: Size: QL="+str(self.contentSize.L)+" QC="+str(self.contentSize.C))
        print("Grid constructor - content size param:")
        self.contentSize.ShowConsole()
        #
        if isinstance(rowsNsLimsToDispl, TRowsNsLims):
            self.rowsNsLimsToDispl=copy.deepcopy(rowsNsLimsToDispl)
            if vsh==1:
                print("rowsNsLimsToDispl is TRowsNsLims")
        else:
            self.rowsNsLimsToDispl=TRowsNsLims()
            self.rowsNsLimsToDispl.SetFull(TableSize(self.table.GetQLines(), self.table.GetQColumns()))
            if vsh==1:
                print("rowsNsLimsToDispl is NOT TRowsNsLims")
        #self.activeRows.CorrectActiveCellNByShownRowsNs(self.rowsNsLimsToDispl)
        if vsh==1:
            print("Active rows: L="+str(self.activeRows.L)+" C="+str(self.activeRows.C))
            #print(
            #           "Rows to displ: L: "+str(self.rowsNsLimsToDispl.L1)+" ... "+str(self.rowsNsLimsToDispl.L2+" C: "+str(self.rowsNsLimsToDispl.C1)+" ... "+str(self.rowsNsLimsToDispl.C2)
            #    )
            if(self.activeRows.L<self.rowsNsLimsToDispl.L1):
                print("activeL<L1. Correcting...")
            if(self.activeRows.L>self.rowsNsLimsToDispl.L2):
                print("activeL<L2. Correcting...")
            if(self.activeRows.C<self.rowsNsLimsToDispl.C1):
                print("activeC<C1. Correcting...")
            if(self.activeRows.C>self.rowsNsLimsToDispl.C2):
                print("activeC<C2. Correcting...")
        while self.activeRows.L<self.rowsNsLimsToDispl.L1:
            self.rowsNsLimsToDispl.ShiftLinesToPrev(self.table.GetSize())
            if vsh==1:
                print("ShiftLinesToNext. activeL="+str(activeRows.L)+" Now L1="+str(self.rowsNsLimsToDispl.L1)+" L2="+str(self.rowsNsLimsToDispl.L2))
        while self.activeRows.L>self.rowsNsLimsToDispl.L2:
            self.rowsNsLimsToDispl.ShiftLinesToNext(self.table.GetSize())
            if vsh==1:
                print("ShiftLinesToPrev. activeL="+str(activeRows.L)+" Now L1="+str(self.rowsNsLimsToDispl.L1)+" L2="+str(self.rowsNsLimsToDispl.L2))
        while self.activeRows.C<self.rowsNsLimsToDispl.C1:
            self.rowsNsLimsToDispl.ShiftColumnsToPrev(self.table.GetSize())
            if vsh==1:
                print("ShiftLinesToNext. activeC="+str(activeRows.C)+" Now C1="+str(self.rowsNsLimsToDispl.C1)+" C2="+str(self.rowsNsLimsToDispl.C2))
        while self.activeRows.C>self.rowsNsLimsToDispl.C2:
            self.rowsNsLimsToDispl.ShifttColumnsToNext(self.table.GetSize())
            if vsh==1:
                print("ShiftLinesToPrev. activeC="+str(activeRows.C)+" Now C1="+str(self.rowsNsLimsToDispl.C1)+" C2="+str(self.rowsNsLimsToDispl.C2))
        #self.activeRows.CorrectActiveCellNByShownRowsNs(self.rowsNsLimsToDispl)
        #
        #
        for i in range(1, self.contentSize.C+1):
            self.widthArray.append(DfltWidth)
        #
        self.tableViewMainFrame=gui.Frame(master=mstr)#ja, inot fa it ine
        if self.GuiControls.Align_Left1Top2Bottom3Right4==1:
            self.tableViewMainFrame.pack(side=gui.LEFT)
        elif self.GuiControls.Align_Left1Top2Bottom3Right4==2:
            self.tableViewMainFrame.pack(side=gui.TOP)
        elif self.GuiControls.Align_Left1Top2Bottom3Right4==3:
            self.tableViewMainFrame.pack(side=gui.BOTTOM)
        elif self.GuiControls.Align_Left1Top2Bottom3Right4==3:
            self.tableViewMainFrame.pack(side=gui.RIGHT)
        else:
            self.tableViewMainFrame.pack()                       
        if self.headerSize.L>0 and self.headerSize.C>0: #other vrns s'ne checked et max likely ne work, ma ne needed
            self.upperHeaderFrame=gui.Frame(master=self.tableViewMainFrame)
            self.upperHeaderFrame.pack()
            self.cornerFrame=gui.Frame(master=self.upperHeaderFrame)
            self.cornerFrame.pack(side=gui.LEFT)
            self.colHeaderFrame=gui.Frame(master=self.upperHeaderFrame)
            self.colHeaderFrame.pack(side=gui.LEFT)
            self.contentWithLineHeaderFrame=gui.Frame(master=self.tableViewMainFrame)
            self.contentWithLineHeaderFrame.pack()
            self.lineHeaderFrame=gui.Frame(master=self.contentWithLineHeaderFrame)
            self.lineHeaderFrame.pack(side=gui.LEFT)
            self.contentFrame=gui.Frame(master=self.contentWithLineHeaderFrame)
            self.contentFrame.pack(side=gui.LEFT)
            #
            #below are vrns, at ic wa ac upperHeaderFrame et contentWithLineHeaderFrame:
            # erst - at ic cornerFrame (packed left), colHeaderFrame (packed left)
            # lineHeaderFrame (packed below em, ac side name), 
            #
            #self.cornerFrame=gui.Frame(master=self.tableViewMainFrame)
            #self.cornerFrame.pack(side=gui.LEFT)
            #self.colHeaderFrame=gui.Frame(master=self.tableViewMainFrame)
            #self.colHeaderFrame.pack(side=gui.LEFT)
            #self.lineHeaderFrame=gui.Frame(master=self.tableViewMainFrame)
            ##self.lineHeaderFrame.pack(side=gui.BOTTOM)
            #self.lineHeaderFrame.pack()
            #self.contentFrame=gui.Frame(master=self.tableViewMainFrame)
            ##self.contentFrame.pack(side=gui.RIGHT)
            #self.contentFrame.pack(side=gui.LEFT)
            #
            #self.cornerFrame=gui.Frame(master=self.tableViewMainFrame)
            #self.cornerFrame.pack(side=gui.LEFT)
            #self.lineHeaderFrame=gui.Frame(master=self.tableViewMainFrame)
            ##self.lineHeaderFrame.pack(side=gui.BOTTOM)
            #self.lineHeaderFrame.pack()
            #self.colHeaderFrame=gui.Frame(master=self.tableViewMainFrame)
            #self.colHeaderFrame.pack(side=gui.LEFT)
            #self.contentFrame=gui.Frame(master=self.tableViewMainFrame)
            ##self.contentFrame.pack(side=gui.RIGHT)
            #self.contentFrame.pack(side=gui.LEFT)
            
        elif self.headerSize.L==0 and self. headerSize.C>0:
            #self.cornerFrame=gui.Frame(master=tableViewMainFrame)
            #self.cornerFrame.pack(side=gui.LEFT)
            self.colHeaderFrame=gui.Frame(master=self.tableViewMainFrame)
            self.colHeaderFrame.pack()
            #self.lineHeaderFrame=gui.Frame(master=tableViewMainFrame)
            #self.lineHeaderFrame.pack(side=gui.BOTTOM)
            self.contentFrame=gui.Frame(master=self.tableViewMainFrame)
            self.contentFrame.pack()
        elif self. headerSize.L>0 and self. headerSize.C==0:
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
        #print("table given:")
        #self.table.ShowToConsole()
        #
        self.HandleCells()
    #            
    def HandleCells(self):
        #curCntRowFrame
        #curCntRow
        #curCntCell
        #
        vsh=1
        #
        #print("table given:")
        #self.table.ShowToConsole()#ja idem as in init()
        #
        print("given:  self.rowOrder_LC0_CL1=",  self.GuiControls.structRowOrder_LC0_CL1, " self.sourceOrder_LC0_CL1=",  self.sourceOrder_LC0_CL1)
        #if self.QLineHeaders>0:
        if self.headerSize.L>0:
            #NOp
            zero=0
        #if self.QColumnHeaders>0:
        if self.headerSize.C>0:
            #NOp
            zero=0
        #Header cells
        #if self.QLineHeaders>0 and self.QColumnHeaders>0:#define Corner, ma work nur by self.QLineHeaders==1 et self.QColumnHeaders==1
        if self.headerSize.L>0 and self.headerSize.C>0:#define Corner, ma work nur by self.QLineHeaders==1 et self.QColumnHeaders==1
            MyNameText="cornerCell"#self.table.GetCorner()#
            #MyText=self.table.GetCorner()#"L\C"
            MyText=self.table.ToString_HeaderCorner()#"L\C"
            cornerCell=self.gui.Label(master=self.cornerFrame, name=MyNameText, text=MyText, relief=tk.RAISED, width=self.widthArray[1-1])
            cornerCell.pack()
        print(MyNameText+": "+MyText)
        print("ColOfLineHeader:")
        #if self.QLineHeaders>0:#headerSize.L>0:#
        if self.headerSize.L>0:#headerSize.L>0:#
            #for LineN in range(1, self.QLines+1):
            for LineN in range(1, self.contentSize.L+1):
                #for ColN in range(1, self.QColumns+1):
                MyNameText="lineHdr_"+str(LineN)
                MyText=self.table.ToString_Cell_ColOfLineHeader(LineN, self.repr, vsh)#, Repr=[], vsh=0)#"Line."+str(LineN)
                curLineHdrCell=self.gui.Label(master=self.lineHeaderFrame, name=MyNameText, text=MyText, relief=tk.RAISED, width=self.widthArray[1-1])
                curLineHdrCell.pack()
                print(MyNameText+": "+MyText)
        #if self.QColumnHeaders>0:#headerSize.C>0:#
        print("LineOfColHeader:")
        if self.headerSize.C>0:#headerSize.C>0:#
            #for ColN in range(1, self.QColumns+1):
            #for ColN in range(1, self.contentSize.C+1):
            for ColN in range(self.rowsNsLimsToDispl.C1, self.rowsNsLimsToDispl.C2+1):
                #for LineN in range(1,headerSize.C+1):
                MyNameText="colHdr_"+str(ColN)
                MyText=self.table.ToString_Cell_LineOfColHeader(ColN, self.repr, vsh)#, Repr=[], vsh=0)#"Col."+str(ColN)
                curColHdrCell=self.gui.Label(master=self.colHeaderFrame, name=MyNameText, text=MyText, relief=tk.RAISED, width=self.widthArray[ColN-1])
                curColHdrCell.pack(side=self.gui.LEFT)
                print(MyNameText+": "+MyText)
        #content cells
        #
        vsh=0#1
        #
        #dataSource=0
        #
        curCntRow=[]
        #curCntRowFrame=self.gui.Frame(master=self.contentFrame)#ce wa error
        if self.GuiControls.structRowOrder_LC0_CL1==1:#rowOrder_LC0_CL1==1:
            #for ColN in range(1, self.QColumns+1):
            for ColN in range(1, self.contentSize.C+1):    
                curCntRowFrame=self.gui.Frame(master=self.contentFrame)
                curCntRow=[]
                #for LineN in range(1,self.QLines+1):
                for LineN in range(self.rowsNsLimsToDispl.L1, self.rowsNsLimsToDispl.L2+1):
                    #MyNameText="cellContL"+str(LineN)+"C"+str(ColN)
                    coords=TableSize(LineN, ColN)
                    MyNameText=self.GenerateCellNameByCoords(coords)
                    #if self.GuiControls.Array_ActiveNText1_ActiveItemText2_Combobox3==1 or self.GuiControls.Array_ActiveNText1_ActiveItemText2_Combobox3==3:
                    #    dataSource=self.table.GetContent_Vals()
                    #elif self.GuiControls.Array_ActiveNText1_ActiveItemText2_Combobox3==2:
                    #    dataSource=self.table.GetContent_CurItems()
                    #ToString_Cell(self, LineN, ColN, tblRepr=[], vsh=0):
                    #if dataSource==0 or not isinstance(dataSource,list) or len(dataSource)==0:
                    if not isinstance(self.table, TableController2):
                        MyText="BL"+str(LineN)+"C"+str(ColN)+MyNameText
                    else:
                        #if self.sourceOrder_LC0_CL1==0:
                        #    MyText=str(dataSource[LineN-1][ColN-1])
                        #else:
                        #    MyText=str(dataSource[ColN-1][LineN-1])
                        cell=self.table.GetCell_AsCopy(LineN, ColN)
                        TypeN=cell.GetType()
                        if(TypeN==DataCell_ComboBoxOrMemo_TypeN):
                            if self.GuiControls.Array_ActiveNText1_ActiveItemText2_Combobox3==1:
                                #MyText=str(self.table.ToString_Cell(LineN, ColN, self.repr, vsh))
                                MyText=str(cell.GetVal())
                            else:
                                MyText=str(cell.GetItem())
                        else:
                            MyText=self.table.ToString_Cell(LineN, ColN, self.repr, vsh)
                            #MyText=self.table.ToString_Cell(LineN, ColN)#works ja idem
                        print("cell["+str(LineN)+", "+str(ColN)+"]="+MyText)
                    #if 
                    #print("dataSource extracted:")
                    #print(dataSource)
                    #if LineN==self.ActiveLineN and ColN==self.ActiveColN:
                    if LineN==self.activeRows.L and ColN==self.activeRows.C:
                        curCntCell=self.gui.Label(master=curCntRowFrame, name=MyNameText, text=MyText, relief=tk.SUNKEN, width=self.widthArray[ColN-1])
                    else:
                        curCntCell=self.gui.Label(master=curCntRowFrame, name=MyNameText, text=MyText, relief=tk.RIDGE, width=self.widthArray[ColN-1])
                    curCntCell.pack()
                     #
                    curCntCell.bind('<Button-1>', self.EventHandle_LeftClick_ContentCell)
                    #
                    self.cntRowFrames.append(curCntRowFrame)
                    #self.cntRows.append(curCntCell)
                    curCntRow.append(curCntCell)
                #
                curCntRowFrame.pack(side=self.gui.LEFT)
                #
                self.cntRows.append(curCntRow)
                #
            #self.ActiveCell=self.cntRows[self.ActiveColN-1][self.ActiveLineN-1]
            #self.ActiveCell=self.cntRows[self.activeRows.C-1][self.AcactiveRows.L-1]
        else: #0
            #for LineN in range(1,self.QLines+1):
            for LineN in range(self.rowsNsLimsToDispl.L1, self.rowsNsLimsToDispl.L2+1):
                curCntRowFrame=self.gui.Frame(master=self.contentFrame)
                curCntRow=[]
                #for ColN in range(1, self.QColumns+1):
                #for ColN in range(1, self.contentSize.C+1):
                for ColN in range(self.rowsNsLimsToDispl.C1, self.rowsNsLimsToDispl.C2+1):
                    #MyNameText="cellContL"+str(LineN)+"C"+str(ColN)#works well
                    coords=TableSize(LineN, ColN)
                    MyNameText=self.GenerateCellNameByCoords(coords)
                    #if dataSource==0 or not isinstance(dataSource,list) or len(dataSource)==0:
                    #    MyText="BL"+str(LineN)+"C"+str(ColN)+MyNameText
                    #else:
                    #    if self.sourceOrder_LC0_CL1==0:
                    #        MyText=str(dataSource[LineN-1][ColN-1])
                    #    else:
                    #        MyText=str(dataSource[ColN-1][LineN-1])
                    #if LineN==self.ActiveLineN and ColN==self.ActiveColN:
                    if not isinstance(self.table, TableController2):
                        MyText="BL"+str(LineN)+"C"+str(ColN)+MyNameText
                    else:
                        #if self.sourceOrder_LC0_CL1==0:
                        #    MyText=str(dataSource[LineN-1][ColN-1])
                        #else:
                        #    MyText=str(dataSource[ColN-1][LineN-1])
                        cell=self.table.GetCell_AsCopy(LineN, ColN)
                        TypeN=cell.GetType()
                        if(TypeN==DataCell_ComboBoxOrMemo_TypeN):
                            if self.GuiControls.Array_ActiveNText1_ActiveItemText2_Combobox3==1:
                                #MyText=str(self.table.ToString_Cell(LineN, ColN, self.repr, vsh))
                                MyText=str(cell.GetVal())
                            else:
                                MyText=str(cell.GetItem())
                        else:
                            MyText=self.table.ToString_Cell(LineN, ColN, self.repr, vsh)
                        print("cell["+str(LineN)+", "+str(ColN)+"]="+MyText)
                        #if 
                    #print("dataSource extracted:")
                    #print(dataSource)
                    if LineN==self.activeRows.L and ColN==self.activeRows.C:
                        curCntCell=self.gui.Label(master=curCntRowFrame, name=MyNameText, text=MyText, relief=tk.SUNKEN, width=self.widthArray[ColN-1])
                    else:
                        curCntCell=self.gui.Label(master=curCntRowFrame, name=MyNameText, text=MyText, relief=tk.RIDGE, width=self.widthArray[ColN-1])
                    curCntCell.pack(side=self.gui.LEFT)
                    #
                    curCntCell.bind('<Button-1>', self.EventHandle_LeftClick_ContentCell)
                    #
                    self.cntRowFrames.append(curCntRowFrame)
                    #self.cntRows.append(curCntCell)
                    curCntRow.append(curCntCell)
                #
                curCntRowFrame.pack()
                #
                self.cntRows.append(curCntRow)
                #
            #self.ActiveCell=self.cntRows[self.ActiveLineN-1][self.ActiveColN-1]
            self.ActiveCell=self.cntRows[self.activeRows.L-1][self.activeRows.C-1]
            #
            
                    
    #
    def getQLines(self):
        #return self.QLines
        return self.contentSize.L
    # 
    def getQColumns(self):
        return self.contentSize.C
    #
    #
    def getCurLineN(self):
        #return self.ActiveLineN
        return self.activeRows.L
    # 
    def getCurColumnN(self):
        #return self.ActiveColN
        return self.activeRows.C
    # 
    def SetCurLineN(self, N):
        if N>=1 and N<=self.QLines:
            #self.ActiveLineN=N
            self.activeRows.L=N
    # 
    def SetCurColumnN(self, N):
        if N>=1 and N<=self.QColumns:
            self.activeRows.C=N
    #
    def SetCurRows(self, activeRows):
        if activeRows.C>=1 and activeRows.L>=1 and activeRows.L<=self.QLines and activeRows.C<=self.QColumns:
            #self.ActiveColN=activeRows.C
            #self.ActiveLinelN=activeRows.L
            self.activeRows.C=activeRows.C
            self.activeRows.L=activeRows.L
    #
    def GetCurRows(self):
        r=TableSize(self.activeRows.L, activeRows.C)
        return r
    #
    def SetCurFirstCell(self):
        #self.ActiveLineN=1
        #self.ActiveColN=1
        self.activeRows.L=1
        self.activeRows.C=1
    #
    def SetCurLastCell(self):
        #self.ActiveLineN=self.QLines
        #self.ActiveColN=self.QColumns
        self.activeRows.L=self.QLines
        self.activeRows.C=self.QColumns
    #
    def SetCurFirstLine(self):
        #self.ActiveLineN=1
        self.activeRows.L=1
    #
    def SetCurLastLine(self):
        self.activeRows.L=self.QLines
    #
    def SetCurFirstColumn(self):
        #self.ActiveColeN=1
        self.activeRows.C=1
    #
    def SetCurLastColumn(self):
       # self.ActiveColN=self.QColumns
        self.activeRows.C=self.QColumns
    #
    #
    def GenerateCellNameByCoords(self,coords):
        Name="contL"
        if coords.L<10:
            Name=Name+"000"
        elif  coords.L<100:
            Name=Name+"00"
        elif coords.L<1000:
            Name=Name+"0"
        Name=Name+str(coords.L)
        Name=Name+"C"
        if coords.C<10:
            Name=Name+"000"
        elif  coords.C<100:
            Name=Name+"00"
        elif coords.C<1000:
            Name=Name+"0"
        Name=Name+str(coords.C)
        return Name
    #
    def ExtractCoordsFromName(self,Name):
        #LPart=Name[(6-1):10]
        LPart=Name[(6-1):(10-1)]
        L=int(LPart)
        CPart=Name[11-1:14]
        C=int(CPart)
        coords=TableSize(L,C)
        return coords
    #
    #
    def EventHandle_LeftClick_ContentCell(self, event):
        content=[]
        #finding coords of new active cell
        #Name=event.widget['name'] # so ne works
        #Name=event.widget.name # so ne works
        #Name=event.widget['text'] # so  works, ma ce text, ne name
        Name=event.widget.winfo_name()
        #coords=self.ExtractCoordsFromName(Name)
        cellCoords=self.ExtractCoordsFromName(Name)
        coords=TableSize(self.rowsNsLimsToDispl.ContentGridLineNByTableLineN(cellCoords.L), self.rowsNsLimsToDispl.TableColNByContentGridColN(cellCoords.C))
        #making appearance of former active cell not active
        if self.GuiControls.structRowOrder_LC0_CL1==0:
            self.cntRows[self.activeRows.L-1][self.activeRows.C-1].configure(relief=self.gui.RIDGE)
            #print("Active L=",self.ActiveLineN," C=",self.ActiveColN)
        else:
            self.cntRows[self.activeRows.C-1][self.activeRows.L-1].configure(relief=self.gui.RIDGE)
            #print("Active L=",self.ActiveLineN," C=",self.ActiveColN)
        #making appearance of new active cell  active
        #event.widget.configure(relief=self.gui.SUNKEN)#works well, ma no need, ce s'done below ataly
        #event.widget.configure(name=NameText)# ne knows name
        #event.widget.configure(text=NameText)
        #event.widget.modify(event.widget['relief']=self.gui.SUNKEN)
        #post deactivation, ob mab ce same cell
        #self.ActiveLineN=coords.L
        #self.ActiveColN=coords.C
        self.activeRows.L=coords.L
        self.activeRows.C=coords.C
	#	
        if self.GuiControls.structRowOrder_LC0_CL1==0:
            self.cntRows[self.activeRows.L-1][self.activeRows.C-1].configure(relief=self.gui.SUNKEN)
        else:
            self.cntRows[self.activeRows.C-1][self.activeRows.L-1].configure(relief=self.gui.SUNKEN)
        #
        if self.tblView!=0:
            cellContent=[]
            #
            #if self.GuiControls.structRowOrder_LC0_CL1==0:
            #    cellContent.append(self.cntRows[self.activeRows.L-1][self.activeRows.C-1]['text'])
            #else:
            #    cellContent.append(self.cntRows[self.activeRows.C-1][self.activeRows.L-1]['text'])
            #
            cell=self.table.GetCell_AsCopy(self.activeRows.L, self.activeRows.C)
            cellContent=cell.GetItems()
            #
            self.tblView.combo_ChoosingData.configure(values=cellContent)
            #probe
            #print("cell content of new active cell: ",cellContent)
            #cellContent=[]
            #cellContent=self.tblView.combo_ChoosingData.configure(values=cellContent)#WTF& Qob py ne error
            #self.tblView.combo_ChoosingData.configure(values=cellContent)
            self.tblView.combo_ChoosingData.current(0)#nur for this training version!
            #cellContent=self.tblView.combo_ChoosingData['values']
            ##print(cellContent)
            #if self.rowOrder_LC0_CL1==0:
            #    self.cntRows[self.ActiveLineN-1][self.ActiveColN-1]['text']=cellContent[0]
            #    #self.cntRows[self.ActiveLineN-1][self.ActiveColN-1].configure(text="1234")#cellContent[0])
            #    #so works so problem is not in label, ma in Combobox
            #else:
            #    self.cntRows[self.ActiveColN-1][self.ActiveLineN-1]['text']=cellContent[0]
            #    #self.cntRows[self.ActiveColN-1][self.ActiveLineN-1].configure(text="1234")#text=cellContent[0])
            #    #so works so problem is not in label, ma in Combobox
    #
    #
    def ShowConsole(self):
        gridLength=len(self.cntRows)
        colLength=[]
        print("grid length: "+str(gridLength)," QLines=",self.QLines," QColumns=",self.QColumns)
        if(self.GuiControls.rowOrder_LC0_CL1==0):
            print("Lines")
            print("Gen info  - Lines' Length:")
            for LineN in range(1,gridLength+1):
                print(LineN,"): L=",len(self.cntRows[LineN-1]))
            print("Content:")
            for LineN in range(1,gridLength+1):
                lineLength=len(self.cntRows[LineN-1])
                print("Line ",LineN," Length: ", lineLength)
                for ColN in range(1,lineLength+1):
                    print(self.cntRows[LineN-1][ColN-1]['text'])
        else:
            print("Columns")
            print("Gen info  - Columns' Length:")
            for ColN in range(1,gridLength+1):
                colLength.append(len(self.cntRows[ColN-1]))
                if ColN==1 or (ColN>1 and maxColLength<colLength[ColN-1]):
                    maxColLength=colLength[ColN-1]
                print(ColN,"): L=",len(self.cntRows[ColN-1]))
            print("maxColLEngth=",maxColLength)
            print("Content:")
            for LineN in range(1,maxColLength+1):
                print("Line ",LineN)
                for ColN in range(1,gridLength+1):
                    if LineN>colLength[ColN-1]:
                        print("-")
                    else:
                        print(self.cntRows[ColN-1][LineN-1]['text'])

#TableGridView(self, mstr, gui, curTable, tblInf, GuiControls, activeRows=0, DfltWidth=40, tblView=0)
class TableView:
    def __init__(self, mstr, gui, curTable, tblInf=0, GuiControls=0, rowsNsLimsToDispl=0, activeRows=0, DfltWidth=40, vsh=0):#, rowOrder_LC0_CL1=1,  sourceOrder_LC0_CL1=1):
        self.GuiControls=TableGUIControls()
        if isinstance(GuiControls, TableGUIControls):
            self.GuiControls=copy.deepcopy(GuiControls)
            #Align_Left1Top2Bottom3Right4=GuiControls.Align_Left1Top2Bottom3Right4
        self.tableViewMainFrame=gui.Frame(master=mstr,  relief=tk.RIDGE)
        #
        self.frame_SupplToolbar=gui.Frame(master=self.tableViewMainFrame,  relief=tk.RIDGE)
        #self.frame_SupplToolbar.pack()
        #
        if self.GuiControls.Align_Left1Top2Bottom3Right4==1:
            self.tableViewMainFrame.pack(side=gui.LEFT)
        elif self.GuiControls.Align_Left1Top2Bottom3Right4==2:
            self.tableViewMainFrame.pack(side=gui.TOP)
        elif self.GuiControls.Align_Left1Top2Bottom3Right4==3:
            self.tableViewMainFrame.pack(side=gui.BOTTOM)
        elif self.GuiControls.Align_Left1Top2Bottom3Right4==3:
            self.tableViewMainFrame.pack(side=gui.RIGHT)
        else:
            self.tableViewMainFrame.pack()
        if activeRows==0:
            self.ActiveCell=TableSize(1,1)
        elif isinstance(activeRows, TableSize):
            self.ActiveCell=copy.deepcopy(activeRows)
        #
        self.frame_SupplToolbar.pack()#=gui.Frame(master=self.tableViewMainFrame,  relief=tk.RIDGE)
        #
        self.lbl_TblHeader=gui.Label(master=self.tableViewMainFrame, name="lbl_TblHeader",  text="", height=1) #width=50
        self.lbl_TblHeader.pack()
        #
        print ("TableView constr working")
        if isinstance(tblInf, TableInfo1):
            print ("tblInf is isinstance of  TableInfo1")
        else:
            if isinstance(tblInf, TableSize):
                print ("tblInf is isinstance of  TableSize") 
            else:
                print ("tblInf is ne TableInfo1 nor  TableSize")
        print ("TableView constr working")
        #
        #vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        #
        #TableGridView(     self,                  mstr, gui, curTable, tblInf, GuiControls, rowsNsLimsToDispl, activeRows=0, DfltWidth=40, tblView=0)
        self.grid=TableGridView(self.tableViewMainFrame, gui, curTable, tblInf, GuiControls, rowsNsLimsToDispl, activeRows,   DfltWidth,    self) 
        #
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        #
        #self.frame_SupplToolbar.pack()
        #
        self.frame_MainToolbar=gui.Frame(master=self.tableViewMainFrame,  relief=tk.RIDGE)
        #
        #self.frame_SupplToolbar.pack()
        #self.grid.pack()#pack'ts by constr
        self.frame_MainToolbar.pack()
        #self.frame_MainToolbar.pack()
        #
        self.btn_SetTable=gui.Button(master=self.frame_MainToolbar, name="btn_SetTable", text ="SET Tbl", width=15)
        #self.btn_SetValue=gui.Button(master=self.frame_MainToolbar, name="btn_SetValue", text ="Set", width=10)#below, further
        #self.btn_GetValue=gui.Button(master=self.frame_MainToolbar, name="btn_GetValue", text ="Get", width=10)#below, further
        #
        #
        #
        StructToolbar=gui.Frame(master=self.frame_SupplToolbar,  relief=tk.RIDGE)
        NavigationToolbar=gui.Frame(master=self.frame_SupplToolbar,  relief=tk.RIDGE)
        InfoToolbar=gui.Frame(master=self.frame_SupplToolbar,  relief=tk.RIDGE)
        #
        StructToolbar.pack(side=gui.LEFT)
        NavigationToolbar.pack(side=gui.LEFT)
        InfoToolbar.pack(side=gui.LEFT)
        #
        StructToolbar_Col1=gui.Frame(master=StructToolbar,  relief=tk.RIDGE)
        StructToolbar_Col2=gui.Frame(master=StructToolbar,  relief=tk.RIDGE)
        StructToolbar_Col3=gui.Frame(master=StructToolbar,  relief=tk.RIDGE)
        StructToolbar_Col4=gui.Frame(master=StructToolbar,  relief=tk.RIDGE)
        #
        StructToolbar_Col1.pack(side=gui.LEFT)
        StructToolbar_Col2.pack(side=gui.LEFT)
        StructToolbar_Col3.pack(side=gui.LEFT)
        StructToolbar_Col4.pack(side=gui.LEFT)
        #
        NavigationToolbar_LeftCol=gui.Frame(master=StructToolbar,  relief=tk.RIDGE)#
        NavigationToolbar_MiddleCol=gui.Frame(master=StructToolbar,  relief=tk.RIDGE)
        NavigationToolbar_RightCol=gui.Frame(master=StructToolbar,  relief=tk.RIDGE)#
        #
        NavigationToolbar_Line1=gui.Frame(master=NavigationToolbar_MiddleCol,  relief=tk.RIDGE)
        NavigationToolbar_Line2=gui.Frame(master=NavigationToolbar_MiddleCol,  relief=tk.RIDGE)
        NavigationToolbar_Line3=gui.Frame(master=NavigationToolbar_MiddleCol,  relief=tk.RIDGE)
        #
        #
        self.btn_AddLine=gui.Button(master=StructToolbar_Col1, name="btn_AddLine", text ="Add Line", width=10)
        self.btn_InsLine=gui.Button(master=StructToolbar_Col1, name="btn_InsLine", text ="Ins Line", width=10)
        self.btn_DelLine=gui.Button(master=StructToolbar_Col1, name="btn_DelLine", text ="Del Line", width=10)
        self.btn_AddCol=gui.Button(master=StructToolbar_Col2, name="btn_AddCol", text ="Add Col", width=10)
        self.btn_InsCol=gui.Button(master=StructToolbar_Col2, name="btn_InsCol", text ="Ins Col", width=10)
        self.btn_DelCol=gui.Button(master=StructToolbar_Col2, name="btn_DelCol", text ="Del Col", width=10)
        self.btn_AddBoth=gui.Button(master=StructToolbar_Col3, name="btn_AddBoth", text ="Add Both", width=10)
        self.btn_InsBoth=gui.Button(master=StructToolbar_Col3, name="btn_InsBoth", text ="Ins Both", width=10)
        self.btn_DelBoth=gui.Button(master=StructToolbar_Col3, name="btn_DelBoth", text ="Del Both", width=10)
        #
        self.btn_Transpose=gui.Button(master=StructToolbar, name="btn_Transpose", text ="T", width=3, height=4)
        #
        #self.btn_ArrowToTheLeft=gui.Button(master=NavigationToolbar, name="btn_ArrowToTheLeft", text ="<", width=3, height=4)
        self.btn_ArrowToTheLeft=gui.Button(master=NavigationToolbar_LeftCol, name="btn_ArrowToTheLeft", text ="<", width=3, height=4)
        #
        self.btn_ArrowLeftLim=gui.Button(master=NavigationToolbar_Line1, name="btn_ArrowLeftLim", text ="<<", width=6)#width=8)
        self.btn_ArrowUp=gui.Button(master=NavigationToolbar_Line1, name="btn_ArrowUp", text ="^", width=14)#width=40)
        self.btn_ArrowUpLim=gui.Button(master=NavigationToolbar_Line1, name="btn_ArrowUpLim", text ="^^", width=6)#width=8)
        #
        self.btn_ArrowDnLim=gui.Button(master=NavigationToolbar_Line3, name="btn_ArrowDnLim", text ="vv", width=6)#width=8)
        self.btn_ArrowDn=gui.Button(master=NavigationToolbar_Line3, name="btn_ArrowDn", text ="v", width=14)#width=40)
        self.btn_ArrowRightLim=gui.Button(master=NavigationToolbar_Line3, name="btn_ArrowRightLim", text =">>", width=6)#width=8)
        #
        self.btn_ArrowToTheRight=gui.Button(master=NavigationToolbar, name="btn_ArrowToTheLRight", text =">", width=3, height=4)
        #self.btn_ArrowToTheRight=gui.Button(master=NavigationToolbar_RightCol, name="btn_ArrowToTheLRight", text =">", width=3, height=4)
        #
        self.btn_SetTable=gui.Button(master=self.frame_SupplToolbar, name="btn_SetTable", text ="SET Tbl")
        self.btn_LoadTable=gui.Button(master=self.frame_SupplToolbar, name="btn_LoadTable", text ="(Re)load Last", width=10)
        self.btn_OpenFromFile=gui.Button(master=self.frame_SupplToolbar, name="btn_OpenFromFile", text ="Open", width=10)
        self.btn_SaveToFile=gui.Button(master=self.frame_SupplToolbar, name="btn_SaveToFile", text ="Save", width=10)
        #
        #
        self.btn_AddLine.pack()
        self.btn_InsLine.pack()
        self.btn_DelLine.pack()
        #
        self.btn_AddCol.pack()
        self.btn_InsCol.pack()
        self.btn_DelCol.pack()
        #
        self.btn_AddBoth.pack()
        self.btn_InsBoth.pack()
        self.btn_DelBoth.pack()
        #
        self.btn_Transpose.pack(side=gui.LEFT)
        #
        self.btn_ArrowToTheLeft.pack(side=gui.LEFT)
        #
        NavigationToolbar_LeftCol.pack(side=gui.LEFT)#ac ce btn s at the right
        NavigationToolbar_MiddleCol.pack(side=gui.LEFT)
        #NavigationToolbar_RightCol.pack(side=gui.LEFT)#
        #
        NavigationToolbar_Line1.pack()
        NavigationToolbar_Line2.pack()
        NavigationToolbar_Line3.pack()
        #
        #self.btn_ArrowDn.pack(side=gui.LEFT)
        #
        self.btn_ArrowLeftLim.pack(side=gui.LEFT)
        self.btn_ArrowUp.pack(side=gui.LEFT)
        self.btn_ArrowUpLim.pack(side=gui.LEFT)
        #
        self.btn_ArrowDnLim.pack(side=gui.LEFT)
        self.btn_ArrowDn.pack(side=gui.LEFT)
        self.btn_ArrowRightLim.pack(side=gui.LEFT)
        #
        self.btn_ArrowToTheRight.pack(side=gui.LEFT)
        #
        self.lbl_InfoToolbarHeader=gui.Label(master=InfoToolbar, name="lbl_InfoToolbarHeader",  text="Suppl.Info to show", height=1) #width=50
        #
        #fontExample = ("Courier", 9)
        fontExample = ("Courier", 12)
        #items_ChoosingCell=[
        #                      "Content cell", 
        #                      "Line of Col Header Cell",
        #                      "Col of Line Header Cell",
        #                      "Lines General Name",
        #                      "Columns General Name",
        #                      "Table Name",
        #                      "DB Field Name",
        #                      "DB Table Name",
        #                      "Joined Table Name",
        #                      "Joined Content Field Name",
        #                      "Joined Key Field Name",
        #                      "Cell Items",
        #                      "Field Items"
        #                    ]
        #items_ChoosingAction=[
        #                      "Focus at Cell",
        #                      "Compress Displayed",
        #                      "Expand Displayed",
        #                      "Shift Displayed",
        #                      "Rows Moving" , 
        #                      "Cells Moving",
        #                      "Rows Ins or Add",
        #                      "Rows Del",
        #                      "Rows Size",
        #                      "Text Size",
        #                      "Text in Cell"
        #                    ]
        #items_ChoosingInfo=[
        #                      "Cells Items",
        #                      "Representation in Table",
        #                      "Representation in Text",
        #                      "Ussage Policy",
        #                      "DB Table data",
        #                      "DB Fields data",
        #                      "Cells Types"
        #                    ]
        items_ChoosingData=[]
        items_ChoosingData.append(self.grid.ActiveCell['text'])
        #
        CurFrame=gui.Frame(master=self.frame_MainToolbar)
        CurSubFrame=gui.Frame(master=CurFrame)
        #
        CurFrame.pack(side=gui.LEFT)
        #self.lbl_CmdLineHeader=gui.Label(master=CurFrame, name="lbl_CmdLineHeader",  text="Conmmand Line for DataInput:", relief=tk.RIDGE, width=50) #text="Conmmand Line for DataInput:",
        self.lbl_CmdLineHeader=gui.Label(master=CurFrame, name="lbl_CmdLineHeader",  text="Conmmand Line for DataInput:", width=50) 
        self.lbl_CmdLineHeader.pack()
        #
        self.combo_ChoosingData = ttk.Combobox(master=CurFrame, name="combo_ChoosingData", values=items_ChoosingData, font = fontExample, width=50) 
        self.combo_ChoosingData.current(0)
        self.combo_ChoosingData.pack()
        #
        CurSubFrame.pack()
        self.btn_SetValue=gui.Button(master=CurSubFrame, name="btn_SetValue", text ="Set", width=9)
        self.btn_SetValue.pack(side=gui.LEFT)
        self.btn_GetValue=gui.Button(master=CurSubFrame, name="btn_GetValue", text ="Get", width=9)
        self.btn_GetValue.pack(side=gui.LEFT)
        CurSubFrame.pack()
        #
        self.combo_ChoosingCell = ttk.Combobox(master=CurSubFrame, name="combo_ChoosingCell", values=items_ChoosingCell, font = fontExample)#, padx=20)
        self.combo_ChoosingCell.current(0)
        self.combo_ChoosingCell.pack(side=gui.LEFT)
        #
        #
        self.combo_ChoosingNaviAction = ttk.Combobox(master=NavigationToolbar_Line2, name="combo_ChoosingNaviAction", values=items_ChoosingAction, font = fontExample)#, padx=20)
        self.combo_ChoosingNaviAction.current(0)
        self.combo_ChoosingNaviAction.pack()
        #
        #
        CurFrame=gui.Frame(master=self.frame_MainToolbar)
        CurFrame.pack(side=gui.LEFT)
        #
        #
        self.lbl_InfoToolbarHeader.pack()
        #
        self.combo_ChoosingInfo = ttk.Combobox(master=InfoToolbar, name="combo_ChoosingInfo", values=items_ChoosingInfo, font = fontExample, width=20) 
        self.combo_ChoosingInfo.current(0)
        self.combo_ChoosingInfo.pack()
        #
        self.btn_ShowSupplInf=gui.Button(master=InfoToolbar, name="btn_ShowSupplInf", text ="Show suppl. inf", width=12)
        self.btn_ShowSupplInf.pack(side=gui.LEFT)
        #
        #
        TableSetFrame=gui.Frame(master=self.frame_MainToolbar)
        TableSetFrame.pack(side=gui.LEFT)
        #
        self.btn_SetTable=gui.Button(master=TableSetFrame, name="btn_SetTable", text ="Set Table", width=15, height=4)
        self.btn_SetTable.pack(side=gui.LEFT)
        self.btn_DiscardChanges=gui.Button(master=TableSetFrame, name="btn_DiscardChanges", text ="Discard Changes", width=15, height=4)
        self.btn_DiscardChanges.pack(side=gui.LEFT)
        #
        #----------------------------------------------------------------
        
    
class TableForm:
    def __init__(self, sourceTable, tblInf=0, GuiControls=0, rowsNsLimsToDispl=0, activeRows=0, source=0, DfltWidth=40, vsh=0):
        self.window = tk.Tk()
        #
        self.frame_a = tk.Frame(master=self.window,  relief=tk.RIDGE)
        self.frame_b = tk.Frame(master=self.window)
        self.frame_c = tk.Frame(master=self.window, relief=tk.GROOVE)
 
        self.label_a = tk.Label(master=self.frame_a, text="I'm in Frame A", relief=tk.SUNKEN)
        self.label_a.pack()

        #
        self.bufTable=[]
        self.targetTable=[]
        self.curTable=[]
        self.guiControls=TableGUIControls()
        if isinstance(GuiControls, TableGUIControls):
            self.guiControls=copy.deepcopy(GuiControls)
        if isinstance(sourceTable, TableController2):
            self.targetTable=sourceTable
        else:
            self.targetTable=TableController2()
        if self.guiControls.Control_GUI0_Controller1_Direct2==0:
            self.curTable=copy.deepcopy(self.targetTable)
        elif self.guiControls.Control_GUI0_Controller1_Direct2==2:
            self.curTable=self.targetTable
        else:#self.guiControls.Control_GUI0_Controller1_Direct2==1:
            self.curTable=copy.deepcopy(self.targetTable)
        #
 
        
        #vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        #TableView __init__(self,  mstr,  gui,      curTable, tblInf=0,   GuiControls=0,  rowsNsLimsToDispl=0,activeRows=0, DfltWidth=40, vsh=0):
        grid =    TableView(self.frame_b,  tk,  self.curTable,  tblInf, self.guiControls, rowsNsLimsToDispl,  activeRows,    DfltWidth, vsh)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        self.label_c = tk.Label(master=self.frame_c, text="I'm in Frame C", relief=tk.GROOVE)
        self.label_c.pack()
 
        self.frame_a.pack(expand=tk.YES, fill=tk.X)
        self.frame_b.pack(expand=tk.YES, fill=tk.BOTH)
        self.frame_c.pack(expand=tk.YES, fill=tk.X)

        self.label_c.config(relief=tk.SUNKEN)

        #grid.grid.ShowConsole()

    def Show(self):
        self.window.mainloop()



