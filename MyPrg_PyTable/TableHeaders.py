#from PyStdVector import *
#from MyCellsDiffTypes_NoHeirs_py2 import *
from DataCellSimple import *# refers to from MyStringLib import *
import  MyStringLib# import *


class TableHeaders:
    def __init__(self, TableHeader="", LinesGeneralHeader="", ColumnsGeneralHeader="", vsh=0):
        self.TableHeader=""
        self.LinesGeneralHeader=""
        self.ColumnsGeneralHeader=""
        self.Set(TableHeader, LinesGeneralHeader, ColumnsGeneralHeader, vsh)

    def Set(self, TableHeader="", LinesGeneralHeader="", ColumnsGeneralHeader="", vsh=0):
        if vsh==1:
            print("Set starts working")
        if isinstance(TableHeader, TableHeaders):
            if vsh==1:
                print("First Param is instance of tableHeaders class")
            self.Set(TableHeader.TableHeader, TableHeader.LinesGeneralHeader, TableHeader.ColumnsGeneralHeader)
            #self.SetTableHeader(TableHeader.TableHeader)
            #self.SetLinesGeneralHeader(TableHeader.LinesGeneralHeader)
            #self.SetColumnsGeneralHeader(TableHeader.ColumnsGeneralHeader)
        elif isinstance(TableHeader, str) and LinesGeneralHeader=="" and ColumnsGeneralHeader=="":
            if vsh==1:
                print("First Param is str, 2 other are empty: "+TableHeader)
            TableName=""
            LinesGeneralName=""
            ColumnsGeneralName=""
            TableNames=MyStringLib.ParseTableCorner(TableHeader)
            if vsh==1:
                print("Parsing result: ", TableNames)
            if isinstance(TableNames, list):
                if len(TableNames)==0:
                    if vsh==1:
                        print("Parsing result is empty")
                else:
                    TableName=TableNames[1-1]
                    LinesGeneralName=TableNames[2-1]
                    ColumnsGeneralName=TableNames[3-1]
                    if TableName!="":
                        self.SetTableHeader(DataCell(TableName))
                    if LinesGeneralName!="":
                        self.SetLinesGeneralHeader(DataCell(LinesGeneralName))
                    if ColumnsGeneralName!="":
                        self.SetColumnsGeneralHeader(DataCell(ColumnsGeneralName))
            else:
                if vsh==1:
                    print("Parsing result is not a list")
        else:
            if vsh==1:
                print("General case:")
            self.SetTableHeader(TableHeader)
            self.SetLinesGeneralHeader(LinesGeneralHeader)
            self.SetColumnsGeneralHeader(ColumnsGeneralHeader)
        if vsh==1:
            print("So headers:")
            print("TableHeader: "+self.TableHeader.ToString())
            print("LinesGeneralHeader: "+self.LinesGeneralHeader.ToString())
            print("ColumnsGeneralHeader: "+self.ColumnsGeneralHeader.ToString())
            print("Set finishes working")
        
    def SetTableHeader(self, val1="", val2=[], val3=[], val4=[]):
        if val1=="" and val2==[] and val3==[] and val4==[]:
            self.TableHeader=""
        else:
            self.TableHeader=DataCell(val1, val2, val3, val4)

    def SetLinesGeneralHeader(self, val1="", val2=[], val3=[], val4=[]):
        if val1=="" and val2==[] and val3==[] and val4==[]:
            self.LinesGeneralHeader=""
        else:
            self.LinesGeneralHeader=DataCell(val1, val2, val3, val4)

    def SetColumnsGeneralHeader(self, val1="", val2=[], val3=[], val4=[]):
        if val1=="" and val2==[] and val3==[] and val4==[]:
            self.ColumnsGeneralHeader=""
        else:
            self.ColumnsGeneralHeader=DataCell(val1, val2, val3, val4)
    
    #
    def GetTableHeader(self):
        return self.TableHeader

    def GetLinesGeneralHeader(self):
        return self.LinesGeneralHeader

    def GetColumnsGeneralHeader(self):
        return self.ColumnsGeneralHeader
    #

    def GetTableName(self):
        R=""
        if isinstance(self.TableHeader, DataCell):
            R=self.TableHeader.GetName()
        return R

    def GetLinesGeneralName(self):
        R=""
        if isinstance(self.LinesGeneralHeader, DataCell):
            R=self.LinesGeneralHeader.GetName()
        return R

    def GetColumnsGeneralName(self):
        R=""
        if isinstance(self.ColumnsGeneralHeader, DataCell):
            R=self.ColumnsGeneralHeader.GetName()
        return R

    #
    
    def SetTableName(self, val):
        self.TableHeader.SetName(val)

    def SetLinesGeneralName(self, val):
        self.LinesGeneralHeader.SetName(val)

    def SetColumnsGeneralName(self, val):
        self.ColumnsGeneralHeader.SetName(val)

    def Transpose(self):
        buf=copy.deepcopy(self.LinesGeneralHeader)
        self.LinesGeneralHeader=copy.deepcopy(self.ColumnsGeneralHeader)
        self.ColumnsGeneralHeader=copy.deepcopy(buf)

    #TableHeader-DB

    def GetDBTableDataSuppl(self): #DBTableHdr-1
        R=0
        if isinstance(self.TableHeader, DataCell):
            R=self.TableHeader.GetDBTableDataSuppl()
        return R

    def GetDBTableData(self): #DBTableHdr-2
        R=0
        if isinstance(self.TableHeader, DataCell):
            R=self.TableHeader.GetDBTableData()
        return R
    #
    def GetDBTableNameToDisplay(self): #DBTableHdr-3
        R=0
        if isinstance(self.TableHeader, DataCell):
            R=self.TableHeader.GetDBTableNameToDisplay()
        return R

    def GetTableNameInDB(self): #DBTableHdr-4
        R=0
        if isinstance(self.TableHeader, DataCell):
            R=self.TableHeader.GetTableNameInDB()
        return R

    def GetDBNameInDBCS(self): #DBTableHdr-5
        R=0
        if isinstance(self.TableHeader, DataCell):
            R=self.TableHeader.GetDBNameInDBCS()
        return R

    def GetDBTypeName(self): #DBTableHdr-6
        R=0
        if isinstance(self.TableHeader, DataCell):
            R=self.TableHeader.GetDBTypeName()
        return R

    def GetDBTypeN(self): #DBTableHdr-7
        R=0
        if isinstance(self.TableHeader, DataCell):
            R=self.TableHeader.GetDBTypeN()
        return R

    def GetDBFileFullName(self): #DBTableHdr-8
        R=0
        if isinstance(self.TableHeader, DataCell):
            R=self.TableHeader.GetDBFileFullName()
        return R
    #
    def SetDBTableDataSuppl(self, DBTableDataSuppl):  #DBTableHdr-9
        if isinstance(self.TableHeader, DataCell):
            self.TableHeader.SetDBTableDataSuppl(DBTableDataSuppl)

    def SetDBTableData(self, DBTableData): #DBTableHdr-10
        if isinstance(self.TableHeader, DataCell):
            self.TableHeader.SetDBTableData(DBTableData)
    #
    def SetDBTableNameToDisplay(self, TableNameToDisplay): #DBTableHdr-11
        if isinstance(self.TableHeader, DataCell):
            self.TableHeader.SetDBTableNameToDisplay(TableNameToDisplay)

    def SetDBTableNameInDB(self, DBTableNameInDB): #DBTableHdr-12
        if isinstance(self.TableHeader, DataCell):
            self.TableHeader.SetDBTableNameInDB(DBTableNameInDB)

    def SetDBNameInDBCS(self, DBNameInDBCS): #DBTableHdr-13
        if isinstance(self.TableHeader, DataCell):
            self.TableHeader.SetDBNameInDBCS(DBNameInDBCS)

    def SetDBTypeName(self, DBTypeName): #DBTableHdr-14
        if isinstance(self.TableHeader, DataCell):
            self.TableHeader.SetDBTypeName(DBTypeName)

    def SetDBTypeN(self, DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5): #DBTableHdr-15
        if isinstance(self.TableHeader, DataCell):
            self.TableHeader.SetDBTypeN(DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5)
    
    def SetDBFileFullName(self, name): #DBTableHdr-16
        if isinstance(self.TableHeader, DataCell):
            self.TableHeader.SetDBFileFullName(name)


    #DBField-LGH

    def GetDBFieldInfo_LinesGeneralHeader(self): #ColDBHeaderItems-1
        R=0
        if(isinstance(self.LinesGeneralHeader, DataCell)):
            R=self.self.LinesGeneralHeader.GetDBFieldInfo()
        return R
           
    def GetDBItemsTblInfo_LinesGeneralHeader(self): #ColDBHeaderItems-2
        R=0
        if(isinstance(self.LinesGeneralHeader, DataCell)):
            R=self.self.LinesGeneralHeader.GetDBItemsTblInfo()
        return R
    #
    def SetDBFieldInfo_LinesGeneralHeader(self, DBFldInfo): #ColDBHeaderItems-4
        if(isinstance(self.LinesGeneralHeader, DataCell)):
            R=self.self.LinesGeneralHeader.SetDBFieldInfo()
        return R
    
    def SetDBItemsTblInfo_LinesGeneralHeader(self, DBItemsTblInfo): #ColDBHeaderItems-5
        if isinstance(self.LinesGeneralHeader, DataCell):
            self.LinesGeneralHeader.SetDBItemsTblInfo(DBItemsTblInfo) 
                
    def SetItems_LinesGeneralHeader(self, items):
        if isinstance(self.LinesGeneralHeader, DataCell):
            self.LinesGeneralHeader.SetItems(items)
    #
    #
    def GetColNameToDisplay_LinesGeneralHeader(self): #ColDBHeaderItems-6
        R=0
        if(isinstance(self.LinesGeneralHeader, DataCell)):
            R=self.LinesGeneralHeader.GetColNameToDisplay()
        return R
           
    def GetDBFieldName_LinesGeneralHeader(self): #ColDBHeaderItems-7
        R=0
        if(isinstance(self.LinesGeneralHeader, DataCell)):
            R=self.LinesGeneralHeader.GetDBFieldName()
        return R

    def GetFieldTypeN_LinesGeneralHeader(self): #ColDBHeaderItems-8
        R=0
        if(isinstance(self.LinesGeneralHeader, DataCell)):
            R=self.LinesGeneralHeader.GetFieldTypeN()
        return R

    def GetFieldTypeName_LinesGeneralHeader(self): #ColDBHeaderItems-9
        R=0
        if(isinstance(self.LinesGeneralHeader, DataCell)):
            R=self.LinesGeneralHeader.GetFieldTypeName()
        return R

    def GetFieldLength_LinesGeneralHeader(self): #ColDBHeaderItems-10
        R=0
        if(isinstance(self.LinesGeneralHeader, DataCell)):
            R=self.LinesGeneralHeader.GetFieldLength()
        return R

    def GetDBFieldCharacteristicsNumber_LinesGeneralHeader(self): #ColDBHeaderItems-11
        R=0
        if(isinstance(self.LinesGeneralHeader, DataCell)):
            R=self.LinesGeneralHeader.GetDBFieldCharacteristicsNumber()
        return R

    def GetIfIsKeyField_LinesGeneralHeader(self): #ColDBHeaderItems-12
        R=0
        if(isinstance(self.LinesGeneralHeader, DataCell)):
            R=self.LinesGeneralHeader.GetIfIsKeyField()
        return R

    def GetIfIsCounter_LinesGeneralHeader(self): #ColDBHeaderItems-13
        R=0
        if(isinstance(self.LinesGeneralHeader, DataCell)):
            R=self.LinesGeneralHeader.GetIfIsCounter()
        return R

    def GetIfIsNotNull_LinesGeneralHeader(self): #ColDBHeaderItems-13
        R=0
        if(isinstance(self.LinesGeneralHeader, DataCell)):
            R=self.LinesGeneralHeader.GetIfIsNotNull()
        return R

    def GetIfIsAutoIncrement_LinesGeneralHeader(self): #ColDBHeaderItems-14
        R=0
        if(isinstance(self.LinesGeneralHeader, DataCell)):
            R=self.LinesGeneralHeader.GetIfIsAutoIncrement()
        return R
    #
    def SetColNameToDisplay_LinesGeneralHeader(self, name): #ColDBHeaderItems-15
        if(isinstance(self.LinesGeneralHeader, DataCell)):
            self.LinesGeneralHeader.SetColNameToDisplay(name)
        

    def SetDBFieldName_LinesGeneralHeader(self, name): #ColDBHeaderItems-16
        if(isinstance(self.LinesGeneralHeader, DataCell)):
            self.LinesGeneralHeader.SetDBFieldName(name)

    def SetFieldTypeN_LinesGeneralHeader(self, n): #ColDBHeaderItems-17
        self.cell.SetFieldTypeN(n)

    def SetFieldTypeName_LinesGeneralHeader(self, name): #ColDBHeaderItems-18
        if(isinstance(self.LinesGeneralHeader, DataCell)):
            self.LinesGeneralHeader.SetFieldTypeName(name)

    def SetFieldLength_LinesGeneralHeader(self, n): #ColDBHeaderItems-19
        if(isinstance(self.LinesGeneralHeader, DataCell)):
            self.LinesGeneralHeader.SetFieldLength(n)

    def SetDBFieldCharacteristicsNumber_LinesGeneralHeader(self, CharacteristicsNumber): #ColDBHeaderItems-20
        if(isinstance(self.LinesGeneralHeader, DataCell)):
            self.LinesGeneralHeader.SetDBFieldCharacteristicsNumber(CharacteristicsNumber)

    def SetIfIsKeyField_LinesGeneralHeader(self, isKeyField):  #ColDBHeaderItems-21
        if(isinstance(self.LinesGeneralHeader, DataCell)):
            self.LinesGeneralHeader.SetIfIsKeyField(isKeyField)

    def SetIfIsNotNull_LinesGeneralHeader(self, isNotNull):  #ColDBHeaderItems-22
        if(isinstance(self.LinesGeneralHeader, DataCell)):
            self.LinesGeneralHeader.SetIfIsNotNull(isNotNull)

    def SetIfIsCounter_LinesGeneralHeader(self, isCounter):  #ColDBHeaderItems-22
        if(isinstance(self.LinesGeneralHeader, DataCell)):
            self.LinesGeneralHeader.SetIfIsCounter(isCounter)

    def SetIfIsAutoIncrement_LinesGeneralHeader(self, isAutoIncrement):  #ColDBHeaderItems-23
        if(isinstance(self.LinesGeneralHeader, DataCell)):
            self.LinesGeneralHeader.SetIfIsAutoIncrement(isAutoIncrement)
    #


    #DBField-CoLH

    def GetDBFieldInfo_ColumnsGeneralHeader(self): #ColDBHeaderItems-1
        R=0
        if(isinstance(self.ColumnsGeneralHeader, DataCell)):
            R=self.self.ColumnsGeneralHeader.GetDBFieldInfo()
        return R
           
    def GetDBItemsTblInfo_ColumnsGeneralHeader(self): #ColDBHeaderItems-2
        R=0
        if(isinstance(self.ColumnsGeneralHeader, DataCell)):
            R=self.self.ColumnsGeneralHeader.GetDBItemsTblInfo()
        return R
    #
    def SetDBFieldInfo_ColumnsGeneralHeader(self, DBFldInfo): #ColDBHeaderItems-4
        if(isinstance(self.ColumnsGeneralHeader, DataCell)):
            R=self.self.ColumnsGeneralHeader.SetDBFieldInfo()
        return R
    
    def SetDBItemsTblInfo_ColumnsGeneralHeader(self, DBItemsTblInfo): #ColDBHeaderItems-5
        if isinstance(self.ColumnsGeneralHeader, DataCell):
            self.ColumnsGeneralHeader.SetDBItemsTblInfo(DBItemsTblInfo) 
                
    def SetItems_ColumnsGeneralHeader(self, items):
        if isinstance(self.ColumnsGeneralHeader, DataCell):
            self.ColumnsGeneralHeader.SetItems(items)
    #
    #
    def GetColNameToDisplay_ColumnsGeneralHeader(self): #ColDBHeaderItems-6
        R=0
        if(isinstance(self.ColumnsGeneralHeader, DataCell)):
            R=self.ColumnsGeneralHeader.GetColNameToDisplay()
        return R
           
    def GetDBFieldName_ColumnsGeneralHeader(self): #ColDBHeaderItems-7
        R=0
        if(isinstance(self.ColumnsGeneralHeader, DataCell)):
            R=self.ColumnsGeneralHeader.GetDBFieldName()
        return R

    def GetFieldTypeN_ColumnsGeneralHeader(self): #ColDBHeaderItems-8
        R=0
        if(isinstance(self.ColumnsGeneralHeader, DataCell)):
            R=self.ColumnsGeneralHeader.GetFieldTypeN()
        return R

    def GetFieldTypeName_ColumnsGeneralHeader(self): #ColDBHeaderItems-9
        R=0
        if(isinstance(self.ColumnsGeneralHeader, DataCell)):
            R=self.ColumnsGeneralHeader.GetFieldTypeName()
        return R

    def GetFieldLength_ColumnsGeneralHeader(self): #ColDBHeaderItems-10
        R=0
        if(isinstance(self.ColumnsGeneralHeader, DataCell)):
            R=self.ColumnsGeneralHeader.GetFieldLength()
        return R

    def GetDBFieldCharacteristicsNumber_ColumnsGeneralHeader(self): #ColDBHeaderItems-11
        R=0
        if(isinstance(self.ColumnsGeneralHeader, DataCell)):
            R=self.ColumnsGeneralHeader.GetDBFieldCharacteristicsNumber()
        return R

    def GetIfIsKeyField_ColumnsGeneralHeader(self): #ColDBHeaderItems-12
        R=0
        if(isinstance(self.ColumnsGeneralHeader, DataCell)):
            R=self.ColumnsGeneralHeader.GetIfIsKeyField()
        return R

    def GetIfIsCounter_ColumnsGeneralHeader(self): #ColDBHeaderItems-13
        R=0
        if(isinstance(self.ColumnsGeneralHeader, DataCell)):
            R=self.ColumnsGeneralHeader.GetIfIsCounter()
        return R

    def GetIfIsNotNull_ColumnsGeneralHeader(self): #ColDBHeaderItems-13
        R=0
        if(isinstance(self.ColumnsGeneralHeader, DataCell)):
            R=self.ColumnsGeneralHeader.GetIfIsNotNull()
        return R

    def GetIfIsAutoIncrement_ColumnsGeneralHeader(self): #ColDBHeaderItems-14
        R=0
        if(isinstance(self.ColumnsGeneralHeader, DataCell)):
            R=self.ColumnsGeneralHeader.GetIfIsAutoIncrement()
        return R
    #
    def SetColNameToDisplay_ColumnsGeneralHeader(self, name): #ColDBHeaderItems-15
        if(isinstance(self.ColumnsGeneralHeader, DataCell)):
            self.ColumnsGeneralHeader.SetColNameToDisplay(name)
        

    def SetDBFieldName_ColumnsGeneralHeader(self, name): #ColDBHeaderItems-16
        if(isinstance(self.ColumnsGeneralHeader, DataCell)):
            self.ColumnsGeneralHeader.SetDBFieldName(name)

    def SetFieldTypeN_ColumnsGeneralHeader(self, n): #ColDBHeaderItems-17
        self.cell.SetFieldTypeN(n)

    def SetFieldTypeName_ColumnsGeneralHeader(self, name): #ColDBHeaderItems-18
        if(isinstance(self.ColumnsGeneralHeader, DataCell)):
            self.ColumnsGeneralHeader.SetFieldTypeName(name)

    def SetFieldLength_ColumnsGeneralHeader(self, n): #ColDBHeaderItems-19
        if(isinstance(self.ColumnsGeneralHeader, DataCell)):
            self.ColumnsGeneralHeader.SetFieldLength(n)

    def SetDBFieldCharacteristicsNumber_ColumnsGeneralHeader(self, CharacteristicsNumber): #ColDBHeaderItems-20
        if(isinstance(self.ColumnsGeneralHeader, DataCell)):
            self.ColumnsGeneralHeader.SetDBFieldCharacteristicsNumber(CharacteristicsNumber)

    def SetIfIsKeyField_ColumnsGeneralHeader(self, isKeyField):  #ColDBHeaderItems-21
        if(isinstance(self.ColumnsGeneralHeader, DataCell)):
            self.ColumnsGeneralHeader.SetIfIsKeyField(isKeyField)

    def SetIfIsNotNull_ColumnsGeneralHeader(self, isNotNull):  #ColDBHeaderItems-22
        if(isinstance(self.ColumnsGeneralHeader, DataCell)):
            self.ColumnsGeneralHeader.SetIfIsNotNull(isNotNull)

    def SetIfIsCounter_ColumnsGeneralHeader(self, isCounter):  #ColDBHeaderItems-22
        if(isinstance(self.ColumnsGeneralHeader, DataCell)):
            self.ColumnsGeneralHeader.SetIfIsCounter(isCounter)

    def SetIfIsAutoIncrement_ColumnsGeneralHeader(self, isAutoIncrement):  #ColDBHeaderItems-23
        if(isinstance(self.ColumnsGeneralHeader, DataCell)):
            self.ColumnsGeneralHeader.SetIfIsAutoIncrement(isAutoIncrement)

    #
    def ToString_LinesGeneralHeader(self, sBef="", sAft=""):
        s=""
        if isinstance(self.LinesGeneralHeader, DataCell):
            s=self.LinesGeneralHeader.ToString(sBef, sAft)
        return s

    def ToString_ColumnsGeneralHeader(self, sBef="", sAft=""):
        s=""
        if isinstance(self.ColumnsGeneralHeader, DataCell):
            s=self.ColumnsGeneralHeader.ToString(sBef, sAft)
        return s

    def ToString_TableHeader(self, sBef="", sAft=""):
        s=""
        if isinstance(self.TableHeader, DataCell):
            s=self.TableHeader.ToString(sBef, sAft)
        return s

    def ToString_Corner(self, sBefLoCH="", sAftLoCH="", sBefCoLH="", sAftCoLH=""):
        s=""
        sLGH=self.ToString_LinesGeneralHeader(sBefLoCH, sAftLoCH)
        sCGH=self.ToString_ColumnsGeneralHeader(sBefCoLH, sAftCoLH)
        if sLGH!="":
            s=s+sLGH
            if sLGH!="":
                s=s+"\\"
        if sCGH!="":
            s=s+sCGH
        return s

