#import MyPolynomeEqsLib
from  MyPolynomeEqsLib import *
from  MyLinAlgLibEn import *
#-----------------------------------
#vsh=1
#C=[2, 2, 2, 2]
#X=polynomeEqOfPower3(C, 0, 0, 0, vsh)
#print("Solution:"+str(X))
#vsh=1
#C=[2, 0, -14, -12]
#X=polynomeEqOfPower3(C, 0, 0, 0, vsh)
#print("Solution:"+str(X))
#vsh=1
#C=[-12, -14, 0, 2]
#X=polynomeEqOfPower3(C, 0, 0, 0, vsh)
#print("Solution:"+str(X))
#-----------------------------------
print("complex nums: 2+3*i, 3, 2*i:")
#print(str(MyComplex(2, 3)), str(MyComplex(3, 0)), str(MyComplex(0, 2)))
print(MyComplex(2, 3), MyComplex(3, 0), MyComplex(0, 2))
print("\n")
#-----------------------------------
#R=[2, -1, -1]
#C=polynomeEqGenerator(R)
#print("roots: "+str(R))
#print("coefs: "+str(C))
#-----------------------------------
#
#print("checking generator: ")
#P=len(R)
#for i in range(P):
#    s=fPolynomeIni_coefsOrderNEqualToPower(C, R[i])
#    print("P("+str(R[i])+")="+str(s))
#------------------------------------
#C3=[2, 0, -14, -12]
#X=polynomeEqOfPower3(C3)
#print("eq 0f 3 power: "+str(X))
#------------------------------------
#C3=[-12, -14, 0, 2]
#X=polynomeEqOfPower3(C3)
#print("eq 0f 3 power: "+str(X))
#------------------------------------
R=[1, 2, 3, 4]
C=polynomeEqGenerator(R)
print("roots: "+str(R))
print("coefs: "+str(C))
#
print("1*4**4-10*4**3+35*4**2-50*4+24=",1*4**4-10*4**3+35*4**2-50*4+24)
#
print("checking generator: ")
P=len(R)
for i in range(P):
    s=fPolynomeIni_coefsOrderNEqualToPower(C, R[i])
    print("P("+str(R[i])+")="+str(s))
print("Solution: ")
vsh=1
#X=polynomeEqOfPower4([24, -50, 35, -10, 1])
X=polynomeEqOfPower4([1, -10, 35, -50, 24])
print(X)
