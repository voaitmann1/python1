import math
import copy

import PyStdVector#.py



#  field\cell   |     item          |      suppl
#------------------------------------------------------
#Simple         |  value:  not []   |        -
#ComboboxOrMemo |  items:       []  |  activeN: not []      
#DBFldHdr       |  items:       []  |     names: []

#  field\cell   |   data            |   names
#--------------------------------------------------
#Simple         |  value:   not []  |     -
#ComboboxOrMemo |  activeN: not []  |  items: []       
#DBFldHdr       |  items:       []  |  names: []

#  field\cell    |   data            |   items     | DBFldInf
#-------------------------------------------------------------
# Simple         |  value:   not []  |     -       |    -
# ComboboxOrMemo |  activeN: not []  |  items: []  |    -    
# DBFldHdr       |  names:       []  |  items: []  |  int []


 

class DataCell_Simple:
    def GetType(self):
         return 1
    #    return 1 #1- simple, 3-combobox, , 2-DBFldHdr
    def __init__(self, val=""):
        self.data=val
    def GetVal(self, N=1):
        return self.data

    def GetItem(self, N=1):
        return self.data

    # ConcrType
    def GetFloatVal(self):
        return float(self.data)

    def GetIntVal(self):
        return int(self.data)

    def GetBoolVal(self):
        return bool(self.data)

    def GetStrVal(self):
        return str(self.data)

    # for combobox
    def GetActiveN(self):
        return 1

    def GetActiveItem(self):
        return self.data

    def SetActiveN(self, val):
        zero=0
        #

    def SetActiveNByVal(self, val):
        zero=0
        #

    def GetQItems():
        return 1

    def GetQNames():
        return 1

    # for database
    def GetName(self, N=1):
        return self.GetVal(N)

    def SetName(self, names, N=0):
        self.data = names
    def SetItem(self, items, N=0):
        self.SetName(items,N)

    #
    def Set(self, var1=[], var2=[], var3=[]):
        self.data = var1
        
    def ToString(self, str_bef="", str_aft=""):  # new 2021-08-12
        #return "cell id="+str(id(self))+" content: "+str(self.GetName())+" "
        return str_bef+str(self.GetName())+str_aft
    def GetFieldType(self):
        return 0
    def GetFieldWidth(self):
        return 0
    def GetFieldLength(self):
        return 0
    def GetFieldCharacteristics(self):
        return 0
    def SetFieldType(self,val):
        zero=0
        #
    def SetFieldWidth(self,val):
        zero=0
        #
    def SetFieldCharacteristics(self,val):
        zero=0
        #


class DataCell_ComboboxOrMemo:
    def GetType(self):
         return 3
    #    return 1 #1- simple, 3-combobox, , 2-DBFldHdr
    def __init__(self, data=1, items=[]):
        self.data=data#1
        self.items=items#[]
    #def __init__(self):
    #    DataCell_Simple.__init__(self)#self.data=""
    #    self.items=[]
    def GetVal(self):
        #return self.data
        return self.GetItem( self.data)#self.items[self.data-1]

    def GetItem(self, N=0):
        R = 0
        if isinstance(self.items, list):
            Q = MyLibPy2.ArrayLength(self.items)
            if N >= 1 and N <= Q:
                R = self.items[N - 1]
            else:
                R = self.items[self.data-1]
        else:
            R = self.items[self.data-1]
        return R

    # ConcrType
    def GetFloatVal(self):
        return float(GetVal(self))

    def GetIntVal(self):
        return int(GetVal(self))

    def GetBoolVal(self):
        return bool(GetVal(self))#here must be own function!

    def GetStrVal(self):
        return str(GetVal(self))
   

    # for combobox
    def GetActiveN(self):
        return self.data

    def GetActiveItem(self):
        return self.items[self.data-1]

    def SetActiveN(self, val):
        N=int(val)
        Q=MyLibPy2.ArrayLength(self.items)
        if N>=1 and N<=self.Q:
            self.data=N

    def SetActiveNByVal(self, val):
        N=0
        for item in items:
            N+=1
            if val==items:
                self.data=N

    def GetQItems():
        R = 0
        if not isinstance(self.items, list):
            R = 1
        else:
            R = MyLib.ArrayLength(self.items)
        return R

    def GetQNames():
        return self.GetQItems()

    def GetName(self, N=0):
        return self.GetItem(N)

    # for database
    def SetName(self, names, N=0):
        self.SetItem(names, N)
           
    def SetItem(self, items, N=0):
        Q=MyLibPy2.ArrayLength(self.items)
        if isinstance(items, list):
           self.items = items
        else:
           if N>=1 and N<=Q:
               self.items[N-1]=items

    def SetName(self, names, N=0):
        self.items = names
    #
    def Set(self, var1=[], var2=[], var3=[]):
        #DataCell_Simple.Set(var1, var2, var3)
        self.data=var1
        self.items = var2

    def ToString(self):  # new 2021-08-12
        #return "cell id="+str(id(self))+" content: "+str(self.GetName())+" "
        return str(self.GetName())
    #
    def GetFieldType(self):
        return 0
    def GetFieldWidth(self):
        return 0
    def GetFieldLength(self):
        return 0
    def GetFieldCharacteristics(self):
        return 0
    def SetFieldType(self,val):
        zero=0
        #
    def SetFieldWidth(self,val):
        zero=0
        #
    def SetFieldCharacteristics(self,val):
        zero=0
        #


class DataCell_DBFldHdr (DataCell_ComboboxOrMemo):
    def GetType(self):
         return 2
    #    return 1 #1- simple, 3-combobox, , 2-DBFldHdr
    #def __init__(self):
    #    self.DBFldInfo=[]
    def __init__(self, data=[], items=[], DBFldInfo=[]):
        #DataCell_ComboboxOrMemo.__init__(self)#self.items=[] remains, self.data=0 wi redef'd
        #DataCell_ComboboxOrMemo.data=[]#why not redef
        if isinstance(data, list):
            self.data=data
        else:
            self.data=[]
        if isinstance(data, list):
            self.items=items
        else:
            self.items=[]
        if isinstance(DBFldInfo, list):
            self.DBFldInfo=DBFldInfo
        else:
            self.DBFldInfo=[]
    def GetVal(self):
        #return self.data
        return self.GetName(self)

    def GetItem(self, N=0):
        R = 0
        if isinstance(self.items, list):
            Q = MyLibPy2.ArrayLength(self.items)
            if N >= 1 and N <= Q:
                R = self.items[N - 1]
        else:
            R = self.items[self.data-1]
        return R

    # ConcrType
    def GetFloatVal(self):
        return float(GetVal(self))

    def GetIntVal(self):
        return int(GetVal(self))

    def GetBoolVal(self):
        return bool(GetVal(self))#here must be own function!

    def GetStrVal(self):
        return str(GetVal(self))
   

    # for combobox
    def GetActiveN(self):
        return 0

    def GetActiveItem(self):
        return self.GetItem(0)

    def SetActiveN(self, val):
        zero=0
        #

    def SetActiveNByVal(self, val):
        pass
        #if isinstance(self.item, list) and self.item.count(val) > 0:
        #    self.SupplInf = self.item.index(val)

    def GetQItems():
        R = 0
        if not isinstance(self.items, list):
            R = 1
        else:
            R = MyLibPy2.ArrayLength(self.items)
        return R

    def GetQNames():
        R = 0
        if not isinstance(self.data, list):
            R = 1
        else:
            R = MyLibPy2.ArrayLength(self.data)
        return R

     # for database
    def GetName(self, N=1):
        R = 0
        if isinstance(self.data, list):
            Q = MyLibPy2.ArrayLength(self.data)
            if N >= 1 and N <= Q:
                R = self.data[N - 1]
        elif self.data == []:
            R = self.data
        else:
            R = self.data
        return R

    def SetName(self, names, N=0):
        Q=MyLibPy2.ArrayLength(self.data)
        if isinstance(names, list):
           self.data = names
        else:
           if N>=1 and N<=Q:
               self.data[N-1]=names
           
    def SetItem(self, items, N=0):
        Q=MyLibPy2.ArrayLength(self.items)
        if isinstance(items, list):
           self.items = items
        else:
           if N>=1 and N<=Q:
               self.items[N-1]=items

    #
    def Set(self, var1=[], var2=[], var3=[]):
        #DataCell_Simple.Set(var1, var2, var3)
        self.data = var1
        self.items = var2
        self.DBFldInfo=var3

    def ToString(self):  # new 2021-08-12
        #return "cell id="+str(id(self))+" content: "+str(self.GetName())+" "
        return str(self.GetName()) + " "
    #
    def GetFieldType(self):
        return self.DBFldInfo[1-1]
    def GetFieldWidth(self):
        return self.DBFldInfo[2-1]
    def GetFieldLength(self):
        return self.DBFldInfo[3-1]
    def GetFieldCharacteristics(self):
        return self.DBFldInfo[4-1]
    def SetFieldType(self,val):
        self.DBFldInfo[1-1]=val
        #
    def SetFieldWidth(self,val):
        self.DBFldInfo[2-1]=val
        #
    def SetFieldCharacteristics(self,val):
        self.DBFldInfo[4-1]=val
        #

class DataCell:
    def __init__(self, data="", items=0, DBFldInfo=0):
        if ((isinstance(data, list))and (isinstance(items, list))):
            self.cell
            self.cell=DataCell_Simple()
    def Set_Simple(self,var1):
        self.cell=DataCell_Simple()
        self.cell.Set(var1)
    def Set_ComboboxOrMemo(self,var1, var2):
        self.cell=DataCell_ComboboxOrMemo()
        self.cell.Set(var1, var2)
    def Set_DBFldHdr(self,var1, var2, var3):
        self.cell=DataCell_DBFldHdr()
        self.cell.Set(var1, var2, var3)
    #
    def GetType(self):
         return self.cell.GetType()
    
    def GetVal(self):
        return self.cell.GetVal()

    def GetItem(self, N=0):
        return self.cell.GetItem(N)

    # ConcrType
    def GetFloatVal(self):
        return self.cell.GetFloatVal()

    def GetIntVal(self):
        return self.cell.GetIntVal()

    def GetBoolVal(self):
        return self.cell.GetBoolVal()

    def GetStrVal(self):
        return self.cell.GetStrVal()
   

    # for combobox
    def GetActiveN(self):
        return self.cell.GetActiveN()

    def GetActiveItem(self):
        return self.cell.GetActiveItem()

    def SetActiveN(self, val):
        self.cell.SetActiveN(val)
        #

    def SetActiveNByVal(self, val):
        self.cell.SetActiveNByVal(val)

    def GetQItems(self):
        return self.cell.GetQItems()

    def GetQNames(self):
        return self.cell.GetQNames()

     # for database
    def GetName(self, N=1):
        return self.cell.GetName(N)

    def SetName(self, names, N=0):
        self.cell.SetName(names, N)

    #
    def Set(self, var1=[], var2=[], var3=[]):
        self.cell.Set(var1, var2, var3)

    def ToString(self):  
        return self.cell.ToString()
    #
    def GetFieldType(self):
        return self.cell.GetFieldType()
    def GetFieldWidth(self):
        return self.cell.GetFieldWidth()
    def GetFieldCharacteristics(self):
        return self.cell.GetFieldCharacteristics()
    #
    def SetFieldType(self, TypeN):
        self.cell.SetFieldType(TypeN)    #
    def SetFieldWidth(self, val):
        self.cell.SetFieldWidth(val)
    def SetFieldLength(self, val):
        self.cell.SetFieldLength(val)
    def SetFieldCharacteristics(self, val):
        self.cell.SetFieldCharacteristics(val)
        #
    def ToString(self):
        return self.GetStrVal()

    def __str__(self):
        return ToString()
        

print("\n\nChecking Cells\n")
CellArr=[]
#CellArr[1-1] = DataCell_Simple()
cell= DataCell_Simple()
CellArr.append(cell)
#CellArr[2-1] = DataCell_ComboboxOrMemo()
cell= DataCell_ComboboxOrMemo()
CellArr.append(cell)
#CellArr[2-1] = DataCell_DBFldHdr()
cell = DataCell_DBFldHdr()
CellArr.append(cell)
CellArr[1-1].Set("red")
CellArr[2-1].Set(2, ["white", "blue", "red"])
CellArr[3-1].Set(["Column # 1 !", "Col1", "Column"], ["Item1", "Item2", "Item3"], [1, 2, 3])
N=0
for everyone in CellArr:
    N+=1
    print("Cell ",N," :")
    s = CellArr[N-1].GetActiveN()
    print("activeN=", s)
    s = CellArr[N-1].GetActiveItem()
    print("Active Item=", s)
    s = CellArr[N-1].GetName(2)
    print("name N2=", s)
    s = CellArr[N-1].GetVal()
    print("val=", s)
    s = CellArr[N-1].ToString()  # new
    print("val s =", s)
#


class DataCellRow:
    #row = []
    def __init__(self):
        self.row = []
        
        
    def GetCell(self, cellN=0):
        R = 0
        Q = self.ArrayLength(self.row)
        if cellN >= 1 and cellN <= Q:
            R = self.row[cellN - 1]
        #elif cellN==0:
        #    R=self.header
        return R
    
    def Set(self, arr, header=0):
        #Q=MyLibPy2.ArrayLength(arr)
        #print("DataCellRow.Set starts working")
        #print("Adding ",Q, " items")
        #
        self.row=copy.deepcopy(arr)
        self.header=copy.deepcopy(header)
        #Q=MyLibPy2.ArrayLength(arr)
        #print("DataCellRow.Set finishes working")

    def GetHeader(self):
        return self.header

    def GetLength(self):
        return MyLibPy2.ArrayLength(self.row)

    def GetLengthN(self, cellN):
        R=0
        if cellN>=1 and cellN<=Q:
            R=self.row[cellN-1].GetQItems()
        elif cellN==0 and self.header!=0:
            R=self.header.GetLength()
        return R

    def GetName(self, NameN=1, CellN=0):
        R = ""
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    R=self.row[N-1].GetName(NameN)
        #elif cellN==0:
        #    R=self.header.GetName(NameN)
        cell=self.GetCell(cellN)
        if isinstace(cell, DataCell):
            R=cell.GetName(NameN)
        return R

    def GetQItems(self, cellN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        if cellN>=1 and CellN<=Q:
            R=self.row[N-1].GetQItems()
        #elif CellN==0:
        #    R=self.header.GetQItems()
        return R

    def GetQNames(self, cellN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    R=self.row[N-1].GetQNames()
        if cellN>=1 and CellN<=Q:
            R=self.row[cellN-1].GetQNames()
        #elif cellN==0 and isinstance(self.header, DataCell):
        #    R=self.header.GetQNames()
        return R

    def GetTypeN(self, cellN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    R=self.row[N-1].GetType()
        if cellN>=1 and cellN<=Q:
            R=self.row[N-1].GetTypeN()
        #elif cellN==0 and isinstance(self.header, DataCell):
        #    R=self.header.GetTypeN()
        return R

    def GetActiveN(self, cellN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    R=self.row[N-1].GetActiveN()
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetActiveN()
        return R

    def GetActiveItem(self, cellN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    R=self.row[N-1].GetActiveItem()
        if cellN>=1 and cellN<=Q:
            R=self.row[N-1].GetActiveItem()
        #elif cellN==0 and isinstance(self.header, DataCell):
        #    R=self.header.GetActiveItem()
        return R

   

    def SetActiveNByVal(self, cellN, val):
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        if cellN>=1 and cellN<=Q:
            self.row[cellN-1].SetActiveNByVal(val)
        #elif cellN==0:
        #    self.header.SetActiveNByVal(val)
    
    def GetVal(self, cellN=0, valN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            #if cellN>=0 and cellN<=Q:
            activeN=self.GetActiveNOfN(cellN)
            cellLength=self.GetLengthN(cellN)
            if valN<=0 or valN>cellLength:
                valN=activeN
            R=cell.GetVal(valN)
        return R

    def GetItem(self, cellN, valN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            #activeN=self.GetActiveNOfN(cellN)
            #cellLength=self.GetLengthN(cellN)
            activeN=cell.GetActiveN()
            cellLength=cell.GetLengthN(cellN)
            if valN<=0 or valN>cellLength:
                valN=activeN
            R=self.row[cellN-1].GetItem(valN)
        return R


    def GetFloatVal(self, cellN=0):
        R=0
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetFloatVal()
        return R

    def GetIntVal(self, cellN=0):
        R=0
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetIntVal()
        return R

    def GetBoolVal(self, cellN, valN=0):
        R=0
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetBoolVal()
        return R

    def GetStrVal(self, cellN, valN=0):
        R=0
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetStrVal()
        return R
        
        
    def SetName(self, names, cellN=0, nameN=0):
        Q=len(self.row)
        #i#f(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    self.row[cellN-1].SetName(names, nameN)
        if cellN>=1 and cellN<=Q:
            self.row[cellN-1].SetName(names, nameN)
        #elif:
        #    self.header.SetName(names, nameN)
        return R
        
    def SetItem(self, cellN, names, itemN=0):
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        if cellN>=1 and cellN<=0:
            self.row[cellN-1].SetItem(names, itemN)
        elif cellN==0:
            self.header.SetItem(names, itemN)
            
            

    def Add(self, cellExt):
        cell=copy.deepcopy(cellExt)
        #ArrayAdd(self.row, cell)
        self.row.append(cell)

    def InsN(self, cellExt, N=0):
        row=[]
        Q=len(self.row)
        cell=copy.deepcopy(cellExt)
        #if N==0:
        #    N=Q
        #if N==1 or N==0:
        #    self.row.append(cell)
        #else:
        if N>=1 and N<=Q:
            for i in range(1, N-1+1):
                row.append(self.row[i-1])
            row.append(cell)
            for i in range(N, Q+1):
                row.append(self.row[i-1])
            self.row=row

    def DelN(self, N=0):
        row=[]
        Q=len(self.row)
        cell=copy.deepcopy(cellExt)
        if N==0:
            N=Q
        if N>=1 and N<=Q:
            for i in range(1, N-1+1):
                row.append(self.row[i-1])
            row.append(cell)
            for i in range(N, Q+1):
                row.append(self.row[i-1])
        

    def GetFieldType(self, cellN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        activeN=self.GetActiveNOfN(cellN)
        cellLength=self.GetLengthN(cellN)
        #if cellN>0:
        cell=GetCell(cellN)
            #activeN=self.GetActiveNOfN(cellN)
            #cellLength=self.GetLengthN(cellN)
            #R=self.row[cellN-1].GetFieldType()
        if isinstance(cell, DataCell):
            R=cell.GetFieldType()
        return R

    def GetFieldWidth(self, cellN):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #activeN=self.GetActiveNOfN(cellN)
        #cellLength=self.GetLengthN(cellN)
        #R=self.row[cellN-1].GetFieldWidth()
        cell=GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetFieldWidth()
        return R

    def GetFieldLength(self, cellN):
        R=0
        Q=len(self.row)
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetFieldLength()
        return R

    def GetFieldType(self, cellN):
        R=0
        Q=len(self.row)
        cell=GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetFieldType()
        return R


    def SetFieldType(self, cellN, TypeN):
        Q=len(self.row)
        if cellN>=1 and cellN<=Q:
            self.row[cellN-1].SetFieldType(TypeN)
        

    def SetFieldWidth(self, cellN, val):
        Q=len(self.row)
        if cellN>=1 and cellN<=Q:
            self.row[cellN-1].SetFieldWidth(val)
        #elif cellN==0:
        #    self.header.SetFieldWidth(val)

    def SetFieldChateristics(self, val, cellN=0):
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        if cellN>=1 and cellN<=Q:
            self.row[cellN-1].SetFieldChateristics(val)
        #elif cellN==0:
        #    self.header.SetFieldChateristics(val)



    def ToStringN(self, cellN=0):
        R=""
        Q=len(self.row)
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.ToString()
        return R


    def ToString(self, str_btw=" "):
        #Q=MyLibPy2.ArrayLength(self.row)
        R = ""
        R = "Row #"+str(id(self))+": "+str(Q)+" elements: "
        #Q=MyLibPy2.ArrayLength(self.row)
        Q=len(self.row)
        for i in range(1, Q):#seems Q not including, ce for 1..Q-1
            R=R+self.row[i-1].ToString()
            R=R+str_btw
        if Q>0:
            R=R+self.row[Q-1].ToString()
        return R

    def ToString(self, separator=" ", ShowHeaderLine=0):
        R = ""
        if(ShowHeaderLine!=0):
            R = "Row #"+str(id(self))+": "+str(Q)+" elements: "
            R=R+separator
        Q=len(self.row)
        for i in range(1, Q-1+1):
            R=R+ToStringN(i)
            R=R+separator
        if Q>0:
            R=R+ToStringN(Q)
        return R

    def __str__(self):
        return self.ToString()
#DataCellRow

   


class DataCellRowWithHeader:
    #row = []
    def __init__(self, row=[], header=0):
        #self.row = []
        if(isinstance(row, DataCellRow)):
            self.row =copy.deepcopy(row)
        elif(isinstance(row, list)):
            self.row=DataCellRow(copy.deepcopy(row))
        else:
            self.row = DataCellRow()
        self.header=header#0
        
    def GetCell(self, cellN=0):
        R = 0
        Q = self.ArrayLength(self.row)
        if cellN >= 1 and cellN <= Q:
            #R = self.row[cellN - 1]
            R = self.row.GetCell(cellN)
        elif cellN==0:
            R=self.header
        return R
    
    def Set(self, row, header=0):
        #Q=MyLibPy2.ArrayLength(arr)
        #print("DataCellRow.Set starts working")
        #print("Adding ",Q, " items")
        #
        if(isinstance(row, DataCellRow)):
            self.row =copy.deepcopy(row)
        elif isinstance(row, list):
            self.row=DataCellRow(copy.deepcopy(row))
        self.header=copy.deepcopy(header)
        #Q=MyLibPy2.ArrayLength(arr)
        #print("DataCellRow.Set finishes working")

    def GetHeader(self):
        return self.header

    def GetLength(self):
        return MyLibPy2.ArrayLength(self.row)

    def GetLengthN(self, cellN):
        R=0
        if cellN==0 and self.header!=0:
            R=self.header.GetLength()
        elif cellN>=1 and cellN<=Q:
            R=self.row.GetQItems(cellN)
        return R

    def GetName(self, NameN=1, CellN=0):
        R = ""
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    R=self.row[N-1].GetName(NameN)
        #elif cellN==0:
        #    R=self.header.GetName(NameN)
        cell=self.GetCell(cellN)
        if isinstace(cell, DataCell):
            R=cell.GetName(NameN)
        return R

    def GetQItems(self, cellN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        if cellN>=1 and CellN<=Q:
            #R=self.row[N-1].GetQItems()
            R=self.row.GetQItems(cellN)
        elif CellN==0:
            R=self.header.GetQItems()
        return R

    def GetQNames(self, cellN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    R=self.row[N-1].GetQNames()
        if cellN>=1 and CellN<=Q:
            #R=self.row[cellN-1].GetQNames()
            R=self.row.GetQNames(CellN)
        elif cellN==0 and isinstance(self.header, DataCell):
            R=self.header.GetQNames()
        return R

    def GetTypeN(self, cellN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    R=self.row[N-1].GetType()
        if cellN>=1 and cellN<=Q:
            #R=self.row[N-1].GetTypeN()
            R=self.row.GetTypeN(cellN)
        elif cellN==0 and isinstance(self.header, DataCell):
            R=self.header.GetTypeN()
        return R

    def GetActiveN(self, cellN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    R=self.row[N-1].GetActiveN()
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetActiveN()
        return R

    def GetActiveItem(self, cellN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    R=self.row[N-1].GetActiveItem()
        if cellN>=1 and cellN<=Q:
            #R=self.row[N-1].GetActiveItem()
            R=self.row[N-1].GetActiveItem(cellN)
        elif cellN==0 and isinstance(self.header, DataCell):
            R=self.header.GetActiveItem()
        return R

   

    def SetActiveNByVal(self, cellN, val):
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        if cellN>=1 and cellN<=Q:
            #self.row[cellN-1].SetActiveNByVal(val)
            self.row.SetActiveNByVal(cellN, val)
        elif cellN==0:
            self.header.SetActiveNByVal(val)
    
    def GetVal(self, cellN=0, valN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            #if cellN>=0 and cellN<=Q:
            activeN=self.GetActiveNOfN(cellN)
            cellLength=self.GetLengthN(cellN)
            if valN<=0 or valN>cellLength:
                valN=activeN
            R=cell.GetVal(valN)
        return R

    def GetItem(self, cellN, valN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            #activeN=self.GetActiveNOfN(cellN)
            #cellLength=self.GetLengthN(cellN)
            activeN=cell.GetActiveN()
            cellLength=cell.GetLengthN(cellN)
            if valN<=0 or valN>cellLength:
                valN=activeN
            R=self.row[cellN-1].GetItem(valN)
        return R


    def GetFloatVal(self, cellN=0):
        R=0
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetFloatVal()
        return R

    def GetIntVal(self, cellN=0):
        R=0
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetIntVal()
        return R

    def GetBoolVal(self, cellN, valN=0):
        R=0
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetBoolVal()
        return R

    def GetStrVal(self, cellN, valN=0):
        R=0
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetStrVal()
        return R
        
        
    def SetName(self, names, cellN=0, nameN=0):
        Q=len(self.row)
        #i#f(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    self.row[cellN-1].SetName(names, nameN)
        if cellN>=1 and cellN<=Q:
            self.row[cellN-1].SetName(names, nameN)
        else:
            self.header.SetName(names, nameN)
        return R
        

    def SetItem(self, cellN, names, itemN=0):
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        if cellN>=1 and cellN<=0:
            #self.row[cellN-1].SetItem(names, itemN)
            self.row.SetItem(cellN, names, itemN)
        elif cellN==0:
            self.header.SetItem(names, itemN)
            
            

    def Add(self, cell):
        self.row.Add(cell)

    def InsN(self, cell, N=0):
        self.row.InsN(cell, N)

    def DelN(self, N=0):
        self.DelN(N)
       

    def GetFieldType(self, cellN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        activeN=self.GetActiveNOfN(cellN)
        cellLength=self.GetLengthN(cellN)
        #if cellN>0:
        cell=GetCell(cellN)
            #activeN=self.GetActiveNOfN(cellN)
            #cellLength=self.GetLengthN(cellN)
            #R=self.row[cellN-1].GetFieldType()
        if isinstance(cell, DataCell):
            R=cell.GetFieldType()
        return R

    def GetFieldWidth(self, cellN):
        R=0
        Q=len(self.row)
        if(cellN<=0 or cellN>Q):
            cellN=Q#cellN=1
        #if cellN>0:
        #activeN=self.GetActiveNOfN(cellN)
        #cellLength=self.GetLengthN(cellN)
        #R=self.row[cellN-1].GetFieldWidth()
        cell=GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetFieldWidth()
        return R

    def GetFieldLength(self, cellN):
        R=0
        Q=len(self.row)
        if(cellN<=0 or cellN>Q):
            cellN=Q#cellN=1
        if cellN>0:
        #    activeN=self.GetActiveNOfN(cellN)
        #    cellLength=self.GetLengthN(cellN)
        #    R=self.row[cellN-1].GetFieldLength()
            cell=GetCell(cellN)
            if isinstance(cell, DataCell):
                R=cell.GetFieldLength()
        return R

    def GetFieldType(self, cellN):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    activeN=self.GetActiveNOfN(cellN)
        #    cellLength=self.GetLengthN(cellN)
        #    R=self.row[cellN-1].GetFieldType()
        cell=GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetFieldType()
        return R



    def SetFieldType(self, cellN, TypeN):
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    self.row[cellN-1].SetFieldType(TypeN)
        if cellN>=1 and cellN<=Q:
            #self.row[cellN-1].SetFieldType(TypeN)
            self.row.SetFieldType(cellN, TypeN)
        elif cellN==0:
            self.header.SetFieldType(TypeN)

    def SetFieldWidth(self, cellN, val):
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    self.row[cellN-1].SetFieldWidth(val)
        if cellN>=1 and cellN<=Q:
            self.row.SetFieldWidth(cellN, val)
        elif cellN==0:
            self.header.SetFieldWidth(val)

    def SetFieldChateristics(self, val, cellN=0):
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        if cellN>=1 and cellN<=Q:
            self.row.SetFieldChateristics(val, cellN)
        elif cellN==0:
            self.header.SetFieldChateristics(val)



    def HeaderToString(self):
        R=""
        if(isinstance(self.header,DataCell)):
             R=self.header.ToString()
        return R


    def ToStringN(self, cellN=0):
        R=""
        Q=len(self.row)
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.ToString()
        return R


    def ToString(self, sep_row=" ", sep_hdr=" ", ShowHeaderLine=0):
        #Q=MyLibPy2.ArrayLength(self.row)
        R = ""
        if(ShowHeaderLine>0):
            R = "Row #"+str(id(self))+": "+str(Q)+" elements: "
        #Q=MyLibPy2.ArrayLength(self.row)
        R=R+self.HeaderToString()
        R=R+sep_hdr
        Q=len(self.row)
        for i in range(1, Q):#seems Q not including, ce for 1..Q-1
            R=R+self.ToStringN(cellN)
            R=R+str_btw
        if Q>0:
            R=R+self.row[Q-1].ToString()
        return R

    def ToString(self, separator=" ", SepMain=": "):
        R = ""
        R = "Row #"+str(id(self))+": "+str(Q)+" elements: "
        R=R+ToStringN(0) # maybe 
        R=R+SepMain
        Q=len(self.row)
        for i in range(1, Q-1+1):
            R=R+ToStringN(i)
            R=R+separator
        R=R+ToStringN(Q)
        return R

    def __str__(self):
        return self.ToString()





print("\n\nChecking Cells-2\n")
CellArr=[]
#CellArr[1-1] = DataCell_Simple()
cell= DataCell()
CellArr.append(cell)
#CellArr[2-1] = DataCell_ComboboxOrMemo()
cell= DataCell()
CellArr.append(cell)
#CellArr[2-1] = DataCell_DBFldHdr()
cell = DataCell()
CellArr.append(cell)
CellArr[1-1].Set_Simple("red-1")
CellArr[2-1].Set_ComboboxOrMemo(2, ["white", "blue", "red"])
CellArr[3-1].Set_DBFldHdr(["Column # 3 !", "Col1", "Column"], ["Item1", "Item2", "Item3"], [1, 2, 3])
N=0
for everyone in CellArr:
    N+=1
    print("Cell ",N," :")
    s = CellArr[N-1].GetActiveN()
    print("activeN=", s)
    s = CellArr[N-1].GetActiveItem()
    print("Active Item=", s)
    s = CellArr[N-1].GetName(2)
    print("name N2=", s)
    s = CellArr[N-1].GetVal()
    print("val=", s)
    s = CellArr[N-1].ToString()  # new
    print("val s =", s)
        

print("\n\nChecking DataCell Row\n")
row=DataCellRow()
row.Set(CellArr)
print("L=",row.GetLength())
row.Show("; ")

strng="strong"
Q=len(strng)
print("length of "+strng+" = "+str(Q))
Q=len(CellArr)
print("length of CellArr = "+str(Q))



arr=[[1,2,3],['1','2','3'],[1,2,3,4],['1','2']]
print( "array: ",arr," min, max: ",MyLibPy2.DefExtrRowLensIn2DArr(arr))   


class TableHeader:
    def __init__(self, TableHeader="", LinesGeneralHeader="", ColumnsGeneralHeader=""):
        self.TableHeader=""
        self.LinesGeneralHeader=""
        self.ColumnsGeneralHeader=""
        self.Set(TableHeader, LinesGeneralHeader, ColumnsGeneralHeader)

    def Set(self, TableHeader="", LinesGeneralHeader="", ColumnsGeneralHeader=""):
        if isinstance(TableHeader, DataCell):
            self.TableHeader=copy.deepcopy(TableHeader)
        else:
            self.TableHeader=DataCell(TableHeader)
        if isinstance(LinesGeneralHeader, DataCell):
            self.LinesGeneralHeader=copy.deepcopy(LinesGeneralHeader)
        else:
            self.LinesGeneralHeader=DataCell(LinesGeneralHeader)
        if isinstance(ColumnsGeneralHeader, DataCell):
            self.ColumnsGeneralHeader=copy.deepcopy(ColumnsGeneralHeader)
        else:
            self.ColumnsGeneralHeader=DataCell(ColumnsGeneralHeader)

    def GetTableName(self):
        return self.TableHeader.GetName()

    def GetLinesGeneralName(self):
        return self.LinesGeneralHeader.GetName()

    def GetColumnsGeneralName(self):
        return self.ColumnsGeneralHeader.GetName()

    def GetLinesGeneralName_FieldName(self):
        return self.LinesGeneralHeader.GetName(2-1)

    def GetColumnsGeneralName_FieldName(self):
        return self.ColumnsGeneralHeader.GetName(2-1)

    def GetDBTableName(self):
        return self.TableHeader.GetName(2-1)

    def GetTable_DBGeneralName(self):
        return self.TableHeader.GetName(3-1)

    def GetTable_DBPath(self):
        return self.TableHeader.GetName(4-1)


    def SetTableName(self, val):
        self.TableHeader.SetName()

    def GetLinesGeneralName(self, val):
        self.LinesGeneralHeader.SetName()

    def GetColumnsGeneralName(self, val):
        self.ColumnsGeneralHeader.SetName()

    def GetLinesGeneralName_FieldName(self, val):
        self.LinesGeneralHeader.SetName(2-1)

    def GetColumnsGeneralName_FieldName(self, val):
        self.ColumnsGeneralHeader.SetName(2-1)

    def GetDBTableName(self, val):
        self.TableHeader.SetName(2-1)

    def GetTable_DBGeneralName(self, val):
        self.TableHeader.SetName(3-1)

    def GetTable_DBPath(self, val):
        self.TableHeader.SetName(4-1)

             

class Table:
    def __init__(self, rows=[], RowsAreColumns0Lines1=1, LineOfColHeader=[], ColOfLineHeader=[], TableHeader=0, LinesGeneralHeader=0, ColumnsGeneraklHeader=0, InnerStruct_LC_not_CL_1_VV_0=0,): 
        self.content=[]
        #self.content=
        self.LineOfColHeader=[]
        self.ColOfLineHeader=[]
        self.TableHeader=DataCell()
        self.LinesGeneralHeader=DataCell()
        self.ColumnsGeneralHeader=DataCell()
        self.LC_not_CL=true
        self.Set(rows, RowsAreColumns0Lines1, LineOfColHeader, ColOfLineHeader, TableHeader, LinesGeneralHeader, ColumnsGeneraklHeader, InnerStruct_LC_not_CL_1_VV_0)

    def GetCell(self, LineN, ColN):
        cell=0
        if LineN==0 and ColN>0 and len(self.LineOfColHeader)>0:
            if ColN<len(self.LineOfColHeader):
                cell=self.LineOfColHeader[ColN-1]
        elif LineN>0 and ColN==0 and len(self.ColOfLineHeader)>0:
            if LineN<len(self.ColOfLineHeader):
                cell=self.ColOfLineHeader[LineN-1]
        elif LineN>0 and ColN>0:
            if(self.LC_not_CL):
                ExtRowN=LineN
                IneRowN=ColN
            else:
                IneRowN=LineN
                ExtRowN=ColN
            #if ExtRowN<=len(content):
            #    curRow=content[ExtRowN-1]
            #    if IneRowN<=len(curRow):
            #        cell=curRow[IneRowN-1]
            if ExtRowN>=1 and ExtRowN<=len(self.content) and IneRowN>=1 and IneRowN<=len(self.content[1-1]):
                cell=self.content[ExtRowN-1][IneRowN-1]
        return cell

    def SetCell(self, cellExt, LineN, ColN):
        #cell=copy.deepcopy(cellExt)
        if LineN==0 and ColN>0 and len(self.LineOfColHeader)>0:
            if ColN<len(self.LineOfColHeader):
                self.LineOfColHeader[ColN-1]=copy.deepcopy(cell)
        elif LineN>0 and ColN==0 and len(self.ColOfLineHeader)>0:
            if LineN<len(self.ColOfLineHeader):
                self.ColOfLineHeader[LineN-1]=copy.deepcopy(cell)
        elif LineN>0 and ColN>0:
            if(self.LC_not_CL):
                ExtRowN=LineN
                IneRowN=ColN
            else:
                IneRowN=LineN
                ExtRowN=ColN
            if ExtRowN>=1 and ExtRowN<=len(self.content) and IneRowN>=1 and IneRowN<=len(self.content[1-1]):
                self.content[ExtRowN-1][IneRowN-1]=copy.deepcopy(cellExt)

    def Set(self, rows, RowsAreColumns0Lines1, LineOfColHeader=[], ColOfLineHeader=[], TableHeader=0, LinesGeneralHeader=0, ColumnsGeneraklHeader=0, InnerStruct_LC_not_CL_1_VV_0=0): 
        QRows=len(rows)
        L=len(rows[1-1])
        LoCH_L=len(LineOfColHeader)
        CoLH_L=len(ColOfLineHeader)
        self.content=[]
        self.LineOfColHeader=[]
        self.ColOfLineHeader=[]
        #if InnerStruct_LC_not_CL_1_VV_0==RowsAreColumns0Lines1:
        #    if RowsAreColumns0Lines1==1:
        #        self.content=[]
        #        QRows=len(rows)
        #        for i in range(1, QRows+1):
        #            row=copy.deepcopy(rows[i-1])
        #            self.content.append(row)
        #    else:
        #        for i in range(1,L+1):
        #            row=[]
        #            for j in range(1,QRows+1):
        #                cur=copy.deepcopy(LineOfColHeader[i-1])
        #                row.append(cur)
        #            self.content.append(copy.deepcopy(row))
        #    if InnerStruct_LC_not_CL_1_VV_0==0:
        #        QLines=len(self.content)
        #        QColumns=len(self.content[1-1])
        #    else:
        #        QColumns=len(self.content)
        #        QLines=len(self.content[1-1])
        self.SetContent(rows, RowsAreColumns0Lines1, InnerStruct_LC_not_CL_1_VV_0)    
        #         
        if LoCH_L>0:
            if LoCH_L>QColumns:
                for i in range(1, QColumns+1):
                    cur=copy.deepcopy(LineOfColHeader[i-1])
                    self. LineOfColHeader.append(cur)
            elif LoCH_L<QColumns:
                for i in range(1, LoCH_L+1):
                    cur=copy.deepcopy(LineOfColHeader[i-1])
                    self.LineOfColHeader.append(cur)
                for i in range(LoCH_L+1, QColumns+1):
                    cur=DataCell()
                    self.LineOfColHeader.append(copy.deepcopy(cur))
            else:
                self.LineOfColHeader=copy.deepcopy(LineOfColHeader)
        #
        if CoLH_L>0:
            if CoLH_L>QLines:
                for i in range(1, QLines+1):
                    cur=copy.deepcopy(ColOfLineHeader[i-1])
                    self. ColOfLineHeader.append(cur)
            elif CoLH_L<QLines:
                for i in range(1, LoCH_L+1):
                    cur=copy.deepcopy(ColOfLineHeader[i-1])
                    self.ColOfLineHeader.append(cur)
                for i in range(LoCH_L+1, QLines+1):
                    cur=DataCell()
                    self.ColOfLineHeader.append(copy.deepcopy(cur))
            else:
                self.ColOfLineHeader=copy.deepcopy(ColOfLineHeader)
        #     
        if TableHeader!=0:
            if isinstance(TableHeader, DataCell):
                self.TableHeader=copy.deepcopy(TableHeader)
            elif isinstance(TableHeader, list) or isinstance(TableHeader, str):
                self.TableHeader=DataCell(TableHeader)
            else:
                self.TableHeader=0
        #
        if LinesGeneralHeader!=0:
            if isinstance(LinesGeneralHeader, DataCell):
                self.LinesGeneralHeader=copy.deepcopy(LinesGeneralHeader)
            elif isinstance(LinesGeneralHeader, list) or isinstance(LinesGeneralHeader, str):
                self.LinesGeneralHeader=DataCell(LinesGeneralHeader)
            else:
                self.LinesGeneralHeader=0
        #
        if ColumnsGeneralHeader!=0:
            if isinstance(ColumnsGeneralHeader, DataCell):
                self.ColumnsGeneralHeader=copy.deepcopy(ColumnsGeneralHeader)
            elif isinstance(ColumnsGeneralHeader, list) or isinstance(ColumnsGeneralHeader, str):
                self.ColumnsGeneralHeader=DataCell(ColumnsGeneralHeader)
            else:
                self.LinesGeneralHeader=0
        #
        self.LC_not_CL=InnerStruct_LC_not_CL_1_VV_0
        #if WriteInfoNo0Yes1==1:
        #     self.info=new TableInfo()
        #     self.info.QLines=QLines

    def GetQExtRows(self):
        return len(self.content)

    def GetQIneRows(self):
        QIneRows=0
        QExtRows=len(self.content)
        if QExtRows>0:
             QIneRows=len(self.content[1-1])
        return QIneRows

    def GetQLines(self):
        QIneRows=self.GetQIneRows()
        QExtRows=self.GetQExtRows()
        if self.self.LC_not_CL==1:
            QLines=QExtRows
        else:
            QLines=QIneRows
        return QLines

    def GetQColumns(self):
        QIneRows=self.GetQIneRows()
        QExtRows=self.GetQExtRows()
        if self.self.LC_not_CL==0:
            QColumns=QExtRows
        else:
            QColumns=QIneRows
        return QLines

    def GetLineHeaderCellN(self, LineN):
        cell=0
        Q=len(self.ColOfLineHeader)
        if Q>0 and LineN>=1 and LineN<=Q:
            cell=self.ColOfLineHeader[LineN-1]
        return cell

    def GetColumHeaderCellN(self, ColN):
        cell=0
        Q=len(self.LineOfColHeader)
        if Q>0 and ColN>=1 and ColN<=Q:
            cell=self.LineOfColHeader[ColN-1]
        return cell
            
    def SwapCells(self, LineN1, ColN1, LineN2, ColN2):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if LineN1>=1 and LineN1<=QLines and ColN1>=1 and ColN1<=QColumns and    LineN2>=1 and LineN2<=QLines and ColN2>=1 and ColN2<=QColumns:
            #cellBuf=self.GetCell(LineN2, ColN2)
            #self.SetCell(self.GetCell(LineN1, ColN1), LineN2, ColN2)
            #self.SetCell(cellBuf, LineN1, ColN1)
            #
            cell1=self.GetCell(LineN1, ColN1)
            cell2=self.GetCell(LineN2, ColN2)
            self.SetCell(cell1, LineN2, ColN2)
            self.SetCell(cell2, LineN1, ColN1)

    def SwapLines(self, Line1N, Line2N):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if Line1N>=1 and Line1N<=QLines and Line2N>=1 and Line2N<=QLines:
            for i in range(1, QColumns+1):
                self.SwapCells(Line1N, i, Line2N, i)

    def SwapColumns(self, Col1N, Col2N):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if Col1N>=1 and Col1N<=QColumns and Col2N>=1 and Col2N<=QColumns:
            for i in range(1, QLines+1):
                self.SwapCells(i, Col1N, i, Col2N)

    def SwapLineNWithHeaderLine(self, LineN):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if len(self.LineOfColHeader)>0 and LineN>=1 and LineN<=QLines:
            for i in range(1, QColumns+1):
                hdrCell=copy.deepcopy(self.LineOfColHeader[i-1])
                cntCell=GetCell(LineN, i)
                self.LineOfColHeader[i-1]=copy.deepcopy(cntCell)
                self.SetCel(hdrCell, LineN, i)

    def SwapColNWithHeaderLine(self, ColN):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if len(self.ColOfLineHeader)>0 and ColN>=1 and ColN<=QColumns:
            for i in range(1, QLines+1):
                hdrCell=copy.deepcopy(self.ColOfLineHeader[i-1])
                cntCell=GetCell(i, ColN)
                self.ColOfLineHeader[i-1]=copy.deepcopy(cntCell)
                self.SetCel(hdrCell, i, ColN)

    def OrderVisaVersaLines(self):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if(QLines%2==0):
            N=QLines
        else:
            N=QLines-1
        for i in range(1, N+1):
            N1=i
            N2=QLines+i-1
            self.SwapLines(N1, N2)

    def OrderVisaVersaColumns(self):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if(QLines%2==0):
            N=QColumns
        else:
            N=QColumns-1
        for i in range(1, N+1):
            N1=i
            N2=QColumns+i-1
            self.SwapColumns(N1, N2)

    def OrderVisaVersaLineN(self, N):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if N>=0 and N<=QColumns:
            if(QColumns%2==0):
                N=QColumns
            else:
                N=QColumns-1
            for i in range(1, N+1):
                N1=i
                N2=QColumns+i-1
                self.SwapCells(N, N1, N, N2)

    def OrderVisaVersaColumnN(self, N):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if N>=0 and N<=QColumns:
            if(QLines%2==0):
                N=QLines
            else:
                N=QLines-1
            for i in range(1, N+1):
                N1=i
                N2=QLines+i-1
                self.SwapCells(N1, N, N2, N)

    def OrderVisaVersaHeaderLine(self):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if len(self.LineOfColHeader)>0:
            if(QColumns%2==0):
                N=QColumns
            else:
                N=QColumns-1
        for i in range(1, N+1):
            N1=i
            N2=QColumns+i-1
            cell1=copy.deepcopy(self.LineOfColHeader[N1-1])
            cell2=copy.deepcopy(self.LineOfColHeader[N2-1])
            self.LineOfColHeader[N1-1]=copy.deepcopy(cell2)
            self.LineOfColHeader[N2-1]=copy.deepcopy(cell1)

    def OrderVisaVersaHeaderColumn(self):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if len(self.ColOfLineHeader)>0:
            if(QColumns%2==0):
                N=QLines
            else:
                N=QLines-1
        for i in range(1, N+1):
            N1=i
            N2=QLines+i-1
            cell1=copy.deepcopy(self.ColOfLineHeader[N1-1])
            cell2=copy.deepcopy(self.ColOfLineHeader[N2-1])
            self.ColOfLineHeader[N1-1]=copy.deepcopy(cell2)
            self.ColOfLineHeader[N2-1]=copy.deepcopy(cell1)

    def AddLine(self, row):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if self.LC_not_CL==1:
            self.content.append(row)
        else:
            for i in range(1, QColumns+1):
                self.content[i-1].append(row[i-1])

    def AddColumn(self, row):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if self.LC_not_CL==1:
            for i in range(1, QLines+1):
                self.content[i-1].append(row[i-1])
        else:
            self.content.append(row)

    def InsLineN(self, row, N):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        content=[]
        if self.LC_not_CL==1:
            for i in range(1, N-1+1):
                CurLine=self.GetLine(i)
                content.append(CurLine)
            content.append(row)#into Nth pos
            for i in range(N, QLines+1):
                CurLine=self.GetLine(i)
                content.append(CurLine)
        else:
            for i in range(1, QColumns+1):
                CurRow=[]
                for j in range(1, N-1+1):
                    cell=self.GetCell(j, i)
                    CurRow.append(copy.deepcopy(cell))
                for j in range(1, N-1+1):
                    cell=row[j-1]
                    CurRow.append(copy.deepcopy(cell))
                for j in range(N, QLines+1):
                    cell=self.GetCell(j, i)
                    CurRow.append(copy.deepcopy(cell))
                content.append(CurRow)

    def InsColumnN(self, row, N):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        content=[]
        if self.LC_not_CL==0:
            for i in range(1, N-1+1):
                CurCol=self.GetColumn(i)
                content.append(CurCol)
            content.append(row)#into Nth pos
            for i in range(N, QLines+1):
                CurCol=self.GetColumn(i)
                content.append(CurCol)
        else:
            for i in range(1, QLines+1):
                CurRow=[]
                for j in range(1, N-1+1):
                    cell=self.GetCell(j, i)
                    CurRow.append(copy.deepcopy(cell))
                for j in range(1, N-1+1):
                    cell=row[j-1]
                    CurRow.append(copy.deepcopy(cell))
                for j in range(N, QColumns+1):
                    cell=self.GetCell(j, i)
                    CurRow.append(copy.deepcopy(cell))
                content.append(CurRow)
                

    def Transpose(self):
        content=[]
        #QExtRows=self.GetQExtRows()
        #QIneRows=self.GetQIneRows()
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        #for i in range(1, QIneRows+1):
        #for i in range(1, QIneRows+1):  
            #for i in range(1, QIneRows+1):
            #CurExtRow=[]
            #for j in range(1, QExtRows+1):
                #cell=
        for i in range(1, QColumns+1):  
            CurExtRow=[]
            for j in range(1, QLines+1):
                cell=GetCell(j, i)
                CurExtRow.append(copy.deepcopy(cell))
            content.append(copy.deepcopy(CurExtRow))
        self.content=content
        #
        buf=self.LineOfColHeader
        self.LineOfColHeader=self.ColOfLineHeader
        self.ColOfLineHeader=buf
            
        
    def GetLineN(self, LineN):
        row=DataCellRow()
        QLines=self.GetQLines()
        if LineN>=0 and LineN<=QLines:
             if LineN==0 and len(self.LineOfColHeader)>0:
                 for i in range(1, QLines+1):
                     #cell=GetCell(LineN, i)#also abl
                     cell=self.LineOfColHeader[i-1]
                     row.Add(cell)
             else:
                 for i in range(1, QLines+1):
                     cell=GetCell(LineN, i)
                     row.Add(cell)
        return row

    def GetColumnN(self, ColN):
        row=DataCellRow()
        QColumns=self.GetQColumns()
        if ColN>=0 and ColN<=QColumns:
             if ColN==0 and len(self.ColOfLineHeader)>0:
                 for i in range(1, QLines+1):
                     #cell=GetCell(LineN, i)#also abl
                     cell=self.ColOfLineHeader[i-1]
                     row.Add(cell)
             else:
                 for i in range(1, QColumns+1):
                     cell=GetCell(ColN, i)
                     row.Add(cell)
        return row

    # RowsAreColumns0Lines1 InnerStruct_LC_not_CL_1_VV_0=0
    def SetContent(rows, LinesNotCols=1, LC_not_CL=1):
        if isinstance(rows, list) and len(rows)>0 and len(rows[1-1])>0:
            self.LC_not_CL=LC_not_CL
            self.content=[]
            if LinesNotCols==LC_not_CL:
                for row in rows:
                    self.content.Append(row)
            else:
                #QIneRows=(MyLibPy2.DefExtrRowLensIn2DArr(rows))[2-1]
                QIneRows=0
                QExtRows=len(rows)
                QIneRows=len(rows[1-1])
                for i in range(1, QIneRows+1):
                    CurExtRow=[]
                    for j in range(1, QExtRows+1):
                        cell=row[j-1][i-1]
                        CurExtRow.append(cell)
                    self.content.append(CurExtRow)


    def ToString(self, LineN, ColN):
        R=""
        cell=self.GetCell(LineN, ColN)
        if isinstance(cell, DataCell):
            R=cell.ToString()
        return R

    def CornerToString(self):
        s=""
        s=s+str(self.LinesGeneralHeader.GetName())
        if self.LinesGeneralHeader.GetName()!="" and self.ColumnsGeneralHeader.GetName()!="":
             s=s+"\\"
        s=s+str(self.ColumnsGeneralHeader.GetName())
        return s

    def HeaderLineToString(self, sep_hdr=" ", sep_row=" "):
        s=self.CornerToString()
        s=s+sep_hdr
        QColumns=self.GetQColumns()
        for i in range(1, QColumns-1+1):
            cell=GetColumHeaderCellN(i)
            s=s+cell.ToString()
            s=s+sep_row
        if QColumns>0:
            cell=GetColumHeaderCellN(QColumns)
            s=s+cell.ToString()
        return s

    def LineToString(self, LineN, sep_hdr=" ", sep_row=" "):
        s=""
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if LineN==0:
            s=HeaderLineToString(sep_hdr, sep_row)
        elif LineN<=QLines:
            cell=GetLineHeaderCellN(self, LineN)
            s=cell.ToString()
            if s!="":
                s=s+sep_hdr
            if QColumns>0:
                for i in range(1, QColumns-1+1):
                    cell=self.GetCell(LineN, i)
                    s=s+sell.ToString()
                cell=self.GetCell(LineN, QColumns)
                s=s+sell.ToString()
        return s
                        
                        
        
