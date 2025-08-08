#import copy
#from DataCellSimple import *
#from DBDataClasses import *
from TableHeaders import *#refers to DataCellSimple, an that refers to DBDataClasses
#
cell1=DataCell(1)
cell2=DataCell(2.5)
cell3=DataCell("str")
#cell4=DataCell(['item1', 'item2', 'item3'], 2, 1)
cell4=DataCell(['item1', 'item2', 'item3'], 2)
cell5=DataCell(['item10', 'item20', 'item30'])
#
DBHdr="MyDB"
DBTypeName="SQLite"
DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5=1
DBFileFullName="c:\\temp\\MyDB1.db"
TableNameInDB="MyDBTable"
#                TDBTableDataSuppl  #DBDataClasses
DBTableDataSuppl=TDBTableDataSuppl(DBHdr, DBTypeName, DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5, DBFileFullName)
#def __init__(self, DBHdr="", DBTypeName="",DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5=0, DBFileFullName="")
#           TDBTableData
DBTableData=TDBTableData(TableNameInDB, DBTableDataSuppl)
#
#
ExtItems1=['item01', 'item02', 'item03']
ExtItems2=['My Col #1', 'DBField1', 5, "VARCHAR", 25, 0, 1, 0, 1, 0, "y"]
ExtItems3=['My Col #1', 'DBField1', 5, "VARCHAR", 25, 0, 1, 0, 1, 0, "MyItemsTable", "MyItemsField", "MyKeyField"]
ExtItems4=['My DB Table', 'MyDB', "SQLite", "D:\\temp\\MyDB1.db"]
#
DBFieldInfoSuppl=TDBFieldInfoSuppl()
DBFieldInfoSuppl.FieldTypeN=5#1
DBFieldInfoSuppl.FieldTypeName="VARCHAR"#2
DBFieldInfoSuppl.FieldLength=25#3
DBFieldInfoSuppl.DBFieldCharacteristicsNumber=0#4
DBFieldInfoSuppl.isKeyField=1#5
DBFieldInfoSuppl.isCounter=0#6
DBFieldInfoSuppl.isNotNull=1#7
DBFieldInfoSuppl.isAutoIncrement=0#8
#
DBFieldInfo=TDBFieldInfo()
DBFieldInfo.DBFieldNameToDBTable="DBTable"
DBFieldInfo.DBFieldInfoSuppl=DBFieldInfoSuppl
#
DBItemsTableData=TDBItemsTableData()
DBItemsTableData.ItemsTableName="MyItemsTable"
DBItemsTableData.ItemsTableItemsFieldName="ItemsField"
DBItemsTableData.ItemsTableKeyFieldName="KeyField"
#
cell6=DataCell("My Table", DBTableData)
cell7=DataCell("My Table")
cell7.SetCell_DBTableHeader("My Table")
#
cell8=DataCell("My Col #1", ExtItems2, DBFieldInfo, DBItemsTableData)
cell9=DataCell("My Col #2", ExtItems2)
cell10=DataCell("My Col #3", [], DBFieldInfo)
#
cell11=DataCell(ExtItems2)
#
print("cell1: "+cell1.ToString())
print("cell2: "+cell2.ToString())
print("cell3: "+cell3.ToString())
print("cell4: "+cell4.ToString())
print("cell4: "+str(cell4.GetItem()))
print("cell4: "+str(cell4.GetVal()))
#
cell4.SetVal(30)
#
print("cell4 - last val: "+str(cell4.GetItem(3)))
print("cell6 - main name: " +cell6.ToString())
print("cell6 - path: " +cell6.GetDBFileFullName())
print("cell7 - main name: " +cell7.ToString())
print("cell7 - path: " +cell7.GetDBFileFullName())
#
print("cell8: "+cell8.ToString())
print("cell9: "+cell9.ToString())
print("cell10: "+cell10.ToString())
print("cell11: "+cell11.ToString())
#
print("cell8- itemN2: "+cell8.GetItem(2))
print("cell9- itemN2: "+cell9.GetItem(2))
print("cell10- itemN2: "+cell10.GetItem(2))
print("cell11- itemN2: "+cell11.GetItem(2))
#
#
print("cell8- FieldTypeName: ",cell8.GetFieldTypeName())
print("cell8- FieldTypeN: ",cell8.GetFieldTypeN())
print("cell8- ColNameToDisplay: ",cell8.GetColNameToDisplay())
print("cell8- DBFieldName: ",cell8.GetDBFieldName())
print("cell8- GetFieldLength: ",cell8.GetFieldLength())
print("cell8- CharNum: ",cell8.GetDBFieldCharacteristicsNumber())
#
print("cell9- FieldTypeName: ",cell9.GetFieldTypeName())
print("cell9- FieldTypeN: ",cell9.GetFieldTypeN())
print("cell9- ColNameToDisplay: ",cell9.GetColNameToDisplay())
print("cell9- DBFieldName: ",cell9.GetDBFieldName())
print("cell9- GetFieldLength: ",cell9.GetFieldLength())
print("cell9- CharNum: ",cell8.GetDBFieldCharacteristicsNumber())
#
print("cell10- FieldTypeName: ",cell10.GetFieldTypeName())
print("cell10- FieldTypeN: ",cell10.GetFieldTypeN())
print("cell10- ColNameToDisplay: ",cell10.GetColNameToDisplay())
print("cell10- DBFieldName: ",cell10.GetDBFieldName())
print("cell10- GetFieldLength: ",cell10.GetFieldLength())
print("cell10- CharNum: ",cell8.GetDBFieldCharacteristicsNumber())
#
print("cell11- FieldTypeName: ",cell11.GetFieldTypeName())
print("cell11- FieldTypeN: ",cell11.GetFieldTypeN())
print("cell11- ColNameToDisplay: ",cell11.GetColNameToDisplay())
print("cell11- DBFieldName: ",cell11.GetDBFieldName())
print("cell11- GetFieldLength: ",cell11.GetFieldLength())
print("cell11- CharNum: ",cell8.GetDBFieldCharacteristicsNumber())
#
row=DataCellRow([1,2,3,['item1', 'item2', 'item3'], 'str1', 'str2', ExtItems1])
row.SetActiveN(4,2)
row.SetActiveN(7,2)
print("row: ",row.ToString())
row.Del(3)
print("row: ",row.ToString())
#
tblHdrs=TableHeaders(DataCell("MyTable", DBTableData), DataCell("Cols", [], DBFieldInfo), DataCell("Lines"))
print("Table Headers: ",tblHdrs.ToString_Corner())
print("Table Name in DB: ",tblHdrs.GetTableNameInDB())
print("Table path: ",tblHdrs.GetDBFileFullName())
#
print("Lines general Header: ",tblHdrs.ToString_LinesGeneralHeader())
print("Lines general Header: DB Field name: ",tblHdrs.GetDBFieldName_LinesGeneralHeader())
print("Lines general Header: DB Field typeN: ",tblHdrs.GetFieldTypeN_LinesGeneralHeader())
print("Lines general Header: DB Field typeName: ",tblHdrs.GetFieldTypeName_LinesGeneralHeader())
#
print("Columns general Header: ",tblHdrs.ToString_ColumnsGeneralHeader())
print("Columns general Header: DB Field name: ",tblHdrs.GetDBFieldName_ColumnsGeneralHeader())
print("Columns general Header: DB Field typeN: ",tblHdrs.GetFieldTypeN_ColumnsGeneralHeader())
print("Columns general Header: DB Field typeName: ",tblHdrs.GetFieldTypeName_ColumnsGeneralHeader())
