import math
import copy

import MyLib#.py



print("try own functions Insert in array")
arr1=[10,20,30]
print("arr1=",arr1)
val=15
N=2
MyLib.ArrayIns1(arr1, 3, 25)
print("After inserting val=",val," into pos N=",N," by 1st function: ",arr1)
arr1=[10,20,30]
print("arr1=",arr1)
val=15
N=2
MyLib.ArrayIns2(arr1, 3, 25)
print("After inserting val=",val," into pos N=",N," by 1st function: ",arr1)
arr1=[10,20,30]
print("arr1=",arr1)
print("arr1=",arr1)
val=15
N=2
MyLib.ArrayIns3(arr1, 3, 25)
print("After inserting val=",val," into pos N=",N," by 3rd function: ",arr1)
arr1=[10,20,30]
print("arr1=",arr1)
val=15
N=2
MyLib.ArrayIns4(arr1, 3, 25)
print("After inserting val=",val," into pos N=",N," by 4th function: ",arr1)
arr1=[10,20,30]
print("arr1=",arr1)
val=15
N=2
MyLib.ArrayIns5(arr1, N, val)
print("After inserting val=",val," into pos N=",N," by 5th function: ",arr1)
arr1=[10,20,30]
print("arr1=",arr1)
val=15
N=2
arr1=MyLib.ArrayInsTo(arr1, N, val)
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
    def GetVal(self):
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
    def GetFieldCharacteristics(self):
        return 0
    def SetFieldType(self):
        zero=0
        #
    def SetFieldWidth(self):
        zero=0
        #
    def SetFieldCharacteristics(self):
        zero=0
        #


class DataCell_ComboboxOrMemo (DataCell_Simple):
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
        return GetItem(self, self.data)#self.items[self.data-1]

    def GetItem(self, N=0):
        R = 0
        if isinstance(self.items, list):
            Q = ArrayLength(self.items)
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
        return self.data

    def GetActiveItem(self):
        return self.items[self.data-1]

    def SetActiveN(self, val):
        N=int(val)
        Q=ArrayLength(self.items)
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
            R = ArrayLength(self.items)
        return R

    def GetQNames():
        return self.GetQItems()

    # for database
    def GetName(self, N=1):
        return GetItem(self, N)

    def SetName(self, names, N=0):
        self.items = names
    #
    def Set(self, var1=[], var2=[], var3=[]):
        DataCell_Simple.Set(var1, var2, var3)
        self.items = var2

    def ToString(self):  # new 2021-08-12
        #return "cell id="+str(id(self))+" content: "+str(self.GetName())+" "
        return str(self.GetName()) + " "
    #
    def GetFieldType(self):
        return 0
    def GetFieldWidth(self):
        return 0
    def GetFieldCharacteristics(self):
        return 0
    def SetFieldType(self):
        zero=0
        #
    def SetFieldWidth(self):
        zero=0
        #
    def SetFieldCharacteristics(self):
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
        DataCell_ComboboxOrMemo.__init__(self)#self.items=[] remains, self.data=0 wi redef'd
        DataCell_ComboboxOrMemo.data=[]#why not redef
        self.DBFldInfo=[]
    def GetVal(self):
        #return self.data
        return self.GetName(self)

    def GetItem(self, N=0):
        R = 0
        if isinstance(self.items, list):
            Q = ArrayLength(self.items)
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
        return 1

    def GetActiveItem(self):
        return self.GetItem(self,0)

    def SetActiveN(self, val):
        zero=0
        #

    def SetActiveNByVal(self, val):
        if isinstance(self.item, list) and self.item.count(val) > 0:
            self.SupplInf = self.item.index(val)

    def GetQInems():
        R = 0
        if not isinstance(self.items, list):
            R = 1
        else:
            R = ArrayLength(self.items)
        return R

    def GetQNanmes():
        R = 0
        if not isinstance(self.SupplInf, list):
            R = 1
        else:
            R = ArrayLength(self.SupplInf)
        return R

     # for database
    def GetName(self, N=1):
        R = 0
        if isinstance(self.SupplInf, list):
            Q = ArrayLength(self.SupplInf)
            if N >= 1 and N <= Q:
                R = self.SupplInf[N - 1]
        elif self.SupplInf == []:
            R = self.MainInf
        else:
            R = self.SupplInf
        return R

    def SetName(self, names, N=0):
        self.SupplInf = names

    #
    def Set(self, var1=[], var2=[], var3=[]):
        DataCell_Simple.Set(var1, var2, var3)
        self.items = var2
        self.DBFldInfo=var3

    def ToString(self):  # new 2021-08-12
        #return "cell id="+str(id(self))+" content: "+str(self.GetName())+" "
        return str(self.GetName()) + " "
    #
    def GetFieldType(self):
        return 0
    def GetFieldWidth(self):
        return 0
    def GetFieldCharacteristics(self):
        return 0
    def SetFieldType(self):
        zero=0
        #
    def SetFieldWidth(self):
        zero=0
        #
    def SetFieldCharacteristics(self):
        zero=0
        #


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
CellArr[3-1].Set(["Col1", "Col2", "Col3"], ["Item1", "Item2", "Item3"], [1, 2, 3])
N=0
for everyone in Cell:
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

    def GetNameN(self, CellN, NameN=1):
        R = ""
        cell = self.GetCellN(CellN)
        if cell != 0:
            R = cell.GetName(NameM)
        return R

    def Add(self, cellExt):
        cell=copy.deepcopy(cellExt)
        #ArrayAdd(self.row, cell)
        self.row.append(cell)

    def ToString(self):
        R = ""
        R = "Row #"+str(id(self))+": "
        for element in self.row:
            R = R + str(element.ToString())
        return R

    def Show(self):
        s = self.ToString()
        print(s)


row1 =  DataCellRow()
a = DataCell()
a.Set("N1", "X1")
row1.Add(a)
a.Set("N2")
row1.Add(a)
a.Set("N3", 23)
row1.Add(a)
print("Row1:")
row1.Show()
#
row2 =  DataCellRow()
print("Row 2 before assign")
row2.Show()

print("Row 2, assign")
a1 = DataCell()
a1.Set("N1", "X1")
row2.Add(a1)
a2 = DataCell()
a2.Set("N2")
row2.Add(a2)
a3 = DataCell()
a3.Set("N3", 45)
row2.Add(a3)
print("Row2:")
row2.Show()
print("Row1:")
row1.Show()
#

from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2


a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())
