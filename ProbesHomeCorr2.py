# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
import math
import copy

# import MyLib

# https://www.filepuma.com/download/python_32bit_3.4.0-5405/

class MyClass:
    a=1
    def Set(self, a):
        self.a=a
    def get(self):
        return self.a
    def Show(self):
        print("MyClass object: ", id(self), " content=",self.get())

a=MyClass()
a.Set(2)
print("MyClass object a:")
a.Show()
b=MyClass()
b.Set(3)
print("MyClass object b:")
b.Show()
print("MyClass object a:")
a.Show()
print("MyClass object b:")
b.Show()


def ArrayLength(arr):
    count = 0
    for element in arr:
        count = count + 1
    return count


def ArrayAdd(arr, val):
    arr.append(val)
    # return arr


def ArrayIns1(arr, N, val):  # works incorrect
    print("ArrayIns1 starts working")
    print("fn received: arr=", arr)
    arr1 = []
    OldLength = ArrayLength(arr)
    NewLength = OldLength + 1
    if N >= 1 and N <= OldLength:
        count = 0
        for element in arr:
            count = count + 1
            if count == N:
                arr1.append(val)
                arr1.append(arr[count - 1])
            else:
                arr1.append(arr[count - 1])
    print("arr1=", arr1)
    arr=arr1
    print("in fn: arr=", arr)
    print("ArrayIns1 finishes working")



def ArrayIns2(arr, N, val):  # works incorrect
    print("ArrayIns2 starts working")
    arr1 = []
    OldLength = ArrayLength(arr)
    NewLength = OldLength + 1
    if N >= 1 and N <= OldLength:
        count = 0
        for element in arr:
            count = count + 1
            if count == N:
                arr1.append(val)
                arr1.append(arr[count - 1])
            else:
                arr1.append(arr[count - 1])
    print("ArrayIns2 finishes working")


def ArrayIns3(arr, N, val):  # works incorrect
    print("ArrayIns3 starts working")
    arr1 = []
    OldLength = ArrayLength(arr)
    NewLength = OldLength + 1
    if N >= 1 and N <= OldLength:
        count = 0
        for element in arr:
            count = count + 1
            if count == N:
                arr1.append(val)
                arr1.append(arr[count - 1])
            else:
                arr1.append(arr[count - 1])
    del arr[:]
    # return arr1
    print("in fn: arr1", arr1)
    arr = arr1
    print("in fn: arr", arr)
    print("ArrayIns3 finishes working")



def ArrayIns4(arr, N, val):
    print("ArrayIns4 starts working")
    arr1 = []
    OldLength = ArrayLength(arr)
    NewLength = OldLength + 1
    if N >= 1 and N <= OldLength:
        count = 0
        for element in arr:
            count = count + 1
            if count == N:
                arr1.append(val)
                arr1.append(arr[count - 1])
            else:
                arr1.append(arr[count - 1])
    del arr[:]
    # return arr1
    print("in fn: arr1", arr1)
    for element in arr1:
        arr.append(element)
    print("in fn: arr", arr)
    print("ArrayIns4 finishes working")

def ArrayIns5(arr, N, val):
    print("ArrayIns5 starts working")
    OldLength = ArrayLength(arr)
    NewLength = OldLength + 1
    if N >= 1 and N <= OldLength:
        print("arr=",arr)
        arr.append(val)
        print("arr=", arr)
        i=N
        #while i
        for i in [N+1,NewLength]:
            #i=i+1 # uz while
            j=NewLength-i+N+1
            print("i=", i, " j=", j, "OL=", OldLength, " NL=", NewLength)
            print("a[", j, "]=", arr[j - 1])
            val=arr[j-1]
            print("val=", val)
            arr[j-1]=arr[j-1-1]
            print("a[", j, "]=", arr[j - 1])
            arr[j-1-1]=val
            print("a[", j-1, "]=", arr[j-1-1],'=val=',val)
    arr[N-1]=val
    # return arr1
    print("in fn: arr", arr)
    print("ArrayIns5 finishes working")



print("try own functions Insert in array")
arr1=[10,20,30]
print("arr1=",arr1)
val=15
N=2
ArrayIns1(arr1, 3, 25)
print("After inserting val=",val," into pos N=",N," by 1st function: ",arr1)
arr1=[10,20,30]
print("arr1=",arr1)
val=15
N=2
ArrayIns2(arr1, 3, 25)
print("After inserting val=",val," into pos N=",N," by 1st function: ",arr1)
arr1=[10,20,30]
print("arr1=",arr1)
print("arr1=",arr1)
val=15
N=2
ArrayIns3(arr1, 3, 25)
print("After inserting val=",val," into pos N=",N," by 3rd function: ",arr1)
arr1=[10,20,30]
print("arr1=",arr1)
val=15
N=2
ArrayIns4(arr1, 3, 25)
print("After inserting val=",val," into pos N=",N," by 4th function: ",arr1)
arr1=[10,20,30]
print("arr1=",arr1)
val=15
N=2
ArrayIns5(arr1, N, val)
print("After inserting val=",val," into pos N=",N," by 5th function: ",arr1)

def ArrayInsTo(arr, N, val):
    arr1 = []
    OldLength = ArrayLength(arr)
    # NewLength=OldLength+1
    if N >= 1 and N <= OldLength:
        count = 0
        for element in arr:
            count = count + 1
            if count == N:
                arr1.append(val)
                arr1.append(arr[count - 1])
            else:
                arr1.append(arr[count - 1])
    return arr1


arr1=[10,20,30]
print("arr1=",arr1)
val=15
N=2
arr1=ArrayInsTo(arr1, N, val)
print("After inserting val=",val," into pos N=",N," by To- function: ",arr1)

def ArrayClear(arr):
    del arr[:]


def ArrayDel(arr, FromN, ToN):
    del arr[FromN:ToN]





class DataCell:
    # def GetType(self):
    #    return 1 #1- simple, 2-DB, 3-combobox,
    #def __init__(self):
    #    self.item=""
    def GetVal(self):
        return self.item

    def GetItem(self, N=1):
        R = 0
        if isinstance(self.item, list):
            Q = ArrayLength(self.item)
            if N >= 1 and N <= Q:
                R = self.item[N - 1]
        else:
            R = self.item
        return R

    # ConcrType
    def GetFloatVal(self):
        return self.item

    def GetIntVal(self):
        return self.item

    def GetBoolVal(self):
        return self.item

    def GetStrVal(self):
        return self.item

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

    def SetName(self, names):
        self.SupplInf = names

    # for combobox
    def GetActiveN(self):
        R = 0
        if isinstance(self.SupplInf, int):
            R = self.SupplInf
        return R

    def GetActiveItem(self):
        R = []
        if not isinstance(self.item, list):
            R = self.item
        else:  # list
            if isinstance(self.SupplInf, int) and self.SupplInf >= 1 and self.SupplInf <= ArrayLength(self.item):
                R = self.item[self.SupplInf - 1]
            else:
                R = self.item[1 - 1]
        return R

    def SetActiveN(self, val):
        if isinstance(val, int) and isinstance(self.item, list) and val >= 1 and val <= ArrayLength(self.item):
            self.SupplInf = val
        elif not isinstance(self.item, list):
            self.SupplInf = 1

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

    #
    def Set(self, NainInf, SupplInf=[]):
        self.item = NainInf
        self.SupplInf = SupplInf

    def ToString(self):  # new 2021-08-12
        #return "cell id="+str(id(self))+" content: "+str(self.GetName())+" "
        return str(self.GetName()) + " "



MyCell = DataCell()
MyCell.Set(["one", "two", "three"], 2)
s = MyCell.GetActiveN()
print("activeN=", s)
s = MyCell.GetActiveItem()
print("active val=", s)
MyCell.Set(2, ["Colors", "clr"])
s = MyCell.GetName(2)
print("name N2=", s)
s = MyCell.GetVal()
print("val=", s)
s = MyCell.ToString()  # new
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
