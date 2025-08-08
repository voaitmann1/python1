#import arrSearch2
from arrSearch2 import *

#a1_1=[11, 12, 13, 14, 15, 16, 17, 18]
#a1_2=[21, 22, 23, 24, 25, 26, 27, 28]
#a1_3=[31, 32, 33, 34, 35, 36, 37, 38]
#a1_4=[41, 42, 43, 44, 45, 46, 47, 48]
#a1_5=[51, 52, 53, 54, 55, 56, 57, 58]
#a1_6=[61, 62, 63, 64, 65, 66, 67, 68]
#a1_7=[71, 72, 73, 74, 75, 76, 77, 78]
#a1_8=[81, 82, 83, 84, 85, 86, 87, 88]

a1_1=[30, 20, 10, 20, 30, 10, 20, 30, 19]
a1_2=[21, 22, 40, 23, 24, 40, 26, 27]
a1_3=[31, 60, 50, 60, 34, 35]
a1_4=[41, 42, 40, 44, 45, 46, 10, 20, 30]
a1_5=[51, 10, 20, 30, 55, 40, 57, 58]
a1_6=[61, 20, 63, 10, 40, 50, 60]
a1_7=[71, 30, 73, 20, 75, 60, 77, 78]
a1_8=[81, 82, 83, 30, 85, 86, 87, 88]

a2_1=[a1_1, a1_2, a1_3, a1_4, a1_5, a1_6, a1_7, a1_8]

print("a2_1:")
arr2D_print(a2_1, elementSeparator=", ", lineSeparator="; ", singleLine=0)
print("\na2_1:")
arr2D_print(a2_1, elementSeparator=", ", lineSeparator="; ", singleLine=1)

arr2_2=[[10, 20, 30], [40], [50, 60]]

extRowOfArr2DMayBe_Row0EmptyList1NonList2=1
ExtRowsTransposedAndReversed=0
IneRowsTransposed=0
Ns=arr2D_SeekSubArr2D(a2_1, arr2_2, extRowOfArr2DMayBe_Row0EmptyList1NonList2, ExtRowsTransposedAndReversed, IneRowsTransposed)

print("Ext rows nt transposed and reversed, Ine  rows not ttransposed", Ns)
