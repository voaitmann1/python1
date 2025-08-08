import copy

M1=[[11,12,13,14,15],
    [21,22,23,24,25],
    [31,32,33,34,35],
    [41,42,43,44,45],
    [51,52,53,54,55]
   ]

M3=[[11, 12, 13, 14, 15, 16],
    [21, 22, 23, 24, 25, 26],
    [22, 24, 26, 28, 30, 32],# 11-22
    [00, 00, 00, 00, 00, 00],
    [42, 44, 46, 48, 50, 52],#42 - 21
    [63, 66, 69, 72, 75, 78] #63 - 21
   ]

M2=[[61,12,13,14,15],
    [21,62,23,24,25],
    [31,32,63,34,35],
    [41,42,43,64,45],
    [51,52,53,54,65]
   ]

V1=[105, 195, 285, 375, 465]
V2=[305, 315, 345, 395, 455]
V3=[0, 0, 0, 0, 0]
V4=[0, 0, 0, 0, 1]

def EqualApprox_intR(x1, x2, eps=1E-6):
    R=0
    if(abs(x1-x2)<=eps):
        R=1
    return R

def EqualApprox_bool(x1, x2, eps=1E-6):
    return (abs(x1-x2)<=eps)

def NotEqualApprox_intR(x1, x2, eps=1E-6):
    R=1
    if(abs(x1-x2)<=eps):
        R=0
    return R

def NotEqualApprox_bool(x1, x2, eps=1E-6):
    return (abs(x1-x2)>eps)

def GreaterApprox_intR(x1, x2, eps=1E-6):
    R=0
    if((x1-x2)>eps):
        R=1
    return R

def GreaterApprox_bool(x1, x2, eps=1E-6):
    return((x1-x2)>eps)

def LessApprox_intR(x1, x2, eps=1E-6):
    R=0
    if((x2-x1)>eps):
        R=1
    return R

def LessApprox_bool(x1, x2, eps=1E-6):
    return((x2-x1)>eps)

def GreaterOrEqualApprox_intR(x1, x2, eps=1E-6):
    R=1
    if((x2-x1)>eps):
        R=0
    return R

def GreaterOrEqualsApprox_bool(x1, x2, eps=1E-6):
    return(not(x2-x1)>eps)

def LessOrEqualApprox_intR(x1, x2, eps=1E-6):
    R=1
    if((x1-x2)>eps):
        R=0
    return R

def LessOrEqualsApprox_bool(x1, x2, eps=1E-6):
    return(not(x1-x2)>eps)



def GaussTriangularTransform(Me):
    M=copy.deepcopy(Me)
    QL=len(M)
    QC=len(M[1-1])
    for i in range(1, QL+1):
        ci=-M[i-1][i-1]*1.0
        for j in range(i+1, QL+1):
            cj=M[j-1][i-1]*1.0
            for k in range(1, QC+1):
                M[j-1][k-1]=M[j-1][k-1]*ci*1.0+M[i-1][k-1]*cj*1.0
            if ci!=0:
                for k in range(1, QC+1):
                    M[j-1][k-1]/=ci*1.0
    return M

def AddCol(Q, V):
    L=len(Q)
    M=copy.deepcopy(Q)
    for i in range(1, L+1):
        M[i-1].append(V[i-1])
        
    return M



def ValIsInVectorUnderFirstN(Vec, val):
    N=0
    L=len(Vec)
    for i in range(1, L+1):
        if(Vec[i-1]==val and N==0):
            N=i;
            break;
    return N

def FirstNValsOfVectorAreZeros(V, N, eps=10e-6):
    R=0
    count=0
    for i in range(1, N+1):
        if V[i-1]==0:
            count+=1
    if count==N:
        R=1
    return R

def VectorConsistsOfZerosOnly(V, eps=10e-6):
    R=0
    L=len(V)
    count0=0
    for i in range(1, L+1):
        if EqualApprox_bool(V[i-1], 0, eps):
            count0+=1
    if count0==L:
        R=1
    return R

def VectorConsistsOfZerosOnlyExceptLast(V, eps=10e-6):
    R=0
    L=len(V)
    count0=0
    for i in range(1, L-1+1):
        if EqualApprox_bool(V[i-1], 0, eps):
            count0+=1
    if count0==L-1:
        R=1
    return R

def GaussSolutionTransform(Me):
    QL=len(Me)
    QC=len(Me[1-1])
    M=GaussTriangularTransform(Me)
    X=[]
    for i in range(1, QL+1):
        X.append(0)
    for i in range(1, QL+1):
        N=QL-i+1
        X[N-1]=M[N-1][QC-1]/M[N-1][N-1]*1.0
        for j in range (1, N-1+1):
            M[j-1][QC-1]-=M[j-1][N-1]*X[N-1]*1.0
            M[j-1][N-1]=0
    return M

def GaussSolution(Me):
    M1=copy.deepcopy(Me)
    M2=GaussTriangularTransform(M1)
    M3=GaussSolutionTransform(M2)
    QL=len(Me)
    QC=len(Me[1-1])
    X=[]
    for i in range(1, QL+1):
        X.append(M3[i-1][QC-1]/M3[i-1][i-1])
    return X

def CoefsOfVectors(V1, V2, eps=1e-6, vsh=1):
    if(vsh==1):
        print("CoefsOfVectors starts working")
        print("V1["+str(len(V1))+"]="+str(V1))
        print("V2["+str(len(V2))+"]="+str(V2))
    L=len(V1)
    count=0
    c=[]
    i=L-1
    if((V1[L-1-1]==0) or (V2[L-1-1]==0)):
        c1=0
        if(vsh==1):
            if V1[L-1-1]==0 and V2[L-1-1]!=0:
                print("c1=0 because V1["+str(L-1)+"="+str(V1[L-1-1]))
            elif V1[L-1-1]!=0 and V2[L-1-1]==0:
                print("c1=0 because V2["+str(L-1)+"="+str(V2[L-1-1]))
            elif V1[L-1-1]==0 and V2[L-1-1]==0:
                print("c1=0 because V1["+str(L-1)+"]="+str(V1[L-1-1])+" and V2["+str(L-1)+"]="+str(V2[L-1-1]))
    else:
        c1=1.0*V1[L-1-1]/V2[L-1-1]
        if(vsh==1):
            print("c1= V1["+str(L-1-1)+"]/V2["+str(L-1-1)+"]="+str(c1))
    for i in range(1, L+1):
        if i!=L-1:
            if((V1[i-1]==0) or (V2[i-1]==0)):
                c=0
                if(vsh==1):
                    if V1[i-1]==0 and V2[i-1]!=0:
                        print("c=0 because V1["+str(i)+"="+str(V1[i-1]))
                    elif V1[i-1]!=0 and V2[i-1]==0:
                        print("c=0 because V2["+str(i)+"="+str(V2[L-1-1]))
                    elif V1[i-1]==0 and V2[i-1]==0:
                        print("c=0 because V1["+str(L-1)+"]="+str(V1[-1])+" and V2["+str()+"]="+str(V2[-1]))
            else:
                c=1.0*V1[i-1]/V2[i-1]
                if(vsh==1):
                    print(str(i)+") c= V1["+str(i-1)+"]/V2["+str(i-1)+"]="+str(V1[i-1])+"/"+str(V2[i-1])+"]="+str(c))
            if(NotEqualApprox_bool(c1, c)==1):
                count+=1
                if(vsh==1):
                    print("count="+str(count))
    R=[c1, count]
    if(vsh==1):
        print("Answer: "+str(R))
        print("CoefsOfVectors finishes working")
    return [c1, count]
        
        
def LinearLines(M, eps=1e-6, vsh=1):
    if(vsh==1):
        print("LinearLines starts working")
        print("M="+str(M))
    QL=len(M)
    QC=len(M[1-1])
    R=[]
    R1=[]
    LinDepLinesNs=[]
    countAll=0
    for i in range(1, QL+1):
        if FirstNValsOfVectorAreZeros(M[i-1], QL)==1:
            LinDepLinesNs.append(i)
            countAll+=1
            if(vsh==1):
                print("Line "+str(i)+"consists of zeros: "+str(M[i-1])+" - "+str(countAll)+" linearly dependent line")
    for i in range(1, QL+1):
        if(vsh==1):
            print("Line "+str(i)+": "+str(M[i-1]))
        r1=[]
        r1.append(i)
        if FirstNValsOfVectorAreZeros(M[i-1], QL)==1:
            r1.append(QL-1)
            if(vsh==1):
                print("Line of zeros")
        elif ValIsInVectorUnderFirstN(LinDepLinesNs, i)>0:
            r1.append(QL-1)
            if(vsh==1):
                print("Line is already detected as linearly dependent")
        elif ValIsInVectorUnderFirstN(LinDepLinesNs, i)==0:
            countSingle=0
            for j in range(i+1, QL+1):
                if(vsh==1):
                    if(i==j):
                        print(str(i)+"="+str(j)+" - not considered")
                    if(ValIsInVectorUnderFirstN(LinDepLinesNs,j)>0):
                        print(str(j)+"th line is already noted as linearly dependent")
                if(i!=j and ValIsInVectorUnderFirstN(LinDepLinesNs,j)==0):
                    if(vsh==1):
                        print("  comparing to Line "+str(j)+": "+str(M[j-1]))
                    r2=[]
                    r2=CoefsOfVectors(M[i-1], M[j-1], eps)
                    if r2[2-1]==0:
                        countSingle+=1
                        countAll+=1
                        LinDepLinesNs.append(j)#
                    if(vsh==1):
                        if r2[2-1]!=0:
                            print("these are linearly independent lines")
                        else:
                            print("this is "+str(countAll)+" linearly dependent lin with k="+str(r2[1-1]))
                    
            r1.append(countSingle)
            if(vsh==1):
                print(" Line has "+str(countSingle)+" linearly dependent lines")
        if(vsh==1):
                print(" Matrix has "+str(countAll)+" linearly dependent lines")
        R.append(r1)
    R1.append(countAll)
    R1.append(R)
    R1.append(LinDepLinesNs)
    #R.append(CoefsOfVectors(V1, V2, eps))
    if(vsh==1):
        print("LinearLines finishes working")
    return R1
    
print("Solution by Gauss")
M03=AddCol(M2, V2)
X=GaussSolution(M03)
print(X)
cl=LinearLines(M3)
print(cl)
print(str(V3)+" zeros only? "+str(VectorConsistsOfZerosOnly(V3)))
print(str(V4)+" zeros only? "+str(VectorConsistsOfZerosOnly(V4)))
print(str(V4)+" alm all zeros? "+str(VectorConsistsOfZerosOnlyExceptLast(V4)))
      

            
            
        
        
        
    
