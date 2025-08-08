import math

def Householder(A):

    N=len(A)
    SX = [0.0] * N


    for I in range(1, N-1):
        for K in range(I, N):
            SX[K] = A[N][I] * A[N][K]
        
        for J in range(N-1, I, -1):
            SX[I] = SX[I] + A[J][I] * A[J][I]
        
        for K in range(I+1, N):
            for J in range(N-1, K, -1):
                SX[K] = SX[K] + A[J][I] * A[J][K]
            
            for J in range(K-1, I+1, -1):
                SX[K] = SX[K] + A[J][I] * A[K][J]
            
        ALPHA = math.sqrt(SX[I])
    
        if A[I+1][I] != 0:
            BETA = 1.0 / ALPHA
        
            for J in range(I+2, N):
                A[J][I] = A[J][I] * BETA
            
            SX[I] = A[I+1][I] * BETA + math.copysign(1.0, A[I+1][I])
            A[I+1][I] = ALPHA
            G = 1.0 / abs(SX[I])
            SX2 = 0.0
        
            for K in range(I+2, N):
                SX[K] = SX[K] * BETA * G + math.copysign(A[K][I+1], SX[I])
                SX2 = SX[K] * A[K][I] + SX2
            
            SX2 = G * SX2
        
            for K in range(I+2, N):
                A[K][K] = A[K][K] - 2 * A[K][I] * SX[K] + SX2 * A[K][I] ** 2
            
                for J in range(K+1, N):
                    A[J][K] = A[J][K] - A[J][I] * SX[K] - A[K][I] * SX[I] + SX2 * A[J][I] * A[K][I]
        else:
            if ALPHA != 0:
                BETA = 1.0 / ALPHA
            
                for J in range(I+2, N):
                    A[J][I] = A[J][I] * BETA
                
                SX[I] = -1.0
                A[I+1][I] = ALPHA
                G = 1.0
                SX2 = 0.0
            
                for K in range(I+2, N):
                    SX[K] = SX[K] * BETA * G + math.copysign(A[K][I+1], SX[I])
                    SX2 = SX[K] * A[K][I] + SX2
                
                SX2 = G * SX2
            
                for K in range(I+2, N):
                    A[K][K] = A[K][K] - 2 * A[K][I] * SX[K] + SX2 * A[K][I] ** 2
                
                    for J in range(K+1, N):
                        A[J][K] = A[J][K] - A[J][I] * SX[K] - A[K][I] * SX[I] + SX2 * A[J][I] * A[K][I]
            else:
                SX[I] = 1.0

    return A
