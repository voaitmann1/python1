import math

def copysign(x, y):
    return math.fabs(x) * (1 if y >= 0 else -1)

def householder_transform(A, i):
    m = len(A)
    n = len(A[0])
    
    x = [A[j][i] for j in range(i, m)]
    e = [1.0 if j == i else 0.0 for j in range(i, m)]
    sign_x = copysign(1.0, x[0])
    norm_x = math.sqrt(sum(val * val for val in x))
    v = [val + sign_x * norm_x for val in x]

    beta = 2.0 / sum(val * val for val in v)

    for j in range(i, n):
        dot_product = sum(v[k - i] * A[k][j] for k in range(i, m))
        for k in range(i, m):
            A[k][j] -= beta * v[k - i] * dot_product

    return A, v

def qr_decomposition(A):
    m = len(A)
    n = len(A[0])
    Q = [[0.0] * m for _ in range(m)]
    
    for i in range(n):
        A, v = householder_transform(A, i)
        for j in range(i, m):
            Q[j][i] = v[j - i]

    return Q, A

# Пример использования
A = [
    [12.0, -51.0, 4.0],
    [6.0, 167.0, -68.0],
    [-4.0, 24.0, -41.0]
]

Q, R = qr_decomposition(A)

print "Матрица Q:"
for row in Q:
    print row

print "\nМатрица R:"
for row in R:
    print row
