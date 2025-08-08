MaxInt=36650


def SubArray(X, N1=1, N2=0):
    Y=[]
    if isinstance(X, list) and len(X)>0:
        Q=len(X)
    if(Q>0):
        if N1<=1 or N1>Q:
            N1=1
        if N2<N1:
            N2=Q
        elif N2>Q:
            N2=Q
        for i in range(N1, N2+1):
            Y.append(X[i-1])
    return Y
            
