#import PyStdVector # so ne works!
#I geved so: it'd work, if import fns, ma classes s'import'd as below:
from PyStdVector import My1DArray, My2DArray1, MyCell
import copy
#
#
vector=My1DArray()
#
vector.Add(2)#1
vector.Add(4)#2
vector.Add(10)#3
vector.Add(6)#4
vector.Add(2)#5
vector.Add(5)#6
vector.Add(5)#7
#
print("vector.Add(2)-1")
print("vector.Add(4)-2")
print("vector.Add(10)-3")
print("vector.Add(6)-4")
print("vector.Add(2)-5")
print("vector.Add(5)-6")
print("vector.Add(5)-7")
#
print("\n-vector:\n")
vector.ShowConsole()
print("\n-del last:\n")
vector.Del()
vector.ShowConsole()
print("\n- N (15)\n")
n=vector.SeekFirst(15)
print("found at N=",n)
print("\n-Seek First N (2):\n")
n=vector.SeekFirst(2)
print("found at N=",n)
print("\n-Seek Last N(2):\n")
n=vector.SeekLast(2)
print("found at N=",n)
#print("\n- del N4:\n")
#vector.Del(4)
#vector.ShowConsole()
print("\n- del N3:\n")
vector.Del(3)
vector.ShowConsole()
print("\n- ins 300 to N3:\n")
vector.Ins(300,3)
vector.ShowConsole()
print("\n- Reverse:\n")
vector.Reverse()
vector.ShowConsole()
print("\n- Add 8:\n")
vector.Add(8)
vector.ShowConsole()
print("\n- Reverse:\n")
vector.Reverse()
vector.ShowConsole()
#
print("\n\n- 2D-array:\n")
print("\n- Adding lines thrice:\n")
my2da1_v1=My2DArray1()
print("1:")
my2da1_v1.AddExtRow([11,12,13])
print(my2da1_v1)
my2da1_v1.ShowConsole(";")#1
print("2:")
my2da1_v1.AddExtRow([21,22,23])#2
print(my2da1_v1)
my2da1_v1.ShowConsole()
print("3:")
my2da1_v1.AddExtRow([31,32,33])#3
print(my2da1_v1)
my2da1_v1.ShowConsole()
#works well
print("\n- Adding inner row")
my2da1_v1.AddIneRow([14, 24, 34])#4
my2da1_v1.ShowConsole()
#print("\n- Inserting ext row to 2nd pos:\n")
#my2d_a1.InsExtRow([1521, 1522, 1523, 1524])
print("\n- Inserting ext row to 2nd pos (write alowed):\n")
my2da1_v1.InsExtRow([1521, 1522, 1523, 1524],2,1)
print(my2da1_v1)
my2da1_v1.ShowConsole()#5
print("\n- Inserting ine row instead of last pos:\n")
my2da1_v1.InsIneRow([1354, 2352, 3354, 4354])
print(my2da1_v1)
my2da1_v1.ShowConsole()#6
print("\n- Deleting ext row at 4th pos:\n")
my2da1_v1.DelIneRow(4)
print(my2da1_v1)
my2da1_v1.ShowConsole()#7
#
print("\n\n- MyCell:\n")
cell=MyCell()
cell.data="a"
print(cell)
cell.data=1
print(cell)
cell1=MyCell()
cell1.data=2
cellRow=[cell, cell, cell1, cell1]
print("cell row: ", cellRow)
for i in range(1, len(cellRow)):
    print(i,") ",cellRow[i-1]," - ", str(cellRow[i-1].data))
    #vikt: ne works! why?
if isinstance(cell, MyCell):
    print("cell IS instance of MyCell class")
else:
    print("cell is NOT instance of MyCell class")
print("\n\n- 2D-array - One More:\n")
my2da1_v2=My2DArray1()
my2da1_v2.ShowConsole()#1-0
print("1:")
my2da1_v2.AddIneRow([11, 21, 31])
print(my2da1_v2)
my2da1_v2.ShowConsole(";")#1-1
#works well
print("\n- Adding inner row")
my2da1_v2.AddIneRow([12, 22, 32])#4
my2da1_v2.ShowConsole()#1-2
print("\n- Inserting ext row to 3rd pos:\n")
my2da1_v2.InsExtRow([1521, 1522, 1523, 1524])
print(my2da1_v2)
my2da1_v2.ShowConsole()#1-3
#print("\n- Inserting ext row to 2nd pos, alowing torn and writing steps:\n")
#my2d_a2.InsExtRow([1521, 1522, 1523, 1524],2,1)
print("\n- Inserting ext row to 3rd pos, alowing torn and writing steps:\n")
my2da1_v2.InsExtRow([1521, 1522, 1523, 1524],3,1)
print(my2da1_v2)
my2da1_v2.ShowConsole()#1-4
#print("\n- Deleting ext row at 3rd pos:\n")
#my2da1_v2.DelExtRow(3) #work't gut
print("\n- Deleting ext row at 4th pos:\n")
my2da1_v2.DelExtRow(4)
print(my2da1_v2)
my2da1_v2.ShowConsole()#1-5
print("\n- Inserting ext row to 2th pos, alowing torn and writing steps:\n")
my2da1_v2.InsExtRow([4531, 4532, 4533, 4534],2,1)
print(my2da1_v2)
my2da1_v2.ShowConsole()#1-6
print("\n- Inner (vetical) row N4:\n")
r=my2da1_v2.GetIneRowN_usual(4)
print("r=",r)
print("\n- Inner (vetical) row N2:\n")
r=my2da1_v2.GetIneRowN_usual(2)
print("r=",r)
print("\n- Ext (horizontal) row N1:\n")
r=my2da1_v2.GetExtRowN_usual(1)
print("r=",r)
#
my2da1_v3=My2DArray1()
print("\nTransposing not making rectangular")
list1=my2da1_v2.TransposeTo()
my2da1_v3.row=list1
my2da1_v3.ShowConsole()#2-1
#
print("last cell=",my2da1_v3.row[1-1][2-1])
#print("empty cell=",my2da1_v3.row[1-1][3-1])
print("1st row length="+str(len(my2da1_v3.row[1-1])))
#
my2da1_v4=copy.deepcopy(my2da1_v3)
#
print("Transposing not making rectangular by cutting to min")
list1=my2da1_v2.TransposeTo(1)
my2da1_v3.row=list1
my2da1_v3.ShowConsole()#2-2
print("Transposing not making rectangular by stretching to max")
list2=my2da1_v2.TransposeTo(2)#vikt: ne works! why?
my2da1_v3.row=list2
my2da1_v3.ShowConsole()#2-3
#
print("\nLet be such")
my2da1_v4.ShowConsole()#4-1
print("\nSwap inner rows 1 and 3, stretch forbidden")
my2da1_v4.SwapIneRows(1,3)
my2da1_v4.ShowConsole()#4-2
#
my2da1_v5=copy.deepcopy(my2da1_v4)
#
print("\nSwap inner rows 1 and 2, stretch forbidden")
my2da1_v4.SwapIneRows(1,2)
my2da1_v4.ShowConsole()#4-3
print("\nLet be such")
my2da1_v5.ShowConsole()#5-1
print("\nSwap inner rows 1 and 3, stretch allowed")
print("1st row length="+str(len(my2da1_v5.row[1-1])))
my2da1_v5.SwapIneRows(1,3,1)
print("1st row length="+str(len(my2da1_v5.row[1-1])))
my2da1_v5.ShowConsole()#5-2
print("\nSwap ext rows 2 and 3")
my2da1_v4.SwapExtRows(2,3)
my2da1_v4.ShowConsole()#4-4
print("\nVisa versa ext rows ")
my2da1_v4.OrderVisaVersaExtRows()
my2da1_v4.ShowConsole()#4-5
print("\nVisa versa ine rows (2 - stretch if torn)")
my2da1_v4.OrderVisaVersaIneRows(2)
my2da1_v4.ShowConsole()#4-6

#
print("\n 2D array: seeking value\n")
#
arr=My2DArray1()

ar=[[11,12,13,14,15],[21,22,23,24,25],[31,32,33,34,35],[41,42,43,44,45],[51,52,53,54,55]]
a1=[[11,12,13,666,15],[21,22,23,24,666],[31,32,666,34,35],[41,42,43,44,45],[51,666,53,54,55]]
arr.Set(a1)
print("Array:")
val=666
arr.ShowConsole()
print("Search ",val)
r=arr.Seek(val)
print("Quantity of found values: ",len(r))
for pair in r:
    print("Found at (",pair[1-1],",",pair[2-1],")")
r=arr.Seek_SortByIneRowN(val)
print("Sorted by inner row: ")
for pair in r:
    print("Found at (",pair[1-1],",",pair[2-1],")")
NE1=2
NE2=4
NI1=2
NI2=4
print("Extracting SubMatrix: Ext Rows ",NE1," ... ",NE2," Ine Rows ",NI1," ... ",NI2,"\n")
print("From:\n")
arr.ShowConsole()
print("Answer:\n")
arrS=arr.SubMatrix(2,4,2,4)
print(arrS)
print("Finding position of extracted submatrix")
Ns=[]
Ns=arr.Seek(arrS, 1)
if(Ns==[]):
    print("Not found")
else:
    print("Submatrix found at ", Ns)
valueToSeek=666
print("Finding position of value ",valueToSeek)
Ns=[]
Ns=arr.Seek(valueToSeek, 1)
if(Ns==[]):
    print("Not found")
else:
    print("value found at ", Ns)

# Seek, both overloaded vrns to test is left


