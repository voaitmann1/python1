import copy
from MyPyVibroLib import *


arr=[1, 2, 3, 4, 5]

print(arr)

SwapVals(2,4)
SwapVals(1,3)
SwapVals(5,2)

print(arr)

SortArray(arr, True)

print(arr)

QPoints=125#1250
QSects=10#100
#
##QPoints=len(signal)
#QPairs=QPoints-1
##dt=1/fs
#SectLenMed=QPairs/QSects
#SectLenInt=int(QPairs/QSects)
#rest=QPairs%QSects
#print("QPoints="+str(QPoints)+" QSects="+str(QSects)+" QPairs="+str(QPairs)+" SectLenInt="+str(SectLenInt)+" SectLenMed="+str(SectLenMed)+" rest="+str(rest)+" In all: "+str(SectLenInt*QSects+rest))
#print("Forming rows")
#rows=[]
#row=[]
#rowN=0
#for N in range (1, QPoints+1):
#    print("N="+str(N))
#    row.append(N)
#    if N%QSects==0:
#        if N<SectLenInt*QSects:
#            print("row bound reached")
#            print("row:")
#            print(row)
#            #rowToAdd=copy.deepcopy(row)
#            #rows.append(rowToAdd)
#            rows.append(row)
#            rowN+=1
#            print("last subRow")
#            print(rows[rowN-1])
#            if rowN>2:
#                print("pre-last subRow")
#                print(rows[rowN-2])
#            row=[]
#            #rowToAdd=[]
#            row.append(N)
#            #print("row bound reached")
#        else:
#            print("N="+str(N)+"=SectLenInt*QSects="+str(SectLenInt)+"*"+str(QSects)+"="+str(SectLenInt*QSects)+" - ignoring this point")
#    elif N==QPoints:
#        print("end reached")
#        print("row:")
#        print(row)
#        #rowToAdd=copy.deepcopy(row)
#        #rows.append(rowToAdd)
#        rows.append(row)
#        rowN+=1
#        print("last subRow")
#        print(rows[rowN-1])
#        if rowN>2:
#            print("pre-last subRow")
#            print(rows[rowN-2])
#        #rowToAdd=[]
#        row=[]
#        break
#
##
#QRows=len(rows)
#print("Result - "+str(QRows)+" rows:")
#for rowN in range(1, QRows+1):
#    rowL=len(rows[rowN-1])
#    print("row"+str(rowN)+" L="+str(rowL))
#    for cmpnN in range(1, rowL-1+1):
#        print(str(rows[rowN-1][cmpnN-1])+" ... "+str(rows[rowN-1][cmpnN-1+1]))
#
#print("rows:")
#print(rows)
#print("====================================================================")
#from MyPyVibroLib import MyEnvelopeBuilding_part1of3_SortPointsNumbersToSects_to2DArr
RowNs=MyEnvelopeBuilding_part1of3_SortPointsNumbersToSects_to2DArr(QPoints, QSects, vsh=2)
