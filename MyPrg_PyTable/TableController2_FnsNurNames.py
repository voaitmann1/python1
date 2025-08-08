from PyStdVector2 import *
#from MyCellsDiffTypes_NoHeirs_py2 import *
from TableHeaders import *
from MyStringLib import *
from TableInfoClasses import *

class TableController2:
    def __init__(self, content=[], LineOfColHeader=[], ColOfLineHeader=[], TableHeader=[], ext_LC_0_CL_1=0, ine_LC_0_CL_1=0, vsh=0):
        
    def Set_By2DArray(self, arr2D, RowOfExtRowHeaderExistsNo0Yes1=0, RowOfIneRowHeaderExistsNo0Yes1=0, ext_LC_0_CL_1=0, ine_LC_0_CL_1=0, vsh=0):
        
    def Set_ByContentHeadered(self, contentHeaderedExt, RowOfIneRowHeader, tableHeaders, ext_LC_0_CL_1=0, ine_LC_0_CL_1=0, vsh=0):

    def Set_ByContentHeadered1(self, contentExt, RowOfIneRowHeader, tableHeaders, ext_LC_0_CL_1=0, ine_LC_0_CL_1=0, vsh=0):        
        
    def Set_ByContent_AndSeparateHeaders(self, contentExt, RowOfExtRowHeader, RowOfIneRowHeader, tableHeaders, ext_LC_0_CL_1=0, ine_LC_0_CL_1=0, vsh=0):

    def Set(self, content, LineOfColHeader=[], ColOfLineHeader=[], tableHeader=[], ext_LC_0_CL_1=0, ine_LC_0_CL_1=0, vsh=0):
      
    def GetQExtRows(self):

    def GetQIneRows(self):

    def GetQLines():

    def GetQColumns():

    def GetSize(self):

    def SetContent(self, contentExt, ext_LC_0_CL_1=0, ine_LC_0_CL_1=0, vsh=0):
    
    def SetContentAndItsHeaders_Inner(self, contentExt, ext_LC_0_CL_1=0, ine_LC_0_CL_1=0, vsh=0):
            
    def SetLineOfColHeader(self, LineOfColHeader):

    def SetColOfLineHeader(self, ColOfLineHeader):
   
    def SetTableHeaders(self, TableHeader="", LinesGeneralHeader="", ColumnsGeneralHeader="", vsh=0):

    def GetQExtRows(self):

    def GetQIneRows(self):

    def GetQLines(self):
    
    def GetQColumns(self):

    def GetStructRowOrderLC0CL1(self):

    def GetIf_LineOfColHeaderExists(self):

    def GetIf_ColOfLineHeaderExists(self):

    def SetStructureOtherwise(self):

    def GetCell_AsLink_ExtIne(self, ExtRowN, IneRowN):

    def GetCell_AsCopy_ExtIne(self, ExtRowN, IneRowN):
    
    def GetCell_AsLink(self, LineN, ColN):

    def GetCell_AsCopy(self, LineN, ColN):

    def GetCell_LineOfColHeader_AsLink(self, ColN):

    def GetCell_LineOfColHeader_AsCopy(self, ColN):

    def GetCell_ColOfLineHeader_AsLink(self, LineN):
    
    def GetCell_ColOfLineHeader_AsCopy(self, LineN):

    def GetContentRowExt_AsList_OfDataCells(self, ExtRowN):

    def GetContentRowExt_AsList_OfVals(self, ExtRowN):

    def GetContentRowExt_AsList_OfCurItems(self, ExtRowN):

    def GetContentRowExt_AsDataCellRow(self, ExtRowN):

    def GetContentRowIne_AsList_OfDataCells(self, IneRowN):

    def GetContentRowIne_AsList_OfVals(self, IneRowN):

    def GetContentRowIne_AsList_OfCurItems(self, IneRowN):

    def GetContentRowIne_AsDataCellRow(self, IneRowN):

    def GetContentLine_AsList_OfDataCells(self, LineN):

    def GetContentLine_AsList_OfVals(self, LineN):

    def GetContentLine_AsList_OfCurItems(self, LineN):

    def GetContentLineWithHeader_AsListNested_OfDataCells(self, LineN):

    def GetContentLineWithHeader_AsListNested_OfVals(self, LineN):

    def GetContentLineWithHeader_AsListNested_OfCurItems(self, LineN):

    def GetContentLine_AsDataCellRow(self, LineN):
    
    def GetContentColumn_AsList_OfDataCells(self, ColN):

    def GetContentColumn_AsList_OfVals(self, ColN):

    def GetContentColumn_AsList_OfCurItems(self, ColN):

    def GetContentColumnWithHeader_AsListNested_OfDataCells(self, ColN):

    def GetContentColumnWithHeader_AsListNested_OfVals(self, ColN):

    def GetContentColumnWithHeader_AsListNested_OfCurItems(self, ColN):

    def GetContentColumn_AsDataCellRow(self, ColN):

    def GetContent(self):

    def GetContent_Vals(self):

    def GetContent_CurItems(self):

    def GetLine_WithHeader(self, LineN):

    def GetColumn_WithHeader(self, ColN):

    def GetLineOfColHeader_WithGeneralName(self):

    def GetColOfLineHeader_WithGeneralName(self):
        
    def ToString_TableName(self, sBef="", sAft=""):

    def ToString_LinesGeneralName(self):

    def ToString_ColumnsGeneralName(self):

    def ToString_HeaderCorner(self, sBefLoCH="", sAftLoCH="", sBefCoLH="", sAftCoLH=""):

    def ToString_Cell(self, LineN, ColN, tblRepr=[], vsh=0):
     
    def ToString_Cell_LineOfColHeader(self, ColN, Repr=[], vsh=0):

    def ToString_Cell_ColOfLineHeader(self, LineN, tblRepr=[], vsh=0):#
        
    def ToString_LineOfColHeader(self, delim=" ", tblRepr=[], vsh=0):

    def ToString_HeaderLine(self, delim=" ", delimHdr=": ", tblRepr=[], vsh=0):
        
    def ToString_Line(self, LineN, delim=" ", delimHdr=": ", tblRepr=[], vsh=0):
    
    def MaxColOfLineHeaderLen(TableReprSimple=[]):
        
    def MaxColLen(ColN, TableReprSimple=[]):
        
    def MaxColWithHdrLen(ColN, TableReprSimpleExt=[]):# not finished!
       
    def ShowToConsole(self, delim=" ", delimHdr=": ", tblRepr=[], vsh=0):
        
    def PrepareDataForTableColumn_HdrdCellRow(self, rowCntExt=[], header="", DfltVal="", AddNotOtherAction=1, QToAddForEmpty=1, vsh=0):
        
    def PrepareDataForTableColumn_NestedListOfCells(self, rowCntExt=[], header="", DfltVal="", AddNotOtherAction=1, QToAddForEmpty=1, vsh=0):

    def SetColumn(self, ColN, rowCntExt=[], header="", DfltVal="", QToAddForEmpty=1, vsh=0):

    def AddEmptyColumn(self, DfltVal="", QToAddForEmpty=1, CreateHdrIfEmpty=1, vsh=0):

    def AddColumn(self, rowCntExt=[], header="", DfltVal="", QToAddForEmpty=1, vsh=0):

    def InsColumn(self, ColN, rowCntExt=[], header="", DfltVal="", vsh=0):

    def DelColumn(self, ColN, QCellsAferDelLastLine=1, DfltVal=""):

    def PrepareDataForTableLine(self, rowCntExt=[], header="", DfltVal="", AddNotOtherAction=1, QToAddForEmpty=1, vsh=0):

    def SetLine(self, LineN, rowCntExt=[], header="", DfltVal="", QToAddForEmpty=1, vsh=0):

    def AddEmptyLine(self, DfltVal="", QToAddForEmpty=1, CreateHdrIfEmpty=1, vsh=0):

    def AddLine(self, rowCntExt=[], header="", DfltVal="", QToAddForEmpty=1, vsh=0):

    def InsLine(self, LineN, rowCntExt=[], header="", DfltVal="", vsh=0):

    def DelLine(self, LineN, QCellsAferDelLastLine=1, DfltVal=""):

    def Transpose(self):

    def Get_LineOfColHeader_AsListOfStrVals(self):

    def Get_ColOfLineHeader_AsListOfStrVals(self):

    def __NewValUniqueForLineOfColHeader(self, valExt, colN, vsh=0):
    
    def __NewValUniqueForColOfLineHeader(self, valExt, lineN, vsh=0):
       
    def __AddValToLineOfColHeaderIfPossible(self, valExt, vsh=0):

    def __InsValToLineOfColHeaderIfPossible(self, ColN, valExt, vsh=0):
    
    def __SetValToLineOfColHeaderIfPossible(self, ColN, valExt, vsh=0):
    
    def __AddValToColOfLineHeaderIfPossible(self, valExt, vsh=0):

    def __InsValToColOfLineHeaderIfPossible(self, LineN, valExt, vsh=0):

    def __SetValToColOfLineHeaderIfPossible(self, LineN, valExt, vsh=0):
        
           
        
                    
        

    
