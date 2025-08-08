import numpy as np


def qr_eigenvalues(A, num_iterations=10):
    n = A.shape[0]
    eigenvalues = np.zeros(n)

    for i in range(num_iterations):
        #Q, R = householder_qr(A)
        Q, R = np.linalg.qr(A)
        #A = np.dot(R, Q)#works
        A = np.matmul(R, Q)#works

    for i in range(n):
        eigenvalues[i] = A[i, i]

    return eigenvalues

def complex_qr_algorithm(A, num_iterations):
    #print("complex_qr_algorithm starts working")
    n = A.shape[0]
    for i in range(num_iterations):
        Q, R = np.linalg.qr(A)
        A = np.matmul(R, np.conjugate(Q).T)
    eigenvalues = np.diag(A)
    #print("complex_qr_algorithm finishes working")
    return eigenvalues

A = np.array([[1, 2], [3, 4]], dtype=complex)
num_iterations = 10

eigenvalues = qr_eigenvalues(A, num_iterations)
print("Complex Eigenvalues by QR algorythm:", eigenvalues)
eigenvalues = complex_qr_algorithm(A, num_iterations)
print("Complex Eigenvalues by Complex QR algorythm:", eigenvalues)
v, w=np.linalg.eig(A)
print("Complex Eigenvalues by inner fn:", v)
print("4x4, complex")
A = np.array([[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 0, -34], [41, 42, 43, -44]], dtype=complex)
num_iterations = 10
eigenvalues = qr_eigenvalues(A, num_iterations)
print("Complex Eigenvalues by QR algorythm:", eigenvalues)
eigenvalues = complex_qr_algorithm(A, num_iterations)
print("Complex Eigenvalues by Complex QR algorythm:", eigenvalues)
v, w=np.linalg.eig(A)
print("Complex Eigenvalues by inner fn:", v)
