import copy
import math


def calcOrder(x, base=0):
    order=0
    if x<0:
        y=-x
    else:
        y=x
    if x>=1:
        z=1
        while z<y:
            z*=base
            order+=1
        if z>y:
            order-=1
    else:
        z=y
        while z<1:
            z*=base
            order+=1
        order=-order
    return order

def IntToDigits(x, base=10):
    digits=[]
    if x<0:
        y=-x
    else:
        y=x
    order=calcOrder(x, base)
    rest=y
    for i in range(order+1):
        digit=rest%base
        rest=rest/base
        digits.append(digit)
    #digits.append(digit)
    return digits

x=123400500
print(x, IntToDigits(x))
x=1234059
print(x, IntToDigits(x))
x=2
print(x, IntToDigits(x))

def parseNum(num, base=10):
    signOfMantissaIsMinus=0
    signOfOrderIsMinus=0
    intPart=0
    fracPart=0
    x=num
    if(num<0):
        signOfMantissaIsMinus=1
        x=-num
    if num>=1:
        intPart=1
        while intPart<x:
            intPart+=1
        if intPart>x:
            intPart-=1
    fracPart=x-intPart
    order=calcOrder(x, base)
    mantissa=x
    if x>=1:
        for i in range(order):
            mantissa=1.0*mantissa/base
    else:
        for i in range(-order):
            mantissa=1.0*mantissa*base
    if signOfMantissaIsMinus==1:
        mantissa=-mantissaa 
    return intPart, fracPart, order, mantissa

num=12.34
intPart, fracPart, order, mantissa=parseNum(num)
print("num="+str(num)+"="+str(intPart)+"+"+str(fracPart)+"="+str(mantissa)+"E"+str(order))
num=0.0001234
intPart, fracPart, order, mantissa=parseNum(num)
print("num="+str(num)+"="+str(intPart)+"+"+str(fracPart)+"="+str(mantissa)+"E"+str(order))

def rounding(num, fracLen=0, base=10):#ne work gut
    intPart, fracPart, order, mantissa=parseNum(num, base)
    x=num
    if(num<0):
        x=-num
    if fracLen>0:
        for i in range(fracLen):
            x*=base
        digits=IntToDigits(x, base)
        
    L=len(digits)
    N=0
    continRounding=0 
    if base>3 and ((base%2==0 and digits[0]>base/2)or(base%2!=0 and digits[0]>=(base-1)/2+1)):
        continRounding=1
        while continRounding==1:
            N+=1
            digits[N-1]+=1
            if digits[N-1]<base:
                continRounding=0
            elif N==L:
                continRounding=0
                digits.append(1)
    digits1=[]
    for i in range(1, L+1):
        digits1.append(digits[i-1])
    return digits1


num=12.345
n=2
digits1=rounding(num, n)
print("round "+str(num)+" to "+str(n)+" digits = "+str(digits1))
            
