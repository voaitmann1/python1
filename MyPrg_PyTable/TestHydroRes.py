#import HydroRes1_3
from HydroRes1_3 import *

vsh=1

R1=HResSimple()

print(R1.ToStringLong())
R2=HResSimple()
R3=HResSimple()
#print("add suc")
#R1.AddSucSmart(R2)
#rint("add par")
print('\nAdding succ:\n')
R1.AddSucSmart(R2, 0, 0, 1)
#R1.AddSucSmart(R2)
print('\n_'+R1.ToStringShort()+' Actine SubElt N='+str(R1.curSubElementN)+' of '+str(len(R1.elems))+'\n')
#R2.AddParSmart(R3)
print('\nAdding par:\n')
#R1.elems[R1.curSubElementN-1].AddParSmart(R3, 0, 0, 1)
R1.elems[R1.curSubElementN-1].AddParSmart(R3)
print('\nSystem is:\n')
R1.ShowText(0)
#
print('\n_'+R1.ToStringShort()+' Actine SubElt N='+str(R1.curSubElementN)+' of '+str(len(R1.elems))+'\n')
print('\nCoord:\n')
R1.ShowCoords_IpseAndSub(vsh)
print('\nCoord:\n')
R1.ShowCoords_IpseAndSub(0)
print('\nSystem is:\n')
R1.ShowText(0)
print("Finish")

