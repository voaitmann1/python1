from TableController2 import *
#from MyLib import *
#import PyStdVector2
from TableInfoClasses import *
#from TableGUIGrid import *
#from TableGUI import *
#from TableGUI1 import *
from TableGUI2 import *

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

dataSource4=[["Goods:Name\\Params","Prise actional", "Prise usual", "Marketplace"],
             ["Greel Tefal GC 712 OptiGril",4999,6999,"Foxtrot.ua"],
             ["WacuumCleaner Philips FC9552",3599,4999,"Foxtrot.ua"],
             ["Smartphone POCO X3 Pro",6799,7999,"Foxtrot.ua"],
             ["Notebook Lenovo V15 ",9999,12999,"Foxtrot.ua"],
             ["Notebook Lenovo V15 ",9999,12999,"Foxtrot.ua"],
             ["Smartphone Samsung Galaxy S20 FE (2021)",16999,18999,"rozetka.com.ua"],
             ["CoffeMachine Delongi ECAM 550.85",22999,32999,"rozetka.com.ua"],
           ]

dataSource5=[
             ["Greel Tefal GC 712 OptiGril",[4999,6999,"Foxtrot.ua"]],
             ["WacuumCleaner Philips FC9552",[3599,4999,"Foxtrot.ua"]],
             ["Smartphone POCO X3 Pro",[6799,7999,"Foxtrot.ua"]],
             ["Notebook Lenovo V15 ",[9999,12999,"Foxtrot.ua"]],
             ["Notebook Lenovo V15 ",[9999,12999,"Foxtrot.ua"]],
             ["Smartphone Samsung Galaxy S20 FE (2021)",[16999,18999,"rozetka.com.ua"]],
             ["CoffeMachine Delongi ECAM 550.85",[22999,32999,"rozetka.com.ua"]],
           ]

dataSource6=[
             [[4999,6999,"Foxtrot.ua"],"Greel Tefal GC 712 OptiGril"],
             [[3599,4999,"Foxtrot.ua"],"WacuumCleaner Philips FC9552"],
             [[6799,7999,"Foxtrot.ua"],"Smartphone POCO X3 Pro"],
             [[9999,12999,"Foxtrot.ua"],"Notebook Lenovo V15 "],
             [[9999,12999,"Foxtrot.ua"],"Notebook Lenovo V15 "],
             [[16999,18999,"rozetka.com.ua"],"Smartphone Samsung Galaxy S20 FE (2021)"],
             [[22999,32999,"rozetka.com.ua"],"CoffeMachine Delongi ECAM 550.85"],
           ]



ColOfLineHeader=["Greel Tefal GC 712 OptiGril","WacuumCleaner Philips FC9552", "Smartphone POCO X3 Pro", "Notebook Lenovo V15 ", "Notebook Lenovo V15 ", "Smartphone Samsung Galaxy S20 FE (2021)", "CoffeMachine Delongi ECAM 550.85"]

ColNamesRow=["Name", "Prise actional", "Prise usual", "Marketplace"]
ColNamesRow=["Prise actional", "Prise usual", "Marketplace", "Color"]

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

print("")
print("")
tbl3=TableController2(dataSource3, ColNamesRow, ColOfLineHeader, TableHeaders("MyShop", "Names", "Params"), ext_LC_0_CL_1, ine_LC_0_CL_1, vsh)
print("")
print("tbl3:")
print(tbl3.ToString_TableName())
print(tbl3.ToString_HeaderLine())
QL=tbl3.GetQLines()
#print("QLines="+str(QL))
for i in range(1, QL+1):
    print(tbl3.ToString_Line(i))
print("")
print("")
#
contents=[]
print("forming rows for ")
for i in range(1, len(dataSource2)+1):
    rwh=DataCellRowWithHeader()
    rwh.Set_FirstElementAsHeader(dataSource2[i-1])
    #Set_FirstElementAsHeader(dataSource2[i-1])
    contents.append(rwh)
    print(i, " ", rwh.ToString())
print(contents)
#
#tbl4=TableController2(contents, ColNamesRow, TableHeaders("MyShop", "Names", "Params"), ext_LC_0_CL_1, ine_LC_0_CL_1, vsh)
tbl4=TableController2()
tbl4.Set_ByContentHeadered1(contents, ColNamesRow, TableHeaders("MyShop", "Names", "Params"), ext_LC_0_CL_1=0, ine_LC_0_CL_1=0, vsh=0)
print("")
print("tbl4:")
print(tbl4.ToString_TableName())
print(tbl4.ToString_HeaderLine())
QL=tbl4.GetQLines()
#print("QLines="+str(QL))
for i in range(1, QL+1):
    print(tbl4.ToString_Line(i))
print("")
print("")
print("Content once more:")
print("QLines="+str(QL))
QC=tbl3.GetQColumns()
print("QColumns="+str(QC))
for i in range(1, QL+1):
    for j in range(1, QC+1):
        cell=tbl3.GetCell_AsCopy(i, j)
        print(cell.ToString())
print("")
print("")
print("tbl5  (Set_By2DArray):")
#tbl5=TableController2(dataSource4, 1, 1, ext_LC_0_CL_1, ine_LC_0_CL_1, vsh)
tbl5=TableController2()
tbl5.Set_By2DArray(dataSource4, 1, 1, ext_LC_0_CL_1, ine_LC_0_CL_1, vsh)
print("")
print("tbl5:")
tbl5.ShowToConsole()
print("")
print("")
tbl6=TableController2()
tbl6.Set_ByContentHeadered(dataSource2, ColNamesRow, TableHeaders("MyShop", "Names", "Params"), 0, 0, vsh)
print("")
print("tbl6:")
tbl6.ShowToConsole()
print("")
print("")
print("tbl7:")
tbl7=TableController2()
tbl7.Set_ByContent_AndSeparateHeaders(dataSource3, ColOfLineHeader, ColNamesRow, TableHeaders("MyShop", "Names", "Params"), ext_LC_0_CL_1=0, ine_LC_0_CL_1=0, vsh=0)
print("")
tbl7.ShowToConsole()
print("")
print("")
print("tbl8:")
tbl8=TableController2()
tbl8.Set_ByContentHeadered1(dataSource5, ColNamesRow, TableHeaders("MyShop", "Names", "Params"), ext_LC_0_CL_1=0, ine_LC_0_CL_1=0, vsh=0)
print("")
tbl8.ShowToConsole()
print("")
print("")
print("tbl9:")
tbl9=TableController2()
tbl9.Set_ByContentHeadered1(dataSource6, ColNamesRow, TableHeaders("MyShop", "Names", "Params"), ext_LC_0_CL_1=0, ine_LC_0_CL_1=0, vsh=0)
print("")
tbl8.ShowToConsole()
print("")
print("")
#
dataSource01=[["Equation:X^=\\Coef", "Value"],
            [1.0],
            [2.0],
            [3.0]]

dataSource02=[["Value"],
            [1.0],
            [2.0],
            [3.0]]

tbl01=TableController2()
tbl01.Set_By2DArray(dataSource02, 0, 1, ext_LC_0_CL_1, ine_LC_0_CL_1, vsh)

print("EqTable simply")
tbl01.ShowToConsole()

tblReprEq=TableRepr()
tblReprEq.SetAsSimple()

print("EqTable simple Repr")
tbl01.ShowToConsole(tblReprEq)

tblReprEq.general.ShowLineOfColHeader=1
tblReprEq.general.ShowColOfLineHeader=1
tblReprEq.CoLH.ShowHeader=1#default
tblReprEq.CoLH.ShowGenHeader=1
tblReprEq.CoLH.ShowRowN=1
tblReprEq.CoLHHeaderAndN_GNH1_NGH2_HGN3_HNG4=1
tblReprEq.CoLH.AftGH=SeparCharNEmpty#nil
tblReprEq.CoLHBefHdr=SeparCharNEmpty#nil
tblReprEq.CoLH.AftHdr=SeparCharNEmpty#nil
tblReprEq.CoLH.BefN=SeparCharNEmpty##
tblReprEq.CoLH.AftN=SeparCharNEmpty#
tblReprEq.LoCH.SetAsSimple()
#
print("\nTableHeaders rest")
separTableHeader=TableHeaders()
separTableHeader.Set("Equation", "X^=", "Coef", vsh)
#
print("\nEqTable by repr_")
tbl01.SetTableHeaders("Equation", "X^=", "Coef", vsh)
tbl01.ShowToConsole(" ", ": ", tblReprEq)
print("\nFirst ColOfLineHeaderCell:")
#print(tbl01.ToString_Cell_ColOfLineHeader(1, tblReprEq, vsh))
print(tbl01.ToString_Cell_ColOfLineHeader(1, tblReprEq, 0))
print("\nFirst LineOfColHeaderCell:")
#print(tbl01.ToString_Cell_LineOfColHeader(1, tblReprEq, vsh))
print(tbl01.ToString_Cell_LineOfColHeader(1, tblReprEq, 0))
print("\nFirst Line:")
print(tbl01.ToString_Line(1, " ", ": ", tblReprEq, vsh))
#print(tbl01.ToString_ContentLine(1, " ", tblReprEq, 1))
#print(tbl01.ToString_ContentLine(1, " ", tblReprEq, 0))

#arr=[["one", 1],
#     ["two", 2]),
#     ["three", 3],
#    ]



zb_Corner="MyTable:object\\colour"
zb_colors=["red", "yellow", "green", "light-blue", "blue", "white", "black"]
zb_objects=["air", "water", "grass", "wheat", "coal", "paper", "flag"]
cnt=[
     [zb_objects[(SeekFirst(zb_objects, "air"))-1],[DataCell(zb_colors, (SeekFirst(zb_colors, "light-blue")))]],
     [zb_objects[(SeekFirst(zb_objects, "water"))-1],[DataCell(zb_colors, (SeekFirst(zb_colors, "blue")))]],
     [zb_objects[(SeekFirst(zb_objects, "grass"))-1],[DataCell(zb_colors, (SeekFirst(zb_colors, "green")))]],
     [zb_objects[(SeekFirst(zb_objects, "wheat"))-1],[DataCell(zb_colors, (SeekFirst(zb_colors, "yellow")))]],
     [zb_objects[(SeekFirst(zb_objects, "coal"))-1],[DataCell(zb_colors, (SeekFirst(zb_colors, "black")))]],
     [zb_objects[(SeekFirst(zb_objects, "paper"))-1],[DataCell(zb_colors, (SeekFirst(zb_colors, "white")))]],
     [zb_objects[(SeekFirst(zb_objects, "flag"))-1],[DataCell(zb_colors, (SeekFirst(zb_colors, "red")))]]
]
print("given:")
print("air",SeekFirst(zb_objects, "air")-1,"light-blue",(SeekFirst(zb_colors, "light-blue")-1))
print("water",SeekFirst(zb_objects, "water")-1,"blue",(SeekFirst(zb_colors, "blue")-1))
print("grass",SeekFirst(zb_objects, "grass")-1,"green",(SeekFirst(zb_colors, "green")-1))
print("wheat",SeekFirst(zb_objects, "wheat")-1,"yellow",(SeekFirst(zb_colors, "yellow")-1))
print("coal",SeekFirst(zb_objects, "coal")-1,"black",(SeekFirst(zb_colors, "black")-1))
print("paper",SeekFirst(zb_objects, "paper")-1,"white",(SeekFirst(zb_colors, "white")-1))
print("flag",SeekFirst(zb_objects, "flag")-1,"red",SeekFirst(zb_colors, "red")-1)
    
    
tbl=TableController2()
tbl.Set_ByContentHeadered1(cnt, zb_objects, TableHeaders(zb_Corner),0 ,0 ,1)
cnt=tbl.GetContent_Vals()
print("vals:")
print(cnt)
cnt=tbl.GetContent_CurItems()
print("items:")
print(cnt)
tbl.ShowToConsole()
cell=tbl.GetCell_AsCopy(1,1)
typeN=cell.GetType()
val=cell.GetVal()
item1=cell.GetItem()
item2=cell.GetItem(2)
print("typeN=",typeN," val=",val," item1=",str(item1)," item2=",str(item2))
col=tbl.GetContentColumn_AsList_OfVals(1)
print(col)
col=tbl.GetContentColumn_AsList_OfCurItems(1)
print(col)
print("\nCheck cell constructor")
cell=DataCell(zb_colors, (SeekFirst(zb_objects, "light-blue"))-1)
typeN=cell.GetType()
val=cell.GetVal()
item1=cell.GetItem()#(0,1)
item2=cell.GetItem(2)
print("typeN=",typeN," val=",val," item1=",str(item1)," item2=",str(item2))
#print("arr[two]=",arr["two"])

print ("\n\n\nTrying add col to table")
print("Table before addimng col")
tbl9.ShowToConsole()
#7 lines
newColCnt=[]
for i in range(1, 7+1):
    newColCnt.append(DataCell(zb_colors ,i))
print ("col will be: ", newColCnt)
tbl9.AddColumn(["Color",newColCnt],"", "", 0, 1)
#def AddColumn(self, rowCntExt=[], header="", DfltVal="", QToAddForEmpty=1, vsh=0):
print("Table after addimng col")
tbl9.ShowToConsole()

#def __init__(self, table, tblInf, GuiControls, activeRows=0, Align_Left1Top2Bottom3Right4=0, DfltWidth=40, rowOrder_LC0_CL1=1, sourceOrder_LC0_CL1=1)
tblInf=TableInfo1()
tblInf.repr.SetAsSimple()
guiControls=TableGUIControls()
guiControls.Array_ActiveNText1_ActiveItemText2_Combobox3=2
rowsNsLimsToDispl=TRowsNsLims()
rowsNsLimsToDispl.SetFull(TableSize(tbl9.GetQLines(), tbl9.GetQColumns()))
rowsNsLimsToDispl.DelPrevColumn(TableSize(tbl9.GetQLines(), tbl9.GetQColumns()))
#TableForm:
#def __init__(self,   sourceTable, tblInf=0, GuiControls=0, activeRows=0, source=0, DfltWidth=40, vsh=0)
#wnd=TableForm(                tbl,   tblInf,   guiControls, rowsNsLimsToDispl, TableSize(2,1))
wnd=TableForm(                tbl9,   tblInf,   guiControls, rowsNsLimsToDispl, TableSize(2,1))
#wnd.window.mainloop()
wnd.Show()
#
#tbl9.AddColumn(["Color",newColCnt])

