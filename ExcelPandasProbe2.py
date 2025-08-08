import pandas as pd
path="c:\\temp"
fileName="tblExampleSimple.xls"
#df=pd.DataFrame()
#df=pd.read_excel(path+"\\"+fileName, skiprows=0, skipfooter=2)
#print(df)
#print(df["Unnamed: 0"][1])
#df=pd.read_excel(path+"\\"+fileName, header=None, skiprows=0, skipfooter=2)
#print(df)
#print()
#print(df[1][1])
df=pd.read_excel(path+"\\"+fileName, header=None, skiprows=2, skipfooter=1)
print(df)
print()
print(df[1][1])
