#from MyCellsDiffTypes-NoHeirs-py2 import *#invalid syntrax "-"
from MyCellsDiffTypes_NoHeirs_py2 import *

#def TryFn(a,b):
#    if isinstance(a, list):
#        a.append(b)
#    else:
#        a=b
#    return a
#
#print(TryFn([],4))
##answer: [4]

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
#row.Show("; ")
print(row.ToString())

strng="strong"
Q=len(strng)
print("length of "+strng+" = "+str(Q))
Q=len(CellArr)
print("length of CellArr = "+str(Q))



#arr=[[1,2,3],['1','2','3'],[1,2,3,4],['1','2']]
#print( "array: ",arr," min, max: ",MyLibPy2.DefExtrRowLensIn2DArr(arr))   



cell_smpl1=DataCell("asd")
cell_smpl2=DataCell(2.4)

tbl=Table1()


Row=DataCellRowWithHeader1([1, 2, 3, 4, 50, 60, 7, 50, 60, 10, 11, 50, 13, 60, 14], numbers)

print(Row.

