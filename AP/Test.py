
#import numpy as np
from MyLinAlgLibEn import *
print()
print (complexify(3))
print()
print (complexify([1, 2, 3, 2]))
print()
print (complexify([[1, 2, 3],[2, 3, 4], [4, 5, 6]]))
print()
print (Re(3+0j))
print()
print (Re([1+0j, 2+0j, 3+0j, 2+0j]))
print()
print (Re([[1+0j, 2+0j, 3+0j],[2+0j, 3+0j, 4+0j], [4+0j, 5+0j, 6+0j]]))


A=[[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 0, -34], [41, 42, 43, -44]]
B=np.array(A)
print("Matrix")
#for row in A:
for row in B:
    print(row)
#
#v, w = np.linalg.eig(np.array(A))#works
v, w = np.linalg.eig(B)
print("eigen vals fully auto: "+str(v))
#Qa, Ra=np.linalg.qr(np.array(A))#works
Qa, Ra=np.linalg.qr(B)
print("QR fully auto")
print("Q:")
for row in Qa:
    print(row)
print("R:")
for row in Ra:
    print(row)
E=np.eye(4)
print("E:")
for row in E:
    print(row)
num_iterations=20
for i in range(num_iterations):
    Q, R = np.linalg.qr(B)
    B= np.dot(R, Q)
print("final B:")
for row in B:
   print(row)
print("Eigenvalues of B:")
eigenvalues=[]
for i in range(len(B)):
    #eigenvalues[i] = B[i, i]
    eigenvalues.append(B[i, i])
print(eigenvalues)
B=np.array(A)
print("C = B complexified:")
C=complexify(B)
for row in C:
   print(row)
for i in range(num_iterations):
    Q, R = np.linalg.qr(C)
    C= np.dot(R, Q)
print("final C:")
for row in C:
   print(row)
print("Eigenvalues of B:")
eigenvalues=[]
for i in range(len(C)):
    #eigenvalues[i] = B[i, i]
    eigenvalues.append(C[i, i])
print(eigenvalues)
print("gpt alg1:")
print("C = B complexified:")
C=complexify(B)
for row in C:
   print(row)
eigenvalues=complex_gpt_qr_algorithm(A, num_iterations)
print("Eigenvalues of C:")
print(eigenvalues)
D = np.array([[1, 2], [3, 4]], dtype=complex)
num_iterations = 10
eigenvalues = complex_qr_algorithm(D, num_iterations)
print("Complex Eigenvalues:", eigenvalues)
eigenvalues = complex_gpt_qr_algorithm(D, num_iterations)
print("Complex Eigenvalues:", eigenvalues)
