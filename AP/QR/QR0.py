import numpy as np

def householder_qr(A):
    m, n = A.shape
    R = np.copy(A)
    Q = np.eye(m)

    for k in range(n):
        x = R[k:, k]
        e = np.zeros_like(x)
        e[0] = np.sign(x[0])

        u = x + e * np.linalg.norm(x)
        u /= np.linalg.norm(u)

        R[k:, k:] -= 2.0 * np.outer(u, np.dot(u, R[k:, k:]))
        Q[k:] -= 2.0 * np.outer(u, np.dot(u, Q[k:]))

    return Q, R

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

Q, R = householder_qr(A)

print("Матрица Q:")
print(Q)
print("Матрица R:")
print(R)

