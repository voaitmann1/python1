from TableReprSimple import *

MyRepr=TableRepr()



LineN=1
ColN=3
CellSelfText="11"
LHSelfText="10"
CHSelfText="10"
LGHSelfText="X"
CGHSelfText="Y"
THdrSelfText="M"
vsh=0

print("Simple:")
MyRepr.SetAsSimple()
s=MyRepr.GetContentCellBef(  LineN,       ColN,       CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh)
print(s)
print("Matrix:")
MyRepr.SetAsMatrix()
s=MyRepr.GetContentCellBef(  LineN,       ColN,       CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh)
print(s)
print("Fn 2D:")
MyRepr.SetAsFn2D()
s=MyRepr.GetContentCellBef(  LineN,       ColN,       CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh)
print(s)
print("Full Info:")
MyRepr.SetAsFullInfo()
s=MyRepr.GetContentCellBef(  LineN,       ColN,       CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh)
print(s)
