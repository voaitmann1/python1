import math
import copy

import MyLibPy3#.py



print("try own functions Insert in array")
arr1=[10,20,30]
print("arr1=",arr1)
val=15
N=2
MyLibPy3.ArrayIns1(arr1, 3, 25)
print("After inserting val=",val," into pos N=",N," by 1st function: ",arr1)
arr1=[10,20,30]
print("arr1=",arr1)
val=15
N=2
MyLibPy3.ArrayIns2(arr1, 3, 25)
print("After inserting val=",val," into pos N=",N," by 1st function: ",arr1)
arr1=[10,20,30]
print("arr1=",arr1)
print("arr1=",arr1)
val=15
N=2
MyLibPy3.ArrayIns3(arr1, 3, 25)
print("After inserting val=",val," into pos N=",N," by 3rd function: ",arr1)
arr1=[10,20,30]
print("arr1=",arr1)
val=15
N=2
MyLibPy3.ArrayIns4(arr1, 3, 25)
print("After inserting val=",val," into pos N=",N," by 4th function: ",arr1)
arr1=[10,20,30]
print("arr1=",arr1)
val=15
N=2
MyLibPy3.ArrayIns5(arr1, N, val)
print("After inserting val=",val," into pos N=",N," by 5th function: ",arr1)
arr1=[10,20,30]
print("arr1=",arr1)
val=15
N=2
arr1=MyLibPy3.ArrayInsTo(arr1, N, val)
print("After inserting val=",val," into pos N=",N," by To- function: ",arr1)

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
    def __init__(self):
        self.data=""
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
    def __init__(self):
        self.data=1
        self.items=[]
    #def __init__(self):
    #    DataCell_Simple.__init__(self)#self.data=""
    #    self.items=[]
    def GetVal(self):
        #return self.data
        return self.GetItem( self.data)#self.items[self.data-1]

    def GetItem(self, N=0):
        R = 0
        if isinstance(self.items, list):
            Q = MyLibPy3.ArrayLength(self.items)
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
        Q=MyLibPy3.ArrayLength(self.items)
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
            R = MyLibPy3.ArrayLength(self.items)
        return R

    def GetQNames():
        return self.GetQItems()

    def GetName(self, N=0):
        return self.GetItem(N)

    # for database
    def SetName(self, names, N=0):
        self.SetItem(names, N)
           
    def SetItem(self, items, N=0):
        Q=MyLibPy3.ArrayLength(self.items)
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
    #    self.__init__(self)
    #    #self.__init__(self)#self.data=""# ob self.
    #    self.items=[]
    #    self.data=[]
    #    self.DBFldInfo=[]
    def __init__(self):
        #DataCell_ComboboxOrMemo.__init__(self)#self.items=[] remains, self.data=0 wi redef'd
        #DataCell_ComboboxOrMemo.data=[]#why not redef
        self.data=[]
        self.items=[]
        self.DBFldInfo=[]
    def GetVal(self):
        #return self.data
        #return self.GetName(self)#incompatible int et DataCell_DBFldHdr
        #return self.GetName(self,1)#3args apo 2 s'dat'd
        return self.GetName(1)

    def GetItem(self, N=0):
        R = 0
        if isinstance(self.items, list):
            Q = MyLibPy3.ArrayLength(self.items)
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
            R = MyLibPy3.ArrayLength(self.items)
        return R

    def GetQNames():
        R = 0
        if not isinstance(self.data, list):
            R = 1
        else:
            R = MyLibPy3.ArrayLength(self.data)
        return R

     # for database
    def GetName(self, N=1):
        R = 0
        if isinstance(self.data, list):
            Q = MyLibPy3.ArrayLength(self.data)
            if N >= 1 and N <= Q:
                R = self.data[N - 1]
        elif self.data == []:
            R = self.data
        else:
            R = self.data
        return R

    def SetName(self, names, N=0):
        Q=MyLibPy3.ArrayLength(self.data)
        if isinstance(names, list):
           self.data = names
        else:
           if N>=1 and N<=Q:
               self.data[N-1]=names
           
    def SetItem(self, items, N=0):
        Q=MyLibPy3.ArrayLength(self.items)
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
    def __init__(self):
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
    def SetFieldType(self):
        self.cell.SetFieldType()    #
    def SetFieldWidth(self):
        self.cell.SetFieldWidth()
    def SetFieldLength(self):
        self.cell.SetFieldLength()
    def SetFieldCharacteristics(self):
        self.cell.SetFieldCharacteristics()
        #
        

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
    def GetCellN(self, N):
        R = 0
        Q = self.ArrayLength(self.row)
        if N >= 1 and N <= Q:
            R = self.row[N - 1]
        return R
    def Set(self,arr):
        #Q=MyLibPy3.ArrayLength(arr)
        #print("DataCellRow.Set starts working")
        #print("Adding ",Q, " items")
        #
        self.row=copy.deepcopy(arr)
        #Q=MyLibPy3.ArrayLength(arr)
        #print("DataCellRow.Set finishes working")

    def GetLength(self):
        return MyLibPy3.ArrayLength(self.row)

    def GetNameN(self, CellN, NameN=1):
        R = ""
        cell = self.GetCellN(CellN)
        if cell != 0:
            R = cell.GetName(NameN)
        return R

    def Add(self, cellExt):
        cell=copy.deepcopy(cellExt)
        #ArrayAdd(self.row, cell)
        self.row.append(cell)

    def ToString(self, str_btw=" "):
        Q=MyLibPy3.ArrayLength(self.row)
        R = ""
        R = "Row #"+str(id(self))+": "+str(Q)+" elements: "
        #for element in self.row:
        #    R = R + str(element.ToString())+str_btw
        #return R
        Q=MyLibPy3.ArrayLength(self.row)
        for i in range(1, Q):#seems Q not including, ce for 1..Q-1
            R=R+self.row[i-1].ToString()
            R=R+str_btw
        if Q>0:
            R=R+self.row[Q-1].ToString()
        return R
      
    def Show(self, str_btw=" "):
        s = self.ToString(str_btw)
        print(s)



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
print( "array: ",arr," min, max: ",MyLibPy3.DefExtrRowLensIn2DArr(arr))   


class Table:
    def __init__(self):
        content=[]
        LineOfColHeader=[]
        ColOfLineHeader=[]
        TableHeader=DataCell()
        LinesGeneralHeader=DataCell()
        ColumnsGeneralHeader=DataCell()
        LCNotCL=true
    def SetContent(rows, LinesNotCols=true, LC_not_CL=true):
        if isinstance(rows, list):
            self.LC_not_CL=LC_not_CL
            content=[]
            if LinesNotCols==LC_not_CL:
                for row in rows:
                    content.Append(row)
            else:
                QIneRows=(MyLibPy3.DefExtrRowLensIn2DArr(rows))[2-1]
                for row in rows:
                    CurExtRow=[]
                    ColN=0    
                    for cell in row:
                        ColN+=1
                        
                        
        
