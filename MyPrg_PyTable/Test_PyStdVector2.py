from PyStdVector2 import *
import PyStdVector2 as ArrLib


arr1=[1, 2, 3, 4, 5]
print("ini arr")
print(arr1)
print("arr af set L=10")
ArrLib.Set1DArrayLength(arr1, 10, 0)
print(arr1)
print("arr af set L=5")
Set1DArrayLength(arr1, 5)
print(arr1)



dataSource=[["гриль Тефаль GC 712 OptiGril","4999","6999","Foxtrot.ua"],
            ["Пылесос Philips FC9552","3599","4999","Foxtrot.ua"],
            ["смартфон POCO X3 Pro","6799","7999","Foxtrot.ua"],
            ["Ноутбук Lenovo V15 ","9999","12999","Foxtrot.ua"],
            ["Notebook Lenovo V15 ","9999","12999","Foxtrot.ua"],
            ["Smartphone Samsung Galaxy S20 FE (2021)","16999","18999","rozetka.com.ua"],
            ["Кофемашина Delongi ECAM 550.85","22999","32999","rozetka.com.ua"],
           ]

arr=copy.deepcopy(dataSource)
print("arr:")
ShowToConsole2DArrayWhole(arr, "; ")

col1=["tested", "new", "Was Used", "experimental model", "serial model", "serial model", "serial model"]

line1=["Smartphone Lenovo","11999","13999","aliexpress.com"]#,
line2=["Smartphone Lenovo","11999","13999","new item","aliexpress.com"]#,
# hic wa "," et interp'z consider'te hic vars ne lists, ma tuples!

ExtRowN=1
IneRowN=2
AsLink0Copy1=0

# def  Get2DArrayElement_AsLink(arr, ExtRowN=1, IneRowN=1):
elt  = Get2DArrayElement_AsCopy(arr, ExtRowN, IneRowN)
se=str(elt)
print("se="+se)
sef=ToString2DArrayElement(arr, ExtRowN, IneRowN, "", "")
print("sef="+sef)

Ins2DArrayIneRow(arr, 2, col1)
print("\narr after ins col1")
ShowToConsole2DArrayWhole(arr, "; ")
print("\narr after ins line2 at pos 4")
Ins2DArrayExtRow(arr, 4, line2, 0, 0, 0)#last number is for vsh 
ShowToConsole2DArrayWhole(arr, "; ")
print("\narr after del ext row at pos 4")
Del2DArrayExtRowN(arr, 4)
ShowToConsole2DArrayWhole(arr, "; ")
print("\n","arr[",ExtRowN,", ",IneRowN,"]=",elt)
print("\narr[",ExtRowN,", ",IneRowN,"]=",ToString2DArrayElement(arr, ExtRowN, IneRowN, "", ""))
print("\narr after del ine row at pos 4")
Del2DArrayIneRowN(arr, 2, 0)
ShowToConsole2DArrayWhole(arr, " ")
print("\n2DArrayExtRow N 2:")
row=Get2DArrayExtRowN(arr, 2)
print(ToString1DArray(row))
print("\n2DArrayIneRow N 4:")
row=Get2DArrayIneRowN(arr, 4)
print(ToString1DArray(row))
print("\nSwap ext rows 1 and 7:")
Swap2DArrayExtRows(arr, 1, 7)
ShowToConsole2DArrayWhole(arr, " ")
print("\nSwap ine rows 2 and 2:")
Swap2DArrayIneRows(arr, 2, 3)
ShowToConsole2DArrayWhole(arr, " ")
print("\nSwap elements (1, 2) and (7, 3):")
Swap2DArrayElements(arr, 1, 2, 7, 3)
ShowToConsole2DArrayWhole(arr, " ")
print("\nReverse ext row N 2):")
Reverse2DArrayExtRowN(arr, 2)
ShowToConsole2DArrayWhole(arr, " ")
print("\nReverse ext row N 2):")
Reverse2DArrayExtRowN(arr, 2)
ShowToConsole2DArrayWhole(arr, " ")
print("\nReverse ine row N 1):")
Reverse2DArrayIneRowN(arr, 1)
ShowToConsole2DArrayWhole(arr, " ")
print("\nReverse ine row N 1):")
Reverse2DArrayIneRowN(arr, 1)
ShowToConsole2DArrayWhole(arr, " ")
print("\nReverse ext rows:")
Reverse2DArrayExtRows(arr)
ShowToConsole2DArrayWhole(arr, " ")
print("\nReverse ext rows:")
Reverse2DArrayExtRows(arr)
ShowToConsole2DArrayWhole(arr, " ")
print("\nReverse ine rows:")
Reverse2DArrayIneRows(arr)
ShowToConsole2DArrayWhole(arr, " ")
print("\nReverse ine rows:")
Reverse2DArrayIneRows(arr)
ShowToConsole2DArrayWhole(arr, " ")
print("\nTranspose:")
Transpose2DArray(arr)
ShowToConsole2DArrayWhole(arr, " ")
print("\nTranspose:")
Transpose2DArray(arr)
ShowToConsole2DArrayWhole(arr, " ")
print("\nIf is 1D-sub-array:")
Arr1D1=[1,2,3,4,5,6]
Arr1D2=[3,4,5]
N1=3
N2=5
L=3
y=IsSubArray1D(Arr1D1, Arr1D2, 3)
print("Seeking Sub-array")
print(ToString1DArray(Arr1D2))
print("in")
print(ToString1DArray(Arr1D1))
print("Sub-array from "+str(N1)+" L= "+str(L))
print(GetSubArray1D_FromToN(Arr1D1, N1, N2))
print(GetSubArray1D(Arr1D1, N1, L))
print("so")
print(Arr1D1[3-1:5-1+1])
if y==1:
    print("\nYes, it is sub-array")
else:
    print("\nNo, it is not sub-array")
print("\nConcrete Ns:")
y=SeekFromStart(Arr1D1, Arr1D2, 1, 0, 1)
if y==[]:
    print("\nNNo such subarray found")
else:
    print("\nFound "+str(len(y))+" object(s) at N(s): ",y)
y=SeekFirst( Arr1D1, Arr1D2)
print("answer:"+str(y))
print("Seeking single val")
Arr1D1=[1,2,3,4,5,6]
toseek=3
y=IsSubArray1D(Arr1D1, toseek, 3)
print("Seeking Sub-array")
print(ToString1DArray(Arr1D2))
print("in")
print(ToString1DArray(Arr1D1))
print("Sub-array from "+str(N1)+" L= "+str(L))
print(GetSubArray1D_FromToN(Arr1D1, N1, N2))
print(GetSubArray1D(Arr1D1, N1, L))
print("so")
print(Arr1D1[3-1:3-1+1])
if y==1:
    print("\nYes, it is sub-array")
else:
    print("\nNo, it is not sub-array")
print("\nConcrete Ns:")
y=SeekFromStart(Arr1D1, toseek, 1, 0, 1)
if y==[]:
    print("\nNNo such subarray found")
else:
    print("\nFound "+str(len(y))+" object(s) at N(s): ",y)
y=SeekFirst( Arr1D1, toseek)
print("answer:"+str(y))
    
arr=copy.deepcopy(dataSource)
print("now arr is")
ShowToConsole2DArrayWhole(arr, " ")
print("\nIf is sunmatrix:")
SubMatrixToSeek=[
            ["Пылесос Philips FC9552","3599"],
            ["смартфон POCO X3 Pro","6799"],
            ["Ноутбук Lenovo V15 ","9999"],
          ]
print("SubMatrixToSeek:")
ShowToConsole2DArrayWhole(SubMatrixToSeek, " ")
print("in:")
ShowToConsole2DArrayWhole(arr, " ")
y=IsSubMatrixAt2DArray(arr, 2, 1, SubMatrixToSeek, 1)
if y==1:
    print("\nYes, it is submatrix")
else:
    print("\No, it is not submatrix")
SubMatrixToSeek1=[
            ["Пылесос ","3599"],
            ["смартфон POCO X3 Pro","6799"],
            ["Ноутбук Lenovo V15 ","9999"],
          ]
print("SubMatrixToSeek:")
ShowToConsole2DArrayWhole(SubMatrixToSeek1, " ")
print("in:")
ShowToConsole2DArrayWhole(arr, " ")
y=IsSubMatrixAt2DArray(arr, 2, 1, SubMatrixToSeek1, 1)
if y==1:
    print("\nYes, it is submatrix")
else:
    print("\No, it is not submatrix")
print("Seek Sub-array:")
print(ToString1DArray(Arr1D2))
Arr1D1=[1, 2,  3, 4, 5,  6,  3, 4, 5,  6, 7, 3, 4, 8, 4, 5, 9,  3, 4, 5,  8, 7, 3, 3, 4,  3, 4, 5,  2, 8, 9]
#       1  2   3  4  5   6   7  8  9  10 11 12  13 14 15 16 17  18 19 20  21 22 23 24 25  26 27 28  29 30 31
print("in")
print(ToString1DArray(Arr1D1))
print("from start from 8 to 30:")
Ns=SeekFromStart(Arr1D1, Arr1D2, 8, 30, 0)# lastN - vsh
print("found "+str(len(Ns))+" at: ")
print(Ns)
print("from end from 27 to 4:")
Ns=SeekFromEnd(Arr1D1, Arr1D2, 27, 4, 0)# lastN - vsh
print("found "+str(len(Ns))+" at: ")
print(Ns)
print("\nSubMatrix (2, 4, 1, 3):")
SubMatrixToExtract=SubMatrix(arr, 2, 4, 1, 3)
ShowToConsole2DArrayWhole(SubMatrixToExtract, " ")
print("\nSeek submarix")
Arr2D1=[[11, 12, 13, 14, 15, 16, 10, 20, 30],
        [21, 22, 10, 20, 30, 26, 40, 28, 29],  
        [31, 32, 40, 34, 35, 36, 50, 60],
        [41, 42, 50, 60, 20, 30, 47, 48],
        [10, 20, 30, 40, 55, 56, 57, 10, 20],
        [40, 62, 63, 50, 60, 66, 67, 40, 69],
        [50, 60, 73, 74, 75, 76, 77, 50, 60],
        [81, 82, 83, 84, 85, 86, 87]
       ]
Arr2D2=[[10, 20, 30],
        [40],
        [50, 60]
       ]
Arr2D3=[[10],
        [40],
        [50]
       ]
ShowToConsole2DArrayWhole(Arr2D2, " ")
print("in:")
ShowToConsole2DArrayWhole(Arr2D1, " ")
#def Seek(arr, SubArr, FromExtN=1, FromIneN=1, ToExtN=0, ToIneN=0, OrdEA1ED2IA3ID4=1, vsh=0):
y=SeekSubMatrixOrVal(Arr2D1, Arr2D2, 1, 1, 0, 0, 1, 0)#last N - vsh
print("found: "+str(len(y)))
if(len(y)>0):
    print("at:")
    ShowToConsole2DArrayWhole(y, " ")
print("\nSeek val")
print("what:")
print(50)
y=SeekSubMatrixOrVal(Arr2D1, 50, 1, 1, 0, 0, 1, 0)#last N - vsh
print("found: "+str(len(y)))
if(len(y)>0):
    print("at:")
    ShowToConsole2DArrayWhole(y, " ")
print("\nSeek submarix")
print("what:")
ShowToConsole2DArrayWhole(Arr2D3, " ")
print("in:")
ShowToConsole2DArrayWhole(Arr2D1, " ")
y=SeekSubMatrixOrVal(Arr2D1, Arr2D3, 1, 1, 0, 0, 1, 0)#last N - vsh
print("found: "+str(len(y)))
if(len(y)>0):
    print("at:")
    ShowToConsole2DArrayWhole(y, " ")
print("\n************************************************************************")    
#
t=([10, 20, 30], 100)
if isinstance(t, tuple):
    print(t, "tuple")
t1=[[10, 20, 30], 100]
if isinstance(t1, list) and isinstance(t1[1-1], list) and not isinstance(t1[2-1], list):
    print(t1, "object is like headered row")
#
print("\n************************************************************************")
#
myarr1=My2DArray1(dataSource)
print("\nmyarr:")
myarr1.ShowConsole("; ")
print("\nmyarr after ins col:")
myarr1.InsIneRow(col1, 2)
myarr1.ShowConsole("; ")
print("\nmyarr after ins line:\n")
myarr1.InsExtRow(4, line1, 0, 0, 1)#last number is for vsh
myarr1.ShowConsole("; ")
#
print("\n\n")
print("\nTorn array - setting rect 4x3:\n")
arrTorn1=[[1101, 1201, 1301, 1401],
         [2101, 2201, 2301],
         [3101, 3201, 3301, 3401, 3501],
         [4101, 4201, 4301, 4401]]
#SetRect2DArray(arr, L=0, QE=0, dfltVal=0, vsh=0)
SetRect2DArray(arrTorn1, 4, 3, 0, 1)

arrTorn1=[[1101, 1201, 1301, 1401],
         [2101, 2201, 2301],
         [3101, 3201, 3301, 3401, 3501],
         [4101, 4201, 4301, 4401]]
arrTorn2=[[1102, 1202, 1302, 1402],
         [2102, 2202, 2302],
         [3102, 3202, 3302, 3402, 3502],
         [4102, 4202, 4302, 4402]]
print("\n\n")
print("\nTorn arrays - concat adding (vertically):\n")
QShift=0
How_LastM2_MaxM1_AnyOther=-2
vsh=1
dfltVal=0
Array2DConcatAddingVertically(arrTorn1, arrTorn2)#works well
print("\n\n")
print("\nTorn arrays - concat adding (horisonrally):\n")
arrTorn1=[[1101, 1201, 1301, 1401],
         [2101, 2201, 2301],
         [3101, 3201, 3301, 3401, 3501],
         [4101, 4201, 4301, 4401]]
arrTorn2=[[1102, 1202, 1302, 1402],
         [2102, 2202, 2302],
         [3102, 3202, 3302, 3402, 3502],
         [4102, 4202, 4302, 4402]]
#Array2DConcatStretchingHorisontally(arrToStretch, arrToAdd, QShift=0, How_LastM2_MaxM1_AnyOther=-2, dfltVal=0):
print("\n\n")
print("\nVar 1 First stretching to max element, no vert shift:\n")
arrTorn1=[[1101, 1201, 1301, 1401],
         [2101, 2201, 2301],
         [3101, 3201, 3301, 3401, 3501],
         [4101, 4201, 4301, 4401]]
arrTorn2=[[1102, 1202, 1302, 1402],
         [2102, 2202, 2302],
         [3102, 3202, 3302, 3402, 3502],
         [4102, 4202, 4302, 4402]]
QShift=0
How_LastM2_MaxM1_AnyOther=-1
vsh=1
dfltVal=0
Array2DConcatStretchingHorisontally(arrTorn1, arrTorn2, QShift, How_LastM2_MaxM1_AnyOther, dfltVal, vsh)
ShowToConsole2DArrayWhole(arrTorn1, " ")
print("\n\n")
print("\nVar 2 First making L=max,  vert shift=2:\n")
arrTorn1=[[1101, 1201, 1301, 1401],
         [2101, 2201, 2301],
         [3101, 3201, 3301, 3401, 3501],
         [4101, 4201, 4301, 4401]]
arrTorn2=[[1102, 1202, 1302, 1402],
         [2102, 2202, 2302],
         [3102, 3202, 3302, 3402, 3502],
         [4102, 4202, 4302, 4402]]
QShift=0
How_LastM2_MaxM1_AnyOther=-1
vsh=1
dfltVal=0
Array2DConcatStretchingHorisontally(arrTorn1, arrTorn2, QShift, How_LastM2_MaxM1_AnyOther, dfltVal, vsh)
ShowToConsole2DArrayWhole(arrTorn1, " ")
print("\n\n")
print("\nVar 3 First making L=4,  vert shift=0:\n")
arrTorn1=[[1101, 1201, 1301, 1401],
         [2101, 2201, 2301],
         [3101, 3201, 3301, 3401, 3501],
         [4101, 4201, 4301, 4401]]
arrTorn2=[[1102, 1202, 1302, 1402],
         [2102, 2202, 2302],
         [3102, 3202, 3302, 3402, 3502],
         [4102, 4202, 4302, 4402]]
QShift=0
How_LastM2_MaxM1_AnyOther=4
vsh=1
dfltVal=0
Array2DConcatStretchingHorisontally(arrTorn1, arrTorn2, QShift, How_LastM2_MaxM1_AnyOther, dfltVal, vsh)
ShowToConsole2DArrayWhole(arrTorn1, " ")
print("\n\n")
print("\nVar 4 First making L=4,  vert shift=2:\n")
arrTorn1=[[1101, 1201, 1301, 1401],
         [2101, 2201, 2301],
         [3101, 3201, 3301, 3401, 3501],
         [4101, 4201, 4301, 4401]]
arrTorn2=[[1102, 1202, 1302, 1402],
         [2102, 2202, 2302],
         [3102, 3202, 3302, 3402, 3502],
         [4102, 4202, 4302, 4402]]
QShift=2
How_LastM2_MaxM1_AnyOther=4
vsh=1
dfltVal=0
Array2DConcatStretchingHorisontally(arrTorn1, arrTorn2, QShift, How_LastM2_MaxM1_AnyOther, dfltVal, vsh)
ShowToConsole2DArrayWhole(arrTorn1, " ")
print("\n\n")
print("\nVar 5 First making L=max,  vert shift=2:\n")
arrTorn1=[[1101, 1201, 1301, 1401],
         [2101, 2201, 2301],
         [3101, 3201, 3301, 3401, 3501],
         [4101, 4201, 4301, 4401]]
arrTorn2=[[1102, 1202, 1302, 1402],
         [2102, 2202, 2302],
         [3102, 3202, 3302, 3402, 3502],
         [4102, 4202, 4302, 4402]]
QShift=2
How_LastM2_MaxM1_AnyOther=-1
vsh=1
dfltVal=0
Array2DConcatStretchingHorisontally(arrTorn1, arrTorn2, QShift, How_LastM2_MaxM1_AnyOther, dfltVal, vsh)
ShowToConsole2DArrayWhole(arrTorn1, " ")




