import pandas as pd
#
fName='./Fig3-1.xls'
QSkippedUpperLines=0
QSkippedLowerLines=0
HeaderIsNeeded=1
#
if HeaderIsNeeded==1:
    data_file=pd.read_excel(fName,  spiprows=QSkippedUpperLines, skipfooter=QSkippedLowerLines)
else:
    data_file=pd.read_excel(fName, header=None, spiprows=QSkippedUpperLines, skipfooter=QSkippedLowerLines)
#
