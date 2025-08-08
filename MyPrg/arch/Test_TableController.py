from TableController import *

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

ColNamesRow=["Name", "Prise actional", "Prise usual", "Marketplace"]

content1=dataSource2
content2=My2DArray1(dataSource2)

TableName="MyShop"

LineOfColHeader1=ColNamesRow
LineOfColHeader2=My1DArray(ColNamesRow)

ColOfLineHeader1=[]
ColOfLineHeader2=My1DArray()

tblHdr=TableHeaders(TableName)

tbl1=TableController(content1, LineOfColHeader1, ColOfLineHeader1, TableHeaders(TableName))
tbl2=TableController(content2, LineOfColHeader2, ColOfLineHeader2, TableHeaders(TableName))

print("content2:")
content2.ShowToConsole(" ")
