import math
#import MyLib

#https://www.filepuma.com/download/python_32bit_3.4.0-5405/

print("array a")

#a=list()
#a[0]=10
#a[1]=20
#a[2]=30
#print("a: ", a, " a[1]= ", a[1])

print("a as list of 3 items")
a=[10, 20, 30]
print("a[1]=",a[1])
print("assign a[1]=1")
a[1]=1
print("a[1]=",a[1])
print("a elt by elt")
count=0
for item in a:
    count=count+1
    print("cur=",a[count-1]," = ",item)
#append(a,40)
#for item in a:
#    count=count+1
#    print("cur=",a[count-1]," = ",item)
#a[4-1]=400
#for item in a:
#    count=count+1
#    print("cur=",a[count-1]," = ",item)
#a=list(4)
#for item in a:
#    count=count+1
#    print("cur=",a[count-1]," = ",item)
print("a.append(400)")
a.append(400)
count=0
for item in a:
    count=count+1
    print("cur=",a[count-1]," = ",item)
print("a=[]")
a=[]
print(a)
print("a=list()")
a=list()
print(a)
print("a.append thrice")
a.append(10)
a.append(20)
a.append(30)
print(a)
#a.erase
   

clicks=0

def ArrayLength(arr):
    count=0
    for element in arr:
       count=count+1
    return count
def ArrayAdd(arr, val):
    arr.append(val)
    #return arr
def ArrayIns1(arr, N, val):# works incorrect
    arr1=[]
    OldLength=ArrayLength(arr)
    NewLength=OldLength+1
    if N>=1 and N<=OldLength:
        count=0
        for element in arr:
            count=count+1
            if count==N:
                arr1.append(val)
                arr1.append(arr[count-1])
            else :
                arr1.append(arr[count-1])
    #return arr1
    print ("in fn: arr1", arr1)
    arr=arr1
    print ("in fn: arr", arr)

    
def ArrayIns2(arr, N, val):# works incorrect
    arr1=[]
    OldLength=ArrayLength(arr)
    NewLength=OldLength+1
    if N>=1 and N<=OldLength:
        count=0
        for element in arr:
            count=count+1
            if count==N:
                arr1.append(val)
                arr1.append(arr[count-1])
            else :
                arr1.append(arr[count-1])
    #return arr1
    print ("in fn: arr1", arr1)
    #arr=arr1
    print ("in fn: arr", arr)
    #arr=[]
    #arr.delete()
    print ("in fn: arr=[]=", arr)
    for element in arr1:
        arr.append(element)
    print ("in fn: arr", arr)

def ArrayIns3(arr, N, val):# works incorrect
    arr1=[]
    OldLength=ArrayLength(arr)
    NewLength=OldLength+1
    if N>=1 and N<=OldLength:
        count=0
        for element in arr:
            count=count+1
            if count==N:
                arr1.append(val)
                arr1.append(arr[count-1])
            else :
                arr1.append(arr[count-1])
    del arr[:]
    #return arr1
    print ("in fn: arr1", arr1)
    arr=arr1
    print ("in fn: arr", arr)

def ArrayIns4(arr, N, val):
    arr1=[]
    OldLength=ArrayLength(arr)
    NewLength=OldLength+1
    if N>=1 and N<=OldLength:
        count=0
        for element in arr:
            count=count+1
            if count==N:
                arr1.append(val)
                arr1.append(arr[count-1])
            else :
                arr1.append(arr[count-1])
    del arr[:]
    #return arr1
    print ("in fn: arr1", arr1)
    for element in arr1:
        arr.append(element)
    print ("in fn: arr", arr)

def ArrayInsTo(arr, N, val):
    arr1=[]
    OldLength=ArrayLength(arr)
    #NewLength=OldLength+1
    if N>=1 and N<=OldLength:
        count=0
        for element in arr:
            count=count+1
            if count==N:
                arr1.append(val)
                arr1.append(arr[count-1])
            else :
                arr1.append(arr[count-1])
    #return arr1
    print ("in fn: arr1", arr1)
    arr=arr1
    print ("in fn: arr", arr)
    return arr

def ArrayClear(arr):
    del arr[:]

def ArrayDel(arr, FromN, ToN):
    del arr[FromN:ToN]

print("length of a=",ArrayLength(a))
ArrayAdd(a,500)
print("added 500, now a=",a)
print("Inserted(N4) 1000 into N1",a)
ArrayIns4(a,1,1000)
print("a=",a)
a.insert(2,-45)
print("ins std, a=",a)
#print("now length of a list is: ",a.count())
ArrayDel(a,2,4)
print("Del from a from 2 to 4, now a=",a)
#ArrayIns3(a,1,1000)
#print("Inserted(N3) 1000 into N1, now a=",a)
print("Inserted(N1) 1000 into N1",a)
ArrayIns1(a,1,1000)
print("a=",a)
print("Inserted(N2) 1000 into N1",a)
ArrayIns2(a,1,1000)
print("a=",a)
print("Inserted(N3) 1000 into N1",a)
ArrayIns3(a,1,1000)
print("a=",a)
a=ArrayInsTo(a,1,-1000)
print("InsTo, a=",a)
a.insert(2,-45)
print("ins std, a=",a)
#a.clear()
#print("cleared, a=",a)

class Polynome:
    c=[]
    ReX=[]
    ImX =[]
    def Show_c(self):
        print("c=", self.c)
    def add_c(self, x):
        self.c.append(x)
    def ClearCoefs(self):
        ArrayClear(self.c)
        #del self.c[:]
    def CountCoefs(self):
        return ArrayLength(self.c)
    def SetEquationCoefs(self,c):
        self.c=c
    def Solve(self):
        q=self.CountCoefs()
        del self.ReX[:]
        del self.ImX[:]
        if q<=1:
            print("Equation's coefs are not defined")
        elif q==1+1:
            ReX=-self.c[2-1]/self.c[1-1]
            ImX=0
            self.ReX.append(ReX)
            self.ImX.append(ImX)
        elif q==1+2:
            c=self.c[0]
            b=self.c[1]
            a=self.c[2]
            d=b*b-4*a*c
            if d>=0:
                ReX=(-b-math.sqrt(d))/2/a
                ImX=0
                self.ReX.append(ReX)
                self.ImX.append(ImX)
                ReX=(-b+math.sqrt(d))/2/a
                ImX=0
                self.ReX.append(ReX)
                self.ImX.append(ImX)
            else:
                ReX=-b/(2*a)
                ImX=-math.sqrt(-d)/2/a
                self.ReX.append(ReX)
                self.ImX.append(ImX)
                ImX=math.sqrt(-d)/2/a
                self.ReX.append(ReX)
                self.ImX.append(ImX)
         
    def ShowSolution(self):
        count=0
        Q=ArrayLength(self.ReX)
        print("Equation has ",Q," Solution(s):")
        for x in self.ReX:
            count=count+1
            print(count,") ",x)
    
    def EquationToString(self):
        count=-1
        s=""
        sc=""
        for c in self.c:
            count=count+1
            sc=str(c)
            if count>0:
                sc="+"+sc+"*x"
            if count>1:
                sc=sc+"^"+str(count)
            s=s+sc
        s=s+"=0"
        return s;
    def ShowEquation(self):
        s=self.EquationToString()
        print("Equation: "+s)
    def get_c(self):
        return self.c
    def get_ReX(self):
        return self.ReX
    def get_ImX(self):
        return self.ImX
            

polynome=Polynome()
polynome.Show_c()
polynome.add_c(10)
polynome.add_c(20)
polynome.Show_c()
polynome.ClearCoefs()
polynome.Show_c()
polynome.SetEquationCoefs([2,2])
polynome.ShowEquation()
polynome.Solve()
polynome.ShowSolution()
polynome.SetEquationCoefs([1,4,1])
polynome.ShowEquation()
polynome.Solve()
polynome.ShowSolution()

class Array2D:
    content=[]
    def SetContent(self,content):
        self.content=content
    def GetContent(self):
        return self.content
    def GetQExtRows(self):
        return ArrayLength(self.content)
    def GetLengthOfExtRowN(self, N):
        R=0
        QExtRows=self.GetQExtRows()
        if N>=1 and N<=QExtRows:
            R=ArrayLength(self.content[N-1])
        return R
    def GetExtRowN(self, N):
        return self.content[N-1]
    def GetMaxExtRowLength(self):
        R=0
        count=0
        for ExtRow in self.content:
            count=count+1
            L=ArrayLength(self.GetExtRowN(count))
            if (count==1 or ( count>1 and L>R)):
                R=L
        return R
    def GetMinExtRowLength(self):
        R=0
        count=0
        for ExtRow in self.content:
            count=count+1
            L=ArrayLength(self.GetExtRowN(count))
            if (count==1 or ( count>1 and L<R)):
                R=L
        return R
    def GetInnerRowN(self, N):#, Show1Hide0):
        InnerRow=[]
        count=0
        QExtRows=self.GetQExtRows()
        MinLen=self.GetMinExtRowLength()
        MaxLen=self.GetMaxExtRowLength()
        #print("GetInnerRowN starts working")
        #print("N=",N," QExt=",QExtRows,"MinLen=",MinLen, "MaxLen=",MaxLen)
        if(QExtRows>0 and N>=1 and N<=MinLen):
            #print("N is within length of ext rows. Analyzing...")
            for ExtRow in self.content:
                count=count+1
                LCur=self.GetLengthOfExtRowN(count)
                #print("row # ",count, " Length=",LCur)
                CurRow=self.GetExtRowN(count)
                #print(CurRow)
                if N<=LCur:
                    InnerRow.append(self.content[count-1][N-1])
                #else:
                    #print("nil ab hic row") 
        #else:
            #print("Inner row (column) seems to be empty")
        #print("GetInnerRowN finishes working")
        return InnerRow
    def SetVal(self, val, ExtRowN, IneRowN):
        QExtRows=self.GetQExtRows()
        NLen=self.GetLengthOfExtRowN(IneRowN)
        if(ExtRowN>=1 and ExtRowN<=QExtRows and IneRowN>=1 and IneRowN<=NLen):
            self.content[ExtRowN-1][IneRowN-1]=val
        else:
            print("out of bounds")
    def GetVal(self, ExtRowN, IneRowN):
        QExtRows=self.GetQExtRows()
        NLen=self.GetLengthOfExtRowN(IneRowN)
        if(ExtRowN>=1 and ExtRowN<=QExtRows and IneRowN>=1 and IneRowN<=NLen):
            val=self.content[ExtRowN-1][IneRowN-1]
        else:
            print("out of bounds")
        return val
    # Add, Ins, Del:  Ext and Inner row
    # class tableContent: Lines, Columns acc to LC_not_CL



class Table:
    content=[]
    LineOfColHeader=[]
    ColOfLineHeader=[]
    def SetTableHeader(self, TableHeader):
        self.TableHeader=TableHeader
    def GetTableHeader(self):
        return self.TableHeader
    def GetQLines(self):
        return ArrayLength(slf.content)
    def GetContentLineN(self, N):
        Length=ArrayLength(slf.content)
        if N>=1 and N<=Length:
            return content[N-1]
    def GetLineN(self, N):
        ContentLine=GetContentLineN(N)
        if ArrayLength(self.ColOfLineHeader)>0:
            LineHeader=self.ColOfLineHeader[N-1]
        return [LineHeader, ContentLine]

tbl=Table()
tbl.SetTableHeader("Table")
s=tbl.GetTableHeader()
print("Table header=",s)

print("Array 2D:")
arr2=Array2D()
arr2.SetContent([[11,12,13],[21,22,23],[31,32,33]])
print(arr2.GetContent())
c2=arr2.GetInnerRowN(2)
print("col # 2 = ",c2)
arr2.SetVal(0,2,2)
print("c[2][2]=0")
print(arr2.GetContent())

def BothHaveSameSimpleType(a,b):
    BothSameSimple=not isinstance(a, list) and isinstance(b, list)
    if BothSameSimple:
        BothInt=isinstance(a, int) and isinstance(b, int)
        BothFloat=isinstance(a, float) and isinstance(b, float)
        BothString=isinstance(a, str) and isinstance(b, str)
        BothBool=isinstance(a, bool) and isinstance(bm, bool)
        BothLists=isinstance(a, list) and isinstance(b, list)
        BothSameSimple=BothInt or BothFloat or BothString or BothBool
    return BothSameSimple

def BothHaveSameType(a,b):
    BothInt=isinstance(a, int) and isinstance(b, int)
    BothFloat=isinstance(a, float) and isinstance(b, float)
    BothString=isinstance(a, str) and isinstance(b, str)
    BothBool=isinstance(a, bool) and isinstance(bm, bool)
    BothLists=isinstance(a, list) and isinstance(b, list)
    BothSameSimple=BothInt or BothFloat or BothString or BothBool
    return BothSameSimple


class DataCell:
    #def GetType(self):
    #    return 1 #1- simple, 2-DB, 3-combobox, 
    def GetVal(self):
        return self.item
    def GetItem(self, N=1):
        R=0
        if isinstance(self.item, list):
            Q=ArrayLength(self.item)
            if N>=1 and N<=Q:
                R=self.item[N-1]
        else:
            R=self.item
        return R
    #ConcrType
    def GetFloatVal(self):
        return self.item
    def GetIntVal(self):
        return self.item
    def GetBoolVal(self):
        return self.item
    def GetStrVal(self):
        return self.item
    #for database
    def GetName(self, N=1):
        R=0
        if isinstance(self.SupplInf, list):
            Q=ArrayLength(self.SupplInf)
            if N>=1 and N<=Q:
                R=self.SupplInf[N-1]
        elif self.SupplInf==[]:
            R=self.MainInf
        else:
            R=self.SupplInf
        return R
    def SetName(self, names):
        self.SupplInf=names
    #for combobox
    def GetActiveN(self):
        R=0
        if isinstance(self.SupplInf, int):
            R=self.SupplInf
        return R
    def GetActiveItem(self):
        R=[]
        if not isinstance(self.item, list):
            R=self.item
        else: # list
            if isinstance(self.SupplInf,int) and self.SupplInf>=1 and self.SupplInf<=ArrayLength(self.item):
                R=self.item[self.SupplInf-1]
            else:
                R=self.item[1-1]
        return R
    def SetActiveN(self, val):
        if isinstance(val, int) and isinstance(self.item, list) and val>=1 and val<=ArrayLength(self.item):
            self.SupplInf=val
        elif not isinstance(self.item, list):
            self.SupplInf=1
    def SetActiveNByVal(self, val):
        if isinstance(self.item, list) and self.item.count(val)>0:
            self.SupplInf=self.item.index(val)
    def GetQInems():
        R=0
        if not isinstance(self.items, list):
            R=1
        else:
            R=ArrayLength(self.items)
        return R
    def GetQNanmes():
        R=0
        if not isinstance(self.SupplInf, list):
            R=1
        else:
            R=ArrayLength(self.SupplInf)
        return R
    #
    def Set(self, NainInf, SupplInf=[]):
        self.item=NainInf
        self.SupplInf=SupplInf
    def ToString(self):#new 2021-08-12
        return str(self.GetName())
        
            
            
a=["ab","bc,","bc", "cd"]
print("a=",a)
#Q=count(a,"bc")
print("in a: bc: ",str(a.count("bc"))," times")
#print("in a: bc: ",Q," times")
print("in a: ef: ",str(a.count("ef"))," times")

MyCell=DataCell()
MyCell.Set(["one","two","three"],2)
s=MyCell.GetActiveN()
print("activeN=",s)
s=MyCell.GetActiveItem()
print("active val=",s)
MyCell.Set(2,["Colors", "clr"])
s=MyCell.GetName(2)
print("name N2=",s)
s=MyCell.GetVal()
print("val=",s)
s=MyCell.ToString()#new
print("val s =",s)

#class SimpleDataCell(TDataCell): # ce DataCell
    
#class AdvancedDataCell(TDataCell):

#class ComboboxDataCell(TDataCell):
    

#class AdvancedDataCell(TDataCell):
    

class DataCellRow:
    row=[]
    def GetCellN(self, N):
        R=0
        Q=self.ArrayLength(self.row)
        if N>=1 and N<=Q:
            R=self.row[N-1]
        return R
    def GetNameN(self, CellN, NameN=1):
        R=""
        cell=self.GetCellN(CellN)
        if cell!=0:
            R=cell.GetName(NameM)
        return R
    def Add(self, cell):
        ArrayAdd(self.row, cell)
    def ToString(self):
        R=""
        for element in self.row:
            R=R+element.ToString()
        return R
    def Show(self):
        s=self.ToString()
        print(s)
        

row1=DataCellRow()
a=DataCell()
a.Set("N1", "X1")
row1.Add(a)
a.Set("N2")
row1.Add(a)
a.Set("N3", 23)
row1.Add(a)
print("Row1:")
row1.Show()
#
row2=DataCellRow()
a1=DataCell()
a1.Set("N1", "X1")
row2.Add(a1)
a2=DataCell()
a2.Set("N2")
row2.Add(a2)
a3=DataCell()
a3.Set("N3", 45)
row2.Add(a3)
print("Row2:")
row2.Show()



a=1
b=2
c=8
d=b*b-4*a*c
if d>=0:
    ReX1= (-b - math.sqrt(d)) / (2 * a)
    ReX2= (-b + math.sqrt(d)) / (2 * a)
    ImX1=0
    ImX2=ImX1
    print("x1=", ReX1, " x2=",ReX2)
else:
    ReX1=-b/(2*a)
    ReX2=ReX1
    ImX1=-math.sqrt(-d)/ (2 * a)
    ImX2 = math.sqrt(-d) / (2 * a)
    print("x1=",ReX1,"+ i*",ImX1, "x2=",ReX2,"+ i*",ImX2)

#e=MyLib.Double(b)
#print("b=",b," e=2*b=",e)

from Tkinter import *#ce in t 2 Tkinter, in pt 3 tkinter

def click_button():
    global clicks
    clicks+=1
    root.title("Clicks {}".format(clicks))

root=Tk()
root.title("Графическая программа на Python")
root.geometry("400x300+250+200")
#btn = Button(text="Hello")
btn = Button(text="Click Me", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)
btn.pack()
root.mainloop()
