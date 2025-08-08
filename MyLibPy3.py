
clicks=0

def ArrayLength(arr):
    count=0
    for element in arr:
       count=count+1
    return count
def ArrayAdd(arr, val):
    arr.append(val)
    #return arr


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

def MyStrLJust(data, inLength, FillAft=".", FillBef=" "):
    L=len(data)
    d=inLength-L


def StringFormat(data, bef, aft, inLength, QHidden, AlignL1R2CL3CR4, FillAft=".", FillBef=" "):
    R=""
    q=len(data)
    #StrToPlace=bef+data+aft
    #StrToPlace=bef+data[QHidden:]+aft
    StrFull=bef+data+aft
    StrToPlace=StrFull[QHidden:]
    Li=ArrayLength(StrToPlace)
    if Li>=inLength:
        R= StrFull[QHidden:inLength]  
    else:
        if AlignL1R2CL3CR4==1:
            pass
        elif AlignL1R2CL3CR4==2:
            pass   
        elif AlignL1R2CL3CR4==3:
            R=StrToPlace.center(inLength, bef) 
        elif AlignL1R2CL3CR4==4:
            R=StrToPlace.center(inLength, bef) 
#e=MyLib.Double(b)
#print("b=",b," e=2*b=",e)

#strng="strong"
#Q=len(strng)
#print("length of "+strng+" = "+str(Q))
#arr=[1,2,3,4,5,7]
#Q=len([1,2,3,4,5,7])
#print("length of ",arr," = "+str(Q))
#^ works gut

def DefExtrRowLensIn2DArr(rows):
    Lmax=0
    LMin=0
    LCur=0
    CurRowN=0
    for row in rows:
        CurRowN+=1
        LCur=len(row)
        if CurRowN==1 or LCur>Lmax:
            Lmax=LCur
        if CurRowN==1 or LCur<Lmin:
            Lmin=LCur
    R=[Lmin, Lmax]
    return R

def FindRestOfDivInt(ToDivideExt, DivideToExt):
    if ToDivideExt<0:
        ToDivide=-ToDivideExt
    else:
        ToDivide=ToDivideExt
    if DivideToExt<0:
        DivideTo=-DivideToExt
    else:
        DivideTo=DivideToExt
    z=0
    while z<ToDivide:
        z+=DivideTo
    rest=z-ToDivide
    return rest


#ToDivide=5
#DivideTo=5
#print(ToDivide," % ",DivideTo," = ",FindRestOfDivInt(ToDivide,DivideTo))
#^ works gut

#arr=[[1,2,3],['1','2','3'],[1,2,3,4],['1','2']]
#print( "array: ",arr," min, max: ",MyLib.DefExtrRowLensIn2DArr(arr))
#^ works gut

from tkinter import *#ce in t 2 Tkinter, in pt 3 tkinter

def click_button():
    global clicks
    clicks+=1
    root.title("Clicks {}".format(clicks))

root=Tk()
root.title("Ce Python")
root.geometry("400x300+250+200")
#btn = Button(text="Hello")
btn = Button(text="Click Me", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)
btn.pack()
root.mainloop()
