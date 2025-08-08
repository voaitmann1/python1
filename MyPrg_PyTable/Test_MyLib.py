from MyLib import *
import copy

Lmal=6
Lbig=15
inLength=Lmal
bef="1"
aft="2"
FillAft="."
FillBef=" "
BefCut="<"
AftCut=">"
BefNonCut=" "
AftNonCut=" "
BefMark="+"
AftMark=" "
#
s="MyString"
data=s
AlignL1R2CL3CR4=1
vsh=0
for i in range(0, len(s)-(len(s)-inLength)+1):
    QHidden=i
    #s=StringFormat(data, bef, aft, inLength, QHidden, AlignL1R2CL3CR4)+"|"
    #s=StringFormat(data, inLength, QHidden, AlignL1R2CL3CR4)+"|"
    s=StringFormat(data, inLength, QHidden, AlignL1R2CL3CR4, FillAft, FillBef, BefCut, AftCut, BefNonCut, AftNonCut, BefMark, AftMark, vsh)
    print(s)
print("")
AlignL1R2CL3CR4=2
vsh=0
for i in range(0, len(s)-(len(s)-inLength)+1):
    QHidden=i
    #s=StringFormat(data, bef, aft, inLength, QHidden, AlignL1R2CL3CR4)+"|"
    #s=StringFormat(data, inLength, QHidden, AlignL1R2CL3CR4)+"|"
    s=StringFormat(data, inLength, QHidden, AlignL1R2CL3CR4, FillAft, FillBef, BefCut, AftCut, BefNonCut, AftNonCut, BefMark, AftMark, vsh)
    print(s)
print("")
AlignL1R2CL3CR4=3
vsh=0
for i in range(0, len(s)-(len(s)-inLength)+1):
    QHidden=i
    #s=StringFormat(data, bef, aft, inLength, QHidden, AlignL1R2CL3CR4)+"|"
    #s=StringFormat(data, inLength, QHidden, AlignL1R2CL3CR4)+"|"
    s=StringFormat(data, inLength, QHidden, AlignL1R2CL3CR4, FillAft, FillBef, BefCut, AftCut, BefNonCut, AftNonCut, BefMark, AftMark, vsh)
    print(s)
print("")
AlignL1R2CL3CR4=4
vsh=0
for i in range(0, len(s)-(len(s)-inLength)+1):
    QHidden=i
    #s=StringFormat(data, bef, aft, inLength, QHidden, AlignL1R2CL3CR4)+"|"
    #s=StringFormat(data, inLength, QHidden, AlignL1R2CL3CR4)+"|"
    s=StringFormat(data, inLength, QHidden, AlignL1R2CL3CR4, FillAft, FillBef, BefCut, AftCut, BefNonCut, AftNonCut, BefMark, AftMark, vsh)
    print(s)
print("")
vsh=1
for i in range(0, len(s)-(len(s)-inLength)+1):
    QHidden=i
    #s=StringFormat(data, bef, aft, inLength, QHidden, AlignL1R2CL3CR4,".", " ", 1)+"|"
    #s=StringFormat(data, inLength, QHidden, AlignL1R2CL3CR4,".", " ", 1)+"|"
    s=StringFormat(data, inLength, QHidden, AlignL1R2CL3CR4, FillAft, FillBef, BefCut, AftCut, BefNonCut, AftNonCut, BefMark, AftMark, vsh)
    print("")
print("")
print("")
s="Str"
data=s
AlignL1R2CL3CR4=1
vsh=0
for i in range(0, len(s)-(len(s)-inLength)+1):
    QHidden=i
    #s=StringFormat(data, bef, aft, inLength, QHidden, AlignL1R2CL3CR4)+"|"
    #s=StringFormat(data, inLength, QHidden, AlignL1R2CL3CR4)+"|"
    s=StringFormat(data, inLength, QHidden, AlignL1R2CL3CR4, FillAft, FillBef, BefCut, AftCut, BefNonCut, AftNonCut, BefMark, AftMark, vsh)
    print(s)
print("")
AlignL1R2CL3CR4=2
vsh=0
for i in range(0, len(s)-(len(s)-inLength)+1):
    QHidden=i
    #s=StringFormat(data, bef, aft, inLength, QHidden, AlignL1R2CL3CR4)+"|"
    #s=StringFormat(data, inLength, QHidden, AlignL1R2CL3CR4)+"|"
    s=StringFormat(data, inLength, QHidden, AlignL1R2CL3CR4, FillAft, FillBef, BefCut, AftCut, BefNonCut, AftNonCut, BefMark, AftMark, vsh)
    print(s)
print("")
AlignL1R2CL3CR4=3
vsh=0
for i in range(0, len(s)-(len(s)-inLength)+1):
    QHidden=i
    #s=StringFormat(data, bef, aft, inLength, QHidden, AlignL1R2CL3CR4)+"|"
    #s=StringFormat(data, inLength, QHidden, AlignL1R2CL3CR4)+"|"
    s=StringFormat(data, inLength, QHidden, AlignL1R2CL3CR4, FillAft, FillBef, BefCut, AftCut, BefNonCut, AftNonCut, BefMark, AftMark, vsh)
    print(s)
print("")
AlignL1R2CL3CR4=4
vsh=0
for i in range(0, len(s)-(len(s)-inLength)+1):
    QHidden=i
    #s=StringFormat(data, bef, aft, inLength, QHidden, AlignL1R2CL3CR4)+"|"
    #s=StringFormat(data, inLength, QHidden, AlignL1R2CL3CR4)+"|"
    s=StringFormat(data, inLength, QHidden, AlignL1R2CL3CR4, FillAft, FillBef, BefCut, AftCut, BefNonCut, AftNonCut, BefMark, AftMark, vsh)
    print(s)
print("")
print("")
vsh=1
for i in range(0, len(s)-(len(s)-inLength)+1):
    QHidden=i
    #s=StringFormat(data, bef, aft, inLength, QHidden, AlignL1R2CL3CR4,".", " ", 1)+"|"
    #s=StringFormat(data, inLength, QHidden, AlignL1R2CL3CR4,".", " ", 1)+"|"
    s=StringFormat(data, inLength, QHidden, AlignL1R2CL3CR4, FillAft, FillBef, BefCut, AftCut, BefNonCut, AftNonCut, BefMark, AftMark, vsh)
    print("")

