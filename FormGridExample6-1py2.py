# -*- coding: utf-8 -*-
import Tkinter as tk
import ttk
import copy

#from PyStdVector import My1DArray
 
window = tk.Tk()


dataSource=[["Notebook Lenovo V15 ","9999","12999","Foxtrot.ua"],
            ["Smartphone Samsung Galaxy S20 FE (2021)","16999","18999","rozetka.com.ua"],
           ]
            
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
        self.L=L
        self.C=C
    def ShowConsole(self):
        print("L="+str(self.L)+" C="+str(self.C))

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
    def __init__(self, mstr, gui, contentSize, headerSize, activeRows, Align_Left1Top2Bottom3Right4=0, DfltWidth=40, rowOrder_LC0_CL1=1, tblView=0, dataSource=0, sourceOrder_LC0_CL1=1):
        self.gui=gui
        self.tblView=tblView
        self.rowOrder_LC0_CL1=rowOrder_LC0_CL1
        self.cntRowFrames=[]
        self.cntRows=[]
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
        print("Grid constructor: Size: QL="+str(self.QLines)+" C="+str(self.QColumns))
        print("Grid constructor: data cource length:"+str(len(dataSource)))
        print("Grid constructor - content size param:")
        contentSize.ShowConsole()
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
        self.HandleCells()
    #            
    def HandleCells(self):
        #curCntRowFrame
        #curCntRow
        #curCntCell
        if self.QLineHeaders>0:
            #NOp
            zero=0
        if self.QColumnHeaders>0:
            #NOp
            zero=0
        #content cells
        curCntRow=[]
        #curCntRowFrame=self.gui.Frame(master=self.contentFrame)#ce wa error
        if rowOrder_LC0_CL1==1:
            for ColN in range(1, self.QColumns+1):
                curCntRowFrame=self.gui.Frame(master=self.contentFrame)
                curCntRow=[]
                for LineN in range(1,self.QLines+1):
                    #MyNameText="cellContL"+str(LineN)+"C"+str(ColN)
                    coords=TableSize(LineN, ColN)
                    MyNameText=self.GenerateCellNameByCoords(coords)
                    if dataSource==0 or not isinstance(dataSource,list) or len(dataSource)==0:
                        MyText="BL"+str(LineN)+"C"+str(ColN)+MyNameText
                    else:
                        if sourceOrder_LC0_CL1==0:
                            MyText=str(dataSource[LineN-1][ColN-1])
                        else:
                            MyText=str(dataSource[ColN-1][LineN-1])
                    if LineN==self.ActiveLineN and ColN==self.ActiveColN:
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
            self.ActiveCell=self.cntRows[self.ActiveColN-1][self.ActiveLineN-1]
        else: #0
            for LineN in range(1,self.QLines+1):
                curCntRowFrame=self.gui.Frame(master=self.contentFrame)
                curCntRow=[]
                for ColN in range(1, self.QColumns+1):
                    #MyNameText="cellContL"+str(LineN)+"C"+str(ColN)#works well
                    coords=TableSize(LineN, ColN)
                    MyNameText=self.GenerateCellNameByCoords(coords)
                    if dataSource==0 or not isinstance(dataSource,list) or len(dataSource)==0:
                        MyText="BL"+str(LineN)+"C"+str(ColN)+MyNameText
                    else:
                        if sourceOrder_LC0_CL1==0:
                            MyText=str(dataSource[LineN-1][ColN-1])
                        else:
                            MyText=str(dataSource[ColN-1][LineN-1])
                    if LineN==self.ActiveLineN and ColN==self.ActiveColN:
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
            self.ActiveCell=self.cntRows[self.ActiveLineN-1][self.ActiveColN-1]
            
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
            self.cntRows[self.ActiveLineN-1][self.ActiveColN-1].configure(relief=self.gui.RIDGE)
            #print("Active L=",self.ActiveLineN," C=",self.ActiveColN)
        else:
            #self.cntRows[self.ActiveColN-1][self.ActiveLineN-1].configure(relief=self.gui.RAISED)
            self.cntRows[self.ActiveColN-1][self.ActiveLineN-1].configure(relief=self.gui.RIDGE)
            #print("Active L=",self.ActiveLineN," C=",self.ActiveColN)
        #making appearance of new active cell  active
        #event.widget.configure(relief=self.gui.SUNKEN)#works well, ma no need, ce s'done below ataly
        #event.widget.configure(name=NameText)# ne knows name
        #event.widget.configure(text=NameText)
        #event.widget.modify(event.widget['relief']=self.gui.SUNKEN)
        #post deactivation, ob mab ce same cell
        self.ActiveLineN=coords.L
        self.ActiveColN=coords.C
        if self.rowOrder_LC0_CL1==0:
            #self.cntRows[self.ActiveLineN-1][self.ActiveColN-1].configure(relief=self.gui.RAISED)
            self.cntRows[self.ActiveLineN-1][self.ActiveColN-1].configure(relief=self.gui.SUNKEN)
        else:
            #self.cntRows[self.ActiveColN-1][self.ActiveLineN-1].configure(relief=self.gui.RAISED)
            self.cntRows[self.ActiveColN-1][self.ActiveLineN-1].configure(relief=self.gui.SUNKEN)
        #print("Now: Active L=",self.ActiveLineN," C=",self.ActiveColN)
        #
        if self.tblView!=0:
            #print("grid is a part of table")
            cellContent=[]
            if self.rowOrder_LC0_CL1==0:
                cellContent.append(self.cntRows[self.ActiveLineN-1][self.ActiveColN-1]['text'])
            else:
                cellContent.append(self.cntRows[self.ActiveColN-1][self.ActiveLineN-1]['text'])
            self.tblView.combo_ChoosingData.configure(values=cellContent)
            #probe
            #print("cell content of new active cell: ",cellContent)
            #cellContent=[]
            #cellContent=self.tblView.combo_ChoosingData.configure(values=cellContent)#WTF& Qob py ne error
            self.tblView.combo_ChoosingData.configure(values=cellContent)
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

class TableView:
    def __init__(self, mstr, gui, contentSize, headerSize, activeRows, Align_Left1Top2Bottom3Right4=0, DfltWidth=40, rowOrder_LC0_CL1=1, dataSource=0, sourceOrder_LC0_CL1=1):
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
        self.frame_SupplToolbar=gui.Frame(master=self.tableViewMainFrame,  relief=tk.RIDGE)
        #self.grid=TableGridView(self.tableViewMainFrame, gui,        size, headerSize, ActiveCell, Align_Left1Top2Bottom3Right4,   DfltWidth, rowOrder_LC0_CL1)
        self.grid=TableGridView(self.tableViewMainFrame, gui,        contentSize, headerSize, ActiveCell, Align_Left1Top2Bottom3Right4,   DfltWidth, rowOrder_LC0_CL1, self, dataSource)
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
        
    
 
frame_a = tk.Frame(master=window,  relief=tk.RIDGE)
frame_b = tk.Frame(master=window)
frame_c = tk.Frame(master=window, relief=tk.GROOVE)
 
label_a = tk.Label(master=frame_a, text="I'm in Frame A", relief=tk.SUNKEN)
label_a.pack()
 
#label_b = tk.Label(master=frame_b, text="I'm in Frame B", relief=tk.RIDGE)
#label_b.pack()


size=TableSize(4,4)
ActiveCell=TableSize(1,1)
ActiveCell=TableSize(2,2)
headerSize=TableSize(1,1)

Align_Left1Top2Bottom3Right4=0
DfltWidth=20
rowOrder_LC0_CL1=0 #rowOrder_LC0_CL1=1
sourceOrder_LC0_CL1=0
contentSize=TableSize(len(dataSource),len(dataSource[0]))

print("Ef all:")
print("DS length=",len(dataSource)," DS width=",len(dataSource[0]))
sz=TableSize(len(dataSource),len(dataSource[0]))
print("DS size:")
sz.ShowConsole()

#def __init__(self, mstr,   gui, contentSize, headerSize, activeRows, Align_Left1Top2Bottom3Right4=0, DfltWidth=40, RowOrder_LC0_CL1=1)
#
#grid =    TableGridView(frame_b, tk,        size, headerSize, ActiveCell, Align_Left1Top2Bottom3Right4,   DfltWidth, rowOrder_LC0_CL1)
#self, mstr, gui, contentSize, headerSize, activeRows, Align_Left1Top2Bottom3Right4=0, DfltWidth=40, rowOrder_LC0_CL1=1, dataSource=0
grid =    TableView(frame_b, tk,        TableSize(len(dataSource),len(dataSource[0])), headerSize, ActiveCell, Align_Left1Top2Bottom3Right4,   DfltWidth, rowOrder_LC0_CL1, dataSource, sourceOrder_LC0_CL1)
#

#tbl=TableGrid(frame_b,tk, size)#also works
#
#ShowGrid(frame_b,tk, size, ActiveCell)
#
#grid.Show()
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

#grid.grid.ShowConsole()
 
window.mainloop()



