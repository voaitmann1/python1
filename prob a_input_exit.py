import sys

import numpy as np

A=np.array([[11, 12],[13,14]])
B=np.array([91, 92])

C=A.dot(B)
print("A", A)
print("B",B)
print("C", C)
C=np.dot(A,B)
print("A", A)
print("B",B)
print("C", C)
D=np.linalg.inv(A)
print("D", D)
F=np.dot(D, C)
print("F", F)
G=np.divide(B,A)
print("G", G)
J=np.divide(A,B)
print("J", J)
H=np.divide(A,C)
print("H",H)
X=np.linalg.solve(A, C)
print("X", X)
K=np.linalg.det(A)
print("K", K)
L=np.add(B, C)
print("L", L)
#X1=np.linalg.solve(B, A)
#print("X1", X1)

while 1==1:
    choice=input("continue yes/no?")
    if choice=="yes":
        print('I continue')
    else:
        print('I exit')
        exit()
    for i in range(1, 10+1):
        print(i)


