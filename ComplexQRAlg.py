import numpy as np


def householder_qr(A):
    m, n = A.shape
    R = np.copy(A)
    #R=np.array(A, dtype=float)#disxcars imaginary part
    R=np.array(A, dtype=complex)#disxcars imaginary part
    #R=A*1.0
    Q = np.eye(m)
    Q=np.array(Q,dtype=complex) 
    for k in range(n):
        #x = R[k:, k]
        x = R[k:m, k]
        e = np.zeros_like(x)
        e[0] = np.sign(x[0])

        u = x + e * np.linalg.norm(x)
        u /= np.linalg.norm(u)#arr of not int
        print("u norm'd=",u)
        #u=np.array(u, dtype=complex)

        #R[k:, k:] -= 2.0 * np.outer(u, np.dot(u, R[k:, k:]))#TypeError: Cannot cast ufunc subtract output from dtype('float64') to dtype('int32') with casting rule 'same_kind'
        #R[k:m, k:n] -= 2.0 * np.outer(u, np.dot(u, R[k:m, k:n]))
        #R[k:, k:] -= 2.0 * np.dot(u.T, np.dot(u, R[k:, k:]))#same error
        u=np.dot(u, R[k:, k:])
        u=np.dot(u.T, u)
        R[k:, k:] -= 2.0 *u
        #
        #Q[k:]     -= 2.0 * np.outer(u, np.dot(u, Q[k:]))#Cannot cast ufunc subtract output from dtype('complex128') to dtype('float64') with casting rule 'same_kind'
        Q[k:m, :] -= 2.0 * np.outer(u, np.dot(u, Q[k:m, :]))

    return Q, R

def qr_eigenvalues(A, num_iterations=10):
    n = A.shape[0]
    eigenvalues = np.zeros(n)

    for i in range(num_iterations):
        Q, R = householder_qr(A)
        A = np.dot(R, Q)

    for i in range(n):
        eigenvalues[i] = A[i, i]# not complex discasrds complex

    return eigenvalues


A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
#
normA=np.linalg.norm(A)
print("norm A")
print(normA)
print("A[1:, 1:]:")
print(A[1:, 1:])
print("A[1:]:")
print(A[1:])
print("A[1:, 1]:")
C11=A[1:, 1]
print(A[1:, 1])
print(C11)
print("A")
print(A)
#AT=np.linalg.T#no
AT=A.T
print("AT")
print(AT)
Q, R = householder_qr(A)
eigenvalues = qr_eigenvalues(A)
print("BS Матрица Q:")
print(Q)
print("BS Матрица R:")
print(R)
print("bs) QR")
print(Q*R)




def complex_qr_algorithm(A, num_iterations):
    n = A.shape[0]
    for i in range(num_iterations):
        Q, R = np.linalg.qr(A)
        A = np.matmul(R, np.conjugate(Q).T)
    eigenvalues = np.diag(A)
    return eigenvalues

# Пример использования
A = np.array([[1, 2], [3, 4]], dtype=complex)
num_iterations = 10
print("A")
print(A)
eigenvalues = complex_qr_algorithm(A, num_iterations)
print("Комплексные собственные значения:", eigenvalues)


A = np.array([[1, 2], [3, 4]], dtype=complex)
num_iterations = 10
print("A")
print(A)
v,w=np.linalg.eig(A)
print("Комплексные собственные значения v:")
print(v)
print("Комплексные собственные векторы w:")
print(w)

A = np.array([[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 0,-34],[41, 42, 43, -44]], dtype=complex)
num_iterations = 10
print("A")
print(A)
eigenvalues = complex_qr_algorithm(A, num_iterations)
print('Комплексные собственные значения:', eigenvalues)
v,w=np.linalg.eig(A)
print("Комплексные собственные значения v:")
print(v)
print("Комплексные собственные векторы w:")
print(w)
Q, R = np.linalg.qr(A)
print("Матрица Q (st)")
print(Q)
print("Матрица R (st)")
print(R)
print("Q*R=")
print(np.dot(Q,R))
QR=householder_qr(A)
print("Матрица Q (mod)")
print(QR[1-1])
print("Матрица R (mod)")
print(QR[2-1])
print("Q*R=")
print(np.dot(QR[1-1],QR[2-1]))
print("or")
print(np.dot(QR[2-1],QR[1-1]))
Qh,Rh=householder_qr(A)
print("Матрица Q (mod1)")
print(Qh)
print("Матрица R (mod1)")
print(Rh)
print("Q*R=")
print(np.dot(Qh,Rh))
detA=np.linalg.det(A)
print("det A="+str(detA))
print("Q st - Q mod")
print(Q-QR[1-1])
print("R st - R mod")
print(R-QR[2-1])
