from MyStringLib import *
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

print("")
print("")
print("Corner:")
strs=['TN1:LGN1\CGN1', 'TN2:', 'TN3:\\', 'TN4:\CGN4', "TN4:\CGN4", "LGN4\\", "\\CGN5"]
for i in range(1, len(strs)+1):
    corner=ParseTableCorner(strs[i-1])
    corner=ParseTableCorner(strs[i-1], 1)
    print('corner=',corner)

dataSource=[["0", 1, 2, 3, 4],
            [1, 11, 12, 13, 14],
            [2, 21, 22, 23, 24],
            [3, 31, 32, 33, 34]]

R=Parse2DStrArrayAsTable(dataSource, 0, 0)
print(R)
R=Parse2DStrArrayAsTable(dataSource, 0, 1)
print(R)
R=Parse2DStrArrayAsTable(dataSource, 1, 0)
print(R)
R=Parse2DStrArrayAsTable(dataSource, 1, 1)
print(R)
