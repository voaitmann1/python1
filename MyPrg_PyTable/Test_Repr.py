from TableReprSimple import *

MyRepr=TableRepr()

#Goods
# Item\\ Param         Prise Quantity
# Smartphone Samsung J1  100   20
#
#Goods, Item N1: Smartphone Samsung J1: Param #1 - Price: 100
#Param #1 -Price (Goods, Item #1: Smartphone Samsung J1): 100
#Goods, Param #1 - Price (Item N1: Smartphone Samsung J1): 100
#Goods, 1: Smartphone Samsung J1 - Price: 100
#Price (Goods, 1: Smartphone Samsung J1): 100
#Goods, #1 Price (#1: Smartphone Samsung J1): 100

#Content cell and its surrounding:
LineN=1
ColN=3
CellSelfText="11"
LHSelfText="10"
CHSelfText="20"
LGHSelfText="X"
CGHSelfText="Y"
THdrSelfText="M"
vsh=0

print("Simple:")
MyRepr.SetAsSimple()
s=MyRepr.GetContentCellByRepr(  LineN,       ColN,       CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh)
print(s)
print("Matrix:")
MyRepr.SetAsMatrix()
s=MyRepr.GetContentCellByRepr(  LineN,       ColN,       CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh)
print(s)
print("Fn 2D:")
MyRepr.SetAsFn2D()
s=MyRepr.GetContentCellByRepr(  LineN,       ColN,       CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh)
print(s)
print("Full Info:")
MyRepr.SetAsFullInfo()
s=MyRepr.GetContentCellByRepr(  LineN,       ColN,       CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh)
print(s)
print("Cathegories Of Goods:")
MyRepr.SetAsCathegoriesOfGoods()
s=MyRepr.GetContentCellByRepr(  LineN,       ColN,       CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh)
print(s)
MyRepr.SetAsCathegoriesOfGoods(1,1,1)
s=MyRepr.GetContentCellByRepr(  LineN,       ColN,       CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh)
print(s)
MyRepr.SetAsCathegoriesOfGoods_ItemAsExampleOfParam()
s=MyRepr.GetContentCellByRepr(  LineN,       ColN,       CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh)
print(s)
MyRepr.SetAsCathegoriesOfGoods_ItemAsExampleOfParam(1,1,1)
s=MyRepr.GetContentCellByRepr(  LineN,       ColN,       CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh)
print(s)

LineN=1
ColN=3
CellSelfText="100"
LHSelfText="Smartphone Samsung J1"
CHSelfText="Price"
LGHSelfText="Item"
CGHSelfText="Param"
THdrSelfText="Goods"

print("SetAsCathegoriesOfGoods:")
MyRepr.SetAsCathegoriesOfGoods()
#MyRepr.ShowToConsole()
s=MyRepr.GetContentCellByRepr(  LineN,       ColN,       CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh)
print(s)
print("")
MyRepr.SetAsCathegoriesOfGoods(1,1,1)
#MyRepr.ShowToConsole()
s=MyRepr.GetContentCellByRepr(  LineN,       ColN,       CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh)
print(s)
print("")
MyRepr.SetAsCathegoriesOfGoods_ItemAsExampleOfParam()
#MyRepr.ShowToConsole()
s=MyRepr.GetContentCellByRepr(  LineN,       ColN,       CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh)
print(s)
print("")
MyRepr.SetAsCathegoriesOfGoods_ItemAsExampleOfParam(1,1,1)
#MyRepr.ShowToConsole()
s=MyRepr.GetContentCellByRepr(  LineN,       ColN,       CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh)
print(s)
print("")
#
tblReprEq=TableRepr()
tblReprEq.general.ShowLineOfColHeader=1
tblReprEq.general.ShowColOfLineHeader=1
tblReprEq.CoLH.ShowHeader=1#default
tblReprEq.CoLH.ShowGenHeader=1
tblReprEq.CoLH.ShowRowN=1
tblReprEq.CoLHHeaderAndN_GNH1_NGH2_HGN3_HNG4=1
tblReprEq.CoLH.AftGH=SeparCharNEmpty#nil
tblReprEq.CoLHBefHdr=SeparCharNEmpty#nil
tblReprEq.CoLH.AftHdr=SeparCharNEmpty#nil
tblReprEq.CoLH.BefN=SeparCharNEmpty##
tblReprEq.CoLH.AftN=SeparCharNEmpty#
