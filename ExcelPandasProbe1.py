import pandas as pd
#
#fName='./Fig3-1.xls'
fName2='c:/temp/test.xlsx'
fName1='c:/temp/test.xls'
QSkippedUpperLines=0
QSkippedLowerLines=0
HeaderIsNeeded=1
#
if HeaderIsNeeded==1:
    data_file=pd.read_excel(fName1,  spiprows=QSkippedUpperLines, skipfooter=QSkippedLowerLines)
else:
    data_file=pd.read_excel(fName1, header=None, spiprows=QSkippedUpperLines, skipfooter=QSkippedLowerLines)
#


from openpyexcel import load_workbook

wb=load_workbook(fName2)
sheets=wb.get_sheet_names()
print(sheets)
sheet=wb.get_sheet_by_name('Sheet3')
print(wb.cell(row=4, col=4).Formula)
