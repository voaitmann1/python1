from MyCellsDiffTypes_NoHeirs_py2 import *

cell1=DataCell(1)
cell2=DataCell(2.5)
cell3=DataCell("str")
cell4=DataCell(2, ['item1', 'item2', 'item3'])

print("cell1: "+cell1.ToString())
print("cell2: "+cell2.ToString())
print("cell3: "+cell3.ToString())
print("cell4: "+cell4.ToString())
print("cell4: "+str(cell4.GetItem()))#3 args given, must be 2 max
print("cell4: "+str(cell4.GetVal()))#3 args given, must be 2 max

