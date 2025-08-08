for i in range(0,15-1,2): #arange needs numpy or scipy, or use range 
    print(i)
#x0 =zeros([4]) #zeros needs numpy or scipy
#print(x0)
#
from matplotlib import *
import pandas as pd
#
from numpy import*
from scipy import optimize
import time
#
for i in arange(0,15-1,2):
    print(i)
x0 =zeros([4])
print(x0)
#
print("non-lin eqs")
ti = time.clock() 
n=100
def f(x):
         f = zeros([n])
         for i in arange(0,n-1,1):
                  f[i] = (3 + 2*x[i])*x[i] - x[i-1] - 2*x[i+1] - 2
         f [0] = (3 + 2*x[0] )*x[0] - 2*x[1] - 3
         f[n-1] = (3 + 2*x[n-1] )*x[n-1] - x[n-2] - 4
         return f
x0 =zeros([n])
sol = optimize.root(f,x0, method='krylov')
print('Solution:\n', sol.x)
print('Krylov method iteration = ',sol.nit)
print('Optimize root time', round(time.clock()-ti,3), 'seconds')
#
print("non-lin my")
T_ine_med=289.5
#def fK(Tw):
    
x_my=[]
#x_my[2-1]=-23.488
#x_my[2-1]=261.25
#x_my[3-1]=x_my[1-1]
q_WarmCondAppr7=-23.488
T_wall_ext_Appr7=261.25
q_wall_radiance_7=q_WarmCondAppr7
x_my.append(q_WarmCondAppr7)
x_my.append(T_wall_ext_Appr7)
x_my.append(q_wall_radiance_7)
print(x_my)
#def f_my(x_my):
#    q_WarmCondAppr7=x_my[1-1]
#    T_wall_ext_Appr7=x_my[2-1]
#    q_wall_radiance_7=x_my[3-1]
#    f=zeros[3]
#    f[1-1]=

import matplotlib
print("mpv=",matplotlib.__version__)

import pandas as pd
excel_data_df = pd.read_excel('c:\\temp\\xls1.xls', sheet_name='Лист1', usecols=['t','Nt'])
print(excel_data_df)


from pylab import *
LimVal=20
plot(range(1, LimVal),
     [i * i*i for i in range(1, LimVal)], 'ro')
savefig('example.png')
show()
    

