from TableController2 import *

dataSource1=[["Greel Tefal GC 712 OptiGril","4999","6999","Foxtrot.ua"],
            ["WacuumCleaner Philips FC9552","3599","4999","Foxtrot.ua"],
            ["Smartphone POCO X3 Pro","6799","7999","Foxtrot.ua"],
            ["Notebook Lenovo V15 ","9999","12999","Foxtrot.ua"],
            ["Notebook Lenovo V15 ","9999","12999","Foxtrot.ua"],
            ["Smartphone Samsung Galaxy S20 FE (2021)","16999","18999","rozetka.com.ua"],
            ["CoffeMachine Delongi ECAM 550.85","22999","32999","rozetka.com.ua"],
           ]

dataSource2=[["Greel Tefal GC 712 OptiGril",4999,6999,"Foxtrot.ua"],
            ["WacuumCleaner Philips FC9552",3599,4999,"Foxtrot.ua"],
            ["Smartphone POCO X3 Pro",6799,7999,"Foxtrot.ua"],
            ["Notebook Lenovo V15 ",9999,12999,"Foxtrot.ua"],
            ["Notebook Lenovo V15 ",9999,12999,"Foxtrot.ua"],
            ["Smartphone Samsung Galaxy S20 FE (2021)",16999,18999,"rozetka.com.ua"],
            ["CoffeMachine Delongi ECAM 550.85",22999,32999,"rozetka.com.ua"],
           ]

dataSource3=[[4999,6999,"Foxtrot.ua"],
            [3599,4999,"Foxtrot.ua"],
            [6799,7999,"Foxtrot.ua"],
            [9999,12999,"Foxtrot.ua"],
            [9999,12999,"Foxtrot.ua"],
            [16999,18999,"rozetka.com.ua"],
            [22999,32999,"rozetka.com.ua"],
           ]

ColOfLineHeader=["Greel Tefal GC 712 OptiGril","WacuumCleaner Philips FC9552", "Smartphone POCO X3 Pro", "Notebook Lenovo V15 ", "Notebook Lenovo V15 ", "Smartphone Samsung Galaxy S20 FE (2021)", "CoffeMachine Delongi ECAM 550.85"]

ColNamesRow=["Name", "Prise actional", "Prise usual", "Marketplace"]

content1=dataSource2
content2=My2DArray1(dataSource2)

TableName="MyShop"

LineOfColHeader1=ColNamesRow
#LineOfColHeader2=My1DArray(ColNamesRow)

ColOfLineHeader1=[]
#ColOfLineHeader2=My1DArray()

tblHdr=TableHeaders(TableName, "Items", "N")

tblHdr1=TableHeaders("MyShop", "Names", "Params")
print("table name: "+tblHdr1.ToString_TableHeader())
print("table Lines gen name: "+tblHdr1.ToString_LinesGeneralHeader())
print("table Cols gen name: "+tblHdr1.ToString_ColumnsGeneralHeader())      

#tbl1=TableController(content1, LineOfColHeader1, ColOfLineHeader1, TableHeaders(TableName))
#tbl2=TableController(content2, LineOfColHeader2, ColOfLineHeader2, TableHeaders(TableName))
ext_LC_0_CL_1=0
ine_LC_0_CL_1=0
vsh=1

tbl3=TableController2(dataSource3, ColNamesRow, ColOfLineHeader, TableHeaders("MyShop", "Names", "Params"), ext_LC_0_CL_1, ine_LC_0_CL_1, vsh)
print(tbl3.ToString_TableName())
print(tbl3.ToString_HeaderLine())
QL=tbl3.GetQLines()
print("QLines="+str(QL))
for i in range(1, QL+1):
    print(tbl3.ToString_Line(i))
print("Content once more:")
QC=tbl3.GetQColumns()
print("QColumns="+str(QC))
for i in range(1, QL+1):
    for j in range(1, QC+1):
        cell=tbl3.GetCell_AsCopy(i, j)
        print(cell.ToString())




