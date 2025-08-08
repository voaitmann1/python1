import copy
import math
import numpy as np
#import MyLinAlgLibEn as myLinAlg
#from MyLinAlgLib import *
from MyLinAlgLibEn import *

SysToBuildBy_ExampleWithBeta1_SysWithVz2=1
EquationsoFindFrom_DiffDataSetsOfDiffControlParams1_OneDataSet2=1

T__N=1
T__name="T__data"
T__data=[1, 2, 3, 4, 5, 6, 7, 8, 9]
#Eqs of longitudial move
#general
dVx__N=2
dVx__name="dVx__data"
dVx__data=[11, 12, 13, 14, 15, 16, 17, 18, 19]
cVy__N=3
cVy__name="dVy__data"
cVy__data=[21, 22, 23, 24, 25, 26, 27, 28, 29]
dwz__N=4
dwz__name="dwz__data"
dwz__data=[31, 32, 33, 34, 35, 36, 37, 38, 39]
dW__N=5
dW__name="dW__data"
dW__data=[41, 42, 43, 44, 45, 46, 47, 48, 49]
dtheta__N=6
dtheta__name="dtheta__data"
dtheta__data=[51, 52, 53, 54, 55, 56, 57, 58, 59]
# case
dVx__N=2
dVx__name="dVx__data"
dVx__data=[11, 12, 13, 14, 15, 16, 17, 18, 19]
cVy__N=3
cVy__name="dVy__data"
cVy__data=[21, 22, 23, 24, 25, 26, 27, 28, 29]
dwz__N=4
dwz__name="dwz__data"
dwz__data=[31, 32, 33, 34, 35, 36, 37, 38, 39]
dW__N=5
dW__name="dW__data"
dW__data=[41, 42, 43, 44, 45, 46, 47, 48, 49]
dtheta__N=6
dtheta__name="dtheta__data"
dtheta__data=[51, 52, 53, 54, 55, 56, 57, 58, 59]
#Eqs of side move
#same data and:
dwx__N=7
dwx__name="dwx__data"
dwx__data=[61, 62, 63, 64, 65, 66, 67, 68, 69]
dwy__N=8
dwy__name="dwy__data"
dwy__data=[71, 72, 73, 74, 75, 76, 77, 78, 79]
#and also:
dVz__N=9
dVz__name="dVz__data"
dVz__data=[91, 92, 93, 94, 95, 96, 97, 98, 99]
dgamma__N=10
dgamma__name="dgamma__data"
dgamma__data=[101, 102, 103, 104, 105, 106, 107, 108, 109]
dbeta__N=11
dbeta__name="dbeta__data"
dbeta_data=[81, 82, 83, 84, 85, 86, 87, 88, 89]
#Concrtete incoming signals
#Eqs of longitudial move
delta_v__N=12
delta_v__name="delta_v__data"
delta_v__data=[111, 112, 113, 114, 115, 116, 117, 118, 119]
delta_fi_collPitch__N=13
delta_fi_collPitch__name="delta_fi_collPitch__data"
delta_fi_collPitch__data=[121, 122, 123, 124, 125, 126, 127, 128, 129]
delta_kci_engine__N=14
delta_kci_engine__name="delta_kci_engine__data"
delta_kci_engine__data=[131, 132, 133, 134, 135, 136, 137, 138, 139]
#Eqs of side move
delta_n__N=15
delta_n__name="delta_n__data"
delta_n__data=[141, 142, 143, 144, 145, 146, 147, 148, 149]
delta_k__N=16
delta_k__name="delta_k__data"
delta_k__data=[151, 152, 153, 154, 155, 156, 157, 158, 159]
delta_fi_TR__N=17
delta_fi_TR__name="delta_fi_TR__data"
delta_fi_TR__data=[161, 162, 163, 164, 165, 166, 167, 168, 169]
#
#pre-calc data
#
dataLength=len(T__data)
fi0=1
dt = T__data[2-1]-T__data[1-1]
dT = 1
CorrectSys_SideMove_Sys1Zb0 = 1
w_ctrl=0#t'y, et ja tic val s'ne not'd, nur ut mem, ze tic unit es
#
#
#Eqs of move
#Longitudial
#
# d/dt dVx =   X_Vx*dVx +   X_Vy*dVy +   X_wz*dwz +   X_W*dW +  Xtheta*dtheta +   X_delta_v*delta_v +  X_fi*dfi_collPitch
# d/dt dVy =   Y_Vx*dVx +   Y_Vy*dVy +   Y_wz*dwz +   Y_W*dW +                +   Y_delta_v*delta_v +  Y_fi*dfi_collPitch
# d/dt dwz =  Mz_Vx*dVx +  Mz_Vy*dVy +  Mz_wz*dwz +  Mz_W*dW +                +  Mz_delta_v*delta_v + Mz_fi*dfi_collPitch
# d/dt dW  = Myv_Vx*dVx + Myv_Vy*dVy + Myv_wz*dwz + Myv_W*dW +                + Myv_delta_v*delta_v + Mz_fi*dfi_collPitch + Myv_kc-engine*kci_engine
#
# d/dt dtheta = dwz
#
# Eqs of side move
#
# d/dt dVz =  Z_Vz*dVx +   Z_wx*dwx +   Z_wy*dwy +  Z_gamma_dgamma + Z_delta_k*delta_k + Z_delta_n*delta_n
#
# d/dt dgamma = dwx - tg(fi0)*dwy
#
# 1 vrn
# d/dt dwx = Mx_Vz*dVz +  Mx_wx*dwx +  Mx_wy*dwy +  Mx_delta_k*delta_k +  Mx_delta_n*dfi_TR
# d/dt dwy = My_Vz*dVz +  My_wx*dwx +  My_wy*dwy +  My_delta_k*delta_k +  My_delta_n*dfi_TR
#
# 2 vrn
# d/dt dwx = Mx_beta*dbeta +  Mx_wx*dwx +  Mx_wy*dwy +  Mx_delta_k*delta_k +  Mx_delta_n*dfi_TR
# d/dt dwy = My_beta*dbeta +  My_wx*dwx +  My_wy*dwy +  My_delta_k*delta_k +  My_delta_n*dfi_TR

def fSq(w, q, dt, vsh=0):#cmpx part of signal
    if vsh==1:
        print("Sq starts working")
        print("dt="+str(dt)+" w="+str(w))
    N=len(q)
    S=0
    s1=0
    S=-1*q[1-1]/w-(q[N-1]-q[N-1-1])/(w*w*dt)*math.sin(w*(N-1)*dt)
    for i in range (1, N-2+1):
        c=(-q[i-1]+2*q[i+1-1]-q[i+2-1])*math.sin(w*i*dt)
        s1-=c
    s1/=(w*w*dt)
    S+=s1
    Sq=S
    return Sq

def fCq(w, q, dt):#real part of signal
    N=len(q)
    S=0
    S=(q[N-1]-q[N-1-1])*math.cos(w*(N-1)*dt)+(q[1-1]-q[2-1])
    for i in range (1, N-2+1):
        c=(-q[i-1]+2*q[i+1-1]-q[i+2-1])*math.cos(w*i*dt)
        S+=c
    S/=(w*w*dt)
    Cq=S
    return Cq

def fRq(w, q, dt):#signal amplitude
    Sq=fSq(w, q, dt)
    Cq=fCq(w, q, dt)
    Rq=math.sqrt(Sq*Sq+Cq*Cq)
    return Rq

def ffiq(w, q, dt):#phase angle of signal
    fiq=math.asin(fSq(w, q, dt)/fRq(w, q, dt))
    return fiq



                
#same, uz adgo et abgo signals

def fSx(w, X, dt):
    return fSq(w, X, dt)

def fSy(w, Y, dt):
    return fSq(w, Y, dt)

def fCx(w, X, dt):
    return fCq(w, X, dt)

def fCy(w, Y, dt):
    return fCq(w, Y, dt)
                                                 
def fRx(w, X, dt):
    return fRq(w, X, dt)

def fRy(w, Y, dt):
    return fRq(w, Y, dt)

def ffix(w, X, dt):
    return ffiq(w, X, dt)

def ffiy(w, Y, dt):
    return ffiq(w, Y, dt)

def fA_y_to_x(w, X, Y, dt):
    return fRy(w, Y, dt)/fRx(w, X, dt)

def ffi_y_to_x(w, X, Y, dt):
    return ffiy(w, Y, dt) - ffix(w, X, dt)
#
#
#
#
#
# May be general function, but let it be globals
#
# Side move
#
# wx ( delta_k), fi_TR=0
#
#
w_ctrl=2
#
#
print("\nElaborating experimental data\n")
#
#============================================================
print("\nSide move\n")#
#============================================================
#
print("1) 2nd eq of side move")
#------------------------------------------------------------
#
print("Variant 2 - as in Example, not in Sys (of 2nd eq of side move - dwx)\n")
#
print("d/dt dwx = Mx_beta*dbeta + Mx_wx*dwx + Mx_wy*dwy + Mx_delta_k*delta_k + Mx_delta_n*dfi_TR\n")
#
print("part 1 of 2 (of 2nd eq of side move - dwx; Variant 2 - as in Example): delta k != 0, fi_TR = 0\n")
#
A_beta_to_delta_k = fA_y_to_x(w_ctrl, delta_k__data, dbeta_data, dt)
fi_beta_to_delta_k = ffi_y_to_x(w_ctrl, delta_k__data, dbeta_data, dt)
#
A_wx_to_delta_k = fA_y_to_x(w_ctrl, delta_k__data, dwx__data, dt)
fi_wx_to_delta_k = ffi_y_to_x(w_ctrl, delta_k__data, dwx__data, dt)
#
A_wy_to_delta_k = fA_y_to_x(w_ctrl, delta_k__data, dwy__data, dt)
fi_wy_to_delta_k = ffi_y_to_x(w_ctrl, delta_k__data, dwy__data, dt)
#
X2=[]
Y2=[]
#
for i in range(1, dataLength+1):
    #L2=[]
    #x21=A_beta_to_delta_k * math.sin(w_ctrl * T__data[i-1] + fi_wx_to_delta_k)
    #L2.append(x21)
    #x22=A_wx_to_delta_k * math.sin(w_ctrl * T__data[i-1] + fi_wx_to_delta_k)
    #L2.append(x22)
    #x23=A_wy_to_delta_k * math.sin(w_ctrl * T__data[i-1] + fi_wy_to_delta_k)
    #L2.append(x23)
    #x24=math.sin(w_ctrl * (i-1)* dt)
    #L2.append(x24)
    #X2.append(L2)
    #y2=w_ctrl * (A_wx_to_delta_k * math.sin(w_ctrl * (i-1)* dt + fi_wx_to_delta_k + math.pi/2))
    #Y2.append(y2)
    #
    L2=[]
    x21=A_beta_to_delta_k * math.sin(w_ctrl * (i-1)*dt + fi_beta_to_delta_k)
    L2.append(x21)
    x22=A_wx_to_delta_k * math.sin(w_ctrl * (i-1)*dt + fi_wx_to_delta_k)
    L2.append(x22)
    x23=A_wy_to_delta_k * math.sin(w_ctrl * (i-1)*dt + fi_wy_to_delta_k)
    L2.append(x23)
    x24=math.sin(w_ctrl * (i-1)* dt)
    L2.append(x24)
    X2.append(L2)
    y2=w_ctrl * (A_wx_to_delta_k * math.sin(w_ctrl * (i-1)* dt + fi_wx_to_delta_k + math.pi/2))
    Y2.append(y2)
#
print("X2=")
print(X2)
print("Y2="+str(Y2))
A2=multiply(transpose(X2), X2)
B2=multiply(transpose(X2), Y2)
#A2= multiply( transpose(X2), X2)
#B2= multiply( transpose(X2), Y2)
print("A_wx_to_delta_k="+str(A_wx_to_delta_k))
print("fi_wx_to_delta_k="+str(fi_wx_to_delta_k))
print("A_beta_to_delta_k="+str(A_beta_to_delta_k))
print("fi_beta_to_delta_k="+str(fi_beta_to_delta_k))
print("A_wy_to_delta_k="+str(A_wy_to_delta_k))
print("fi_wy_to_delta_k="+str(fi_wy_to_delta_k))
print("A2=")
print(A2)
print("B2="+str(B2))
howAnywaySeidel0NurIfDetET01AnywayMatrix2=0
MaxQIters=20
eps=1E-6
X0=VectorOfZeros(len(B2))
Mx=Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
X0=VectorOfOnes(len(B2))
Mx=Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str(multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str(LinEqErrVec(A2, B2, Mx))+" err="+str(LinEqErr(A2, B2, Mx)))
print("std solution: A2*Mx="+str(np.linalg.solve(A2, B2))+" B2="+str(B2))
#Mx_side_Vz_delta_k=Mx
#
C_wx_side_delta_k_Var2ExampleNotSys = Mx
#
C_wx_side_beta_delta_k_Var2ExampleNotSys = C_wx_side_delta_k_Var2ExampleNotSys[1-1]
C_wx_side_wx_delta_k_Var2ExampleNotSys = C_wx_side_delta_k_Var2ExampleNotSys[2-1]
C_wx_side_wy_delta_k_Var2ExampleNotSys = C_wx_side_delta_k_Var2ExampleNotSys[3-1]
C_wx_side_delta_k_delta_k_Var2ExampleNotSys = C_wx_side_delta_k_Var2ExampleNotSys[4-1]
#
print("\npart 2 of 2 (of 2nd eq of side move - dwx; Variant 2 - as in Example) :  k == 0, fi_TR != 0\n")
#
A_wx_to_fiTR  =  fA_y_to_x(w_ctrl, delta_fi_TR__data, dwx__data, dt)
fi_wx_to_fiTR = ffi_y_to_x(w_ctrl, delta_fi_TR__data, dwx__data, dt)
#
A_beta_to_fiTR  =  fA_y_to_x(w_ctrl, delta_fi_TR__data, dbeta_data, dt)
fi_beta_to_fiTR = ffi_y_to_x(w_ctrl, delta_fi_TR__data, dbeta_data, dt)
#
A_wy_to_fiTR  =  fA_y_to_x(w_ctrl, delta_fi_TR__data, dwy__data, dt)
fi_wy_to_fiTR = ffi_y_to_x(w_ctrl, delta_fi_TR__data, dwy__data, dt)
#
X2=[]
Y2=[]
#
for i in range(1, dataLength+1):
    #L2=[]
    #x21=A_beta_to_delta_k * math.sin(w_ctrl * T__data[i-1] + fi_wx_to_delta_k)
    #L2.append(x21)
    #x22=A_wx_to_delta_k * math.sin(w_ctrl * T__data[i-1] + fi_wx_to_delta_k)
    #L2.append(x22)
    #x23=A_wy_to_delta_k * math.sin(w_ctrl * T__data[i-1] + fi_wy_to_delta_k)
    #L2.append(x23)
    #x24=math.sin(w_ctrl * (i-1)* dt)
    #L2.append(x24)
    #X2.append(L2)
    #y2=w_ctrl * (A_wx_to_delta_k * math.sin(w_ctrl * (i-1)* dt + fi_wx_to_delta_k + math.pi/2))
    #Y2.append(y2)
    #
    L2=[]
    x21=A_beta_to_fiTR * math.sin(w_ctrl * (i-1)*dt + fi_beta_to_fiTR)
    L2.append(x21)
    x22=A_wx_to_fiTR * math.sin(w_ctrl * (i-1)*dt + fi_wx_to_fiTR)
    L2.append(x22)
    x23=A_wy_to_fiTR * math.sin(w_ctrl * (i-1)*dt + fi_wy_to_fiTR)
    L2.append(x23)
    x24=math.sin(w_ctrl * (i-1)* dt)
    L2.append(x24)
    X2.append(L2)
    y2=w_ctrl * (A_wx_to_fiTR * math.sin(w_ctrl * (i-1)* dt + fi_wx_to_fiTR + math.pi/2))
    Y2.append(y2)
#
print("X2=")
print(X2)
print("Y2="+str(Y2))
A2=multiply( transpose(X2), X2)
B2=multiply( transpose(X2), Y2)
print("A_wx_to_delta_k="+str(A_wx_to_delta_k))
print("fi_wx_to_delta_k="+str(fi_wx_to_delta_k))
print("A_beta_to_delta_k="+str(A_beta_to_delta_k))
print("fi_beta_to_delta_k="+str(fi_beta_to_delta_k))
print("A_wy_to_delta_k="+str(A_wy_to_delta_k))
print("fi_wy_to_delta_k="+str(fi_wy_to_delta_k))
print("A2=")
print(A2)
print("B2="+str(B2))
howAnywaySeidel0NurIfDetET01AnywayMatrix2=0
MaxQIters=20
eps=1E-6
X0=VectorOfZeros(len(B2))
Mx=Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
X0= VectorOfOnes(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
print("std solution: A2*Mx="+str(np.linalg.solve(A2, B2))+" B2="+str(B2))
#Mx_side_Vz_delta_fiTR=Mx
#
C_wx_side_fiTR_Var2ExampleNotSys=Mx#Mx above#= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
#
C_wx_side_beta_fiTR_Var2ExampleNotSys=C_wx_side_fiTR_Var2ExampleNotSys[1-1]
C_wx_side_wx_fiTR_Var2ExampleNotSys=C_wx_side_fiTR_Var2ExampleNotSys[2-1]
C_wx_side_wy_fiTR_Var2ExampleNotSys=C_wx_side_fiTR_Var2ExampleNotSys[3-1]
C_wx_side_fiTR_fiTR_Var2ExampleNotSys=C_wx_side_fiTR_Var2ExampleNotSys[4-1]
#
print("\naverage values:\n")
#
C_wx_side_beta_Var2ExampleNotSys = (C_wx_side_beta_delta_k_Var2ExampleNotSys + C_wx_side_beta_fiTR_Var2ExampleNotSys)/2
C_wx_side_wx_Var2ExampleNotSys = (C_wx_side_beta_delta_k_Var2ExampleNotSys + C_wx_side_wx_fiTR_Var2ExampleNotSys)/2
C_wx_side_wy_Var2ExampleNotSys = (C_wx_side_wy_delta_k_Var2ExampleNotSys + C_wx_side_wy_fiTR_Var2ExampleNotSys)/2
#C_wx_side_fiTR_fiTR_Var2ExampleNotSys = (C_wx_side_fiTR_fiTR_Var2ExampleNotSys + C_wx_side_fiTR_fiTR_Var2ExampleNotSys)/2
#
print("C_wx_side_beta=("+str(C_wx_side_beta_delta_k_Var2ExampleNotSys)+"+"+str(C_wx_side_beta_fiTR_Var2ExampleNotSys)+")/2="+str(C_wx_side_beta_Var2ExampleNotSys))
print("C_wx_side_wx=("+str(C_wx_side_beta_delta_k_Var2ExampleNotSys)+"+"+str(C_wx_side_wx_fiTR_Var2ExampleNotSys)+")/2="+str(C_wx_side_wx_Var2ExampleNotSys))
print("C_wx_side_wy=("+str(C_wx_side_wy_delta_k_Var2ExampleNotSys)+"+"+str(C_wx_side_wy_fiTR_Var2ExampleNotSys)+")/2="+str(C_wx_side_wy_Var2ExampleNotSys))
#print("C_wx_side_fiTR=("+str(C_wx_side_fiTR_fiTR_Var2ExampleNotSys)+"+"+str(C_wx_side_fiTR_fiTR_Var2ExampleNotSys)+")/2="+str(C_wx_side_fiTR_fiTR_Var2ExampleNotSys))
#
#
print("\nVariant 1 - as  in Sys, not in example (of 2nd eq of side move - dwx)\n")
#
print("d/dt dwx = Mx_Vz*dVz + Mx_wx*dwx + Mx_wy*dwy + Mx_delta_k*delta_k + Mx_delta_n*dfi_TR\n")
#
print("part 1 of 2 (of 2nd eq of side move - dwx): delta k != 0, fi_TR = 0\n")
#
A_wx_to_delta_k = fA_y_to_x(w_ctrl, delta_k__data, dwx__data, dt)
fi_wx_to_delta_k = ffi_y_to_x(w_ctrl, delta_k__data, dwx__data, dt)
#
A_Vz_to_delta_k = fA_y_to_x(w_ctrl, delta_k__data, dVz__data, dt)
fi_Vz_to_delta_k = ffi_y_to_x(w_ctrl, delta_k__data, dVz__data, dt)
#
A_wy_to_delta_k = fA_y_to_x(w_ctrl, delta_k__data, dwy__data, dt)
fi_wy_to_delta_k = ffi_y_to_x(w_ctrl, delta_k__data, dwy__data, dt)
#
#
X2=[]
Y2=[]
#
for i in range(1, dataLength+1):
    #L2=[]
    #x21=A_beta_to_delta_k * math.sin(w_ctrl * T__data[i-1] + fi_wx_to_delta_k)
    #L2.append(x21)
    #x22=A_wx_to_delta_k * math.sin(w_ctrl * T__data[i-1] + fi_wx_to_delta_k)
    #L2.append(x22)
    #x23=A_wy_to_delta_k * math.sin(w_ctrl * T__data[i-1] + fi_wy_to_delta_k)
    #L2.append(x23)
    #x24=math.sin(w_ctrl * (i-1)* dt)
    #L2.append(x24)
    #X2.append(L2)
    #y2=w_ctrl * (A_wx_to_delta_k * math.sin(w_ctrl * (i-1)* dt + fi_wx_to_delta_k + math.pi/2))
    #Y2.append(y2)
    #
    L2=[]
    x21=A_Vz_to_delta_k * math.sin(w_ctrl * (i-1)*dt + fi_Vz_to_delta_k)
    L2.append(x21)
    x22=A_wx_to_delta_k * math.sin(w_ctrl * (i-1)*dt + fi_wx_to_delta_k)
    L2.append(x22)
    x23=A_wy_to_delta_k * math.sin(w_ctrl * (i-1)*dt + fi_wy_to_delta_k)
    L2.append(x23)
    x24=math.sin(w_ctrl * (i-1)* dt)
    L2.append(x24)
    X2.append(L2)
    y2=w_ctrl * (A_wy_to_delta_k * math.sin(w_ctrl * (i-1)* dt + fi_wy_to_delta_k + math.pi/2))
    Y2.append(y2)
#
print("X2=")
print(X2)
print("Y2="+str(Y2))
A2= multiply( transpose(X2), X2)
B2= multiply( transpose(X2), Y2)
print("A_wx_to_delta_k="+str(A_wx_to_delta_k))
print("fi_wx_to_delta_k="+str(fi_wx_to_delta_k))
print("A_beta_to_delta_k="+str(A_beta_to_delta_k))
print("fi_beta_to_delta_k="+str(fi_beta_to_delta_k))
print("A_wy_to_delta_k="+str(A_wy_to_delta_k))
print("fi_wy_to_delta_k="+str(fi_wy_to_delta_k))
print("A2=")
print(A2)
print("B2="+str(B2))
howAnywaySeidel0NurIfDetET01AnywayMatrix2=0
MaxQIters=20
eps=1E-6
X0= VectorOfZeros(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
X0= VectorOfOnes(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
print("std solution: A2*Mx="+str(np.linalg.solve(A2, B2))+" B2="+str(B2))
#Mx_side_Vz_delta_k=Mx
#
C_wx_side_delta_k_Var1SysNotExample = Mx
C_wx_side_Vz_delta_k_Var1SysNotExample = C_wx_side_delta_k_Var1SysNotExample[1-1]
C_wx_side_wx_delta_k_Var1SysNotExample = C_wx_side_delta_k_Var1SysNotExample[2-1]
C_wx_side_wy_delta_k_Var1SysNotExample = C_wx_side_delta_k_Var1SysNotExample[3-1]
C_wx_side_delta_k_delta_k_Var1SysNotExample = C_wx_side_delta_k_Var1SysNotExample[4-1]
#
print("part 2 of 2 (2nd eq of sode move; Variant 1 - as  in Sys)")
#
A_wx_to_fiTR  =  fA_y_to_x(w_ctrl, delta_fi_TR__data, dwx__data, dt)
fi_wx_to_fiTR = ffi_y_to_x(w_ctrl, delta_fi_TR__data, dwx__data, dt)
#
A_Vz_to_fiTR  =  fA_y_to_x(w_ctrl, delta_fi_TR__data, dVz__data, dt)
fi_Vz_to_fiTR = ffi_y_to_x(w_ctrl, delta_fi_TR__data, dVz__data, dt)
#
A_wy_to_fiTR  =  fA_y_to_x(w_ctrl, delta_fi_TR__data, dwy__data, dt)
fi_wy_to_fiTR = ffi_y_to_x(w_ctrl, delta_fi_TR__data, dwy__data, dt)
#
X2=[]
Y2=[]
#
for i in range(1, dataLength+1):
    #L2=[]
    #x21=A_beta_to_delta_k * math.sin(w_ctrl * T__data[i-1] + fi_wx_to_delta_k)
    #L2.append(x21)
    #x22=A_wx_to_delta_k * math.sin(w_ctrl * T__data[i-1] + fi_wx_to_delta_k)
    #L2.append(x22)
    #x23=A_wy_to_delta_k * math.sin(w_ctrl * T__data[i-1] + fi_wy_to_delta_k)
    #L2.append(x23)
    #x24=math.sin(w_ctrl * (i-1)* dt)
    #L2.append(x24)
    #X2.append(L2)
    #y2=w_ctrl * (A_wx_to_delta_k * math.sin(w_ctrl * (i-1)* dt + fi_wx_to_delta_k + math.pi/2))
    #Y2.append(y2)
    #
    L2=[]
    x21=A_Vz_to_fiTR * math.sin(w_ctrl * (i-1)*dt + fi_Vz_to_fiTR)
    L2.append(x21)
    x22=A_wx_to_fiTR * math.sin(w_ctrl * (i-1)*dt + fi_wx_to_fiTR)
    L2.append(x22)
    x23=A_wy_to_fiTR * math.sin(w_ctrl * (i-1)*dt + fi_wy_to_fiTR)
    L2.append(x23)
    x24=math.sin(w_ctrl * (i-1)* dt)
    L2.append(x24)
    X2.append(L2)
    y2=w_ctrl * (A_wx_to_fiTR * math.sin(w_ctrl * (i-1)* dt + fi_wx_to_fiTR + math.pi/2))
    Y2.append(y2)
#
print("X2=")
print(X2)
print("Y2="+str(Y2))
A2= multiply( transpose(X2), X2)
B2= multiply( transpose(X2), Y2)
print("A_wx_to_delta_k="+str(A_wx_to_delta_k))
print("fi_wx_to_delta_k="+str(fi_wx_to_delta_k))
print("A_Vz_to_delta_k="+str(A_Vz_to_delta_k))
print("fi_Vz_to_delta_k="+str(fi_Vz_to_delta_k))
print("A_wy_to_delta_k="+str(A_wy_to_delta_k))
print("fi_wy_to_delta_k="+str(fi_wy_to_delta_k))
print("A2=")
print(A2)
print("B2="+str(B2))
howAnywaySeidel0NurIfDetET01AnywayMatrix2=0
MaxQIters=20
eps=1E-6
X0= VectorOfZeros(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
X0= VectorOfOnes(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
print("std solution: A2*Mx="+str(np.linalg.solve(A2, B2))+" B2="+str(B2))
#Mx_side_Vz_delta_fiTR=Mx
#
C_wx_side_fiTR_Var1SysNotExample=Mx#Mx above#= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
#
C_wx_side_Vz_fiTR_Var1SysNotExample=C_wx_side_fiTR_Var1SysNotExample[1-1]
C_wx_side_wx_fiTR_Var1SysNotExample=C_wx_side_fiTR_Var1SysNotExample[2-1]
C_wx_side_wy_fiTR_Var1SysNotExample=C_wx_side_fiTR_Var1SysNotExample[3-1]
C_wx_side_fiTR_fiTR_Var1SysNotExample=C_wx_side_fiTR_Var1SysNotExample[4-1]
#      
#
print("average values (2nd eq of sode move; Variant 1 - as  in Sys):")
#
C_wx_side_wx_Var1SysNotExample = (C_wx_side_wx_delta_k_Var1SysNotExample + C_wx_side_wx_fiTR_Var1SysNotExample)/2
C_wx_side_Vz_Var1SysNotExample = (C_wx_side_Vz_delta_k_Var1SysNotExample + C_wx_side_Vz_fiTR_Var1SysNotExample)/2
C_wx_side_wy_Var1SysNotExample = (C_wx_side_wy_delta_k_Var1SysNotExample + C_wx_side_wy_fiTR_Var1SysNotExample)/2
#C_wx_side_fiTR_fiTR_Var2ExampleNotSys = (C_wx_side_fiTR_fiTR_Var2ExampleNotSys + C_wx_side_fiTR_fiTR_Var2ExampleNotSys)/2
#
print("C_wx_side_beta=("+str(C_wx_side_Vz_delta_k_Var1SysNotExample)+"+"+str(C_wx_side_Vz_fiTR_Var1SysNotExample)+")/2="+str(C_wx_side_Vz_Var1SysNotExample))
print("C_wx_side_wx=("+str(C_wx_side_beta_delta_k_Var1SysNotExample)+"+"+str(C_wx_side_wx_fiTR_Var1SysNotExample)+")/2="+str(C_wx_side_wx_Var1SysNotExample))
print("C_wx_side_wy=("+str(C_wx_side_wy_delta_k_Var1SysNotExample)+"+"+str(C_wx_side_wy_fiTR_Var1SysNotExample)+")/2="+str(C_wx_side_wy_Var1SysNotExample))
#print("C_wx_side_fiTR=("+str(C_wx_side_fiTR_fiTR_Var2ExampleNotSys)+"+"+str(C_wx_side_fiTR_fiTR_Var2ExampleNotSys)+")/2="+str(C_wx_side_fiTR_fiTR_Var2ExampleNotSys))
#
#
#this is the end of 2nd equation and start of 3rd ------------------------------------------------------------------------------------------------------
#
print("2) 3rd eq of side move")
#-----------------------------------------------------
#
print("Variant 2 - as in Example, not in Sys (of 2nd eq of side move - dwx)")
#
print("d/dt dwy = Mx_beta*dbeta + Mx_wx*dwx + Mx_wy*dwy + Mx_delta_k*delta_k + Mx_delta_n*dfi_TR")
print("delta k != 0, fi_TR = 0 (of 3rd eq of side move - dwy)")
#
print("part 1 of 2 (of 3rd eq of side move - dwy)")
#
A_beta_to_delta_k = fA_y_to_x(w_ctrl, delta_k__data, dbeta_data, dt)
fi_beta_to_delta_k = ffi_y_to_x(w_ctrl, delta_k__data, dbeta_data, dt)
#
A_wx_to_delta_k = fA_y_to_x(w_ctrl, delta_k__data, dwx__data, dt)
fi_wx_to_delta_k = ffi_y_to_x(w_ctrl, delta_k__data, dwx__data, dt)
#
A_wy_to_delta_k = fA_y_to_x(w_ctrl, delta_k__data, dwy__data, dt)
fi_wy_to_delta_k = ffi_y_to_x(w_ctrl, delta_k__data, dwy__data, dt)
#
X2=[]
Y2=[]
#
for i in range(1, dataLength+1):
    #L2=[]
    #x21=A_beta_to_delta_k * math.sin(w_ctrl * T__data[i-1] + fi_wx_to_delta_k)
    #L2.append(x21)
    #x22=A_wx_to_delta_k * math.sin(w_ctrl * T__data[i-1] + fi_wx_to_delta_k)
    #L2.append(x22)
    #x23=A_wy_to_delta_k * math.sin(w_ctrl * T__data[i-1] + fi_wy_to_delta_k)
    #L2.append(x23)
    #x24=math.sin(w_ctrl * (i-1)* dt)
    #L2.append(x24)
    #X2.append(L2)
    #y2=w_ctrl * (A_wx_to_delta_k * math.sin(w_ctrl * (i-1)* dt + fi_wx_to_delta_k + math.pi/2))
    #Y2.append(y2)
    #
    L2=[]
    x21=A_beta_to_delta_k * math.sin(w_ctrl * (i-1)*dt + fi_beta_to_delta_k)
    L2.append(x21)
    x22=A_wx_to_delta_k * math.sin(w_ctrl * (i-1)*dt + fi_wx_to_delta_k)
    L2.append(x22)
    x23=A_wy_to_delta_k * math.sin(w_ctrl * (i-1)*dt + fi_wy_to_delta_k)
    L2.append(x23)
    x24=math.sin(w_ctrl * (i-1)* dt)
    L2.append(x24)
    X2.append(L2)
    y2=w_ctrl * (A_wy_to_delta_k * math.sin(w_ctrl * (i-1)* dt + fi_wy_to_delta_k + math.pi/2))
    Y2.append(y2)
#
print("X2=")
print(X2)
print("Y2="+str(Y2))
A2= multiply( transpose(X2), X2)
B2= multiply( transpose(X2), Y2)
print("A_wx_to_delta_k="+str(A_wx_to_delta_k))
print("fi_wx_to_delta_k="+str(fi_wx_to_delta_k))
print("A_beta_to_delta_k="+str(A_beta_to_delta_k))
print("fi_beta_to_delta_k="+str(fi_beta_to_delta_k))
print("A_wy_to_delta_k="+str(A_wy_to_delta_k))
print("fi_wy_to_delta_k="+str(fi_wy_to_delta_k))
print("A2=")
print(A2)
print("B2="+str(B2))
howAnywaySeidel0NurIfDetET01AnywayMatrix2=0
MaxQIters=20
eps=1E-6
X0= VectorOfZeros(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
X0= VectorOfOnes(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
print("std solution: A2*Mx="+str(np.linalg.solve(A2, B2))+" B2="+str(B2))
#Mx_side_Vz_delta_k=Mx
#
C_wy_side_delta_k_Var2ExampleNotSys = Mx
#
C_wy_side_beta_delta_k_Var2ExampleNotSys = C_wy_side_delta_k_Var2ExampleNotSys[1-1]
C_wy_side_wx_delta_k_Var2ExampleNotSys = C_wy_side_delta_k_Var2ExampleNotSys[2-1]
C_wy_side_wy_delta_k_Var2ExampleNotSys = C_wy_side_delta_k_Var2ExampleNotSys[3-1]
C_wy_side_delta_k_delta_k_Var2ExampleNotSys = C_wy_side_delta_k_Var2ExampleNotSys[4-1]
#
print("part 2 of 2 (of 3rd eq of side move - dwy)")
#
A_wx_to_fiTR  =  fA_y_to_x(w_ctrl, delta_fi_TR__data, dwx__data, dt)
fi_wx_to_fiTR = ffi_y_to_x(w_ctrl, delta_fi_TR__data, dwx__data, dt)
#
A_beta_to_fiTR  =  fA_y_to_x(w_ctrl, delta_fi_TR__data, dbeta_data, dt)
fi_beta_to_fiTR = ffi_y_to_x(w_ctrl, delta_fi_TR__data, dbeta_data, dt)
#
A_wy_to_fiTR  =  fA_y_to_x(w_ctrl, delta_fi_TR__data, dwy__data, dt)
fi_wy_to_fiTR = ffi_y_to_x(w_ctrl, delta_fi_TR__data, dwy__data, dt)
#
X2=[]
Y2=[]
#
for i in range(1, dataLength+1):
    #L2=[]
    #x21=A_beta_to_delta_k * math.sin(w_ctrl * T__data[i-1] + fi_wx_to_delta_k)
    #L2.append(x21)
    #x22=A_wx_to_delta_k * math.sin(w_ctrl * T__data[i-1] + fi_wx_to_delta_k)
    #L2.append(x22)
    #x23=A_wy_to_delta_k * math.sin(w_ctrl * T__data[i-1] + fi_wy_to_delta_k)
    #L2.append(x23)
    #x24=math.sin(w_ctrl * (i-1)* dt)
    #L2.append(x24)
    #X2.append(L2)
    #y2=w_ctrl * (A_wx_to_delta_k * math.sin(w_ctrl * (i-1)* dt + fi_wx_to_delta_k + math.pi/2))
    #Y2.append(y2)
    #
    L2=[]
    x21=A_beta_to_fiTR * math.sin(w_ctrl * (i-1)*dt + fi_beta_to_fiTR)
    L2.append(x21)
    x22=A_wx_to_fiTR * math.sin(w_ctrl * (i-1)*dt + fi_wx_to_fiTR)
    L2.append(x22)
    x23=A_wy_to_fiTR * math.sin(w_ctrl * (i-1)*dt + fi_wy_to_fiTR)
    L2.append(x23)
    x24=math.sin(w_ctrl * (i-1)* dt)
    L2.append(x24)
    X2.append(L2)
    y2=w_ctrl * (A_wy_to_fiTR * math.sin(w_ctrl * (i-1)* dt + fi_wy_to_fiTR + math.pi/2))
    Y2.append(y2)
#
print("X2=")
print(X2)
print("Y2="+str(Y2))
A2= multiply( transpose(X2), X2)
B2= multiply( transpose(X2), Y2)
print("A_wx_to_delta_k="+str(A_wx_to_delta_k))
print("fi_wx_to_delta_k="+str(fi_wx_to_delta_k))
print("A_beta_to_delta_k="+str(A_beta_to_delta_k))
print("fi_beta_to_delta_k="+str(fi_beta_to_delta_k))
print("A_wy_to_delta_k="+str(A_wy_to_delta_k))
print("fi_wy_to_delta_k="+str(fi_wy_to_delta_k))
print("A2=")
print(A2)
print("B2="+str(B2))
howAnywaySeidel0NurIfDetET01AnywayMatrix2=0
MaxQIters=20
eps=1E-6
X0= VectorOfZeros(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
X0= VectorOfOnes(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
print("std solution: A2*Mx="+str(np.linalg.solve(A2, B2))+" B2="+str(B2))
#Mx_side_Vz_delta_fiTR=Mx
#
C_wy_side_fiTR_Var2ExampleNotSys=Mx#Mx above#= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
#
C_wy_side_beta_fiTR_Var2ExampleNotSys=C_wy_side_fiTR_Var2ExampleNotSys[1-1]
C_wy_side_wx_fiTR_Var2ExampleNotSys=C_wy_side_fiTR_Var2ExampleNotSys[2-1]
C_wy_side_wy_fiTR_Var2ExampleNotSys=C_wy_side_fiTR_Var2ExampleNotSys[3-1]
C_wy_side_fiTR_fiTR_Var2ExampleNotSys=C_wy_side_fiTR_Var2ExampleNotSys[4-1]
#
print("average values:")
#
C_wx_side_beta_Var2ExampleNotSys = (C_wx_side_beta_delta_k_Var2ExampleNotSys + C_wx_side_beta_fiTR_Var2ExampleNotSys)/2
C_wx_side_wx_Var2ExampleNotSys = (C_wx_side_beta_delta_k_Var2ExampleNotSys + C_wx_side_wx_fiTR_Var2ExampleNotSys)/2
C_wx_side_wy_Var2ExampleNotSys = (C_wx_side_wy_delta_k_Var2ExampleNotSys + C_wx_side_wy_fiTR_Var2ExampleNotSys)/2
#C_wx_side_fiTR_fiTR_Var2ExampleNotSys = (C_wx_side_fiTR_fiTR_Var2ExampleNotSys + C_wx_side_fiTR_fiTR_Var2ExampleNotSys)/2
#
print("C_wx_side_beta=("+str(C_wx_side_beta_delta_k)+"+"+str(C_wx_side_beta_fiTR_Var2ExampleNotSys)+")/2="+str(C_wx_side_beta_Var2ExampleNotSys))
print("C_wx_side_wx=("+str(C_wx_side_beta_delta_k_Var2ExampleNotSys)+"+"+str(C_wx_side_wx_fiTR_Var2ExampleNotSys)+")/2="+str(C_wx_side_wx_Var2ExampleNotSys))
print("C_wx_side_wy=("+str(C_wx_side_wy_delta_k_Var2ExampleNotSys)+"+"+str(C_wx_side_wy_fiTR_Var2ExampleNotSys)+")/2="+str(C_wx_side_wy_Var2ExampleNotSys))
#print("C_wx_side_fiTR=("+str(C_wx_side_fiTR_fiTR_Var2ExampleNotSys)+"+"+str(C_wx_side_fiTR_fiTR_Var2ExampleNotSys)+")/2="+str(C_wx_side_fiTR_fiTR_Var2ExampleNotSys))
#
#
print("\nVariant 1 - as  in Sys, not in example (of 3rd eq of side move - dwy)\n")
#
print("d/dt dwy = Mx_Vz*dVz + Mx_wx*dwx + Mx_wy*dwy + Mx_delta_k*delta_k + Mx_delta_n*dfi_TR")
print("delta k != 0, fi_TR = 0")
#
print("part 1 of 2 (of 3rd eq of side move - dwy)")
#
A_Vz_to_delta_k = fA_y_to_x(w_ctrl, delta_k__data, dVz__data, dt)
fi_Vz_to_delta_k = ffi_y_to_x(w_ctrl, delta_k__data, dVz__data, dt)
#
A_wx_to_delta_k = fA_y_to_x(w_ctrl, delta_k__data, dwx__data, dt)
fi_wx_to_delta_k = ffi_y_to_x(w_ctrl, delta_k__data, dwx__data, dt)
#
A_wy_to_delta_k = fA_y_to_x(w_ctrl, delta_k__data, dwy__data, dt)
fi_wy_to_delta_k = ffi_y_to_x(w_ctrl, delta_k__data, dwy__data, dt)
#
#
X2=[]
Y2=[]
#
for i in range(1, dataLength+1):
    #L2=[]
    #x21=A_beta_to_delta_k * math.sin(w_ctrl * T__data[i-1] + fi_wx_to_delta_k)
    #L2.append(x21)
    #x22=A_wx_to_delta_k * math.sin(w_ctrl * T__data[i-1] + fi_wx_to_delta_k)
    #L2.append(x22)
    #x23=A_wy_to_delta_k * math.sin(w_ctrl * T__data[i-1] + fi_wy_to_delta_k)
    #L2.append(x23)
    #x24=math.sin(w_ctrl * (i-1)* dt)
    #L2.append(x24)
    #X2.append(L2)
    #y2=w_ctrl * (A_wx_to_delta_k * math.sin(w_ctrl * (i-1)* dt + fi_wx_to_delta_k + math.pi/2))
    #Y2.append(y2)
    #
    L2=[]
    x21=A_Vz_to_delta_k * math.sin(w_ctrl * (i-1)*dt + fi_Vz_to_delta_k)
    L2.append(x21)
    x22=A_wx_to_delta_k * math.sin(w_ctrl * (i-1)*dt + fi_wx_to_delta_k)
    L2.append(x22)
    x23=A_wy_to_delta_k * math.sin(w_ctrl * (i-1)*dt + fi_wy_to_delta_k)
    L2.append(x23)
    x24=math.sin(w_ctrl * (i-1)* dt)
    L2.append(x24)
    X2.append(L2)
    y2=w_ctrl * (A_wy_to_delta_k * math.sin(w_ctrl * (i-1)* dt + fi_wy_to_delta_k + math.pi/2))
    Y2.append(y2)
#
print("X2=")
print(X2)
print("Y2="+str(Y2))
A2= multiply( transpose(X2), X2)
B2= multiply( transpose(X2), Y2)
print("A_wx_to_delta_k="+str(A_wx_to_delta_k))
print("fi_wx_to_delta_k="+str(fi_wx_to_delta_k))
print("A_beta_to_delta_k="+str(A_beta_to_delta_k))
print("fi_beta_to_delta_k="+str(fi_beta_to_delta_k))
print("A_wy_to_delta_k="+str(A_wy_to_delta_k))
print("fi_wy_to_delta_k="+str(fi_wy_to_delta_k))
print("A2=")
print(A2)
print("B2="+str(B2))
howAnywaySeidel0NurIfDetET01AnywayMatrix2=0
MaxQIters=20
eps=1E-6
X0= VectorOfZeros(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
X0= VectorOfOnes(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
print("std solution: A2*Mx="+str(np.linalg.solve(A2, B2))+" B2="+str(B2))
#Mx_side_Vz_delta_k=Mx
#
C_wy_side_delta_k_Var1SysNotExample = Mx
C_wy_side_Vz_delta_k_Var1SysNotExample = C_wy_side_delta_k_Var1SysNotExample[1-1]
C_wy_side_wx_delta_k_Var1SysNotExample = C_wy_side_delta_k_Var1SysNotExample[2-1]
C_wy_side_wy_delta_k_Var1SysNotExample = C_wy_side_delta_k_Var1SysNotExample[3-1]
C_wy_side_delta_k_delta_k_Var1SysNotExample = C_wy_side_delta_k_Var1SysNotExample[4-1]
#
print("part 2 of 2 (of 3rd eq of side move - dwy)")
#
A_wy_to_fiTR  =  fA_y_to_x(w_ctrl, delta_fi_TR__data, dwy__data, dt)
fi_wy_to_fiTR = ffi_y_to_x(w_ctrl, delta_fi_TR__data, dwy__data, dt)
#
A_Vz_to_fiTR  =  fA_y_to_x(w_ctrl, delta_fi_TR__data, dVz_data, dt)
fi_Vz_to_fiTR = ffi_y_to_x(w_ctrl, delta_fi_TR__data, dVz_data, dt)
#
A_wx_to_fiTR  =  fA_y_to_x(w_ctrl, delta_fi_TR__data, dwx__data, dt)
fi_wx_to_fiTR = ffi_y_to_x(w_ctrl, delta_fi_TR__data, dwx__data, dt)
#
X2=[]
Y2=[]
#
for i in range(1, dataLength+1):
    #L2=[]
    #x21=A_beta_to_delta_k * math.sin(w_ctrl * T__data[i-1] + fi_wx_to_delta_k)
    #L2.append(x21)
    #x22=A_wx_to_delta_k * math.sin(w_ctrl * T__data[i-1] + fi_wx_to_delta_k)
    #L2.append(x22)
    #x23=A_wy_to_delta_k * math.sin(w_ctrl * T__data[i-1] + fi_wy_to_delta_k)
    #L2.append(x23)
    #x24=math.sin(w_ctrl * (i-1)* dt)
    #L2.append(x24)
    #X2.append(L2)
    #y2=w_ctrl * (A_wx_to_delta_k * math.sin(w_ctrl * (i-1)* dt + fi_wx_to_delta_k + math.pi/2))
    #Y2.append(y2)
    #
    L2=[]
    x21=A_Vz_to_fiTR * math.sin(w_ctrl * (i-1)*dt + fi_beta_to_fiTR)
    L2.append(x21)
    x22=A_wx_to_fiTR * math.sin(w_ctrl * (i-1)*dt + fi_wx_to_fiTR)
    L2.append(x22)
    x23=A_wy_to_fiTR * math.sin(w_ctrl * (i-1)*dt + fi_wy_to_fiTR)
    L2.append(x23)
    x24=math.sin(w_ctrl * (i-1)* dt)
    L2.append(x24)
    X2.append(L2)
    y2=w_ctrl * (A_wy_to_fiTR * math.sin(w_ctrl * (i-1)* dt + fi_wy_to_fiTR + math.pi/2))
    Y2.append(y2)
#
print("X2=")
print(X2)
print("Y2="+str(Y2))
A2= multiply( transpose(X2), X2)
B2= multiply( transpose(X2), Y2)
print("A_wx_to_delta_k="+str(A_wx_to_delta_k))
print("fi_wx_to_delta_k="+str(fi_wx_to_delta_k))
print("A_Vz_to_delta_k="+str(A_Vz_to_delta_k))
print("fi_Vz_to_delta_k="+str(fi_Vz_to_delta_k))
print("A_wy_to_delta_k="+str(A_wy_to_delta_k))
print("fi_wy_to_delta_k="+str(fi_wy_to_delta_k))
print("A2=")
print(A2)
print("B2="+str(B2))
howAnywaySeidel0NurIfDetET01AnywayMatrix2=0
MaxQIters=20
eps=1E-6
X0= VectorOfZeros(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
X0= VectorOfOnes(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
print("std solution: A2*Mx="+str(np.linalg.solve(A2, B2))+" B2="+str(B2))
#Mx_side_Vz_delta_fiTR=Mx
#
C_wx_side_fiTR_Var1SysNotExample=Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
#
C_wx_side_Vz_fiTR_Var1SysNotExample=C_Wx_side_fiTR[1-1]
C_wx_side_wx_fiTR_Var1SysNotExample=C_wx_side_fiTR[2-1]
C_wx_side_wy_fiTR_Var1SysNotExample=C_wy_side_fiTR[3-1]
C_wx_side_fiTR_fiTR_Var1SysNotExample=C_wy_side_fiTR[4-1]
#      
#
print("average values:")
#
C_wx_side_Vz_Var1SysNotExample = (C_wx_side_Vz_delta_k_Var1SysNotExample + C_wx_side_Vz_fiTR_Var1SysNotExample)/2
C_wx_side_wx_Var1SysNotExample = (C_wx_side_beta_delta_k_Var1SysNotExample + C_wx_side_wx_fiTR_Var1SysNotExample)/2
C_wx_side_wy_Var1SysNotExample = (C_wx_side_wy_delta_k_Var1SysNotExample + C_wx_side_wy_fiTR_Var1SysNotExample)/2
#C_wx_side_fiTR_fiTR_Var2ExampleNotSys = (C_wx_side_fiTR_fiTR_Var2ExampleNotSys + C_wx_side_fiTR_fiTR_Var2ExampleNotSys)/2
#
print("C_wx_side_beta=("+str(C_wx_side_Vz_delta_k_Var1SysNotExample)+"+"+str(C_wx_side_Vz_fiTR_Var1SysNotExample)+")/2="+str(C_wx_side_Vz_Var1SysNotExample))
print("C_wx_side_wx=("+str(C_wx_side_beta_delta_k_Var1SysNotExample)+"+"+str(C_wx_side_wx_fiTR_Var1SysNotExample)+")/2="+str(C_wx_side_wx_Var1SysNotExample))
print("C_wx_side_wy=("+str(C_wx_side_wy_delta_k_Var1SysNotExample)+"+"+str(C_wx_side_wy_fiTR_Var1SysNotExample)+")/2="+str(C_wx_side_wy_Var1SysNotExample))
#print("C_wx_side_fiTR=("+str(C_wx_side_fiTR_fiTR_Var2ExampleNotSys)+"+"+str(C_wx_side_fiTR_fiTR_Var2ExampleNotSys)+")/2="+str(C_wx_side_fiTR_fiTR_Var2ExampleNotSys))
#
#
#------------------------------------------------------
print("3) 1st eq of side move")
#------------------------------------------------------
#
print("d/dt dVz = Z_vz*dVz + Z_wx*dwx + Z_wy*dwy  + Z_gamma*dgamma + Z_delta_k*delta_k + Z_delta_n*delta_n")
print("delta k != 0, fi_TR = 0")
#
print("part 1 of 2 (1st eq of side move)")
#
A_Vz_to_fiTR  =  fA_y_to_x(w_ctrl, delta_fi_TR__data, dVz_data, dt)
fi_Vz_to_fiTR = ffi_y_to_x(w_ctrl, delta_fi_TR__data, dVz_data, dt)
#
A_wx_to_delta_k = fA_y_to_x(w_ctrl, delta_k__data, dwx__data, dt)
fi_wx_to_delta_k = ffi_y_to_x(w_ctrl, delta_k__data, dwx__data, dt)
#
A_wy_to_delta_k = fA_y_to_x(w_ctrl, delta_k__data, dwy__data, dt)
fi_wy_to_delta_k = ffi_y_to_x(w_ctrl, delta_k__data, dwy__data, dt)
#
A_gamma_to_delta_k = fA_y_to_x(w_ctrl, delta_k__data, dgamma__data, dt)
fi_gamma_to_delta_k = ffi_y_to_x(w_ctrl, delta_k__data, dgamma__data, dt)
#
X2=[]
Y2=[]
#
for i in range(1, dataLength+1):
    #L2=[]
    L2=[]
    x21=A_Vz_to_delta_k * math.sin(w_ctrl * (i-1)*dt + fi_beta_to_delta_k)
    L2.append(x21)
    x22=A_wx_to_delta_k * math.sin(w_ctrl * (i-1)*dt + fi_wx_to_delta_k)
    L2.append(x22)
    x23=A_wy_to_delta_k * math.sin(w_ctrl * (i-1)*dt + fi_wy_to_delta_k)
    L2.append(x23)
    x24=A_gamma_to_delta_k * math.sin(w_ctrl * (i-1)*dt + fi_gamma_to_delta_k)
    L2.append(x24)
    x25=math.sin(w_ctrl * (i-1)* dt)
    L2.append(x25)
    X2.append(L2)
    y2=w_ctrl * (A_wx_to_delta_k * math.sin(w_ctrl * (i-1)* dt + fi_wx_to_delta_k + math.pi/2))
    Y2.append(y2)   
#
print("X2=")
print(X2)
print("Y2="+str(Y2))
A2= multiply( transpose(X2), X2)
B2= multiply( transpose(X2), Y2)
print("A_Vz_to_delta_k="+str(A_Vz_to_delta_k))
print("fi_Vz_to_delta_k="+str(fi_Vz_to_delta_k))
print("A_wx_to_delta_k="+str(A_wx_to_delta_k))
print("fi_wx_to_delta_k="+str(fi_wx_to_delta_k))
print("A_wy_to_delta_k="+str(A_wy_to_delta_k))
print("fi_wy_to_delta_k="+str(fi_wy_to_delta_k))
print("A_gamma_to_delta_k="+str(A_gamma_to_delta_k))
print("fi_gamma_to_delta_k="+str(fi_gamma_to_delta_k))
print("A2=")
print(A2)
print("B2="+str(B2))
howAnywaySeidel0NurIfDetET01AnywayMatrix2=0
MaxQIters=20
eps=1E-6
X0= VectorOfZeros(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
X0= VectorOfOnes(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
print("std solution: A2*Mx="+str(np.linalg.solve(A2, B2))+" B2="+str(B2))
#Mx_side_Vz_delta_fiTR=Mx
#
C_Vz_side_delta_k_=Mx#Mx above#= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
#
C_Vz_side_Vz_delta_k_=C_Vz_side_delta_k_[1-1]
C_Vz_side_wx_delta_k_=C_Vz_side_delta_k_[2-1]
C_Vz_side_wy_delta_k_=C_Vz_side_delta_k_[3-1]
C_Vz_side_gamma_delta_k_=C_Vz_side_delta_k_[4-1]
C_Vz_side_delta_k_delta_k_=C_Vz_side_delta_k_[5-1]
#
#
print("part 2 of 2 (1st eq dVz of side move)")
#
A_wx_to_fiTR  =  fA_y_to_x(w_ctrl, delta_fi_TR__data, dwx__data, dt)
fi_wx_to_fiTR = ffi_y_to_x(w_ctrl, delta_fi_TR__data, dwx__data, dt)
#
A_Vz_to_fiTR  =  fA_y_to_x(w_ctrl, delta_fi_TR__data, dVz_data, dt)
fi_Vz_to_fiTR = ffi_y_to_x(w_ctrl, delta_fi_TR__data, dVz_data, dt)
#
A_wy_to_fiTR  =  fA_y_to_x(w_ctrl, delta_fi_TR__data, dwy__data, dt)
fi_wy_to_fiTR = ffi_y_to_x(w_ctrl, delta_fi_TR__data, dwy__data, dt)
#
A_gamma_to_fiTR  =  fA_y_to_x(w_ctrl, delta_fi_TR__data, dgamma__data, dt)
fi_gamma_to_fiTR = ffi_y_to_x(w_ctrl, delta_fi_TR__data, dgamma__data, dt)
#
X2=[]
Y2=[]
#
for i in range(1, dataLength+1):
    #L2=[]
    L2=[]
    x21=A_Vz_to_fiTR * math.sin(w_ctrl * (i-1)*dt + fi_Vz_to_fiTR)
    L2.append(x21)
    x22=A_wx_to_fiTR * math.sin(w_ctrl * (i-1)*dt + fi_wx_to_fiTR)
    L2.append(x22)
    x23=A_wy_to_fiTR * math.sin(w_ctrl * (i-1)*dt + fi_wy_to_fiTR)
    L2.append(x23)
    x24=A_gamma_to_fiTR * math.sin(w_ctrl * (i-1)*dt + fi_gamma_to_fiTR)
    L2.append(x24)
    x25=math.sin(w_ctrl * (i-1)* dt)
    L2.append(x25)
    X2.append(L2)
    y2=w_ctrl * (A_wx_to_fiTR * math.sin(w_ctrl * (i-1)* dt + fi_wx_to_fiTR + math.pi/2))
    Y2.append(y2)  
#
print("X2=")
print(X2)
print("Y2="+str(Y2))
A2= multiply( transpose(X2), X2)
B2= multiply( transpose(X2), Y2)
print("A_Vz_to_fiTR="+str(A_Vz_to_fiTR))
print("fi_Vz_to_fiTR="+str(fi_Vz_to_fiTR))
print("A_wx_to_fiTR="+str(A_wx_to_fiTR))
print("fi_wx_to_fiTR="+str(fi_wx_to_fiTR))
print("A_wy_to_fiTR="+str(A_wy_to_fiTR))
print("fi_wy_to_fiTR="+str(fi_wy_to_fiTR))
print("A_gamma_to_fiTR="+str(A_Vz_to_fiTR))
print("fi_gamma_to_fiTR="+str(fi_Vz_to_fiTR))
print("A2=")
print(A2)
print("B2="+str(B2))
howAnywaySeidel0NurIfDetET01AnywayMatrix2=0
MaxQIters=20
eps=1E-6
X0= VectorOfZeros(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
X0= VectorOfOnes(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
print("std solution: A2*Mx="+str(np.linalg.solve(A2, B2))+" B2="+str(B2))
#Mx_side_Vz_delta_fiTR=Mx
#
C_Vz_side_fiTR_=Mx#Mx above#= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
#
C_Vz_side_Vz_fiTR_=C_Vz_side_fiTR[1-1]
C_Vz_side_wx_fiTR_=C_Vz_side_fiTR[2-1]
C_Vz_side_wy_fiTR_=C_Vz_side_fiTR[3-1]
C_Vz_side_gamma_fiTR_=C_Vz_side_fiTR[4-1]
#      
#
print("average values:")
#
C_Vz_side_Vz_ = (C_Vz_side_Vz_delta_k_ + C_Vz_side_Vz_fiTR_)/2
C_Vz_side_wx_ = (C_Vz_side_beta_delta_k_ + C_Vz_side_wx_fiTR_)/2
C_Vz_side_wy_ = (C_Vz_side_wy_delta_k_ + C_Vz_side_wy_fiTR_)/2
C_Vz_side_gamma_ = (C_Vz_side_gamma_delta_k_ + C_Vz_side_gamma_fiTR_)/2
#
#
#Equation 4 of side move - nothing to calculate
#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#========================================================
print("\n\n Longitudinal move \n")
#========================================================
#
#Eqa Vx
print("1st equation of longitudinal move")
#----------------------------------------------
print("dVx/dt = XVx*dVx + XVy*dVy + Xwz*dwz + XW*dW + Xth*dtheta + X_delta_v*delta_v + Xfi*delta_fiMR")
#
print("part 1 of 2 (1st eq longit)")
#
A_Vx_to_delta_v  =  fA_y_to_x(w_ctrl, delta_v__data, dVx__data, dt)
fi_Vx_to_delta_v = ffi_y_to_x(w_ctrl, delta_v__data, dVx__data, dt)
#
A_Vy_to_delta_v  =  fA_y_to_x(w_ctrl, delta_v__data, dVy__data, dt)
fi_Vy_to_delta_v = ffi_y_to_x(w_ctrl, delta_v__data, dVy__data, dt)
#
A_wz_to_delta_v  =  fA_y_to_x(w_ctrl, delta_v__data, dwz__data, dt)
fi_wz_to_delta_v = ffi_y_to_x(w_ctrl, delta_v__data, dwz__data, dt)
#
A_W_to_delta_v  =  fA_y_to_x(w_ctrl, delta_v__data, dW__data, dt) #W = Omega
fi_W_to_delta_v = ffi_y_to_x(w_ctrl, delta_v__data, dW__data, dt)
#
A_dtheta_to_delta_v  =  fA_y_to_x(w_ctrl, delta_v__data, dtheta__data, dt)
fi_dtheta_to_delta_v = ffi_y_to_x(w_ctrl, delta_v__data, dtheta__data, dt)
#
#
X2=[]
Y2=[]
#
for i in range(1, dataLength+1):
    #
    L2=[]
    x21=A_Vx_to_delta_v * math.sin(w_ctrl * (i-1)*dt + fi_Vx_to_delta_v)
    L2.append(x21)
    x21=A_Vy_to_delta_v * math.sin(w_ctrl * (i-1)*dt + fi_Vy_to_delta_v)
    L2.append(x22)
    x23=A_wz_to_delta_v * math.sin(w_ctrl * (i-1)*dt + fi_wz_to_delta_v)
    L2.append(x23)
    x24=A_W_to_delta_v * math.sin(w_ctrl * (i-1)*dt + fi_W_to_delta_v)
    L2.append(x24)
    x25=A_theta_to_delta_v * math.sin(w_ctrl * (i-1)*dt + fi_theta_to_delta_v)
    L2.append(x25)
    x26=math.sin(w_ctrl * (i-1)* dt)
    L2.append(x26)
    X2.append(L2)
    y2=w_ctrl * (A_Vx_to_delta_v * math.sin(w_ctrl * (i-1)* dt + fi_Vx_to_delta_v + math.pi/2))
    Y2.append(y2)
#
print("X2=")
print(X2)
print("Y2="+str(Y2))
A2= multiply( transpose(X2), X2)
B2= multiply( transpose(X2), Y2)
print("A_Vx_to_delta_v="+str(A_Vx_to_delta_v))
print("fi_Vx_to_delta_v="+str(fi_Vx_to_delta_v))
print("A_Vy_to_delta_v="+str(A_Vy_to_delta_v))
print("fi_Vy_to_delta_v="+str(fi_Vy_to_delta_v))
print("A_wz_to_delta_v="+str(A_wz_to_delta_v))
print("fi_wz_to_delta_v="+str(fi_wz_to_delta_v))
print("A_W_to_delta_v="+str(A_W_to_delta_v))
print("fi_W_to_delta_v="+str(fi_W_to_delta_v))
print("A_theta_to_delta_v="+str(A_theta_to_delta_v))
print("fi_theta_to_delta_v="+str(fi_theta_to_delta_v))
print("A2=")
print(A2)
print("B2="+str(B2))
#
howAnywaySeidel0NurIfDetET01AnywayMatrix2=0
MaxQIters=20
eps=1E-6
X0= VectorOfZeros(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
X0= VectorOfOnes(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
print("std solution: A2*Mx="+str(np.linalg.solve(A2, B2))+" B2="+str(B2))
#Mx_side_Vz_delta_k=Mx
#
C_Vx_longit_delta_v_ = Mx
#
C_Vx_longit_Vx_delta_v = C_Vx_longit_delta_v_[1-1]
C_Vx_longit_Vy_delta_v = C_Vx_longit_delta_v_[2-1]
C_Vx_longit_wz_delta_v = C_Vx_longit_delta_v_[3-1]
C_Vx_longit_W_delta_v = C_Vx_longit_delta_v_[4-1]
C_Vx_longit_theta_delta_v = C_Vx_longit_delta_v_[5-1]
C_Vx_longit_delta_v_delta_v = C_Vx_longit_delta_v_[6-1]
#
print("part 2 of 2 (Eq 1 dVx longit)")#from_here!
#
A_Vx_to_delta_fiMR  =  fA_y_to_x(w_ctrl, delta_fiMR__data, dVx__data, dt)
fi_Vx_to_delta_fiMR = ffi_y_to_x(w_ctrl, deltafiMR___data, dVx__data, dt)
#
A_Vy_to_delta_fiMR  =  fA_y_to_x(w_ctrl, delta_fiMR__data, dVy__data, dt)
fi_Vy_to_delta_fiMR = ffi_y_to_x(w_ctrl, delta_fiMR__data, dVy__data, dt)
#
A_wz_to_delta_fiMR  =  fA_y_to_x(w_ctrl, deltafiMR___data, dwz__data, dt)
fi_wz_to_delta_fiMR = ffi_y_to_x(w_ctrl, delta_fiMR__data, dwz__data, dt)
#
A_W_to_delta_fiMR  =  fA_y_to_x(w_ctrl, delta_fiMR__data, dW__data, dt) #W = Omega
fi_W_to_delta_fiMR = ffi_y_to_x(w_ctrl, delta_fiMR__data, dW__data, dt)
#
A_dtheta_to_delta_fiMR  =  fA_y_to_x(w_ctrl, delta_fiMR__data, dtheta__data, dt)
fi_dtheta_to_delta_fiMR = ffi_y_to_x(w_ctrl, delta_fiMR__data, dtheta__data, dt)
#
#
X2=[]
Y2=[]
#
for i in range(1, dataLength+1):
    #
    L2=[]
    x21=A_Vx_to_delta_fiMR * math.sin(w_ctrl * (i-1)*dt + fi_Vx_to_delta_fiMR)
    L2.append(x21)
    x21=A_Vy_to_delta_fiMR * math.sin(w_ctrl * (i-1)*dt + fi_Vy_to_delta_fiMR)
    L2.append(x22)
    x23=A_wz_to_delta_fiMR * math.sin(w_ctrl * (i-1)*dt + fi_wz_to_delta_fiMR)
    L2.append(x23)
    x24=A_W_to_delta_fiMR * math.sin(w_ctrl * (i-1)*dt + fi_W_to_delta_fiMR)
    L2.append(x24)
    x25=A_theta_to_delta_fiMR * math.sin(w_ctrl * (i-1)*dt + fi_theta_to_delta_fiMR)
    L2.append(x25)
    x26=math.sin(w_ctrl * (i-1)* dt)
    L2.append(x26)
    X2.append(L2)
    y2=w_ctrl * (A_Vx_to_delta_fiMR * math.sin(w_ctrl * (i-1)* dt + fi_Vx_to_delta_fiMR + math.pi/2))
    Y2.append(y2)
#
print("X2=")
print(X2)
print("Y2="+str(Y2))
A2= multiply( transpose(X2), X2)
B2= multiply( transpose(X2), Y2)
print("A_Vx_to_delta_fiMR="+str(A_Vx_to_delta_fiMR))
print("fi_Vx_to_delta_fiMR="+str(fi_Vx_to_delta_fiMR))
print("A_Vy_to_delta_fiMR="+str(A_Vy_to_delta_fiMR))
print("fi_Vy_to_delta_fiMR="+str(fi_Vy_to_delta_fiMR))
print("A_wz_to_delta_fiMR="+str(A_wz_to_delta_fiMR))
print("fi_wz_to_delta_fiMR="+str(fi_wz_to_delta_fiMR))
print("A_W_to_delta_fiMR="+str(A_W_to_delta_fiMR))
print("fi_W_to_delta_fiMR="+str(fi_W_to_delta_fiMR))
print("A_theta_to_delta_fiMR="+str(A_theta_to_delta_fiMR))
print("fi_theta_to_delta_fiMR="+str(fi_theta_to_delta_fiMR))
print("A2=")
print(A2)
print("B2="+str(B2))
#
howAnywaySeidel0NurIfDetET01AnywayMatrix2=0
MaxQIters=20
eps=1E-6
X0= VectorOfZeros(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
X0= VectorOfOnes(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
print("std solution: A2*Mx="+str(np.linalg.solve(A2, B2))+" B2="+str(B2))
#Mx_side_Vz_delta_k=Mx
#
C_Vx_longit_delta_fiMR_ = Mx
#
C_Vx_longit_Vx_delta_fiMR = C_Vx_longit_delta_fiMR_[1-1]
C_Vx_longit_Vy_delta_fiMR = C_Vx_longit_delta_fiMR_[2-1]
C_Vx_longit_wz_delta_fiMR = C_Vx_longit_delta_fiMR_[3-1]
C_Vx_longit_W_delta_fiMR = C_Vx_longit_delta_fiMR_[4-1]
C_Vx_longit_theta_delta_fiMR = C_Vx_longit_delta_fiMR_[5-1]
C_Vx_longit_delta_v_delta_fiMR_ = C_Vx_longit_delta_fiMR_[6-1]
#
print("average values: (1st eq dVx longit)")
#
C_Vx_longit_Vx_ = (C_Vx_longit_Vx_delta_v + C_Vx_longit_Vx_delta_fiMR)/2
C_Vx_longit_Vy_ = (C_Vx_longit_Vy_delta_v + C_Vx_longit_Vy_delta_fiMR)/2
C_Vx_longit_wz_ = (C_Vx_longit_wz_delta_v + C_Vx_longit_wz_delta_fiMR)/2
C_Vx_longit_W_ = (C_Vx_longit_W_delta_v + C_Vx_longit_W_delta_fiMR)/2
C_Vx_longit_theta_ = (C_Vx_longit_theta_delta_v + C_Vx_longit_theta_delta_fiMR)/2
#
print("C_Vx_longit_Vx="+str(C_Vx_longit_Vx_))
print("C_Vx_longit_Vy="+str(C_Vx_longit_Vy_))
print("C_Vx_longit_wz="+str(C_Vx_longit_wz_))
print("C_Vx_longit_W="+str(C_Vx_longit_W_))
print("C_Vx_longit_theta="+str(C_Vx_longit_theta_))
#
#
print(" 2nd eq of longitudinal move - Vy")
#-------------------------------------------------------------
print("dVy/dt = XVx*dVx + XVy*dVy + Xwz*dwz + XW*dW + Xth*dtheta + X_delta_v*delta_v + Xfi*delta_fiMR")
#
print("part 1 of 2 (2nd eq dVy longit)")
#
A_Vx_to_delta_v  =  fA_y_to_x(w_ctrl, delta_v__data, dVx__data, dt)
fi_Vx_to_delta_v = ffi_y_to_x(w_ctrl, delta_v__data, dVx__data, dt)
#
A_Vy_to_delta_v  =  fA_y_to_x(w_ctrl, delta_v__data, dVy__data, dt)
fi_Vy_to_delta_v = ffi_y_to_x(w_ctrl, delta_v__data, dVy__data, dt)
#
A_wz_to_delta_v  =  fA_y_to_x(w_ctrl, delta_v__data, dwz__data, dt)
fi_wz_to_delta_v = ffi_y_to_x(w_ctrl, delta_v__data, dwz__data, dt)
#
A_W_to_delta_v  =  fA_y_to_x(w_ctrl, delta_v__data, dW__data, dt) #W = Omega
fi_W_to_delta_v = ffi_y_to_x(w_ctrl, delta_v__data, dW__data, dt)
#
A_dtheta_to_delta_v  =  fA_y_to_x(w_ctrl, delta_v__data, dtheta__data, dt)
fi_dtheta_to_delta_v = ffi_y_to_x(w_ctrl, delta_v__data, dtheta__data, dt)
#
#
X2=[]
Y2=[]
#
for i in range(1, dataLength+1):
    #
    L2=[]
    x21=A_Vx_to_delta_v * math.sin(w_ctrl * (i-1)*dt + fi_Vx_to_delta_v)
    L2.append(x21)
    x21=A_Vy_to_delta_v * math.sin(w_ctrl * (i-1)*dt + fi_Vy_to_delta_v)
    L2.append(x22)
    x23=A_wz_to_delta_v * math.sin(w_ctrl * (i-1)*dt + fi_wz_to_delta_v)
    L2.append(x23)
    x24=A_W_to_delta_v * math.sin(w_ctrl * (i-1)*dt + fi_W_to_delta_v)
    L2.append(x24)
    x25=A_theta_to_delta_v * math.sin(w_ctrl * (i-1)*dt + fi_theta_to_delta_v)
    L2.append(x25)
    x26=math.sin(w_ctrl * (i-1)* dt)
    L2.append(x26)
    X2.append(L2)
    y2=w_ctrl * (A_Vy_to_delta_v * math.sin(w_ctrl * (i-1)* dt + fi_Vy_to_delta_v + math.pi/2))
    Y2.append(y2)
#
print("X2=")
print(X2)
print("Y2="+str(Y2))
A2= multiply( transpose(X2), X2)
B2= multiply( transpose(X2), Y2)
print("A_Vx_to_delta_v="+str(A_Vx_to_delta_v))
print("fi_Vx_to_delta_v="+str(fi_Vx_to_delta_v))
print("A_Vy_to_delta_v="+str(A_Vy_to_delta_v))
print("fi_Vy_to_delta_v="+str(fi_Vy_to_delta_v))
print("A_wz_to_delta_v="+str(A_wz_to_delta_v))
print("fi_wz_to_delta_v="+str(fi_wz_to_delta_v))
print("A_W_to_delta_v="+str(A_W_to_delta_v))
print("fi_W_to_delta_v="+str(fi_W_to_delta_v))
print("A_theta_to_delta_v="+str(A_theta_to_delta_v))
print("fi_theta_to_delta_v="+str(fi_theta_to_delta_v))
print("A2=")
print(A2)
print("B2="+str(B2))
#
howAnywaySeidel0NurIfDetET01AnywayMatrix2=0
MaxQIters=20
eps=1E-6
X0= VectorOfZeros(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
X0= VectorOfOnes(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
print("std solution: A2*Mx="+str(np.linalg.solve(A2, B2))+" B2="+str(B2))
#Mx_side_Vz_delta_k=Mx
#
C_Vy_longit_delta_v_ = Mx
#
C_Vy_longit_Vx_delta_v = C_Vy_longit_delta_v_[1-1]
C_Vy_longit_Vy_delta_v = C_Vy_longit_delta_v_[2-1]
C_Vy_longit_wz_delta_v = C_Vy_longit_delta_v_[3-1]
C_Vy_longit_W_delta_v = C_Vy_longit_delta_v_[4-1]
C_Vy_longit_theta_delta_v = C_Vy_longit_delta_v_[5-1]
C_Vy_longit_delta_v_delta_v = C_Vy_longit_delta_v_[6-1]
#
print("part 2 of 2 (2nd eq dVy longit)")
#
A_Vx_to_delta_fiMR  =  fA_y_to_x(w_ctrl, delta_fiMR__data, dVx__data, dt)
fi_Vx_to_delta_fiMR = ffi_y_to_x(w_ctrl, delta_fiMR__data, dVx__data, dt)
#
A_Vy_to_delta_fiMR  =  fA_y_to_x(w_ctrl, delta_fiMR__data, dVy__data, dt)
fi_Vy_to_delta_fiMR = ffi_y_to_x(w_ctrl, delta_fiMR__data, dVy__data, dt)
#
A_wz_to_delta_fiMR  =  fA_y_to_x(w_ctrl, delta_fiMR__data, dwz__data, dt)
fi_wz_to_delta_fiMR = ffi_y_to_x(w_ctrl, delta_fiMR__data, dwz__data, dt)
#
A_W_to_delta_fiMR  =  fA_y_to_x(w_ctrl, delta_fiMR__data, dW__data, dt) #W = Omega
fi_W_to_delta_fiMR = ffi_y_to_x(w_ctrl, delta_fiMR__data, dW__data, dt)
#
A_dtheta_to_delta_fiMR  =  fA_y_to_x(w_ctrl, delta_fiMR__data, dtheta__data, dt)
fi_dtheta_to_delta_fiMR = ffi_y_to_x(w_ctrl, delta_fiMR__data, dtheta__data, dt)
#
#
X2=[]
Y2=[]
#
for i in range(1, dataLength+1):
    #
    L2=[]
    x21=A_Vx_to_delta_fiMR * math.sin(w_ctrl * (i-1)*dt + fi_Vx_to_delta_fiMR)
    L2.append(x21)
    x21=A_Vy_to_delta_fiMR * math.sin(w_ctrl * (i-1)*dt + fi_Vy_to_delta_fiMR)
    L2.append(x22)
    x23=A_wz_to_delta_fiMR * math.sin(w_ctrl * (i-1)*dt + fi_wz_to_delta_fiMR)
    L2.append(x23)
    x24=A_W_to_delta_fiMR * math.sin(w_ctrl * (i-1)*dt + fi_W_to_delta_fiMR)
    L2.append(x24)
    x25=A_theta_to_delta_fiMR * math.sin(w_ctrl * (i-1)*dt + fi_theta_to_delta_fiMR)
    L2.append(x25)
    x26=math.sin(w_ctrl * (i-1)* dt)
    L2.append(x26)
    X2.append(L2)
    y2=w_ctrl * (A_Vy_to_delta_fiMR * math.sin(w_ctrl * (i-1)* dt + fi_Vy_to_delta_fiMR + math.pi/2))
    Y2.append(y2)
#
print("X2=")
print(X2)
print("Y2="+str(Y2))
A2= multiply( transpose(X2), X2)
B2= multiply( transpose(X2), Y2)
print("A_Vx_to_delta_fiMR="+str(A_Vx_to_delta_fiMR))
print("fi_Vx_to_delta_fiMR="+str(fi_Vx_to_delta_fiMR))
print("A_Vy_to_delta_fiMR="+str(A_Vy_to_delta_fiMR))
print("fi_Vy_to_delta_fiMR="+str(fi_Vy_to_delta_fiMR))
print("A_wz_to_delta_fiMR="+str(A_wz_to_delta_fiMR))
print("fi_wz_to_delta_fiMR="+str(fi_wz_to_delta_fiMR))
print("A_W_to_delta_fiMR="+str(A_W_to_delta_fiMR))
print("fi_W_to_delta_fiMR="+str(fi_W_to_delta_fiMR))
print("A_theta_to_delta_fiMR="+str(A_theta_to_delta_fiMR))
print("fi_theta_to_delta_fiMR="+str(fi_theta_to_delta_fiMR))
print("A2=")
print(A2)
print("B2="+str(B2))
#
howAnywaySeidel0NurIfDetET01AnywayMatrix2=0
MaxQIters=20
eps=1E-6
X0= VectorOfZeros(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
X0= VectorOfOnes(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
print("std solution: A2*Mx="+str(np.linalg.solve(A2, B2))+" B2="+str(B2))
#Mx_side_Vz_delta_k=Mx
#
C_Vy_longit_delta_fiMR_ = Mx
#
C_Vy_longit_Vx_delta_fiMR = C_Vy_longit_delta_fiMR_[1-1]
C_Vy_longit_Vy_delta_fiMR = C_Vy_longit_delta_fiMR_[2-1]
C_Vy_longit_wz_delta_fiMR = C_Vy_longit_delta_fiMR_[3-1]
C_Vy_longit_W_delta_fiMR = C_Vy_longit_delta_fiMR_[4-1]
C_Vy_longit_theta_delta_fiMR = C_Vy_longit_delta_fiMR_[5-1]
C_Vy_longit_delta_fiMR_delta_fiMR = C_Vy_longit_delta_fiMR_[6-1]
#
print("average values: (2nd eq dVy longit)")
#
C_Vy_longit_Vx_ = (C_Vy_longit_Vx_delta_v + C_Vy_longit_Vx_delta_fiMR)/2
C_Vy_longit_Vy_ = (C_Vy_longit_Vy_delta_v + C_Vy_longit_Vy_delta_fiMR)/2
C_Vy_longit_wz_ = (C_Vy_longit_wz_delta_v + C_Vy_longit_wz_delta_fiMR)/2
C_Vy_longit_W_ = (C_Vy_longit_W_delta_v + C_Vy_longit_W_delta_fiMR)/2
C_Vy_longit_theta_ = (C_Vy_longit_theta_delta_v + C_Vy_longit_theta_delta_fiMR)/2
#
print("C_Vy_longit_Vx="+str(C_Vy_longit_Vx_))
print("C_Vy_longit_Vy="+str(C_Vy_longit_Vy_))
print("C_Vy_longit_wz="+str(C_Vy_longit_wz_))
print("C_Vy_longit_W="+str(C_Vy_longit_W_))
print("C_Vy_longit_theta="+str(C_Vy_longit_theta_))
#
#
#
#
print(" 3rd eq of longitudinal move - Vy")
#-----------------------------------------------------------------------------------------------
print("dwz/dt = MzVx*dVx + MzVy*dVy + MzWz*dwz + MzW*dW + X_delta_v*delta_v + Xfi*delta_fiMR")
#-----------------------------------------------------------------------------------------------
print("part 1 of 2 (3rd eq dwz longit)")
#
A_Vx_to_delta_v  =  fA_y_to_x(w_ctrl, delta_v__data, dVx__data, dt)
fi_Vx_to_delta_v = ffi_y_to_x(w_ctrl, delta_v__data, dVx__data, dt)
#
A_Vy_to_delta_v  =  fA_y_to_x(w_ctrl, delta_v__data, dVy__data, dt)
fi_Vy_to_delta_v = ffi_y_to_x(w_ctrl, delta_v__data, dVy__data, dt)
#
A_wz_to_delta_v  =  fA_y_to_x(w_ctrl, delta_v__data, dwz__data, dt)
fi_wz_to_delta_v = ffi_y_to_x(w_ctrl, delta_v__data, dwz__data, dt)
#
A_W_to_delta_v  =  fA_y_to_x(w_ctrl, delta_v__data, dW__data, dt) #W = Omega
fi_W_to_delta_v = ffi_y_to_x(w_ctrl, delta_v__data, dW__data, dt)
#
A_dtheta_to_delta_v  =  fA_y_to_x(w_ctrl, delta_v__data, dtheta__data, dt)
fi_dtheta_to_delta_v = ffi_y_to_x(w_ctrl, delta_v__data, dtheta__data, dt)
#
#
X2=[]
Y2=[]
#
for i in range(1, dataLength+1):
    #
    L2=[]
    x21=A_Vx_to_delta_v * math.sin(w_ctrl * (i-1)*dt + fi_Vx_to_delta_v)
    L2.append(x21)
    x21=A_Vy_to_delta_v * math.sin(w_ctrl * (i-1)*dt + fi_Vy_to_delta_v)
    L2.append(x22)
    x23=A_wz_to_delta_v * math.sin(w_ctrl * (i-1)*dt + fi_wz_to_delta_v)
    L2.append(x23)
    x24=A_W_to_delta_v * math.sin(w_ctrl * (i-1)*dt + fi_W_to_delta_v)
    L2.append(x24)
    x25=math.sin(w_ctrl * (i-1)* dt)
    L2.append(x25)
    X2.append(L2)
    y2=w_ctrl * (A_wz_to_delta_v * math.sin(w_ctrl * (i-1)* dt + fi_wz_to_delta_v + math.pi/2))
    Y2.append(y2)
#
print("X2=")
print(X2)
print("Y2="+str(Y2))
A2= multiply( transpose(X2), X2)
B2= multiply( transpose(X2), Y2)
print("A_Vx_to_delta_v="+str(A_Vx_to_delta_v))
print("fi_Vx_to_delta_v="+str(fi_Vx_to_delta_v))
print("A_Vy_to_delta_v="+str(A_Vy_to_delta_v))
print("fi_Vy_to_delta_v="+str(fi_Vy_to_delta_v))
print("A_wz_to_delta_v="+str(A_wz_to_delta_v))
print("fi_wz_to_delta_v="+str(fi_wz_to_delta_v))
print("A_W_to_delta_v="+str(A_W_to_delta_v))
print("fi_W_to_delta_v="+str(fi_W_to_delta_v))
print("A_theta_to_delta_v="+str(A_theta_to_delta_v))
print("fi_theta_to_delta_v="+str(fi_theta_to_delta_v))
print("A2=")
print(A2)
print("B2="+str(B2))
#
howAnywaySeidel0NurIfDetET01AnywayMatrix2=0
MaxQIters=20
eps=1E-6
X0= VectorOfZeros(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
X0= VectorOfOnes(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
print("std solution: A2*Mx="+str(np.linalg.solve(A2, B2))+" B2="+str(B2))
#Mx_side_Vz_delta_k=Mx
#
C_wz_longit_delta_v_ = Mx
#
C_wz_longit_Vx_delta_v = C_wz_longit_delta_v_[1-1]
C_wz_longit_Vy_delta_v = C_wz_longit_delta_v_[2-1]
C_wz_longit_wz_delta_v = C_wz_longit_delta_v_[3-1]
C_wz_longit_W_delta_v = C_wz_longit_delta_v_[4-1]
C_wz_longit_delta_v_delta_v = C_wz_longit_delta_v_[5-1]
#
print("part 2 of 2 (3rd eq dwz longit)")
#
A_Vx_to_delta_fiMR  =  fA_y_to_x(w_ctrl, delta_fiMR__data, dVx__data, dt)
fi_Vx_to_delta_fiMR = ffi_y_to_x(w_ctrl, delta_fiMR__data, dVx__data, dt)
#
A_Vy_to_delta_fiMR  =  fA_y_to_x(w_ctrl, delta_fiMR__data, dVy__data, dt)
fi_Vy_to_delta_fiMR = ffi_y_to_x(w_ctrl, delta_fiMR__data, dVy__data, dt)
#
A_wz_to_delta_fiMR  =  fA_y_to_x(w_ctrl, delta_fiMR__data, dwz__data, dt)
fi_wz_to_delta_fiMR = ffi_y_to_x(w_ctrl, delta_fiMR__data, dwz__data, dt)
#
A_W_to_delta_fiMR  =  fA_y_to_x(w_ctrl, delta_fiMR__data, dW__data, dt) #W = Omega
fi_W_to_delta_fiMR = ffi_y_to_x(w_ctrl, delta_fiMR__data, dW__data, dt)
#
#A_dtheta_to_delta_fiMR  =  fA_y_to_x(w_ctrl, delta_fiMR__data, dtheta__data, dt)
#fi_dtheta_to_delta_fiMR = ffi_y_to_x(w_ctrl, delta_fiMR__data, dtheta__data, dt)
#
#
X2=[]
Y2=[]
#
for i in range(1, dataLength+1):
    #
    L2=[]
    x21=A_Vx_to_delta_fiMR * math.sin(w_ctrl * (i-1)*dt + fi_Vx_to_delta_fiMR)
    L2.append(x21)
    x21=A_Vy_to_delta_fiMR * math.sin(w_ctrl * (i-1)*dt + fi_Vy_to_delta_fiMR)
    L2.append(x22)
    x23=A_wz_to_delta_fiMR * math.sin(w_ctrl * (i-1)*dt + fi_wz_to_delta_fiMR)
    L2.append(x23)
    x24=A_W_to_delta_fiMR * math.sin(w_ctrl * (i-1)*dt + fi_W_to_delta_fiMR)
    L2.append(x24)
    x25=math.sin(w_ctrl * (i-1)* dt)
    L2.append(x25)
    X2.append(L2)
    y2=w_ctrl * (A_wz_to_delta_fiMR * math.sin(w_ctrl * (i-1)* dt + fi_wz_to_delta_fiMR + math.pi/2))
    Y2.append(y2)
#
print("X2=")
print(X2)
print("Y2="+str(Y2))
A2= multiply( transpose(X2), X2)
B2= multiply( transpose(X2), Y2)
print("A_Vx_to_delta_fiMR="+str(A_Vx_to_delta_fiMR))
print("fi_Vx_to_delta_fiMR="+str(fi_Vx_to_delta_fiMR))
print("A_Vy_to_delta_fiMR="+str(A_Vy_to_delta_fiMR))
print("fi_Vy_to_delta_fiMR="+str(fi_Vy_to_delta_fiMR))
print("A_wz_to_delta_fiMR="+str(A_wz_to_delta_fiMR))
print("fi_wz_to_delta_fiMR="+str(fi_wz_to_delta_fiMR))
print("A_W_to_delta_fiMR="+str(A_W_to_delta_fiMR))
print("fi_W_to_delta_fiMR="+str(fi_W_to_delta_fiMR))
print("A_theta_to_delta_fiMR="+str(A_theta_to_delta_fiMR))
print("fi_theta_to_delta_fiMR="+str(fi_theta_to_delta_fiMR))
print("A2=")
print(A2)
print("B2="+str(B2))
#
howAnywaySeidel0NurIfDetET01AnywayMatrix2=0
MaxQIters=20
eps=1E-6
X0= VectorOfZeros(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
X0= VectorOfOnes(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
print("std solution: A2*Mx="+str(np.linalg.solve(A2, B2))+" B2="+str(B2))
#Mx_side_Vz_delta_k=Mx
#
C_wz_longit_delta_fiMR_ = Mx
#
C_wz_longit_Vx_delta_fiMR = C_wz_longit_delta_fiMR_[1-1]
C_wz_longit_Vy_delta_fiMR = C_wz_longit_delta_fiMR_[2-1]
C_wz_longit_wz_delta_fiMR = C_wz_longit_delta_fiMR_[3-1]
C_wz_longit_W_delta_fiMR = C_wz_longit_delta_fiMR_[4-1]
C_wz_longit_theta_delta_fiMR = C_wz_longit_delta_fiMR_[5-1]
C_wz_longit_delta_fiMR_delta_fiMR = C_wz_longit_delta_fiMR_[6-1]
#
print("average values: (3rd eq dwz longit)")
#
C_wz_longit_Vx_ = (C_wz_longit_Vx_delta_v + C_wz_longit_Vx_delta_fiMR)/2
C_wz_longit_Vy_ = (C_wz_longit_Vy_delta_v + C_wz_longit_Vy_delta_fiMR)/2
C_wz_longit_wz_ = (C_wz_longit_wz_delta_v + C_wz_longit_wz_delta_fiMR)/2
C_wz_longit_W_ = (C_wz_longit_W_delta_v + C_wz_longit_W_delta_fiMR)/2
C_wz_longit_theta_ = (C_wz_longit_theta_delta_v + C_wz_longit_theta_delta_fiMR)/2
#
print("C_wz_longit_Vx="+str(C_wz_longit_Vx_))
print("C_wz_longit_Vy="+str(C_wz_longit_Vy_))
print("C_wz_longit_wz="+str(C_wz_longit_wz_))
print("C_wz_longit_W="+str(C_wz_longit_W_))
#
#
#
#
print(" 4th eq dW of longitudinal move")
#-------------------------------------------------------------
print("dW/dt = MyaVx*dVx + XVy*dVy + Xwz*dwz + XW*dW + X_delta_v*delta_v + Xfi*delta_fiMR")
#-------------------------------------------------------------
print("part 1 of 2 (4th eq dW of longitudinal move)")
#
A_Vx_to_delta_v  =  fA_y_to_x(w_ctrl, delta_v__data, dVx__data, dt)
fi_Vx_to_delta_v = ffi_y_to_x(w_ctrl, delta_v__data, dVx__data, dt)
#
A_Vy_to_delta_v  =  fA_y_to_x(w_ctrl, delta_v__data, dVy__data, dt)
fi_Vy_to_delta_v = ffi_y_to_x(w_ctrl, delta_v__data, dVy__data, dt)
#
A_wz_to_delta_v  =  fA_y_to_x(w_ctrl, delta_v__data, dwz__data, dt)
fi_wz_to_delta_v = ffi_y_to_x(w_ctrl, delta_v__data, dwz__data, dt)
#
A_W_to_delta_v  =  fA_y_to_x(w_ctrl, delta_v__data, dW__data, dt) #W = Omega
fi_W_to_delta_v = ffi_y_to_x(w_ctrl, delta_v__data, dW__data, dt)
#
A_dtheta_to_delta_v  =  fA_y_to_x(w_ctrl, delta_v__data, dtheta__data, dt)
fi_dtheta_to_delta_v = ffi_y_to_x(w_ctrl, delta_v__data, dtheta__data, dt)
#
#
X2=[]
Y2=[]
#
for i in range(1, dataLength+1):
    #
    L2=[]
    x21=A_Vx_to_delta_v * math.sin(w_ctrl * (i-1)*dt + fi_Vx_to_delta_v)
    L2.append(x21)
    x21=A_Vy_to_delta_v * math.sin(w_ctrl * (i-1)*dt + fi_Vy_to_delta_v)
    L2.append(x22)
    x23=A_wz_to_delta_v * math.sin(w_ctrl * (i-1)*dt + fi_wz_to_delta_v)
    L2.append(x23)
    x24=A_W_to_delta_v * math.sin(w_ctrl * (i-1)*dt + fi_W_to_delta_v)
    L2.append(x24)
    x25=math.sin(w_ctrl * (i-1)* dt)
    L2.append(x25)
    X2.append(L2)
    y2=w_ctrl * (A_wz_to_delta_v * math.sin(w_ctrl * (i-1)* dt + fi_wz_to_delta_v + math.pi/2))
    Y2.append(y2)
#
print("X2=")
print(X2)
print("Y2="+str(Y2))
A2= multiply( transpose(X2), X2)
B2= multiply( transpose(X2), Y2)
print("A_Vx_to_delta_v="+str(A_Vx_to_delta_v))
print("fi_Vx_to_delta_v="+str(fi_Vx_to_delta_v))
print("A_Vy_to_delta_v="+str(A_Vy_to_delta_v))
print("fi_Vy_to_delta_v="+str(fi_Vy_to_delta_v))
print("A_wz_to_delta_v="+str(A_wz_to_delta_v))
print("fi_wz_to_delta_v="+str(fi_wz_to_delta_v))
print("A_W_to_delta_v="+str(A_W_to_delta_v))
print("fi_W_to_delta_v="+str(fi_W_to_delta_v))
print("A_theta_to_delta_v="+str(A_theta_to_delta_v))
print("fi_theta_to_delta_v="+str(fi_theta_to_delta_v))
print("A2=")
print(A2)
print("B2="+str(B2))
#
howAnywaySeidel0NurIfDetET01AnywayMatrix2=0
MaxQIters=20
eps=1E-6
X0= VectorOfZeros(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
X0= VectorOfOnes(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
print("std solution: A2*Mx="+str(np.linalg.solve(A2, B2))+" B2="+str(B2))
#Mx_side_Vz_delta_k=Mx
#
C_wz_longit_delta_v_ = Mx
#
C_wz_longit_Vx_delta_v = C_wz_longit_delta_v_[1-1]
C_wz_longit_Vy_delta_v = C_wz_longit_delta_v_[2-1]
C_wz_longit_wz_delta_v = C_wz_longit_delta_v_[3-1]
C_wz_longit_W_delta_v = C_wz_longit_delta_v_[4-1]
C_wz_longit_delta_v_delta_v = C_wz_longit_delta_v_[5-1]
#
print("part 2 of 2 (4th eq dW of longitudinal move)")
#
A_Vx_to_delta_fiMR  =  fA_y_to_x(w_ctrl, delta_fiMR__data, dVx__data, dt)
fi_Vx_to_delta_fiMR = ffi_y_to_x(w_ctrl, delta_fiMR__data, dVx__data, dt)
#
A_Vy_to_delta_fiMR  =  fA_y_to_x(w_ctrl, delta_fiMR__data, dVy__data, dt)
fi_Vy_to_delta_fiMR = ffi_y_to_x(w_ctrl, delta_fiMR__data, dVy__data, dt)
#
A_wz_to_delta_fiMR  =  fA_y_to_x(w_ctrl, delta_fiMR__data, dwz__data, dt)
fi_wz_to_delta_fiMR = ffi_y_to_x(w_ctrl, delta_fiMR__data, dwz__data, dt)
#
A_W_to_delta_fiMR  =  fA_y_to_x(w_ctrl, delta_fiMR__data, dW__data, dt) #W = Omega
fi_W_to_delta_fiMR = ffi_y_to_x(w_ctrl, delta_fiMR__data, dW__data, dt)
#
#A_dtheta_to_delta_fiMR  =  fA_y_to_x(w_ctrl, delta_fiMR__data, dtheta__data, dt)
#fi_dtheta_to_delta_fiMR = ffi_y_to_x(w_ctrl, delta_fiMR__data, dtheta__data, dt)
#
#
X2=[]
Y2=[]
#
for i in range(1, dataLength+1):
    #
    L2=[]
    x21=A_Vx_to_delta_fiMR * math.sin(w_ctrl * (i-1)*dt + fi_Vx_to_delta_fiMR)
    L2.append(x21)
    x21=A_Vy_to_delta_fiMR * math.sin(w_ctrl * (i-1)*dt + fi_Vy_to_delta_fiMR)
    L2.append(x22)
    x23=A_wz_to_delta_fiMR * math.sin(w_ctrl * (i-1)*dt + fi_wz_to_delta_fiMR)
    L2.append(x23)
    x24=A_W_to_delta_fiMR * math.sin(w_ctrl * (i-1)*dt + fi_W_to_delta_fiMR)
    L2.append(x24)
    x25=math.sin(w_ctrl * (i-1)* dt)
    L2.append(x25)
    X2.append(L2)
    y2=w_ctrl * (A_wz_to_delta_fiMR * math.sin(w_ctrl * (i-1)* dt + fi_wz_to_delta_fiMR + math.pi/2))
    Y2.append(y2)
#
print("X2=")
print(X2)
print("Y2="+str(Y2))
A2= multiply( transpose(X2), X2)
B2= multiply( transpose(X2), Y2)
print("A_Vx_to_delta_fiMR="+str(A_Vx_to_delta_fiMR))
print("fi_Vx_to_delta_fiMR="+str(fi_Vx_to_delta_fiMR))
print("A_Vy_to_delta_fiMR="+str(A_Vy_to_delta_fiMR))
print("fi_Vy_to_delta_fiMR="+str(fi_Vy_to_delta_fiMR))
print("A_wz_to_delta_fiMR="+str(A_wz_to_delta_fiMR))
print("fi_wz_to_delta_fiMR="+str(fi_wz_to_delta_fiMR))
print("A_W_to_delta_fiMR="+str(A_W_to_delta_fiMR))
print("fi_W_to_delta_fiMR="+str(fi_W_to_delta_fiMR))
print("A_theta_to_delta_fiMR="+str(A_theta_to_delta_fiMR))
print("fi_theta_to_delta_fiMR="+str(fi_theta_to_delta_fiMR))
print("A2=")
print(A2)
print("B2="+str(B2))
#
howAnywaySeidel0NurIfDetET01AnywayMatrix2=0
MaxQIters=20
eps=1E-6
X0= VectorOfZeros(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
X0= VectorOfOnes(len(B2))
Mx= Seidel(A2, B2, X0, eps, MaxQIters, howAnywaySeidel0NurIfDetET01AnywayMatrix2)
print("Mx="+str(Mx)+" ini vector="+str(X0))
print("A2*Mx="+str( multiply(A2,Mx))+" B2="+str(B2))
print("MQError="+str( LinEqErrVec(A2, B2, Mx))+" err="+str( LinEqErr(A2, B2, Mx)))
print("std solution: A2*Mx="+str(np.linalg.solve(A2, B2))+" B2="+str(B2))
#Mx_side_Vz_delta_k=Mx
#
C_wz_longit_delta_fiMR_ = Mx
#
C_wz_longit_Vx_delta_fiMR = C_wz_longit_delta_fiMR_[1-1]
C_wz_longit_Vy_delta_fiMR = C_wz_longit_delta_fiMR_[2-1]
C_wz_longit_wz_delta_fiMR = C_wz_longit_delta_fiMR_[3-1]
C_wz_longit_W_delta_fiMR = C_wz_longit_delta_fiMR_[4-1]
C_wz_longit_theta_delta_fiMR = C_wz_longit_delta_fiMR_[5-1]
C_wz_longit_delta_fiMR_delta_fiMR = C_wz_longit_delta_fiMR_[6-1]
#
print("average values: (4th eq dW of longitudinal move)")
#
C_wz_longit_Vx_ = (C_wz_longit_Vx_delta_v + C_wz_longit_Vx_delta_fiMR)/2
C_wz_longit_Vy_ = (C_wz_longit_Vy_delta_v + C_wz_longit_Vy_delta_fiMR)/2
C_wz_longit_wz_ = (C_wz_longit_wz_delta_v + C_wz_longit_wz_delta_fiMR)/2
C_wz_longit_W_ = (C_wz_longit_W_delta_v + C_wz_longit_W_delta_fiMR)/2
C_wz_longit_theta_ = (C_wz_longit_theta_delta_v + C_wz_longit_theta_delta_fiMR)/2
#
print("C_wz_longit_Vx="+str(C_wz_longit_Vx_))
print("C_wz_longit_Vy="+str(C_wz_longit_Vy_))
print("C_wz_longit_wz="+str(C_wz_longit_wz_))
print("C_wz_longit_W="+str(C_wz_longit_W_))
#
#
print("--------------------------------------------------------------------------------")
print("A_side:")
printMatrix(A_side)
print("Answer: A_side, Krylov:")
CharEq=fKrylovCharEq(A_side, eps=1e-6, MaxQIters=10, vsh=1)
print(str(CharEq))
printListAsPolynome(CharEq, 0)
print("Alg eq solution:")
AlgRoots=polynomeEqOfPower4(CharEq[4], CharEq[3], CharEq[2], CharEq[1], CharEq[0], 1)
print("roots:")
realParts=AlgRoots[0]
cmpxParts=AlgRoots[1]
countComplex=0
for val in cmpxParts:
    if val!=0:
        countComplex+=1
if countComplex==0:
    Roots=realParts
else:
    Roots=[]
    L1=len(realParts)
    for i in range(L1):
        Roots.append(Complex(realParts[i], cmpxParts[i]).get())
print("Alg eq answer (first):")
print(AlgRoots)
print("Alg eq answer (final):")
print(Roots)
errs=CalcEigenValError(A_side, Roots)
print("Error value(s): "+str(errs))
print("---------------------------- (Chk eq 3rd power:)")
AlgRoots=polynomeEqOfPower3(2, 2.533, -1.33, -2.004, 1)
print("Alg eq answer:")
print(AlgRoots)
print("test power")
q=-0.571
Q=0.017
print("q=-0.571="+str(-0.571)+"="+str(q))
print("Q=0.017="+str(0.017)+"="+str(Q))
print("-1.0*q/2="+str(-1.0*q/2))
print("math.sqrt(Q)="+str(math.sqrt(Q)))
print("-1.0*q/2+math.sqrt(Q)="+str(-1.0*q/2+math.sqrt(Q)))
print("math.pow((-1.0*q/2+math.sqrt(Q)),1/3)="+str(math.pow((-1.0*q/2+math.sqrt(Q)),1/3)))
print("math.pow((-1.0*q/2+math.sqrt(Q)),1.0/3)="+str(math.pow((-1.0*q/2+math.sqrt(Q)),1.0/3)))
print("math.pow((-1.0*q/2+math.sqrt(Q)),0.3333)="+str(math.pow((-1.0*q/2+math.sqrt(Q)),0.3333)))
print("(-1.0*q/2+math.sqrt(Q))**(1/3)="+str((-1.0*q/2+math.sqrt(Q))**(1/3)))
print("(-1.0*q/2+math.sqrt(Q))**(1.0/3)="+str((-1.0*q/2+math.sqrt(Q))**(1.0/3)))
print("(-1.0*q/2+math.sqrt(Q))**(0.3333)="+str((-1.0*q/2+math.sqrt(Q))**(0.3333)))
#print("math.pow((-1.0*q/2+math.sqrt(Q)),0.3333)="+str(math.pow((-1.0*q/2+math.sqrt(Q)),0.3333)))
print("--------------------------------------------------------------------------------")
print("A_lngt:")
printMatrix(A_lngt)
print("Answer: A_lngt, Krylov:")
CharEq=fKrylovCharEq(A_lngt, eps=1e-6, MaxQIters=10, vsh=1)
print(str(CharEq))
printListAsPolynome(CharEq, 0)
GershgorinCircles=fGershgorinCircles(A_lngt, 1)
print("GershgorinCircles")
printMatrix(GershgorinCircles)
QCircles=len(GershgorinCircles)
BestCircleN=0
#for circle in range GershgorinCircles:
for i in range (1, QCircles+1):
    circle=GershgorinCircles[i-1]
    x=circle[0]
    r=circle[1]
    if complex(x).imag==0 and complex(r).imag==0:
        BestCircleN=i
if BestCircleN==0:
    BestCircleN=QCircles
print("-----------------------------------------------------------------------------------")
