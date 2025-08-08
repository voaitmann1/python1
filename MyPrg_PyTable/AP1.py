import numpy as np


#Data

dVx__data=np.array([])
dVy__data=np.array([])
dwz__data=np.array([])
dOwz__data=np.array([])
theta__data=np.array([])

dwx__data=np.array([])
dwy__data=np.array([])
dVz_data=np.array([])
dgamma_data=np.array([])
dbeta_data=np.array([])

delta_vB__data=np.array([])
delta_Fi_ColPitch__data=np.array([])
delta_eps_engine__data=np.array([])

delta_nH__data=np.array([])
delta_K__data=np.array([])
delta_Fi_TR__data=np.array([])

# Params

dt=0.5
theta0=1

CorrectSys_MoveAsude__SysNotZB=1

# 1-th signal elab

def fSq(w, q, dt):
    R=0
    N=len(q)
    part1=(-q[1-1])/w)-((q[N-1]-q[N-1-1])/(w*w*dt))*sin(w*(N-1)*dt)
    summ=0
    for i in range(1, N-2+1):
        cur=(-q[i-1-1]+2*q[i+1-1]-q[i+2-1])*sin(w*i*dt)
        summ=summ+cur
    R=part1-(1/(w*w*dt))*summ
    return R

def fCq(w, q, dt):
    R=0
    N=len(q)
    part1=(-q[1-1])/w)-((q[N-1]-q[N-1-1])/(w*w*dt))*sin(w*(N-1)*dt)
    summ=0
    for i in range(1, N-2+1):
        cur=(-q[i-1-1]+2*q[i+1-1]-q[i+2-1])*sin(w*i*dt)
        summ=summ+cur
    R=part1-(1/(w*w*dt))*summ
    return R


