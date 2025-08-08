import Tkinter as tk
import ttk
import copy
from TableInfoClasses import *

#from PyStdVector import My1DArray
 
window = tk.Tk()

#print(dataSource[2-1][1-1])


#QLines=5
#QColumns=4
#LineHeaders=1
#ColumnHeaders=1
#ActiveLineN=2
#ActiveColumnN=2
#relief=tk.: RAISED, SUNKEN, GROOVE, RIDGE, FLAT

class TableSize:
    def __init__(self, L=1, C=1):
        if isinstance(L, int) and isinstance(C, int):
            self.L=L
            self.C=C
        elif C==1 and isinstance(L, list) and len(L)==2 and isinstance(L[1-1], int) and isinstance(L[2-1], int):
            self.L=L[1-1]
            self.C=L[2-1]
    def ShowConsole(self):
        print("L="+str(self.L)+" C="+str(self.C))



class TableGridView:
    #
    #def __init__(self, mstr, gui, curTable, tblInf, GuiControls, activeRows, Align_Left1Top2Bottom3Right4=0, DfltWidth=40, rowOrder_LC0_CL1=1, tblView=0,  sourceOrder_LC0_CL1=1):
    def __init__(self, mstr, gui, curTable, tblInf, GuiControls, activeRows, Align_Left1Top2Bottom3Right4=0, DfltWidth=40, rowOrder_LC0_CL1=0, tblView=0,  sourceOrder_LC0_CL1=0):
        self.gui=gui
        self.tblView=tblView
        self.rowOrder_LC0_CL1=rowOrder_LC0_CL1
        self.cntRowFrames=[]
        self.cntRows=[]
        self.cellsOfContent=[]
        self.cellsOfLoCH=[]
        self.cellsOfCoLH=[]
        self.widthArray=[]
        #
       if isinstance(tblInf, TableInfo1) and  isinstance(tblInf.ussagePolicy, TableUssagePolicy):
            self.ussagePolicy=copy.deepcopy(tblInf.ussagePolicy)
        else:
            self.ussagePolicy=TableUssagePolicy()
        if isinstance(tblInf, TableInfo1) and  isinstance(tblInf.repr, TableRepr):
            self.repr=copy.deepcopy(tblInf.repr)
        else:
            self.repr=TableRepr()# if ne ecri ce - error: TableGridView has no attr repr
        #s#elf.ussagePolicy=self.tblInf.ussagePolicy
        #self.repr=self.tblInf.repr
        self.GuiControls=TableGUIControls()
        if isinstance(GuiControls, TableGUIControls):
            self.GuiControls=copy.deepcopy(GuiControls)
        else:
            self.GuiControls=TableGUIControls()
        #
        self.sourceOrder_LC0_CL1=curTable.GetStructRowOrderLC0CL1()
        self.rowOrder_LC0_CL1=self.GuiControls.structRowOrder_LC0_CL1
        #
        self.contentSize=TableSize()
        self.contentSize.L=curTable.GetQLines()
        self.contentSize.C=curTable.GetQColumns()
        self. headerSize=TableSize()
        self.activeRows=TableSize()
        self.activeRows.L=1
        self.activeRows.C=1
        if activeRows!=[] and activeRows!=0:
            self.activeRows=copy.deepcopy(activeRows)
        if self.repr.GetIfLineOfColHeaderToShow()!=0 or curTable.GetIf_LineOfColHeaderExists()!=0:
           self. headerSize.C=1
        else:
           self. headerSize.C=0
        if self.repr.GetIfColOfLineHeaderToShow()!=0 or curTable.GetIf_ColOfLineHeaderExists()!=0:
           self. headerSize.L=1
        else:
           self. headerSize.L=0    
        #
        print ("TableGrid constr working")
        if isinstance(tblInf, TableInfo1):
            print ("tblInf is isinstance of  TableInfo1")
        else:
            if isinstance(tblInf, TableSize):
                print ("tblInf is isinstance of  TableSize") 
            else:
                print ("tblInf is ne TableInfo1 nor  TableSize")
        print ("TableGrid constr working")
        self.table=curTable#ja so, link
        #print("Grid constructor: Size: QL="+str(self.QLines)+" C="+str(self.QColumns))
        print("Grid constructor: Size: QL="+str(self.contentSize.L)+" QC="+str(self.contentSize.C))
        #print("Grid constructor: data cource length:"+str(len(dataSource)))
        print("Grid constructor - content size param:")
        self.contentSize.ShowConsole()
        #
        for i in range(1, self.contentSize.C+1):
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
        #if self.QLineHeaders>0 and self.QColumnHeaders>0: #other vrns s'ne checked et max likely ne work, ma ne needed
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
                    #elif self.QLineHeaders==0 and self.QColumnHeaders>0:
        elif self.headerSize.L==0 and self. headerSize.C>0:
            #self.cornerFrame=gui.Frame(master=tableViewMainFrame)
            #self.cornerFrame.pack(side=gui.LEFT)
            self.colHeaderFrame=gui.Frame(master=self.tableViewMainFrame)
            self.colHeaderFrame.pack()
            #self.lineHeaderFrame=gui.Frame(master=tableViewMainFrame)
            #self.lineHeaderFrame.pack(side=gui.BOTTOM)
            self.contentFrame=gui.Frame(master=self.tableViewMainFrame)
            self.contentFrame.pack()
        #elif self.QLineHeaders>0 and self.QColumnHeaders==0:
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
        print("table given:")
        self.table.ShowToConsole()
        #
        self.HandleCells()
    #            
    def HandleCells(self):
        #curCntRowFrame
        #curCntRow
        #curCntCell
        print("given:  self.rowOrder_LC0_CL1=",  self.rowOrder_LC0_CL1, " self.sourceOrder_LC0_CL1=",  self.sourceOrder_LC0_CL1)
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
        #if self.QLineHeaders>0:#headerSize.L>0:#
        if self.headerSize.L>0:#headerSize.L>0:#
            #for LineN in range(1, self.QLines+1):
            for LineN in range(1, self.contentSize.L+1):
                #for ColN in range(1, self.QColumns+1):
                MyNameText="lineHdr_"+str(LineN)
                MyText=self.table.ToString_Cell_ColOfLineHeader(self, LineN)#, Repr=[], vsh=0)#"Line."+str(LineN)
                curLineHdrCell=self.gui.Label(master=self.lineHeaderFrame, name=MyNameText, text=MyText, relief=tk.RAISED, width=self.widthArray[1-1])
                curLineHdrCell.pack()
        #if self.QColumnHeaders>0:#headerSize.C>0:#
        if self.headerSize.C>0:#headerSize.C>0:#
            #for ColN in range(1, self.QColumns+1):
            for ColN in range(1, self.contentSize.C+1):
                #for LineN in range(1,headerSize.C+1):
                MyNameText="colHdr_"+str(ColN)
                MyText=self.table.ToString_Cell_LineOfColHeader(self, ColN)#, Repr=[], vsh=0)#"Col."+str(ColN)
                curColHdrCell=self.gui.Label(master=self.colHeaderFrame, name=MyNameText, text=MyText, relief=tk.RAISED, width=self.widthArray[ColN-1])
                curColHdrCell.pack(side=self.gui.LEFT)
        #content cells
        #
        dataSource=0
        #
        curCntRow=[]
        #curCntRowFrame=self.gui.Frame(master=self.contentFrame)#ce wa error
        if self.rowOrder_LC0_CL1==1:#rowOrder_LC0_CL1==1:
            #for ColN in range(1, self.QColumns+1):
            for ColN in range(1, self.contentSize.C+1):    
                curCntRowFrame=self.gui.Frame(master=self.contentFrame)
                curCntRow=[]
                #for LineN in range(1,self.QLines+1):
                for LineN in range(1,self.contentSize.L+1):
                    #MyNameText="cellContL"+str(LineN)+"C"+str(ColN)
                    coords=TableSize(LineN, ColN)
                    MyNameText=self.GenerateCellNameByCoords(coords)
                    if self.GuiControls.Array_ActiveNText1_ActiveItemText2_Combobox3==1 or self.GuiControls.Array_ActiveNText1_ActiveItemText2_Combobox3==3:
                        dataSource=self.table.GetContent_Vals()
                    elif self.GuiControls.Array_ActiveNText1_ActiveItemText2_Combobox3==2:
                        dataSource=self.table.GetContent_CurItems()
                    #ToString_Cell(self, LineN, ColN, tblRepr=[], vsh=0):
                    if dataSource==0 or not isinstance(dataSource,list) or len(dataSource)==0:
                        MyText="BL"+str(LineN)+"C"+str(ColN)+MyNameText
                    else:
                        if self.sourceOrder_LC0_CL1==0:
                            MyText=str(dataSource[LineN-1][ColN-1])
                        else:
                            MyText=str(dataSource[ColN-1][LineN-1])
                    print("dataSource extracted:")
                    print(dataSource)
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
            for LineN in range(1,self.contentSize.L+1):
                curCntRowFrame=self.gui.Frame(master=self.contentFrame)
                curCntRow=[]
                #for ColN in range(1, self.QColumns+1):
                for ColN in range(1, self.contentSize.C+1):
                    #MyNameText="cellContL"+str(LineN)+"C"+str(ColN)#works well
                    coords=TableSize(LineN, ColN)
                    MyNameText=self.GenerateCellNameByCoords(coords)
                    if dataSource==0 or not isinstance(dataSource,list) or len(dataSource)==0:
                        MyText="BL"+str(LineN)+"C"+str(ColN)+MyNameText
                    else:
                        if self.sourceOrder_LC0_CL1==0:
                            MyText=str(dataSource[LineN-1][ColN-1])
                        else:
                            MyText=str(dataSource[ColN-1][LineN-1])
                    #if LineN==self.ActiveLineN and ColN==self.ActiveColN:
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
        coords=self.ExtractCoordsFromName(Name)
        #making appearance of former active cell not active
        if self.rowOrder_LC0_CL1==0:
            #self.cntRows[self.ActiveLineN-1][self.ActiveColN-1].configure(relief=self.gui.RAISED)
            #self.cntRows[self.ActiveLineN-1][self.ActiveColN-1].configure(relief=self.gui.RIDGE)
            self.cntRows[self.activeRows.L-1][self.activeRows.C-1].configure(relief=self.gui.RIDGE)
            #print("Active L=",self.ActiveLineN," C=",self.ActiveColN)
        else:
            #self.cntRows[self.ActiveColN-1][self.ActiveLineN-1].configure(relief=self.gui.RAISED)
            #self.cntRows[self.ActiveColN-1][self.ActiveLineN-1].configure(relief=self.gui.RIDGE)
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
		
        if self.rowOrder_LC0_CL1==0:
            #self.cntRows[self.ActiveLineN-1][self.ActiveColN-1].configure(relief=self.gui.RAISED)
            #self.cntRows[self.ActiveLineN-1][self.ActiveColN-1].configure(relief=self.gui.SUNKEN)
            self.cntRows[self.activeRows.L-1][self.activeRows.C-1].configure(relief=self.gui.SUNKEN)
        else:
            #self.cntRows[self.ActiveColN-1][self.ActiveLineN-1].configure(relief=self.gui.RAISED)
            #self.cntRows[self.ActiveColN-1][self.ActiveLineN-1].configure(relief=self.gui.SUNKEN)
            self.cntRows[self.activeRows.C-1][self.activeRows.L-1].configure(relief=self.gui.SUNKEN)
        #print("Now: Active L=",self.ActiveLineN," C=",self.ActiveColN)
        #
        if self.tblView!=0:
            #print("grid is a part of table")
            cellContent=[]
            if self.rowOrder_LC0_CL1==0:
                #cellContent.append(self.cntRows[self.ActiveLineN-1][self.ActiveColN-1]['text'])
                cellContent.append(self.cntRows[self.activeRows.L-1][self.activeRows.C-1]['text'])
            else:
                #cellContent.append(self.cntRows[self.ActiveColN-1][self.ActiveLineN-1]['text'])
                cellContent.append(self.cntRows[self.activeRows.C-1][self.activeRows.L-1]['text'])
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
        if(self.rowOrder_LC0_CL1==0):
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

#TableGridView(self, mstr, gui, curTable, tblInf, GuiControls, activeRows, Align_Left1Top2Bottom3Right4=0, DfltWidth=40, rowOrder_LC0_CL1=1, tblView=0,  sourceOrder_LC0_CL1=1)
class TableView:
    def __init__(self, mstr, gui, curTable, tblInf, GuiControls, activeRows, Align_Left1Top2Bottom3Right4=0, DfltWidth=40):#, rowOrder_LC0_CL1=1,  sourceOrder_LC0_CL1=1):
        self.tableViewMainFrame=gui.Frame(master=mstr,  relief=tk.RIDGE)
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
        if activeRows==0:
            self.ActiveCell=TableSize(1,1)
        elif isinstance(activeRows, TableSize):
            self.ActiveCell=copy.deepcopy(activeRows)
        #
        #self.sourceOrder_LC0_CL1=curTable.GetStructRowOrderLC0CL1()
        #self.rowOrder_LC0_CL1=GuiControls.structRowOrder_LC0_CL1
        #
        self.frame_SupplToolbar=gui.Frame(master=self.tableViewMainFrame,  relief=tk.RIDGE)
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
        #self.grid=TableGridView(self.tableViewMainFrame, gui,        size, headerSize, ActiveCell, Align_Left1Top2Bottom3Right4,   DfltWidth, rowOrder_LC0_CL1)
        #self.grid=TableGridView(self.tableViewMainFrame, gui,        contentSize, headerSize, self.ActiveCell, Align_Left1Top2Bottom3Right4,   DfltWidth, rowOrder_LC0_CL1, self, dataSource)
        #         TableGridView(self,              mstr, gui, curTable, tblInf, GuiControls, activeRows, Align_Left1Top2Bottom3Right4=0, DfltWidth=40, rowOrder_LC0_CL1=1, tblView=0,  sourceOrder_LC0_CL1=1)
        self.grid=TableGridView(self.tableViewMainFrame, gui, curTable, tblInf, GuiControls, activeRows, Align_Left1Top2Bottom3Right4,   DfltWidth,    rowOrder_LC0_CL1,   self,            sourceOrder_LC0_CL1) 
        #
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        #
        self.frame_MainToolbar=gui.Frame(master=self.tableViewMainFrame,  relief=tk.RIDGE)
        #
        self.frame_SupplToolbar.pack()
        #self.grid.pack()#pack'ts by constr
        self.frame_MainToolbar.pack()
        #
        self.btn_SetTable=gui.Button(master=self.frame_MainToolbar, name="btn_SetTable", text ="SET Tbl", width=15)
        #self.btn_SetValue=gui.Button(master=self.frame_MainToolbar, name="btn_SetValue", text ="Set", width=10)#below, further
        #self.btn_GetValue=gui.Button(master=self.frame_MainToolbar, name="btn_GetValue", text ="Get", width=10)#below, further
        #
        self.btn_AddLine=gui.Button(master=self.frame_MainToolbar, name="btn_AddLine", text ="Add Line", width=10)
        self.btn_InsLine=gui.Button(master=self.frame_MainToolbar, name="btn_InsLine", text ="Ins Line", width=10)
        self.btn_DelLine=gui.Button(master=self.frame_MainToolbar, name="btn_DelLine", text ="Del Line", width=10)
        self.btn_AddCol=gui.Button(master=self.frame_MainToolbar, name="btn_AddCol", text ="Add Col", width=10)
        self.btn_InsCol=gui.Button(master=self.frame_MainToolbar, name="btn_InsCol", text ="Ins Col", width=10)
        self.btn_DelCol=gui.Button(master=self.frame_MainToolbar, name="btn_DelCol", text ="Del Col", width=10)
        self.btn_AddBoth=gui.Button(master=self.frame_MainToolbar, name="btn_AddBoth", text ="Add Both", width=10)
        self.btn_InsBoth=gui.Button(master=self.frame_MainToolbar, name="btn_InsBoth", text ="Ins Both", width=10)
        self.btn_DelBoth=gui.Button(master=self.frame_MainToolbar, name="btn_DelBoth", text ="Del Both", width=10)
        #
        self.btn_ArrowUp=gui.Button(master=self.frame_MainToolbar, name="btn_ArrowUp", text ="^", width=40)
        self.btn_ArrowUpLim=gui.Button(master=self.frame_MainToolbar, name="btn_ArrowUpLim", text ="^^", width=8)
        self.btn_ArrowDn=gui.Button(master=self.frame_MainToolbar, name="btn_ArrowDn", text ="v", width=40)
        self.btn_ArrowDnLim=gui.Button(master=self.frame_MainToolbar, name="btn_ArrowDnLim", text ="vv", width=8)
        self.btn_ArrowToTheLeft=gui.Button(master=self.frame_MainToolbar, name="btn_ArrowToTheLeft", text ="<", width=8)
        self.btn_ArrowLeftLim=gui.Button(master=self.frame_MainToolbar, name="btn_ArrowLeftLim", text ="<<", width=8)
        self.btn_ArrowToTheRight=gui.Button(master=self.frame_MainToolbar, name="btn_ArrowToTheLRight", text =">", width=8)
        self.btn_ArrowRightLim=gui.Button(master=self.frame_MainToolbar, name="btn_ArrowRightLim", text =">>", width=8)
        #
        self.btn_SetTable=gui.Button(master=self.frame_MainToolbar, name="btn_SetTable", text ="SET Tbl")
        self.btn_LoadTable=gui.Button(master=self.frame_MainToolbar, name="btn_LoadTable", text ="(Re)load Last", width=10)
        self.btn_OpenFromFile=gui.Button(master=self.frame_MainToolbar, name="btn_OpenFromFile", text ="Open", width=10)
        self.btn_SaveToFile=gui.Button(master=self.frame_MainToolbar, name="btn_SaveToFile", text ="Save", width=10)
        #
        #fontExample = ("Courier", 16, "bold")
        fontExample = ("Courier", 9)
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
                              "Rows Moving" , 
                              "Cells Moving",
                              "Compress Table",
                              "Expand Table",
                              "Size of Cells",
                              "Text or Items"
                            ]
        items_ChoosingData=[]
        items_ChoosingData.append(self.grid.ActiveCell['text'])
        #
        #----------------------------------------------------------------
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
        CurFrame=gui.Frame(master=self.frame_MainToolbar)
        CurFrame.pack(side=gui.LEFT)
        #
        #----------------------------------------------------------------


        #
class TableForm:
    #def __init__(self, mstr, gui, contentSize, headerSize, activeRows, Align_Left1Top2Bottom3Right4=0, DfltWidth=40, rowOrder_LC0_CL1=1, dataSource=0, sourceOrder_LC0_CL1=1
    #def __init__(self, table, tblInf, GuiControls, activeRows=0, Align_Left1Top2Bottom3Right4=0, DfltWidth=40, rowOrder_LC0_CL1=1, sourceOrder_LC0_CL1=1):
    def __init__(self, table, tblInf, GuiControls, activeRows=0, Align_Left1Top2Bottom3Right4=0, DfltWidth=40, rowOrder_LC0_CL1=0, sourceOrder_LC0_CL1=0):    
        self.curTable=[]
        self.targetTable=[]
        self.bufTable=[]
        self.ussagePolicy=[]
        self.controlsGUI=TableGUIControls()
        self.window = tk.Tk()
        self.activeRows=TableSize()
        #
        self.DfltWidth=40
        #
        print ("TableForm constr working")
        if isinstance(tblInf, TableInfo1):
            print ("tblInf is isinstance of  TableInfo1")
        else:
            if isinstance(tblInf, TableSize):
                print ("tblInf is isinstance of  TableSize") 
            else:
                print ("tblInf is ne TableInfo1 nor  TableSize")
        print ("TableForm constr working")
        #
        if activeRows==0:
            self.activeRows.L=1
            self.activeRows.C=1
        elif isinstance(activeRows, TableSize):
            self.activeRows=activeRows
        if GuiControls.Array_ActiveNText1_ActiveItemText2_Combobox3==2 or GuiControls.Array_ActiveNText1_ActiveItemText2_Combobox3==3: 
            dataSource=table.GetContent_CurItems()
        else:
            dataSource=table.GetContent_Vals()
        self.targetTable=table
        if GuiControls.Control_GUI0_Controller1_Direct2==0:
            pass
        elif GuiControls.Control_GUI0_Controller1_Direct2==1:
            self.curTable=copy.deepcopy(self.targetTable)
        else: # GuiControls.Control_GUI0_Controller1_Direct2==2:
            self.curTable=self.targetTable
        #mstr=self.window
        #gui=frame_b 
                #
        window = tk.Tk()
        frame_a = tk.Frame(master=window,  relief=tk.RIDGE)
        frame_b = tk.Frame(master=window)
        frame_c = tk.Frame(master=window, relief=tk.GROOVE)
        frame_a = tk.Frame(master=window,  relief=tk.RIDGE)
        label_a = tk.Label(master=frame_a, text="I'm in Frame A", relief=tk.SUNKEN)
        label_a.pack()
        #
        headerSize=TableSize(1,1)
        #
        #vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        #
        #              TableView(mstr,    gui, contentSize,                                    headerSize, activeRows,      Align_Left1Top2Bottom3Right4=0, DfltWidth=40, rowOrder_LC0_CL1=1, dataSource=0, sourceOrder_LC0_CL1=1)
        #self.tableView=TableView(frame_b, tk,  TableSize(len(dataSource), len(dataSource[0])), headerSize, self.activeRows, Align_Left1Top2Bottom3Right4,   DfltWidth,    rowOrder_LC0_CL1,   dataSource,   sourceOrder_LC0_CL1)
        #
        #TableViewdef __init__(self, mstr, gui,      curTable, tblInf, GuiControls, activeRows, Align_Left1Top2Bottom3Right4=0,   DfltWidth=40, rowOrder_LC0_CL1=1,  sourceOrder_LC0_CL1=1)
        self.tableView=TableView( frame_b,  tk, self.curTable, tblInf, GuiControls, activeRows, Align_Left1Top2Bottom3Right4,   self.DfltWidth,   rowOrder_LC0_CL1,    sourceOrder_LC0_CL1) 
        #
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        #

    def Show(self):
        #pass
        self.window.mainloop()
        
