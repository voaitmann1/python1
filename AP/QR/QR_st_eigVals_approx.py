import numpy as np
import MyLinAlgLibEn

def qr_iteration_eigenvalues(A, num_iterations=50):
    n = A.shape[0]
    B = A.copy()

    for _ in range(num_iterations):
        Q, R = np.linalg.qr(B)
        B = np.dot(R, Q)

    eigenvalues = [B[i, i] for i in range(n)]
    return eigenvalues

#A = np.array([
#    [12.0, -51.0, 4.0],
#    [6.0, 167.0, -68.0],
#    [-4.0, 24.0, -41.0]
#])

A = np.array([
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
    [41, 42, 43, 44, 45],
    [51, 52, 53, 54, 55]
])

d=np.linalg.det(A)
print("det=",d)

eigenvalues = qr_iteration_eigenvalues(A)
print("approx eigenvals: ", eigenvalues)

v, w=np.linalg.eig(A)
print("erig vals std: ", v)

print("Errs of eig vals")
#errs=[]
for i in range(len(v)):
    err=MyLinAlgLibEn.EigenValErr(A, eigenvalues[i-1])
    print(str(i+1)+") eig.val="+str(eigenvalues[i-1])+" => err = "+str(err))
