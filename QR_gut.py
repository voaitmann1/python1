import numpy as np

A = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
])

Q, R = np.linalg.qr(A)


print("A:")
print(A)
print("Q:")
print(Q)
print("R:")
print(R)

def HouseHolderVector(M, N):
    v=[]
    
