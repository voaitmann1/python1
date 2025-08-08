#from PyStdVector import *
from PyStdVector2 import *
from MyCellsDiffTypes_NoHeirs_py2 import *
from TableHeaders import *

class TableController:

    # Main part (1) ------------------------------------------------------------------------------------------------------------------
    
    def __init__(self, content=[], LineOfColHeader=[], ColOfLineHeader=[], TableHeaders=[], LC_1_CL_0=1):
        self.content=My2DArray1()
        self.LineOfColHeader=My2DArray1()
        self.LineOfColHeader=My2DArray1()
        self.Headers=TableHeaders()
        self.LC_1_CL_0=1
        #
        self.Set(content, LineOfColHeader, ColOfLineHeader, TableHeaders= LC_1_CL_0)
#   #
    def Set(self, content, LineOfColHeader=[], ColOfLineHeader=[], TableHeaders=[], LC_1_CL_0=1):
        self.SetContent( content)
        self.SetLineOfColHeadert(LineOfColHeader)
        self.SetColOfLineHeader(ColOfLineHeader)
        self.SetTableHeaders(TableHeaders)
        self.LC_1_CL_0=LC_1_CL_0
    #
    def SetContent(self, contentExt):
        content=copy.deepcopy(contentExt)
        self.content.Set(content)
        self.content.Stretch()
    def SetLineOfColHeader(self, LineOfColHeader):
        self.LineOfColHeader.Set(LineOfColHeader)
    def SetColOfLineHeader(self, ColOfLineHeader):
        self.ColOfLineHeader.Set(ColOfLineHeader)
    def SetTableHeaders(self, TableHeaders):
        self.Headers.Set(TableHeaders)
    def DetStructure(self, LC_1_CL_0):
        if self.LC_1_CL_0!=LC_1_CL_0:
            self.content.Transpose()
            self.LC_1_CL_0=LC_1_CL_0
    #
    def SetCell(self, dataExt, LineN=1, ColN=1):
        if self.LC_1_CL_0==1:
            ExtRowN=LineN
            IneRowN=ColN
        else:
            ExtRowN=ColN
            IneRowN=LineN
        data=DataCell()
        if isinstance(dataExt, DataCell):
            data.cell=copy.deepcopy(dataExt.cell)
        else:
            data(dataExt.cell)
        self.content.SetElement(ExtRowN, IneRowN)
    #
    def GetQExtRows(self):
        return self.content.GetLength()
    #
    def GetQIneRows(self):
        return self.content.GetLengthN()#default N=1
    #
    def GetQLines(self):
        if self.LC_1_CL_0==1:
            QLines=self.GetQExtRows()
            QColumns=self.GetQIneRows()
        else:
            QColumns=self.GetQExtRows()
            QLines=self.GetQIneRows()
        return QLines
    #
    def GetQColumns(self):
        if self.LC_1_CL_0==1:
            QLines=self.GetQExtRows()
            QColumns=self.GetQIneRows()
        else:
            QColumns=self.GetQExtRows()
            QLines=self.GetQIneRows()
        return QColumns
    #
    def GetCell(self, LineN=1, ColN=1):
        #
        if self.LC_1_CL_0==1:
            QLines=self.GetQExtRows()
            QColumns=self.GetQIneRows()
            ExtRowN=LineN
            IneRowN=ColN
        else:
            QColumns=self.GetQExtRows()
            QLines=self.GetQIneRows()
            IneRowN=LineN
            ExtRowN=ColN
        if LineN>=1 and LineN<=QLines and ColN>=1 and ColN<=QColumns:
            cell=self.content[ExtRowN][IneRowN]
        else:
            cell=0
        return cell
    #
    #TableHeaders (2) ----------------------------------------------------------------------------------------------------------------------
    
    def Set(self, TableHeader="", LinesGeneralHeader="", ColumnsGeneralHeader=""):
        if isinstance(obj, TableHeaders):
            self.Set(obj.TableHeader, obj.LinesGeneralHeader, obj.ColumnsGeneralHeader)
        else:
            self.SetTableHeader(TableHeader)
            self.SetLinesGeneralHeader(LinesGeneralHeader)
            self.SetColumnsGeneralHeader(ColumnsGeneralHeader)
        
    def SetTableHeader(self, val):
        if isinstance(val, DataCell):
            self.TableHeader=copy.deepcopy(val)
        else:
            self.TableHeader=DataCell(val)

    def SetLinesGeneralHeader(self, val):
        if isinstance(val, DataCell):
            self.LinesGeneralHeader=copy.deepcopy(val)
        else:
            self.LinesGeneralHeader=DataCell(val)

    def SetColumnsGeneralHeader(self, val):
        if isinstance(val, DataCell):
            self.ColumnsGeneralHeader=copy.deepcopy(val)
        else:
            self.ColumnsGeneralHeader=DataCell(val)
    
    #
    def GetTableHeader(self):
        return self.TableHeader

    def GetLinesGeneralHeader(self, val):
        return self.LinesGeneralHeader

    def GetColumnsGeneralHeader(self, val):
        return self.LinesGeneralHeader
    #

    def GetTableName(self):
        return self.TableHeader.GetName()

    def GetLinesGeneralName(self):
        return self.LinesGeneralHeader.GetName()

    def GetColumnsGeneralName(self):
        return self.ColumnsGeneralHeader.GetName()

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

    def GetDBTableNameToDisplay(self): #DBTableHdr-3
        R=0
        if isinstance(self.TableHeader, DataCell):
            R=self.TableHeader.GetDBTableNameToDisplay()
        return R

    def GetDBTableNameInDB(self): #DBTableHdr-4
        R=0
        if isinstance(self.TableHeader, DataCell):
            R=self.TableHeader.GetDBTableNameInDB()
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
           
    def GetDBFieldNameToDisplay_LinesGeneralHeader(self): #ColDBHeaderItems-7
        R=0
        if(isinstance(self.LinesGeneralHeader, DataCell)):
            R=self.LinesGeneralHeader.GetDBFieldNameToDisplay()
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

    #DBField-CGH

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
           
    def GetDBFieldNameToDisplay_ColumnsGeneralHeader(self): #ColDBHeaderItems-7
        R=0
        if(isinstance(self.ColumnsGeneralHeader, DataCell)):
            R=self.ColumnsGeneralHeader.GetDBFieldNameToDisplay()
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
        
    #LineOfColHeader (3) (3.1) --------------------------------------------------------------------------------------------------------------------

    def GetIfLineOfColHeaderExists(self):
        R=0
        if isinstance(self.LineOfColHeader, My1DArray) and self.LineOfColHeader.GetLength>0:
            R=1
        elif isinstance(self.LineOfColHeader, list) and len(self.LineOfColHeader)>0:
            R=1
        return R

    
    #LineOfColHeader cells (3.2) --------------------------------------------------------------------------------------------------------------
    
    def Set_Simple_Cell_LineOfColHeader(self, CellN, val): #1-11-1
        cell=DataCell(val)
        QColumns=self.GetQColumns()
        if self.GetIfLineOfColHeaderExists()==1 and CellN>=1 and CellN<=QColumns:
            if isinstance(self.LineOfColHeader, My1DArray):
                self.LineOfColHeader.SetElement(CellN, cell)
            elif isinstance(self.LineOfColHeader, list):
                self.LineOfColHeader[CellN-1]=copy.deepcopy(cell)
        
    def Set_ComboboxOrMemo_Cell_LineOfColHeader(self, CellN, ActiveN, items):  #1-11-2
        cell=DataCell_ComboboxOrMemo(ActiveN, items)
        if self.GetIfLineOfColHeaderExists()==1 and CellN>=1 and CellN<=QColumns:
            if isinstance(self.LineOfColHeader, My1DArray):
                self.LineOfColHeader.SetElement(CellN, cell)
            elif isinstance(self.LineOfColHeader, list):
                self.LineOfColHeader[CellN-1]=copy.deepcopy(cell)
                
    def Set_DBTableHeader_Cell_LineOfColHeader(self, CellN, name="", DBTableData=[]):  #1-11-3
        self.cell=DataCell_DBTableHeader(name, DBTableData)
        if self.GetIfLineOfColHeaderExists()==1 and CellN>=1 and CellN<=QColumns:
            if isinstance(self.LineOfColHeader, My1DArray):
                self.LineOfColHeader.SetElement(CellN, cell)
            elif isinstance(self.LineOfColHeader, list):
                self.LineOfColHeader[CellN-1]=copy.deepcopy(cell)
                
    def Set_ColHdr_DBFldOrItems_Cell_LineOfColHeader(self, CellN, data="", items=[], DBFldInfo=[], DBItemsTblInfo=[):  #1-11-3
        self.cell=DataCell_ColHeader_DBFieldOrItems()
        self.cell.Set(var1, var2, var3)

    def Set_Cell_LineOfColHeader(self, CellN,  var1, var2=[], var3=[], var4=[]): #11
        if var2==[] and var3=[] and var4==[]:
            self. Set_Simple(var1)
        elif isinstance(var1, int) and isinstance(var2, list) and var3==[] and var4==[]:
            self.Set_ComboboxOrMemo(var1, var2)
        elif isinstance(var2, TDBTableData):
            self.Set_DBTableHeader(var1, var2)
        elif isinstance(var3, TDBFieldInfo):
            self.Set_ColHdr_DBFldOrItems(var1, var2, var3, var4)
        elif isinstance(var2, TDBFieldInfo): #why not - DB Field without items
            self.Set_ColHdr_DBFldOrItems(var1, var3, var2, var4)
        else:
            if isinstance(var1, DataCell):
                self.cell=copy.deepcopy(var.cell)
            elif isinstance(var1, DataCell_Simple) or isinstance(var1, DataCell_ComboboxOrMemo) or isinstance(var1, DataCell_DBTableHeader) or isinstance(var1, DataCell_ColHeader_DBFieldOrItems):
                self.cell=copy.deepcopy(var1)
            elif isinstance(var1, float) or isinstance(var1, int) or isinstance(var1, str):
                self. Set_Simple(var1)
            else:
                self. Set_Simple(0)
    #
    def GetType_Cell_LineOfColHeader(self, CellN): #2
         return self.cell.GetType()
    
    def GetVal_Cell_LineOfColHeader(self, CellN, N=1): #3
        return self.cell.GetVal(self, N)

    def GetItem_Cell_LineOfColHeader(self, CellN, N=1): #4
        return self.cell.GetItem(self, N)

    # ConcrType
    def GetFloatVal_Cell_LineOfColHeader(self, CellN): #5
        return float(self.cell.GetFloatVal())

    def GetIntVal_Cell_LineOfColHeader(self, CellN): #6
        return int(self.cell.GetIntVal())

    def GetBoolVal_Cell_LineOfColHeader(self, CellN): #7
        return bool(self.cell.GetBoolVal())

    def GetStrVal_Cell_LineOfColHeader(self, CellN): #8
        return str(self.cell.GetStrVal())

    # for combobox
    def GetActiveN_Cell_LineOfColHeader(self, CellN): #for combobox-1
        return self.cell.GetActiveN()

    def GetActiveItem_Cell_LineOfColHeader(self, CellN): #for combobox-2
        return self.cell.GetActiveItem()
    
    def SetActive_Cell_LineOfColHeaderN(self, CellN, val): #for combobox-3
         self.cell.SetActiveN(val)
        #
    def SetActiveNByVa_Cell_LineOfColHeaderl(self, CellN, val): #for combobox-4
        self.cell.SetActiveNByVal(val)
        #
    def GetQItem_Cell_LineOfColHeaders(self, CellN): #for combobox-5
        return self.cell.GetQItems()

    def GetQName_Cell_LineOfColHeaders(self, CellN): # for database-0
         return self.cell.GetQNames()

    # for database
    def GetName(self, N=1): # for database-1
        return self.cell.GetName(N)

    def SetName_Cell_LineOfColHeader(selfself, CellN, names, N=0): # for database-2
        self.cell.SetName(names, N)
        
    def SetItem_Cell_LineOfColHeader(self, CellN, items, N=0): # for database-3
        self.cell.SetItem(items, N)

    #
    def Set_Cell_LineOfColHeader(self, CellN, var1=[], var2=[], var3=[], var4=[]): #11
        if isinstance(self.LineOfColHeader, My1DArray):
            L=self.LineOfColHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=DataCell(var1, var2, var3, var4)
                self.LineOfColHeader.SetCell(CellN, cell)
        elif isinstance(self.LineOfColHeader, list):
            L=len(self.LineOfColHeader)>0
            if CellN>=1 and CellN<=L:
                cell=DataCell(var1, var2, var3, var4)
                self.LineOfColHeader[CellN-1]=cell
    #
    #
    #SetName - above
    #
    # functions of DB FieldHeaderOrItems
    #
    def GetDBFieldInfo_Cell_LineOfColHeader(self, CellN): #ColDBHeaderItems-1
        R=0
        cell=[]
        if isinstance(self.LineOfColHeader, My1DArray):
            L=self.LineOfColHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=LineOfColHeader.GetElement_AsLink(CellN)
        elif isinstance(self.LineOfColHeader, list):
            L=len(self.LineOfColHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.LineOfColHeader[CellN-1]
        #
        if isinstance(cell, DataCell):
            R=cell.GetDBFieldInfo()
        return R
           
    def GetDBItemsTblInfo_Cell_LineOfColHeader(self, CellN): #ColDBHeaderItems-2
        R=0
        cell=[]
        if isinstance(self.LineOfColHeader, My1DArray):
            L=self.LineOfColHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=LineOfColHeader.GetElement_AsLink(CellN)
        elif isinstance(self.LineOfColHeader, list):
            L=len(self.LineOfColHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.LineOfColHeader[CellN-1]
        #
        if isinstance(cell, DataCell):
            R=cell.GetDBItemsTblInfo()
        return R
    #
    def SetDBFieldInfo_Cell_LineOfColHeader(self, CellN, DBFldInfo): #ColDBHeaderItems-4
        if isinstance(self.LineOfColHeader, My1DArray):
            cell=[]
            L=self.LineOfColHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=LineOfColHeader.GetElement_AsLink(CellN)
                cell.SetDBFieldInfo(DBFldInfo)
        elif isinstance(self.LineOfColHeader, list):
            L=len(self.LineOfColHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.LineOfColHeader[CellN-1].SetDBFieldInfo(DBFldInfo)
            
    def SetDBItemsTblInfo_Cell_LineOfColHeader(self, CellN, DBItemsTblInfo): #ColDBHeaderItems-5
        if isinstance(self.LineOfColHeader, My1DArray):
            cell=[]
            L=self.LineOfColHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=LineOfColHeader.GetElement_AsLink(CellN)
                cell.SetDBItemsTblInfo(DBItemsTblInfo)
        elif isinstance(self.LineOfColHeader, list):
            L=len(self.LineOfColHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.LineOfColHeader[CellN-1].SetDBItemsTblInfo(DBItemsTblInfo) 
                
    # def SetItems - united in SetItem below
    #
    #
    def GetColNameToDisplay_Cell_LineOfColHeader(self, CellN): #ColDBHeaderItems-6
        R=0
        cell=[]
        if isinstance(self.LineOfColHeader, My1DArray):
            L=self.LineOfColHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=LineOfColHeader.GetElement_AsLink(CellN)
        elif isinstance(self.LineOfColHeader, list):
            L=len(self.LineOfColHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.LineOfColHeader[CellN-1]
        #
        if isinstance(cell, DataCell):
            R=cell.GetColNameToDisplay()
        return R
           
    def GetDBFieldName_Cell_LineOfColHeader(self, CellN): #ColDBHeaderItems-7#was: to display - must be: in dB table
        R=0
        cell=[]
        if isinstance(self.LineOfColHeader, My1DArray):
            L=self.LineOfColHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=LineOfColHeader.GetElement_AsLink(CellN)
        elif isinstance(self.LineOfColHeader, list):
            L=len(self.LineOfColHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.LineOfColHeader[CellN-1]
        #
        if isinstance(cell, DataCell):
            R=cell.GetDBFieldName()
        return R

    def GetFieldTypeN_Cell_LineOfColHeader(self, CellN): #ColDBHeaderItems-8
        R=0
        cell=[]
        if isinstance(self.LineOfColHeader, My1DArray):
            L=self.LineOfColHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=LineOfColHeader.GetElement_AsLink(CellN)
        elif isinstance(self.LineOfColHeader, list):
            L=len(self.LineOfColHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.LineOfColHeader[CellN-1]
        #
        if isinstance(cell, DataCell):
            R=cell.GetFieldTypeN()
        return R

    def GetFieldTypeName_Cell_LineOfColHeader(self, CellN): #ColDBHeaderItems-9
        R=0
        cell=[]
        if isinstance(self.LineOfColHeader, My1DArray):
            L=self.LineOfColHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=LineOfColHeader.GetElement_AsLink(CellN)
        elif isinstance(self.LineOfColHeader, list):
            L=len(self.LineOfColHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.LineOfColHeader[CellN-1]
        #
        if isinstance(cell, DataCell):
            R=cell.GetFieldTypeName()
        return R

    def GetFieldLength_Cell_LineOfColHeader(self, CellN): #ColDBHeaderItems-10
        R=0
        cell=[]
        if isinstance(self.LineOfColHeader, My1DArray):
            L=self.LineOfColHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=LineOfColHeader.GetElement_AsLink(CellN)
        elif isinstance(self.LineOfColHeader, list):
            L=len(self.LineOfColHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.LineOfColHeader[CellN-1]
        #
        if isinstance(cell, DataCell):
            R=cell.GetFieldLength()
        return R

    def GetDBFieldCharacteristicsNumber_Cell_LineOfColHeader(self, CellN): #ColDBHeaderItems-11
        R=0
        cell=[]
        if isinstance(self.LineOfColHeader, My1DArray):
            L=self.LineOfColHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=LineOfColHeader.GetElement_AsLink(CellN)
        elif isinstance(self.LineOfColHeader, list):
            L=len(self.LineOfColHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.LineOfColHeader[CellN-1]
        #
        if isinstance(cell, DataCell):
            R=cell.GetDBFieldCharacteristicsNumber()
        return R

    def GetIfIsKeyField_Cell_LineOfColHeader(self, CellN): #ColDBHeaderItems-12
        R=0
        cell=[]
        if isinstance(self.LineOfColHeader, My1DArray):
            L=self.LineOfColHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=LineOfColHeader.GetElement_AsLink(CellN)
        elif isinstance(self.LineOfColHeader, list):
            L=len(self.LineOfColHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.LineOfColHeader[CellN-1]
        #
        if isinstance(cell, DataCell):
            R=cell.GetIfIsKeyField()
        return R

    def GetIfIsCounter_Cell_LineOfColHeader(self, CellN): #ColDBHeaderItems-13
        R=0
        cell=[]
        if isinstance(self.LineOfColHeader, My1DArray):
            L=self.LineOfColHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=LineOfColHeader.GetElement_AsLink(CellN)
        elif isinstance(self.LineOfColHeader, list):
            L=len(self.LineOfColHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.LineOfColHeader[CellN-1]
        #
        if isinstance(cell, DataCell):
            R=cell.GetIfIsCounter()
        return R

    def GetIfIsNotNull_Cell_LineOfColHeader(self, CellN): #ColDBHeaderItems-13
        R=0
        cell=[]
        if isinstance(self.LineOfColHeader, My1DArray):
            L=self.LineOfColHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=LineOfColHeader.GetElement_AsLink(CellN)
        elif isinstance(self.LineOfColHeader, list):
            L=len(self.LineOfColHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.LineOfColHeader[CellN-1]
        #
        if isinstance(cell, DataCell):
            R=cell.GetIfIsNotNull()
        return R

     def GetIfIsAutoIncrement_Cell_LineOfColHeader(self, CellN): #ColDBHeaderItems-14
        R=0
        cell=[]
        if isinstance(self.LineOfColHeader, My1DArray):
            L=self.LineOfColHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=LineOfColHeader.GetElement_AsLink(CellN)
        elif isinstance(self.LineOfColHeader, list):
            L=len(self.LineOfColHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.LineOfColHeader[CellN-1]
        #
        if isinstance(cell, DataCell):
            R=cell.GetIfIsAutoIncrement()
        return R
    #
    def SetColNameToDisplay_Cell_LineOfColHeader(self, CellN, name): #ColDBHeaderItems-15
        if isinstance(self.LineOfColHeader, My1DArray):
            cell=[]
            L=self.LineOfColHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=LineOfColHeader.GetElement_AsLink(CellN)
                cell.SetColNameToDisplay(name)
        elif isinstance(self.LineOfColHeader, list):
            L=len(self.LineOfColHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.LineOfColHeader[CellN-1].SetColNameToDisplay(name)

    def SetDBFieldName_Cell_LineOfColHeader(self, CellN, name): #ColDBHeaderItems-16
        if isinstance(self.LineOfColHeader, My1DArray):
            cell=[]
            L=self.LineOfColHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=LineOfColHeader.GetElement_AsLink(CellN)
                cell.SetDBFieldName(name)
        elif isinstance(self.LineOfColHeader, list):
            L=len(self.LineOfColHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.LineOfColHeader[CellN-1].SetDBFieldName(name)

    def SetFieldTypeN_Cell_LineOfColHeader(self, CellN, n): #ColDBHeaderItems-17
        if isinstance(self.LineOfColHeader, My1DArray):
            cell=[]
            L=self.LineOfColHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=LineOfColHeader.GetElement_AsLink(CellN)
                cell.SetFieldTypeN(n)
        elif isinstance(self.LineOfColHeader, list):
            L=len(self.LineOfColHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.LineOfColHeader[CellN-1].SetFieldTypeN(n)

    def SetFieldTypeName_Cell_LineOfColHeader(self, CellN, name): #ColDBHeaderItems-18
        if isinstance(self.LineOfColHeader, My1DArray):
            cell=[]
            L=self.LineOfColHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=LineOfColHeader.GetElement_AsLink(CellN)
                cell.SetFieldTypeName(name)
        elif isinstance(self.LineOfColHeader, list):
            L=len(self.LineOfColHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.LineOfColHeader[CellN-1].SetFieldTypeName(name)

    def SetFieldLength_Cell_LineOfColHeader(self, CellN, n): #ColDBHeaderItems-19
        if isinstance(self.LineOfColHeader, My1DArray):
            cell=[]
            L=self.LineOfColHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=LineOfColHeader.GetElement_AsLink(CellN)
                cell.SetFieldLength(n)
        elif isinstance(self.LineOfColHeader, list):
            L=len(self.LineOfColHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.LineOfColHeader[CellN-1].SetFieldLength(n)

    def SetDBFieldCharacteristicsNumber_Cell_LineOfColHeader(self, CellN, CharacteristicsNumber): #ColDBHeaderItems-20
        if isinstance(self.LineOfColHeader, My1DArray):
            cell=[]
            L=self.LineOfColHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=LineOfColHeader.GetElement_AsLink(CellN)
                cell.SetDBFieldCharacteristicsNumber(CharacteristicsNumber)
        elif isinstance(self.LineOfColHeader, list):
            L=len(self.LineOfColHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.LineOfColHeader[CellN-1].SetDBFieldCharacteristicsNumber(CharacteristicsNumber)
    
    def SetIfIsKeyField_Cell_LineOfColHeader(self, CellN, isKeyField):  #ColDBHeaderItems-21
        if isinstance(self.LineOfColHeader, My1DArray):
            cell=[]
            L=self.LineOfColHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=LineOfColHeader.GetElement_AsLink(CellN)
                cell.SetIfIsKeyField(isKeyField)
        elif isinstance(self.LineOfColHeader, list):
            L=len(self.LineOfColHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.LineOfColHeader[CellN-1].SetIfIsKeyField(isKeyField)
        
    def SetIfIsNotNull_Cell_LineOfColHeader(self, CellN, isNotNull):  #ColDBHeaderItems-22
        if isinstance(self.LineOfColHeader, My1DArray):
            cell=[]
            L=self.LineOfColHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=LineOfColHeader.GetElement_AsLink(CellN)
                cell.SetIfIsNotNull(isNotNull)
        elif isinstance(self.LineOfColHeader, list):
            L=len(self.LineOfColHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.LineOfColHeader[CellN-1].SetIfIsNotNull(isNotNull)

    def SetIfIsCounter_Cell_LineOfColHeader(self, CellN, isCounter):  #ColDBHeaderItems-22
        if isinstance(self.LineOfColHeader, My1DArray):
            cell=[]
            L=self.LineOfColHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=LineOfColHeader.GetElement_AsLink(CellN)
                cell.SetIfIsCounter(isCounter)
        elif isinstance(self.LineOfColHeader, list):
            L=len(self.LineOfColHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.LineOfColHeader[CellN-1].SetIfIsCounter(isCounter)

    def SetIfIsAutoIncrement_Cell_LineOfColHeader(self, CellN, isAutoIncrement):  #ColDBHeaderItems-23
        if isinstance(self.LineOfColHeader, My1DArray):
            cell=[]
            L=self.LineOfColHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=LineOfColHeader.GetElement_AsLink(CellN)
                cell.SetIfIsCounter(isCounter)
        elif isinstance(self.LineOfColHeader, list):
            L=len(self.LineOfColHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.LineOfColHeader[CellN-1].SetIfIsAutoIncrement(isAutoIncrement)

    ##
    ## functions of DBTableHeader
    ##
    #def GetDBTableDataSupp_Cell_LineOfColHeaderl(self, CellN): #DBTableHdr-1
    #    return self.cell.GetDBTableDataSuppl()
    #
    #def GetDBTableDat_Cell_LineOfColHeadera(self, CellN): #DBTableHdr-2
    #    return self.cell.GetDBTableData()
    #
    #def GetDBTableNameToDispla_Cell_LineOfColHeadery(self, CellN): #DBTableHdr-3
    #    return self.cell.GetDBTableNameToDisplay()
    #
    #def GetDBTableNameInDB_Cell_LineOfColHeader(self, CellN): #DBTableHdr-4
    #     return self.cell.GetDBTableNameInDB()
    #
    #def GetDBNameInDBC_Cell_LineOfColHeaderS(self, CellN): #DBTableHdr-5
    #    return self.cell.GetDBNameInDBCS()
    #
    #def GetDBTypeNam_Cell_LineOfColHeadere(self, CellN): #DBTableHdr-6
    #    return self.cell.GetDBTypeName()
    #
    #def GetDBTypeN_Cell_LineOfColHeader(self, CellN): #DBTableHdr-7
    #    return self.cell.GetDBTypeN()
    #
    #def GetDBFileFullName_Cell_LineOfColHeader(self, CellN): #DBTableHdr-8
    #    return self.cell.GetDBFileFullName()
    ##
    #def SetDBTableDataSupp_Cell_LineOfColHeaderl(self, CellN, DBTableDataSuppl):  #DBTableHdr-9
    #    self.cell.SetDBTableDataSuppl(DBTableDataSuppl)
    #
    #def SetDBTableData_Cell_LineOfColHeader(self, CellN, DBTableData): #DBTableHdr-10
    #    self.cell.SetDBTableData(DBTableData)
    #
    #def SetDBTableNameToDispla_Cell_LineOfColHeadery(self, CellN, TableNameToDisplay): #DBTableHdr-11
    #    self.cell.SetDBTableNameToDisplay(TableNameToDisplay)
    #
    #def SetDBTableNameInDB_Cell_LineOfColHeader(self, CellN, DBTableNameInDB): #DBTableHdr-12
    #    self.cell.SetDBTableNameInDB(DBTableNameInDB)
    #
    #def SetDBNameInDBC_Cell_LineOfColHeaderS(self, DBNameInDBCS): #DBTableHdr-13
    #    self.cell.SetDBNameInDBCS(DBNameInDBCS)
    #
    #def SetDBTypeName_Cell_LineOfColHeader(self, DBTypeName): #DBTableHdr-14
    #    self.cell.SetDBTypeName(DBTypeName)
    #
    #def SetDBTypeN_Cell_LineOfColHeader(self, DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5): #DBTableHdr-15
    #    self.cell.SetDBTypeN(DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5)
    #
    #def SetDBFileFullNam_Cell_LineOfColHeadere(self, name): #DBTableHdr-16
    #    self.cell.SetDBFileFullName(name)
    ##    
    ##   
    #def ToString_Cell_LineOfColHeader(self, str_bef="", str_aft=""):  # represent-1
    #    #return "cell id="+str(id(self))+" content: "+str(self.GetName())+" "
    #    return str_bef+str(self.GetName())+str_aft
    #
    #def ToString_Info_Cell_LineOfColHeader(self):  # represent-3
    #    return "DataCell Type="+str(self.GetTypeN())+" id="+str(id(self))+" val="+str(self.GetVal())

    #ColOfLineHeader (4) (4.1) --------------------------------------------------------------------------------------------------------------------

    def GetIfColOfLineHeaderExists(self):
        R=0
        if isinstance(self.ColOfLineHeader, My1DArray) and self.ColOfLineHeader.GetLength>0:
            R=1
        elif if isinstance(self.ColOfLineHeader, list) and len(self.ColOfLineHeader)>0:
            R=1
        return R

    #ColOfLineHeader cells (4.2) --------------------------------------------------------------------------------------------------------------
    
    def Set_Simple_Cell_ColOfLineHeader(self, CellN, var1): #1-11-1
        cell=DataCell(var1)
        QColumns=self.GetQColumns()
        if self.GetIfColOfLineHeaderExists()==1 and CellN>=1 and CellN<=QColumns:
            self.
        
    def Set_ComboboxOrMemo_Cell_ColOfLineHeader(self, CellN, var1, var2):  #1-11-2
        self.cell=DataCell_ComboboxOrMemo()
        self.cell.Set(var1, var2)
    def Set_DBTableHeader_Cell_ColOfLineHeader(self, CellN, var1, var2, var3):  #1-11-3
        self.cell=DataCell_DBTableHeader()
        self.cell.Set(var1, var2, var3)
    def Set_ColHdr_DBFldOrItems_Cell_ColOfLineHeader(self, CellN,  var1, var2=[], var3=[], var4=[]):  #1-11-3
        self.cell=DataCell_ColHeader_DBFieldOrItems()
        self.cell.Set(var1, var2, var3)

    def Set_Cell_ColOfLineHeader(self, CellN, var1, var2=[], var3=[], var4=[]): #11
        if var2==[] and var3=[] and var4==[]:
            self. Set_Simple(var1)
        elif isinstance(var1, int) and isinstance(var2, list) and var3==[] and var4==[]:
            self.Set_ComboboxOrMemo(var1, var2)
        elif isinstance(var2, TDBTableData):
            self.Set_DBTableHeader(var1, var2)
        elif isinstance(var3, TDBFieldInfo):
            self.Set_ColHdr_DBFldOrItems(var1, var2, var3, var4)
        elif isinstance(var2, TDBFieldInfo): #why not - DB Field without items
            self.Set_ColHdr_DBFldOrItems(var1, var3, var2, var4)
        else:
            if isinstance(var1, DataCell):
                self.cell=copy.deepcopy(var.cell)
            elif isinstance(var1, DataCell_Simple) or isinstance(var1, DataCell_ComboboxOrMemo) or isinstance(var1, DataCell_DBTableHeader) or isinstance(var1, DataCell_ColHeader_DBFieldOrItems):
                self.cell=copy.deepcopy(var1)
            elif isinstance(var1, float) or isinstance(var1, int) or isinstance(var1, str):
                self. Set_Simple(var1)
            else:
                self. Set_Simple(0)
    #
    def GetType_Cell_ColOfLineHeader(self, CellN): #2
         return self.cell.GetType()
    
    def GetVal_Cell_ColOfLineHeader(self, CellN, N=1): #3
        return self.cell.GetVal(self, N)

    def GetItem_Cell_ColOfLineHeader(self, CellN, N=1): #4
        return self.cell.GetItem(self, N)

    # ConcrType
    def GetFloatVal_Cell_ColOfLineHeader(self, CellN): #5
        return float(self.cell.GetFloatVal())

    def GetIntVal_Cell_ColOfLineHeader(self, CellN): #6
        return int(self.cell.GetIntVal())

    def GetBoolVal_Cell_ColOfLineHeader(self, CellN): #7
        return bool(self.cell.GetBoolVal())

    def GetStrVal_Cell_ColOfLineHeader(self, CellN): #8
        return str(self.cell.GetStrVal())

    # for combobox
    def GetActiveN_Cell_ColOfLineHeader(self, CellN): #for combobox-1
        return self.cell.GetActiveN()

    def GetActiveItem_Cell_ColOfLineHeader(self, CellN): #for combobox-2
        return self.cell.GetActiveItem()
    
    def SetActive_Cell_ColOfLineHeaderN(self, CellN, val): #for combobox-3
         self.cell.SetActiveN(val)
        #
    def SetActiveNByVa_Cell_ColOfLineHeaderl(self, CellN, val): #for combobox-4
        self.cell.SetActiveNByVal(val)
        #
    def GetQItem_Cell_ColOfLineHeaders(self, CellN): #for combobox-5
        return self.cell.GetQItems()

    def GetQName_Cell_ColOfLineHeaders(self, CellN): # for database-0
         return self.cell.GetQNames()

    # for database
    def GetName(self, N=1): # for database-1
        return self.cell.GetName(N)

    def SetName_Cell_ColOfLineHeader(selfself, CellN, names, N=0): # for database-2
        self.cell.SetName(names, N)
        
    def SetItem_Cell_ColOfLineHeader(self, CellN, items, N=0): # for database-3
        self.cell.SetItem(items, N)

    #
    def Set_Cell_ColOfLineHeader(self, CellN, var1=[], var2=[], var3=[], var4=[]): #11
        if isinstance(self.ColOfLineHeader, My1DArray):
            L=self.ColOfLineHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=DataCell(var1, var2, var3, var4)
                self.ColOfLineHeader.SetCell(CellN, cell)
        elif isinstance(self.ColOfLineHeader, list):
            L=len(self.ColOfLineHeader)>0
            if CellN>=1 and CellN<=L:
                cell=DataCell(var1, var2, var3, var4)
                self.ColOfLineHeader[CellN-1]=cell
    #
    #
    #SetName - above
    #
    # functions of DB FieldHeaderOrItems
    #
    def GetDBFieldInfo_Cell_ColOfLineHeader(self, CellN): #ColDBHeaderItems-1
        R=0
        cell=[]
        if isinstance(self.ColOfLineHeader, My1DArray):
            L=self.ColOfLineHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=ColOfLineHeader.GetElement_AsLink(CellN)
        elif isinstance(self.ColOfLineHeader, list):
            L=len(self.ColOfLineHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.ColOfLineHeader[CellN-1]
        #
        if isinstance(cell, DataCell):
            R=cell.GetDBFieldInfo()
        return R
           
    def GetDBItemsTblInfo_Cell_ColOfLineHeader(self, CellN): #ColDBHeaderItems-2
        R=0
        cell=[]
        if isinstance(self.ColOfLineHeader, My1DArray):
            L=self.ColOfLineHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=ColOfLineHeader.GetElement_AsLink(CellN)
        elif isinstance(self.ColOfLineHeader, list):
            L=len(self.ColOfLineHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.ColOfLineHeader[CellN-1]
        #
        if isinstance(cell, DataCell):
            R=cell.GetDBItemsTblInfo()
        return R
    #
    def SetDBFieldInfo_Cell_ColOfLineHeader(self, CellN, DBFldInfo): #ColDBHeaderItems-4
        if isinstance(self.ColOfLineHeader, My1DArray):
            cell=[]
            L=self.ColOfLineHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=ColOfLineHeader.GetElement_AsLink(CellN)
                cell.SetDBFieldInfo(DBFldInfo)
        elif isinstance(self.ColOfLineHeader, list):
            L=len(self.ColOfLineHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.ColOfLineHeader[CellN-1].SetDBFieldInfo(DBFldInfo)
            
    def SetDBItemsTblInfo_Cell_ColOfLineHeader(self, CellN, DBItemsTblInfo): #ColDBHeaderItems-5
        if isinstance(self.ColOfLineHeader, My1DArray):
            cell=[]
            L=self.ColOfLineHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=ColOfLineHeader.GetElement_AsLink(CellN)
                cell.SetDBItemsTblInfo(DBItemsTblInfo)
        elif isinstance(self.ColOfLineHeader, list):
            L=len(self.ColOfLineHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.ColOfLineHeader[CellN-1].SetDBItemsTblInfo(DBItemsTblInfo) 
                
    # def SetItems - united in SetItem below
    #
    #
    def GetColNameToDisplay_Cell_ColOfLineHeader(self, CellN): #ColDBHeaderItems-6
        R=0
        cell=[]
        if isinstance(self.ColOfLineHeader, My1DArray):
            L=self.ColOfLineHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=ColOfLineHeader.GetElement_AsLink(CellN)
        elif isinstance(self.ColOfLineHeader, list):
            L=len(self.ColOfLineHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.ColOfLineHeader[CellN-1]
        #
        if isinstance(cell, DataCell):
            R=cell.GetColNameToDisplay()
        return R
           
    def GetDBFieldName_Cell_ColOfLineHeader(self, CellN): #ColDBHeaderItems-7#was: to display - must be: in dB table
        R=0
        cell=[]
        if isinstance(self.ColOfLineHeader, My1DArray):
            L=self.ColOfLineHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=ColOfLineHeader.GetElement_AsLink(CellN)
        elif isinstance(self.ColOfLineHeader, list):
            L=len(self.ColOfLineHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.ColOfLineHeader[CellN-1]
        #
        if isinstance(cell, DataCell):
            R=cell.GetDBFieldName()
        return R

    def GetFieldTypeN_Cell_ColOfLineHeader(self, CellN): #ColDBHeaderItems-8
        R=0
        cell=[]
        if isinstance(self.ColOfLineHeader, My1DArray):
            L=self.ColOfLineHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=ColOfLineHeader.GetElement_AsLink(CellN)
        elif isinstance(self.ColOfLineHeader, list):
            L=len(self.ColOfLineHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.ColOfLineHeader[CellN-1]
        #
        if isinstance(cell, DataCell):
            R=cell.GetFieldTypeN()
        return R

    def GetFieldTypeName_Cell_ColOfLineHeader(self, CellN): #ColDBHeaderItems-9
        R=0
        cell=[]
        if isinstance(self.ColOfLineHeader, My1DArray):
            L=self.ColOfLineHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=ColOfLineHeader.GetElement_AsLink(CellN)
        elif isinstance(self.ColOfLineHeader, list):
            L=len(self.ColOfLineHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.ColOfLineHeader[CellN-1]
        #
        if isinstance(cell, DataCell):
            R=cell.GetFieldTypeName()
        return R

    def GetFieldLength_Cell_ColOfLineHeader(self, CellN): #ColDBHeaderItems-10
        R=0
        cell=[]
        if isinstance(self.ColOfLineHeader, My1DArray):
            L=self.ColOfLineHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=ColOfLineHeader.GetElement_AsLink(CellN)
        elif isinstance(self.ColOfLineHeader, list):
            L=len(self.ColOfLineHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.ColOfLineHeader[CellN-1]
        #
        if isinstance(cell, DataCell):
            R=cell.GetFieldLength()
        return R

    def GetDBFieldCharacteristicsNumber_Cell_ColOfLineHeader(self, CellN): #ColDBHeaderItems-11
        R=0
        cell=[]
        if isinstance(self.ColOfLineHeader, My1DArray):
            L=self.ColOfLineHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=ColOfLineHeader.GetElement_AsLink(CellN)
        elif isinstance(self.ColOfLineHeader, list):
            L=len(self.ColOfLineHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.ColOfLineHeader[CellN-1]
        #
        if isinstance(cell, DataCell):
            R=cell.GetDBFieldCharacteristicsNumber()
        return R

    def GetIfIsKeyField_Cell_ColOfLineHeader(self, CellN): #ColDBHeaderItems-12
        R=0
        cell=[]
        if isinstance(self.ColOfLineHeader, My1DArray):
            L=self.ColOfLineHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=ColOfLineHeader.GetElement_AsLink(CellN)
        elif isinstance(self.ColOfLineHeader, list):
            L=len(self.ColOfLineHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.ColOfLineHeader[CellN-1]
        #
        if isinstance(cell, DataCell):
            R=cell.GetIfIsKeyField()
        return R

    def GetIfIsCounter_Cell_ColOfLineHeader(self, CellN): #ColDBHeaderItems-13
        R=0
        cell=[]
        if isinstance(self.ColOfLineHeader, My1DArray):
            L=self.ColOfLineHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=ColOfLineHeader.GetElement_AsLink(CellN)
        elif isinstance(self.ColOfLineHeader, list):
            L=len(self.ColOfLineHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.ColOfLineHeader[CellN-1]
        #
        if isinstance(cell, DataCell):
            R=cell.GetIfIsCounter()
        return R

    def GetIfIsNotNull_Cell_ColOfLineHeader(self, CellN): #ColDBHeaderItems-13
        R=0
        cell=[]
        if isinstance(self.ColOfLineHeader, My1DArray):
            L=self.ColOfLineHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=ColOfLineHeader.GetElement_AsLink(CellN)
        elif isinstance(self.ColOfLineHeader, list):
            L=len(self.ColOfLineHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.ColOfLineHeader[CellN-1]
        #
        if isinstance(cell, DataCell):
            R=cell.GetIfIsNotNull()
        return R

     def GetIfIsAutoIncrement_Cell_ColOfLineHeader(self, CellN): #ColDBHeaderItems-14
        R=0
        cell=[]
        if isinstance(self.ColOfLineHeader, My1DArray):
            L=self.ColOfLineHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=ColOfLineHeader.GetElement_AsLink(CellN)
        elif isinstance(self.ColOfLineHeader, list):
            L=len(self.ColOfLineHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.ColOfLineHeader[CellN-1]
        #
        if isinstance(cell, DataCell):
            R=cell.GetIfIsAutoIncrement()
        return R
    #
    def SetColNameToDisplay_Cell_ColOfLineHeader(self, CellN, name): #ColDBHeaderItems-15
        if isinstance(self.ColOfLineHeader, My1DArray):
            cell=[]
            L=self.ColOfLineHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=ColOfLineHeader.GetElement_AsLink(CellN)
                cell.SetColNameToDisplay(name)
        elif isinstance(self.ColOfLineHeader, list):
            L=len(self.ColOfLineHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.ColOfLineHeader[CellN-1].SetColNameToDisplay(name)

    def SetDBFieldName_Cell_ColOfLineHeader(self, CellN, name): #ColDBHeaderItems-16
        if isinstance(self.ColOfLineHeader, My1DArray):
            cell=[]
            L=self.ColOfLineHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=ColOfLineHeader.GetElement_AsLink(CellN)
                cell.SetDBFieldName(name)
        elif isinstance(self.ColOfLineHeader, list):
            L=len(self.ColOfLineHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.ColOfLineHeader[CellN-1].SetDBFieldName(name)

    def SetFieldTypeN_Cell_ColOfLineHeader(self, CellN, n): #ColDBHeaderItems-17
        if isinstance(self.ColOfLineHeader, My1DArray):
            cell=[]
            L=self.ColOfLineHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=ColOfLineHeader.GetElement_AsLink(CellN)
                cell.SetFieldTypeN(n)
        elif isinstance(self.ColOfLineHeader, list):
            L=len(self.ColOfLineHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.ColOfLineHeader[CellN-1].SetFieldTypeN(n)

    def SetFieldTypeName_Cell_ColOfLineHeader(self, CellN, name): #ColDBHeaderItems-18
        if isinstance(self.ColOfLineHeader, My1DArray):
            cell=[]
            L=self.ColOfLineHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=ColOfLineHeader.GetElement_AsLink(CellN)
                cell.SetFieldTypeName(name)
        elif isinstance(self.ColOfLineHeader, list):
            L=len(self.ColOfLineHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.ColOfLineHeader[CellN-1].SetFieldTypeName(name)

    def SetFieldLength_Cell_ColOfLineHeader(self, CellN, n): #ColDBHeaderItems-19
        if isinstance(self.ColOfLineHeader, My1DArray):
            cell=[]
            L=self.ColOfLineHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=ColOfLineHeader.GetElement_AsLink(CellN)
                cell.SetFieldLength(n)
        elif isinstance(self.ColOfLineHeader, list):
            L=len(self.ColOfLineHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.ColOfLineHeader[CellN-1].SetFieldLength(n)

    def SetDBFieldCharacteristicsNumber_Cell_ColOfLineHeader(self, CellN, CharacteristicsNumber): #ColDBHeaderItems-20
        if isinstance(self.ColOfLineHeader, My1DArray):
            cell=[]
            L=self.ColOfLineHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=ColOfLineHeader.GetElement_AsLink(CellN)
                cell.SetDBFieldCharacteristicsNumber(CharacteristicsNumber)
        elif isinstance(self.ColOfLineHeader, list):
            L=len(self.ColOfLineHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.ColOfLineHeader[CellN-1].SetDBFieldCharacteristicsNumber(CharacteristicsNumber)
    
    def SetIfIsKeyField_Cell_ColOfLineHeader(self, CellN, isKeyField):  #ColDBHeaderItems-21
        if isinstance(self.ColOfLineHeader, My1DArray):
            cell=[]
            L=self.ColOfLineHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=ColOfLineHeader.GetElement_AsLink(CellN)
                cell.SetIfIsKeyField(isKeyField)
        elif isinstance(self.ColOfLineHeader, list):
            L=len(self.ColOfLineHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.ColOfLineHeader[CellN-1].SetIfIsKeyField(isKeyField)
        
    def SetIfIsNotNull_Cell_ColOfLineHeader(self, CellN, isNotNull):  #ColDBHeaderItems-22
        if isinstance(self.ColOfLineHeader, My1DArray):
            cell=[]
            L=self.ColOfLineHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=ColOfLineHeader.GetElement_AsLink(CellN)
                cell.SetIfIsNotNull(isNotNull)
        elif isinstance(self.ColOfLineHeader, list):
            L=len(self.ColOfLineHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.ColOfLineHeader[CellN-1].SetIfIsNotNull(isNotNull)

    def SetIfIsCounter_Cell_ColOfLineHeader(self, CellN, isCounter):  #ColDBHeaderItems-22
        if isinstance(self.ColOfLineHeader, My1DArray):
            cell=[]
            L=self.ColOfLineHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=ColOfLineHeader.GetElement_AsLink(CellN)
                cell.SetIfIsCounter(isCounter)
        elif isinstance(self.ColOfLineHeader, list):
            L=len(self.ColOfLineHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.ColOfLineHeader[CellN-1].SetIfIsCounter(isCounter)

    def SetIfIsAutoIncrement_Cell_ColOfLineHeader(self, CellN, isAutoIncrement):  #ColDBHeaderItems-23
        if isinstance(self.ColOfLineHeader, My1DArray):
            cell=[]
            L=self.ColOfLineHeader.GetLength()
            if CellN>=1 and CellN<=L:
                cell=ColOfLineHeader.GetElement_AsLink(CellN)
                cell.SetIfIsCounter(isCounter)
        elif isinstance(self.ColOfLineHeader, list):
            L=len(self.ColOfLineHeader)>0
            if CellN>=1 and CellN<=L:
                cell=self.ColOfLineHeader[CellN-1].SetIfIsAutoIncrement(isAutoIncrement)
        self.cell.SetIfIsAutoIncrement(isAutoIncrement)
        
    #Content cells (5) ---------------------------------------------------------------------------------------------------------------------

    def Set_Cell_Simple_ExtIne(self, ExtRowN, IneRowN, var1): #1-11-1
        
        cell=self.GetCell_AsLink(LineN, ColN)
        self.cell=DataCell(var1)
        #self.cell.Set(var1)
    def Set_Cell_ComboboxOrMemo_ExtIne(self, LineN, ColN, var1, var2):  #1-11-2
        self.cell=DataCell_ComboboxOrMemo()
        self.cell.Set(var1, var2)
    #def Set_DBTableHeader(self,var1, var2, var3):  #1-11-3
    #    self.cell=DataCell_DBTableHeader()
    #    self.cell.Set(var1, var2, var3)
    #def Set_ColHdr_DBFldOrItems(self, var1, var2=[], var3=[], var4=[]):  #1-11-3
    #    self.cell=DataCell_ColHeader_DBFieldOrItems()
    #    self.cell.Set(var1, var2, var3)

    def Set_Cell_ExtIne(self, ExtRowN, IneRowN, var1, var2=[], var3=[], var4=[]): #11
        if var2==[] and var3=[] and var4==[]:
            cell=
            self.Set_Simple(var1)
        elif isinstance(var1, int) and isinstance(var2, list) and var3==[] and var4==[]:
            self.Set_ComboboxOrMemo(var1, var2)
        elif isinstance(var2, TDBTableData):
            self.Set_DBTableHeader(var1, var2)
        elif isinstance(var3, TDBFieldInfo):
            self.Set_ColHdr_DBFldOrItems(var1, var2, var3, var4)
        elif isinstance(var2, TDBFieldInfo): #why not - DB Field without items
            self.Set_ColHdr_DBFldOrItems(var1, var3, var2, var4)
        else:
            if isinstance(var1, DataCell):
                self.cell=copy.deepcopy(var.cell)
            elif isinstance(var1, DataCell_Simple) or isinstance(var1, DataCell_ComboboxOrMemo) or isinstance(var1, DataCell_DBTableHeader) or isinstance(var1, DataCell_ColHeader_DBFieldOrItems):
                self.cell=copy.deepcopy(var1)
            elif isinstance(var1, float) or isinstance(var1, int) or isinstance(var1, str):
                self. Set_Simple(var1)
            else:
                self. Set_Simple(0)
    #
    def GetType_ExtIne(self, ExtRowN, IneRowN): #2
         return self.cell.GetType()
    
    def GetVal_ExtIne(self, ExtRowN, IneRowN, N=1): #3
        return self.cell.GetVal(self, N)

    def GetItem_ExtIne(self, ExtRowN, IneRowN, N=1): #4
        return self.cell.GetItem(self, N)

    # ConcrType
    def GetFloatVal_ExtIne(self, ExtRowN, IneRowN): #5
        return float(self.cell.GetFloatVal())

    def GetIntVal_ExtIne(self, ExtRowN, IneRowN): #6
        return int(self.cell.GetIntVal())

    def GetBoolVal_ExtIne(self, ExtRowN, IneRowN): #7
        return bool(self.cell.GetBoolVal())

    def GetStrVal_ExtIne(self, ExtRowN, IneRowN): #8
        return str(self.cell.GetStrVal())

    # for combobox
    def GetActiveN_ExtIne(self, ExtRowN, IneRowN): #for combobox-1
        return self.cell.GetActiveN()

    def GetActiveItem_ExtIne(self, ExtRowN, IneRowN): #for combobox-2
        return self.cell.GetActiveItem()
    
    def SetActiveN_ExtIne(self, ExtRowN, IneRowN, val): #for combobox-3
         self.cell.SetActiveN(val)
        #
    def SetActiveNByVal_ExtIne(self, ExtRowN, IneRowN, val): #for combobox-4
        self.cell.SetActiveNByVal(val)
        #
    def GetQItems_ExtIne(self, ExtRowN, IneRowN): #for combobox-5
        return self.cell.GetQItems()

    def GetQNames_ExtIne(self, ExtRowN, IneRowN): # for database-0
         return self.cell.GetQNames()

    # for database
    def GetName_ExtIne(self, ExtRowN, IneRowN, N=1): # for database-1
        return self.cell.GetName(N)

    def SetName_ExtIne(self, ExtRowN, IneRowN, names, N=0): # for database-2
        self.cell.SetName(names, N)
        
    def SetItem_ExtIne(self, ExtRowN, IneRowN, items, N=0): # for database-3
        self.cell.SetItem(items, N)
    #
    #
    #
    def Set_Cell_Simple(self, LineN, ColN, var1): #1-11-1
        self.cell=DataCell_Simple()
        self.cell.Set(var1)
    def Set_Cell_ComboboxOrMemo(self, LineN, ColN, var1, var2):  #1-11-2
        self.cell=DataCell_ComboboxOrMemo()
        self.cell.Set(var1, var2)
    #def Set_DBTableHeader(self,var1, var2, var3):  #1-11-3
    #    self.cell=DataCell_DBTableHeader()
    #    self.cell.Set(var1, var2, var3)
    #def Set_ColHdr_DBFldOrItems(self, var1, var2=[], var3=[], var4=[]):  #1-11-3
    #    self.cell=DataCell_ColHeader_DBFieldOrItems()
    #    self.cell.Set(var1, var2, var3)

    def Set_Cell(self, LineN, ColN, var1, var2=[], var3=[], var4=[]): #11
        if var2==[] and var3=[] and var4==[]:
            self. Set_Simple(var1)
        elif isinstance(var1, int) and isinstance(var2, list) and var3==[] and var4==[]:
            self.Set_ComboboxOrMemo(var1, var2)
        elif isinstance(var2, TDBTableData):
            self.Set_DBTableHeader(var1, var2)
        elif isinstance(var3, TDBFieldInfo):
            self.Set_ColHdr_DBFldOrItems(var1, var2, var3, var4)
        elif isinstance(var2, TDBFieldInfo): #why not - DB Field without items
            self.Set_ColHdr_DBFldOrItems(var1, var3, var2, var4)
        else:
            if isinstance(var1, DataCell):
                self.cell=copy.deepcopy(var.cell)
            elif isinstance(var1, DataCell_Simple) or isinstance(var1, DataCell_ComboboxOrMemo) or isinstance(var1, DataCell_DBTableHeader) or isinstance(var1, DataCell_ColHeader_DBFieldOrItems):
                self.cell=copy.deepcopy(var1)
            elif isinstance(var1, float) or isinstance(var1, int) or isinstance(var1, str):
                self. Set_Simple(var1)
            else:
                self. Set_Simple(0)
    #
    def GetType(self, LineN, ColN, ): #2
         return self.cell.GetType()
    
    def GetVal(self, N=1): #3
        return self.cell.GetVal(self, N)

    def GetItem(self, LineN, ColN, N=1): #4
        return self.cell.GetItem(self, N)

    # ConcrType
    def GetFloatVal(self, LineN, ColN): #5
        return float(self.cell.GetFloatVal())

    def GetIntVal(self, LineN, ColN): #6
        return int(self.cell.GetIntVal())

    def GetBoolVal(self, LineN, ColN): #7
        return bool(self.cell.GetBoolVal())

    def GetStrVal(self, LineN, ColN): #8
        return str(self.cell.GetStrVal())

    # for combobox
    def GetActiveN(self, LineN, ColN): #for combobox-1
        return self.cell.GetActiveN()

    def GetActiveItem(self, LineN, ColN): #for combobox-2
        return self.cell.GetActiveItem()
    
    def SetActiveN(self, LineN, ColN, val): #for combobox-3
         self.cell.SetActiveN(val)
        #
    def SetActiveNByVal(self, LineN, ColN, val): #for combobox-4
        self.cell.SetActiveNByVal(val)
        #
    def GetQItems(self, LineN, ColN): #for combobox-5
        return self.cell.GetQItems()

    def GetQNames(self, LineN, ColN): # for database-0
         return self.cell.GetQNames()

    # for database
    def GetName(self, LineN, ColN, N=1): # for database-1
        return self.cell.GetName(N)

    def SetName(self, LineN, ColN, names, N=0): # for database-2
        self.cell.SetName(names, N)
        
    def SetItem(self, LineN, ColN, items, N=0): # for database-3
        self.cell.SetItem(items, N)

    #
    #
    #
    #SetName - above
    #
    # functions of DB FieldHeaderOrItems
    #
    #def GetDBFieldInfo(self): #ColDBHeaderItems-1
    #    return self.cell.GetDBFieldInfo()
           
    #def GetDBItemsTblInfo(self): #ColDBHeaderItems-2
    #    return self.cell.GetDBItemsTblInfo()
    #
    #def SetDBFieldInfo(self, DBFldInfo): #ColDBHeaderItems-4
    #    self.cell.SetDBFieldInfo(DBFldInfo)
    
    #def SetDBItemsTblInfo(self, DBItemsTblInfo): #ColDBHeaderItems-5
    #    self.cell.SetDBItemsTblInfo(DBItemsTblInfo) 
                
    # def SetItems - united in SetItem below
    #
    #
    #def GetColNameToDisplay(self): #ColDBHeaderItems-6
    #    return self.cell.GetColNameToDisplay()
           
    #def GetDBFieldNameToDisplay(self): #ColDBHeaderItems-7
    #    return self.cell.GetDBFieldNameToDisplay()

    #def GetFieldTypeN(self): #ColDBHeaderItems-8
    #    return self.cell.GetFieldTypeN()

    #def GetFieldTypeName(self): #ColDBHeaderItems-9
    #    return self.cell.GetFieldTypeName()

    #def GetFieldLength(self): #ColDBHeaderItems-10
    #    return self.cell.GetFieldLength()

    #def GetDBFieldCharacteristicsNumber(self): #ColDBHeaderItems-11
    #    return self.cell.GetDBFieldCharacteristicsNumber()

    #def GetIfIsKeyField(self): #ColDBHeaderItems-12
    #    return self.cell.GetIfIsKeyField()

    #def GetIfIsCounter(self): #ColDBHeaderItems-13
    #    return self.cell.GetIfIsCounter()

    #def GetIfIsNotNull(self): #ColDBHeaderItems-13
    #    return self.cell.GetIfIsNotNull()

    #def GetIfIsAutoIncrement(self): #ColDBHeaderItems-14
    #    return self.cell.GetIfIsAutoIncrement()
    #
    #def SetColNameToDisplay(self, name): #ColDBHeaderItems-15
    #    self.cell.SetColNameToDisplay(name)

    #def SetDBFieldName(self, name): #ColDBHeaderItems-16
    #    self.cell.SetDBFieldName(name)

    #def SetFieldTypeN(self, n): #ColDBHeaderItems-17
    #    self.cell.SetFieldTypeN(n)

    #def SetFieldTypeName(self, name): #ColDBHeaderItems-18
    #    self.cell.SetFieldTypeName(name)

    #def SetFieldLength(self, n): #ColDBHeaderItems-19
    #    self.cell.SetFieldLength(n)

    #def SetDBFieldCharacteristicsNumber(self, CharacteristicsNumber): #ColDBHeaderItems-20
    #    self.cell.SetDBFieldCharacteristicsNumber(CharacteristicsNumber)

    #def SetIfIsKeyField(self, isKeyField):  #ColDBHeaderItems-21
    #    self.cell.SetIfIsKeyField(isKeyField)

    #def SetIfIsNotNull(self, isNotNull):  #ColDBHeaderItems-22
    #    self.cell.SetIfIsCounter(isNotNull)

    #def SetIfIsCounter(self, isCounter):  #ColDBHeaderItems-22
    #    self.cell.SetIfIsCounter(isCounter)

    #def SetIfIsAutoIncrement(self, isAutoIncrement):  #ColDBHeaderItems-23
    #    self.cell.SetIfIsAutoIncrement(isAutoIncrement)
    #
    # functions of DBTableHeader
    #
    #def GetDBTableDataSuppl(self): #DBTableHdr-1
    #    return self.cell.GetDBTableDataSuppl()

    #def GetDBTableData(self): #DBTableHdr-2
    #    return self.cell.GetDBTableData()

    #def GetDBTableNameToDisplay(self): #DBTableHdr-3
    #    return self.cell.GetDBTableNameToDisplay()

    #def GetDBTableNameInDB(self): #DBTableHdr-4
    #    return self.cell.GetDBTableNameInDB()

    #def GetDBNameInDBCS(self): #DBTableHdr-5
    #    return self.cell.GetDBNameInDBCS()

    #def GetDBTypeName(self): #DBTableHdr-6
    #    return self.cell.GetDBTypeName()

    #def GetDBTypeN(self): #DBTableHdr-7
    #    return self.cell.GetDBTypeN()

    #def GetDBFileFullName(self): #DBTableHdr-8
    #    return self.cell.GetDBFileFullName()
    #
    #def SetDBTableDataSuppl(self, DBTableDataSuppl):  #DBTableHdr-9
    #    self.cell.SetDBTableDataSuppl(DBTableDataSuppl)

    #def SetDBTableData(self, DBTableData): #DBTableHdr-10
    #    self.cell.SetDBTableData(DBTableData)

    #def SetDBTableNameToDisplay(self, TableNameToDisplay): #DBTableHdr-11
    #    self.cell.SetDBTableNameToDisplay(TableNameToDisplay)

    #def SetDBTableNameInDB(self, DBTableNameInDB): #DBTableHdr-12
    #    self.cell.SetDBTableNameInDB(DBTableNameInDB)

    #def SetDBNameInDBCS(self, DBNameInDBCS): #DBTableHdr-13
    #    self.cell.SetDBNameInDBCS(DBNameInDBCS)

    #def SetDBTypeName(self, DBTypeName): #DBTableHdr-14
    #    self.cell.SetDBTypeName(DBTypeName)

    #def SetDBTypeN(self, DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5): #DBTableHdr-15
    #    self.cell.SetDBTypeN(DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5)
    
    #def SetDBFileFullName(self, name): #DBTableHdr-16
    #    self.cell.SetDBFileFullName(name)
    #    
    #   
    def ToString(self, str_bef="", str_aft=""):  # represent-1
        #return "cell id="+str(id(self))+" content: "+str(self.GetName())+" "
        return str_bef+str(self.GetName())+str_aft

    def __str__(): #represent-2
        return str(self.GetName()
        
    def ToString_Info(self):  # represent-3
        return "DataCell Type="+str(self.GetTypeN())+" id="+str(id(self))+" val="+str(self.GetVal())

.
    #My2DArray1 & My1DArray (6) (6.1)------------------------------------------------------------------------------------------------------------

    def SetExtRow(self, N, ExtRow, RowHdr=[]):
        pass

    def SetIneRow(self, N, ExtRow, RowHdr=[]):
        pass

    def SetLine(self, N, ExtLine, LineHdr=[]):
        pass

    def SetColumn(self, N, ExtCol, ColHdr=[]):
        pass

    def SetCell_Content_ExtIne(self, cellExt, ExtRowN, IneRowN):
        cell=copy.deepcopy(cellExt)
        if ExtRowN>=1 and IneRowN>=1:
            if isinstance(self.content, My2DArray1) and ExtRowN<=self.content.Getlength() and IneRowN<=self.content.GetMinLength():
                self.content.SetElement(cellExt, ExtRowN, IneRowN)
            if isinstance(self.content, list):
                if isinstance(self.content[ExtRowN-1], list) and ExtRowN<=len(self.content) and IneRowN<=len(self.content[ExtRowN-1]):
                    self.content[ExtRowN-1][IneRowN-1]=copy.deepcopy(cell)
                                                
    def SetCell_Content(self, N, cellExt, LineN, ColN):
        if self.LC_1_CL_0==1:
            ExtRowN=LineN
            IneRowN=ColN
        else:
            ExtRowN=ColN
            IneRowN=LineN
        self.SetCell_Content_ExtIne(cellExt, ExtRowN, IneRowN)

    def SetCell_LineOfColHeader(self, cellExt, ColN):
        cell=copy.deepcopy(cellExt)
        if self.GetIfLineOfColHeaderExists()==1 and ColN>=1:
            if isinstance(self.LineOfColHeader, My1DArray) and ColN<=self.LineOfColHeader.GetLength():
                self.LineOfColHeader.SetElement(cell, ColN, 1)
            elif isinstance(self.LineOfColHeader, list) and ColN<=len(self.LineOfColHeader):
                self.LineOfColHeader[ColN-1]=copy.deepcopy(cell)

    def SetCell_ColOfLineHeader(self, cellExt, LineN):
        cell=copy.deepcopy(cellExt)
        if self.GetIfColOfLineHeaderExists()==1 and LineN>=1:
            if isinstance(self.ColOfLineHeader, My1DArray) and LineN<=self.ColOfLineHeader.GetLength():
                self.ColOfLineHeader.SetElement(cell, LineN, 1)
            elif isinstance(self.ColOfLineHeader, list) and LineN<=len(self.ColOfLineHeader):
                self.ColOfLineHeader[LineN-1]=copy.deepcopy(cell)
    
    def Transpose(self):
        if isinstance(self.content):
            self.content.Transpose()
        elif isinstance(self.content, list):
            self.
        #
        if self.GetIfColOfLineHeaderExists()==1:
            
            
        
    # My1DArray: (6.2) -----------------------------------------------------------------------------------------------------------------------
    
    def GetCell_Content_ExtIne(self, ExtRowN=1, IneRowN=1, AsLink0Copy1=0):
        cell=[]
        if AsLink0Copy1==0 :
            cell=self.GetCell_Content_ExtIne_AsLink(ExtRowN, IneRowN)
        else:
            cell=self.GetCell_Content_ExtIne_AsCopy(ExtRowN, IneRowN)
        return cell

    def GetCell_Content_ExtIne_AsLink(self, ExtRowN=1, IneRowN=1):
        cell=[]
        if isinstance(self.content, My2DFArray1):
            cell=self.content.GetElement_AsLink(ExtRowN, IneRowN)
        elif isinstance(self.content, list):
            cell=self.content[ExtRowN-1][IneRowN-1]
        return cell

    def GetCell_Content_ExtIne_AsCopy(self, ExtRowN=1, IneRowN=1):
        cell=[]
        if isinstance(self.content, My2DFArray1):
            cell=copy.deepcopy(self.content.GetElement_AsLink(ExtRowN, IneRowN))
        elif isinstance(self.content, list):
            cell=copy.deepcopy(self.content[ExtRowN-1][IneRowN-1])
        return cell

    #def GetCell_RowHdr_Ext(self, ExtRowN):
    #    pass

    #def GetCell_RowHdr_Ine(self, ExtRowN):
    #    pass

    def GetCell(self, LineN=1, ColN=1, AsLink0Copy1=0):
        cell=[]
        if self.LC_1_CL_0==1:
            ExtRowN=LineN
            IneRowN=ColN
        else:
            ExtRowN=ColN
            IneRowN=LineN
        cell=self.GetCell_Content_ExtIne(ExtRowN, IneRowN, AsLink0Copy1)
        return cell

    def GetCell_AsLink(self, LineN=1, ColN=1):
        cell=[]
        if self.LC_1_CL_0==1:
            ExtRowN=LineN
            IneRowN=ColN
        else:
            ExtRowN=ColN
            IneRowN=LineN
        cell=self.GetCell_Content_ExtIne_AsLink(ExtRowN, IneRowN)
        return cell

    def GetCell_AsCopy(self, LineN=1, ColN=1):
        cell=[]
        if self.LC_1_CL_0==1:
            ExtRowN=LineN
            IneRowN=ColN
        else:
            ExtRowN=ColN
            IneRowN=LineN
        cell=self.GetCell_Content_ExtIne_AsCopy(ExtRowN, IneRowN)
        return cell

    def GetCell_LineOfColHeader(self, ColN=1, AsLink0Copy1=0):
        cell=[]
        if ColN>=1 and ColN<=self.LineOfColHeader.GetLength():
            if AsLink0Copy1==0:
                cell=self.GetCell_LineOfColHeader_AsLink(ColN)
            else:
                cell=self.GetCell_LineOfColHeader_AsCopy(ColN)
        return cell

    def GetCell_LineOfColHeader_AsLink(self, ColN):
        cell=[]
        if isinstance(self.LineOfColHeader, My1DArray):
            if ColN>=1 and ColN<=self.LineOfColHeader.GetLength():
                cell=self.LineOfColHeader.GetElement_AsLink(ColN)
        elif isinstance(self.LineOfColHeader, list):
            if ColN>=1 and ColN<=self.LineOfColHeader.GetLength():
                cell=self.LineOfColHeader[ColN-1]
        return cell

    def GetCell_LineOfColHeader_AsCopy(self, ColN):
        cell=[]
        if isinstance(self.LineOfColHeader, My1DArray):
            if ColN>=1 and ColN<=self.LineOfColHeader.GetLength():
                cell=self._LineOfColHeader.GetElement_Copy(ColN)
        elif isinstance(self.LineOfColHeader, list):
            if ColN>=1 and ColN<=self.LineOfColHeader.GetLength():
                cell=copy.deepcopy(self.LineOfColHeader[ColN-1])
        return cell

    def GetCell_ColOfLineHeader(self, LineN=1, AsLink0Copy1=0):
        cell=[]
        if LineN>=1 and LineN<=self.ColOfLineHeader.GetLength():
            if AsLink0Copy1==0:
                cell=self.GetCell_ColOfLineHeader_AsLink(LineN)
            else:
                cell=self.GetCell_ColOfLineHeader_AsCopy(LineN)
        return cell

    def GetCell_ColOfLineHeader_AsLink(self, LineN):
        cell=[]
        if isinstance(self.ColOfLineHeader, My1DArray):
            if LineN>=1 and LineN<=self.ColOfLineHeader.GetLength():
                cell=self.ColOfLineHeader.GetElement_AsLink(LineN)
        elif isinstance(self.ColOfLineHeader, list):
            if LineN>=1 and LineN<=self.ColOfLineHeader.GetLength():
                cell=self.ColOfLineHeader[LineN-1]
        return cell

    def GetCell_ColOfLineHeader_AsCopy(self, LineN):
        cell=[]
        if isinstance(self.ColOfLineHeader, My1DArray):
            if LineN>=1 and LineN<=self.ColOfLineHeader.GetLength():
                cell=self._ColOfLineHeader.GetElement_Copy(LineN)
        elif isinstance(self.ColOfLineHeader, list):
            if LineN>=1 and LineN<=self.ColOfLineHeader.GetLength():
                cell=copy.deepcopy(self.ColOfLineHeader[LineN-1])
        return cell

    #

    def GetExtRow(self, ExtRowN):
        row=[]
        if isinstance(self.content, My2DArray1):
            row=self.content.GetExtRowN_usual(ExtRowN)
        elif isinstance(self.content, list):
            row=self.content[ExtRowN-1])
        DcRow=DataCellRow1(row)
        return DcRow
    
    def GetIneRow(self, IneRowN):
        row=[]
        if isinstance(self.content, My2DArray1):
            row=self.content.GetIneRowN_usual(IneRowN)
        elif isinstance(self.content, list):
            LE=len(self.content)
            MaxLen=0
            MinLen=0
            for i in range(1, LE+1):
                CurLen=len(self.content[i-1])
                if i==1 or (i>1 and CurLen>MaxLen):
                    MaxLen=Curlen
                if i==1 or (i>1 and CurLen<MinLen):
                    MinLen=Curlen
            if IneRowN>=1 and IneRowN<=MinLen
                for i in range(1, LE+1):
                    row.append(self.content[i-1][IneRowN-1])
        DcRow=DataCellRow1(row)
        return DcRow

    def GetExtRow_WithHdr(self, ExtRowN):
        pass
    
    def GetIneRow_WithHdr(self, IneRowN):
        pass

    def GetLine(self, LineN):
        if self.LC_1_CL_0==1:
            row=self.GetExtRow(self, LineN)
        else:
            row=self.GetIneRow(self, LineN)
    
    def GetColumn(self, ColN):
        if self.LC_1_CL_0==0:
            row=self.GetExtRow(self, ColN)
        else:
            row=self.GetIneRow(self, ColN)

    def GetLine_WithHdr(self, LineN):
        DCR=self.GetLine(LineN)
        LH=self.GetCell_ColOfLineHeader_AsCopy(LineN)
        DCRH=DataCellRowWithHeader1(DCR, LH)
        return DCRH
    
    def GetColumn_WithHdr(self, ColN):
        DCR=self.GetColumn(ColN)
        LH=self.GetCell_LineOfColHeader_AsCopy(ColN)
        DCRH=DataCellRowWithHeader1(DCR, LH)
        return DCRH

    def Seek(self, valToSeek):#copy, changed values equality expr|: val itself and cell's fn GetVal
        count=0
        #print("Seek starts working")
        QE=len(self.row)
        #print("2D array has ",QE," ext rows")
        pairRow=[]
        for i in range(1, QE+1):
            QI=len(self.row[i-1])
            #print("Length of ",i," th row = ", QI)
            for j in range (1,QI+1):
                pair=[]
                curVal=copy.deepcopy(self.row[i-1][j-1].GetVal())
                if curVal==valToSeek:
                    #print("i=",i," j=",j," CurVal=",curVal," == "," valToSeek= ",valToSeek)
                    pair.append(i)
                    pair.append(j)
                    #print(pair)
                    pairRow.append(copy.deepcopy(pair))
                    count=count+1
                    #print("Found at (",pair[1-1],",",pair[2-1],")")
                    #print("Found at (",pair[1-1],",",pair[2-1],")")
                else:
                    pass
                    #print("i=",i," j=",j," CurVal=",curVal," != "," valToSeek= ",valToSeek)
        #print("Seek finishes working")
        return pairRow

    def Seek_SortByExtRowN(self, val):#copy, yes
        return self.Seek(val)

    def Seek_SortByIneRowN(self, val):#copy, yes
        row=self.Seek(val)
        Q=len(row)
        for i in range(1, Q+1):
            for j in range(i, Q+1):
                #if j==i or (j>i and row[j-1][2-1]<row[i-1][2-1]):
                if row[j-1][2-1]<row[i-1][2-1]:
                    buf=row[j-1]
                    row[j-1]=row[i-1]
                    row[i-1]=buf
        return row

    def Seek_SortByLines(self, val):
        if self.LC_1_CL_0==1:
            row=Seek_SortByExtRowN(val)
        else:
            row=Seek_SortByIneRowN(val)
        return row
        

    def Seek_SortByColumns(self, val):
        if self.LC_1_CL_0==0:
            row=Seek_SortByExtRowN(val)
        else:
            row=Seek_SortByIneRowN(val)
        return row

    

    # REPRESENTATION (7) --------------------------------------------------------------------------------------------------------

    def GetHeader_AsString(self):
        cell=self.GetTableHeader()
        R=cell.ToString()
        return R
    
    def GetCorner_AsString(self, BefCorner="", AftCorner="):
        s=""
        TH=self.GetTableHeader()
        CGH=self.GetColumnsGeneralHeader()
        LGH=self.GetLinesGeneralHeader()
        if LGH!="" and LGH!="":
            s=LGH.ToString()+"\\"+CGH.ToString()
            s=BefCorner+s
            s=s+AftCorner
        elif LGH=="" and LGH!="":
            s=CGH.ToString()
            s=BefCorner+s
            s=s+AftCorner
        elif LGH!="" and LGH=="":
            s=LGH.ToString()
            s=BefCorner+s
            s=s+AftCorner
        return s

    def GetLineOfColHeaderCell_AsString(self,  ColN, BefCell="", AftCell=""):
        s=""
        cell=self.GetCell_LineOfColHeader(ColN)
        if cell!=[] and cell!=0:
            s=cell.ToString(BefCell, AftCell)
        return s

    def GetColOfLineHeaderCell_AsString(self, LineN, BefCell="", AftCell=""):
        s=""
        cell=self.GetCell_ColOfLineHeader(LineN)
        if cell!=[] and cell!=0:
            s=cell.ToString(BefCell, AftCell)
        return s

    def GetCellContent_AsString(self, LineN, ColN, BefCell="", AftCell=""):
        s=""
        cell=GetCell(LineN, ColN)
        if cell!=0 and cell!=[]:
            s=cell.ToString(BefCell, AftCell)
        return s

    def GetLineOfColHeader_AsString(self, CellDelim="", BefCell="", AftCell=""):
        s=""
        if GetrIfLineOfColHeaderExists()==1:
            QColumns=self.GetQColumns()
            for i in range(1, QColumns-1+1):
                s=s+self.GetLineOfColHeaderCell_AsString(i, BefCell, AftCell)
                s=s+CellDelim
            if QColumns>0:
                s=s+self.GetLineOfColHeaderCell_AsString(QColumns, BefCell, AftCell)
        return s
        
    def GetHeaderLine_AsString(self, CornerDelim="", CellDelim="", BefCorner="", AftCorner="", BefCell="", AftCell=""):
        s=""
        sCorner=self.GetCorner_AsString(BefCorner, AftCorner)
        if sCorner!="":
            s=s+sCorner
            s=s+CornerDelim
        sLoCH=self.GetLineOfColHeader_AsString(CornerDelim, CellDelim, BefCorner, AftCorner, BefCell, AftCell)
        if sLoCH!="":
            s=s+sLoCH
        return s

    def GetContentLine_AsString(self, LineN, CellDelim="",  BefCell="", AftCell=""):
        s=""
        QColumns=self.GetQColumns()
        for i in range(1, QColumns-1+1):
            curCell=self.GetCell(LineN, i)
            s=s+curCell.ToString(BefCell, AftCell)
            s=s+CellDelim
        if QColumns>0:
            curCell=self.GetCell(LineN, QColumns)
            s=s+curCell.ToString(BefCell, AftCell)
        return s
                           

    def GetLineWithHeader_AsString(self, LineN, HdrDelim="", CellDelim="", BefHdr="", AftHdr="", BefCell="", AftCell=""):
        s=""
        QColumns=self.GetQColumns()
        sHdr=""
        if self.GetIfColOfLineHeaderExists(LineN)==1:
            sHdr=self.GetColOfLineHeaderCell_AsString(LineN, BefHdr, AftHdr)
            s=sHdr+HdrDelim
        sCntLine=self.GetContentLine_AsString(LineN, CellDelim,  BefCell, AftCell)
        s=s+sCntLine
        return s

    def ShowToConsole(self, BefCell="", AftCell="", CornerDelim="", CellDelim="", BefCorner="", AftCorner="", HdrDelim="", BefHdr="", AftHdr="", CellDelim=""):
        s=self.GetHeader_AsString()
        print(s)
        s=self.GetHeaderLine_AsString(self, CornerDelim, CellDelim, BefCorner, AftCorner, BefCell, AftCell)
        print(s)
        QLines=self.GetQLines()
        for i in range(1, QLines+1):
            s=self.GetLineWithHeader_AsString(i, HdrDelim, CellDelim, BefHdr, AftHdr, BefCell, AftCell)
            print(s)
        
