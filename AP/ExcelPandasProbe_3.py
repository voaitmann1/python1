#import pandas as pd
#path="c:\\temp"
#fileName="tblExampleSimple.xls"
#df=pd.DataFrame()
#df=pd.read_excel(path+"\\"+fileName, skiprows=0, skipfooter=2)
#print(df)
#print(df["Unnamed: 0"][1])
#df=pd.read_excel(path+"\\"+fileName, header=None, skiprows=0, skipfooter=2)
#print(df)
#print()
#print(df[1][1])
import pandas as pd
#variant with headers
dwz__name="dwz"
path="iNIdATA"
fileName="INIdATA1.xls"
df=pd.read_excel(path+"\\"+fileName)#, header=1, skiprows=1, skipfooter=0)
print(df)
print()
#print(df[2][1])
print("df[dwz__name][3]=",df[dwz__name][3])
dwz__data=df[dwz__name]
print("dwz__data[3]=",dwz__data[3])
print()
#variant with headers
dwz_N=3
dwz__name="dwz"
path="iNIdATA"
fileName="INIdATA1.xls"
df=pd.read_excel(path+"\\"+fileName, header=None, skiprows=1, skipfooter=0)
print(df)
print()
print(df[2][1])
print("df[dwz__name][4]=",df[dwz_N][4-1])
dwz__data=df[dwz_N]
print("dwz__data[4]=",dwz__data[4-1])
#
#
T__N=1
T__name="T__data"
T__data=[1, 2, 3, 4, 5, 6, 7, 8, 9]
#Eqs of longitudial move
#general
dVx__N=2
dVx__name="dVx__data"
#dVx__data=[11, 12, 13, 14, 15, 16, 17, 18, 19]
dVy__N=3
dVy__name="dVy__data"
#dVy__data=[21, 22, 23, 24, 25, 26, 27, 28, 29]
dwz__N=4
dwz__name="dwz__data"
#dwz__data=[31, 32, 33, 34, 35, 36, 37, 38, 39]
dW__N=5
dW__name="dW__data"
dW__data=[41, 42, 43, 44, 45, 46, 47, 48, 49]
dtheta__N=6
dtheta__name="dtheta__data"
#dtheta__data=[51, 52, 53, 54, 55, 56, 57, 58, 59]
# case
#dVx__N=2
#dVx__name="dVx__data"
#dVx__data=[11, 12, 13, 14, 15, 16, 17, 18, 19]
#dVy__N=3
#dVy__name="dVy__data"
#dVy__data=[21, 22, 23, 24, 25, 26, 27, 28, 29]
#dwz__N=4
#dwz__name="dwz__data"
#dwz__data=[31, 32, 33, 34, 35, 36, 37, 38, 39]
#dW__N=5
#dW__name="dW__data"
#dW__data=[41, 42, 43, 44, 45, 46, 47, 48, 49]
dtheta__N=6
dtheta__name="dtheta__data"
#dtheta__data=[51, 52, 53, 54, 55, 56, 57, 58, 59]
#Eqs of side move
#same data and:
dwx__N=7
dwx__name="dwx__data"
#dwx__data=[61, 62, 63, 64, 65, 66, 67, 68, 69]
dwy__N=8
dwy__name="dwy__data"
#dwy__data=[71, 72, 73, 74, 75, 76, 77, 78, 79]
#and also:
dVz__N=9
dVz__name="dVz__data"
#dVz__data=[91, 92, 93, 94, 95, 96, 97, 98, 99]
dgamma__N=10
dgamma__name="dgamma__data"
#dgamma__data=[101, 102, 103, 104, 105, 106, 107, 108, 109]
dbeta__N=10
dbeta__name="dbeta__data"
#dbeta_data=[81, 82, 83, 84, 85, 86, 87, 88, 89]
#Concrtete incoming signals
#Eqs of longitudial move
delta_v__N=12
delta_v__name="delta_v__data"
#delta_v__data=[111, 112, 113, 114, 115, 116, 117, 118, 119]
delta_fi_collPitch__N=13
delta_fi_collPitch__name="delta_fi_collPitch__data"
#delta_fi_collPitch__data=[121, 122, 123, 124, 125, 126, 127, 128, 129]
delta_kci_engine__N=14
delta_kci_engine__name="delta_kci_engine__data"
#delta_kci_engine__data=[131, 132, 133, 134, 135, 136, 137, 138, 139]
#Eqs of side move
delta_n__N=15
delta_n__name="delta_n__data"
#delta_n__data=[141, 142, 143, 144, 145, 146, 147, 148, 149]
delta_k__N=16
delta_k__name="delta_k__data"
#delta_k__data=[151, 152, 153, 154, 155, 156, 157, 158, 159]
delta_fi_TR__N=17
delta_fi_TR__name="delta_fi_TR__data"
#delta_fi_TR__data=[161, 162, 163, 164, 165, 166, 167, 168, 169]
#
#
#
#dwz__data=df[dwz_N]
T__data=df[T__N-1]
dVx__data=df[dVx__N-1]
dVy__data=df[dVy__N-1]
dwz__data=df[dwz__N-1]
dW__data=df[dW__N-1]
dtheta__data=df[dtheta__N-1]
dwx__data=df[dwx__N-1]
dwy__data=df[dwy__N-1]
dVz__data=df[dVz__N-1]
dwx__data=df[dwx__N-1]
dwy__data=df[dwy__N-1]
dVz__data=df[dVz__N-1]
dgamma__data=df[dgamma__N-1]
dbeta__data=df[dbeta__N-1]
delta_v__data=df[delta_v__N-1]
delta_fi_collPitch__data=df[delta_fi_collPitch__N-1]
delta_kci_engine__data=df[delta_kci_engine__N-1]
delta_n__data=df[delta_n__N-1]
delta_k__data=df[delta_k__N-1]
delta_fi_TR__data=df[delta_fi_TR__N-1]
#
print("T__data=df["+str(T__N)+"]=",T__data)
print("dVx__data=df["+str(dVx__N)+"]=",dVx__data)
print("dVy__data=df["+str(dVy__N)+"]=",dVy__data)
print("dwz__data=df["+str(dwz__N)+"]=",dwz__data)
print("dW__data=df["+str(dW__N)+"]=",dW__data)
print("dtheta__data=df["+str(dtheta__N)+"]=",dtheta__data)
print("dwx__data=df["+str(dwx__N)+"]=",dwx__data)
print("dwy__data=df["+str(dwy__N)+"]=",dwy__data)
print("dVz__data=df["+str(dVz__N)+"]=",dVz__data)
print("dwx__data=df["+str(dwx__N)+"]=",dwx__data)
print("dwy__data=df["+str(dwy__N)+"]=",dwy__data)
print("dVz__data=df["+str(dVz__N)+"]=",dVz__data)
print("dgamma__data=df["+str(dgamma__N)+"]=",dgamma__data)
print("dbeta__data=df["+str(dbeta__N)+"]=",dbeta__data)
print("delta_v__data=df["+str(delta_v__N)+"]=",delta_v__data)
print("delta_fi_collPitch__data=df["+str(delta_fi_collPitch__N)+"]=",delta_fi_collPitch__data)
print("delta_kci_engine__data=df["+str(delta_kci_engine__N)+"]=",delta_kci_engine__data)
print("delta_n__data=df["+str(delta_n__N)+"]=",delta_n__data)
print("delta_k__data=df["+str(delta_k__N)+"]=",delta_k__data)
print("delta_fi_TR__data=df["+str(delta_fi_TR__N)+"]=",delta_fi_TR__data)
#
print("values quantity: "+str(len(delta_fi_TR__data)))

