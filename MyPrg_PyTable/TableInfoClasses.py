
import TableReprSimple
from TableReprSimple import *

class TableSize:
    def __init__(self, L=1, C=1):
        if isinstance(L, int) and isinstance(C, int):
            self.L=L
            self.C=C
        elif isinstance(L, list) and len(L)==2 and isinstance(L[1-1], int) and isinstance(L[2-1], int):
            self.L=L[1-1]
            self.C=L[2-1]
    def ShowConsole(self):
        print("L="+str(self.L)+" C="+str(self.C))

    def CorrectActiveCellNByShownRowsNs(self, RowsNsLims):
        if self.L<RowsNsLims.L1:
            self.L=RowsNsLims.L1
        if self.L>RowsNsLims.L2:
            self.L=RowsNsLims.L2
        if self.C<RowsNsLims.C1:
            self.C=RowsNsLims.C1
        if self.C>RowsNsLims.C2:
            self.C=RowsNsLims.C2

class TRowsNsLims:
    def __init__(self, L1=1, C1=1, L2=0, C2=0, tblSize=0):
        self.L1=L1
        self.C1=C1
        if L1<1:
            self.L1=1
        if C1<1:
            self.C1=1
        if isinstance(tblSize, TableSize):
            if L2==0 or L2<L1 or L2>tblSize.L:
                self.L2=tblSize.L
            else:
                self.L2=L2
            if C2==0 or C2<C1 or C2>tblSize.C:
                self.C2=tblSize.C
            else:
                self.C2=C2
        else:
            self.L2=L1
            self.C2=C1

    def ContentGridLineNByTableLineN(self, TableLineN):
        return TableLineN-self.L1+1

    def TableLineNByContentGridLineN(self, GridLineN):
        return GridLineN+self.L1-1

    def ContentGridColNByTableColN(self, TableColN):
        return TableColN-self.L1+1

    def TableColNByContentGridColN(self, GridColN):
        return GridColN+self.L1-1

    def Correct(self, tblSize=0):
        if isinstance(tblSize, TableSize):
            if self.L2>tblSize.L:#so if 0
                self.L2=tblSize.L
            if self.C2>tblSize.C:#so if 0
                self.C2=tblSize.C
        if self.L1>self.L2:
            self.L1=self.L2
        if self.C1>self.C2:
            self.C1=self.C2
        if self.L1<1:
            self.L1=1
        if self.C1<1:
            self.C1=1

    def AddNextLine(self, tblSize=0):
        if not (isinstance(tblSize, TableSize) and self.L2>=tblSize.L):
            self.L2=self.L2+1
        self.Correct(tblSize)

    def AddPrevLine(self, tblSize=0):
        if self.L1>1:
            self.L1=self.L1-1
        self.Correct(tblSize)

    def AddNextColumn(self, tblSize=0):
        if not (isinstance(tblSize, TableSize) and self.C2>=tblSize.C):
            self.C2=self.C2+1
        self.Correct(tblSize)

    def AddPrevColumn(self, tblSize=0):
        if self.C1>1:
            self.C1=self.C1-1
        self.Correct(tblSize)

    def DelNextLine(self, tblSize=0):
        if not (self.L2<=self.L1):
            self.L2=self.L2-1
        self.Correct(tblSize)

    def DelPrevLine(self, tblSize=0):
        if not(self.L1>=self.L2):
            self.L1=self.L1+1
        self.Correct(tblSize)

    def DelNextColumn(self, tblSize=0):
        if not(self.C2<=self.C1):
            self.C2=self.C2-1
        self.Correct(tblSize)

    def DelPrevColumn(self, tblSize=0):
        if not(self.C1>=self.C2):
            self.C1=self.C1+1
        self.Correct(tblSize)

    def ShiftLinesToNext(self, tblSize=0):
        if not (isinstance(tblSize, TableSize) and self.L2>=tblSize.L):
            self.L2=self.L2+1
            self.L1=self.L1+1
        self.Correct(tblSize)

    def ShiftLinesToPrev(self, tblSize=0):
        if self.L1>1:
            self.L1=self.L1-1
            self.L1=self.L1-1
        self.Correct(tblSize)

    def ShiftColumnsToNext(self, tblSize=0):
        if not (isinstance(tblSize, TableSize) and self.C2>=tblSize.C):
            self.C2=self.C2+1
            self.C1=self.C1+1
        #self.Correct(tblSize)

    def ShiftColumnsToPrev(self, tblSize=0):
        if self.C1>1:
            self.C1=self.C1-1
            self.C2=self.C2-1
        self.Correct(tblSize)

    def SetFirst(self):
        self.L1=1
        self.C1=1
        self.L2=self.L1
        self.C2=self.C1
        #self.Correct(tblSize)

    def SetFull(self, tblSize=0):
        self.SetFirst()
        if isinstance(tblSize, TableSize):
            self.L2=tblSize.L
            self.C2=tblSize.C
        self.Correct(tblSize)
            

class TableGUIControls:
    def __init__(self):
        #self.Array_Text1_Combobox2=2
        self.Array_ActiveNText1_ActiveItemText2_Combobox3=3
        self.Bool_Text1_Combobox2_CheckBox3=3
        self.Control_GUI0_Controller1_Direct2=1
        self.Align_Left1Top2Bottom3Right4=2#1#3
        self.structRowOrder_LC0_CL1=0

    def ToTable(self):
        pass
        tbl=TableController2()
        itemsForArray=["ActiveNText", "ActiveItemText", "Combobox"]
        itemsForBool=["Text", "Combobox", "CheckBox"]
        itemsForControlMethods=["GUI", "Controller", "Direct"]
        itemsForRowOrder=["array of Lines", "array of Columns"]
        itemsForAlign=["Left", "Top", "Bottom", "Right"]
        content=[DataCell(itemsForArray, self.Array_ActiveNText1_ActiveItemText2_Combobox3),
                 DataCell(itemsForBool, self.Bool_Text1_Combobox2_CheckBox3),
                 DataCell(itemsForControlMethods,self. Control_GUI0_Controller1_Direct2+1),
                 DataCell(itemsForControlMethods, self.structRowOrder_LC0_CL1+1),
                 DataCell(itemsForControlMethods, self.Align_Left1Top2Bottom3Right4)]
        header=TableHeaders("Table GUI Controls", "Params")
        #tbl.Set
        return tbl

    def GetFromTable(self, tbl):
        pass
        #self.Array_Text1_Combobox2=tbl.Get

class TableUssagePolicy:
    def __init__(self):
        self.AllowShowTableInfo=0
        #
        self.AllowAddLine=1
        self.AllowInsLine=1
        self.AllowDelLine=1
        #
        self.AllowAddColumn=1
        self.AllowInsColumn=1
        self.AllowDelColumn=1
        #
        self.AllowAddBoth=1
        self.AllowInsBoth=1
        self.AllowDelBoth=1
        #
        self.AllowReplaceLines=1
        self.AllowReplaceColumns=1
        self.AllowReplaceCells=1
        #self.AllowReplaceBoth=1
        #
        self.AllowEditContentCells=1
        self.AllowEditLineOfColHeaderCells=1
        self.AllowEditColOfLineHeaderCells=1
        self.AllowEditLinesGeneralName=1
        self.AllowEditColumnsGeneralName=1
        self.AllowEditTableName=1

    def ToString(self):
        s=""
        s=s+" AllowShowTableInfo="
        s=s+str(self.AllowShowTableInfo)
        #
        s=s+" AllowAddLine="
        s=s+str(self.AllowAddLine)
        s=s+" AllowInsLine="
        s=s+str(self.AllowInsLine)
        s=s+" AllowDelLine="
        s=s+str(self.AllowDelLine)
        #
        s=s+" AllowAddColumn="
        s=s+str(self.AllowAddColumn)
        s=s+" AllowInsColumn="
        s=s+str(self.AllowInsColumn)
        s=s+" AllowDelColumn="
        s=s+str(self.AllowDelColumn)
        #
        s=s+" AllowAddBoth="
        s=s+str(self.AllowAddBoth)
        s=s+" AllowInsBoth="
        s=s+str(self.AllowInsBoth)
        s=s+" AllowDelBoth="
        s=s+str(self.AllowDelBoth)
        #
        s=s+" AllowReplaceLines="
        s=s+str(self.AllowReplaceLines)
        s=s+" AllowReplaceColumns="
        s=s+str(self.AllowReplaceColumns)
        s=s+" AllowReplaceCells="
        s=s+str(self.AllowReplaceCells)
        #self.AllowReplaceBoth)
        #
        s=s+" AllowEditContentCells="
        s=s+str(self.AllowEditContentCells)
        s=s+" AllowEditLineOfColHeaderCells="
        s=s+str(self.AllowEditLineOfColHeaderCells)
        s=s+" AllowEditColOfLineHeaderCells="
        s=s+str(self.AllowEditColOfLineHeaderCells)
        s=s+" AllowEditLinesGeneralName="
        s=s+str(self.AllowEditLinesGeneralName)
        s=s+" AllowEditColumnsGeneralName="
        s=s+str(self.AllowEditColumnsGeneralName)
        s=s+" AllowEditTableName="
        s=s+str(elf.AllowEditTableName)
        #
        return s

    def LinesOnly(self):
        self.AllowAddLine=1
        self.AllowInsLine=1
        self.AllowDelLine=1
        self.AllowAddColumn=0
        self.AllowInsColumn=0
        self.AllowDelColumn=0
        self.AllowAddBoth=0
        self.AllowInsBoth=0
        self.AllowDelBoth=0

    def ColumnsOnly(self):
        self.AllowAddLine=0
        self.AllowInsLine=0
        self.AllowDelLine=0
        self.AllowAddColumn=1
        self.AllowInsColumn=1
        self.AllowDelColumn=1
        self.AllowAddBoth=0
        self.AllowInsBoth=0
        self.AllowDelBoth=0

    def BothOnly(self):
        self.AllowAddLine=0
        self.AllowInsLine=0
        self.AllowDelLine=0
        self.AllowAddColumn=0
        self.AllowInsColumn=0
        self.AllowDelColumn=0
        self.AllowAddBoth=1
        self.AllowInsBoth=1
        self.AllowDelBoth=1

    def AllowChangeRowsQuantityAll(self):
        #self.AllowShowTableInfo=1
        #
        self.AllowAddLine=1
        self.AllowInsLine=1
        self.AllowDelLine=1
        #
        self.AllowAddColumn=1
        self.AllowInsColumn=1
        self.AllowDelColumn=1
        #
        self.AllowAddBoth=1
        self.AllowInsBoth=1
        self.AllowDelBoth=1
        #
        #self.AllowReplaceLines=1
        #self.AllowReplaceColumns=1
        #self.AllowReplaceCells=1
        #self.AllowReplaceBoth=1
        #
        #self.AllowEditContentCells=1
        #self.AllowEditLineOfColHeaderCells=1
        #self.AllowEditColOfLineHeaderCells=1
        #self.AllowEditLinesGeneralName=1
        #self.AllowEditColumnsGeneralName=1
        #self.AllowEditTableName=1

    def AllowEditAll(self):
        #self.AllowShowTableInfo=1
        #
        #self.AllowAddLine=1
        #self.AllowInsLine=1
        #self.AllowDelLine=1
        #
        #self.AllowAddColumn=1
        #self.AllowInsColumn=1
        #self.AllowDelColumn=1
        #
        #self.AllowAddBoth=1
        #self.AllowInsBoth=1
        #self.AllowDelBoth=1
        #
        #self.AllowReplaceLines=1
        #self.AllowReplaceColumns=1
        #self.AllowReplaceCells=1
        #self.AllowReplaceBoth=1
        #
        self.AllowEditContentCells=1
        self.AllowEditLineOfColHeaderCells=1
        self.AllowEditColOfLineHeaderCells=1
        self.AllowEditLinesGeneralName=1
        self.AllowEditColumnsGeneralName=1
        self.AllowEditTableName=1

    def AllowReplaceAll(self):
        #self.AllowShowTableInfo=1
        #
        #self.AllowAddLine=1
        #self.AllowInsLine=1
        #self.AllowDelLine=1
        #
        #self.AllowAddColumn=1
        #self.AllowInsColumn=1
        #self.AllowDelColumn=1
        #
        #self.AllowAddBoth=1
        #self.AllowInsBoth=1
        #self.AllowDelBoth=1
        #
        self.AllowReplaceLines=1
        self.AllowReplaceColumns=1
        self.AllowReplaceCells=1
        self.AllowReplaceBoth=1
        #
        #self.AllowEditContentCells=1
        #self.AllowEditLineOfColHeaderCells=1
        #self.AllowEditColOfLineHeaderCells=1
        #self.AllowEditLinesGeneralName=1
        #self.AllowEditColumnsGeneralName=1
        #self.AllowEditTableName=1

    def AllowAll(self):
        self.AllowChangeRowsQuantityAll()
        self.AllowEditAll()
        self.AllowReplaceAll()

    def ForbidChangeRowsQuantityAll(self):
        #self.AllowShowTableInfo=0
        #
        self.AllowAddLine=0
        self.AllowInsLine=0
        self.AllowDelLine=0
        #
        self.AllowAddColumn=0
        self.AllowInsColumn=0
        self.AllowDelColumn=0
        #
        self.AllowAddBoth=0
        self.AllowInsBoth=0
        self.AllowDelBoth=0
        #
        #self.AllowReplaceLines=0
        #self.AllowReplaceColumns=0
        #self.AllowReplaceCells=0
        #self.AllowReplaceBoth=1
        #
        #self.AllowEditContentCells=0
        #self.AllowEditLineOfColHeaderCells=0
        #self.AllowEditColOfLineHeaderCells=0
        #self.AllowEditLinesGeneralName=0
        #self.AllowEditColumnsGeneralName=0
        #self.AllowEditTableName=0

    def ForbidEditAll(self):
        #self.AllowShowTableInfo=0
        #
        #self.AllowAddLine=0
        #self.AllowInsLine=0
        #self.AllowDelLine=0
        #
        #self.AllowAddColumn=0
        #self.AllowInsColumn=0
        #self.AllowDelColumn=0
        #
        #self.AllowAddBoth=0
        #self.AllowInsBoth=0
        #self.AllowDelBoth=0
        #
        #self.AllowReplaceLines=0
        #self.AllowReplaceColumns=0
        #self.AllowReplaceCells=0
        #self.AllowReplaceBoth=1
        #
        self.AllowEditContentCells=0
        self.AllowEditLineOfColHeaderCells=0
        self.AllowEditColOfLineHeaderCells=0
        self.AllowEditLinesGeneralName=0
        self.AllowEditColumnsGeneralName=0
        self.AllowEditTableName=0

    def ForbidReplaceAll(self):
        #self.AllowShowTableInfo=0
        #
        #self.AllowAddLine=0
        #self.AllowInsLine=0
        #self.AllowDelLine=0
        #
        #self.AllowAddColumn=0
        #self.AllowInsColumn=0
        #self.AllowDelColumn=0
        #
        #self.AllowAddBoth=0
        #self.AllowInsBoth=0
        #self.AllowDelBoth=0
        #
        self.AllowReplaceLines=0
        self.AllowReplaceColumns=0
        self.AllowReplaceCells=0
        self.AllowReplaceBoth=1
        #
        #self.AllowEditContentCells=0
        #self.AllowEditLineOfColHeaderCells=0
        #self.AllowEditColOfLineHeaderCells=0
        #self.AllowEditLinesGeneralName=0
        #self.AllowEditColumnsGeneralName=0
        #self.AllowEditTableName=0

    def ForbidAll(self):
        self.ForbidChangeRowsQuantityAll()
        self.ForbidEditAll()
        self.ForbidReplaceAll()

    def AllowerivativeTables(self):
        self.AllowShowTableInfo=1

    def ForbidDerivativeTables(self):
        self.AllowShowTableInfo=0

    #class TableSize

class TableInfo1:
    def __init__(self):
        self.ussagePolicy=TableUssagePolicy()
        self.repr=TableRepr()
