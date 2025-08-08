#import HydroRes1_3
from HydroRes1_3 import *

R1=HResSimple()

print(R1.ToStringLong())
R2=HResSimple()
#print("add suc")
#R1.AddSucSmart(R2)
print("add par")
R1.AddParSmart(R2)

R1.ShowText()
print("Finish")

