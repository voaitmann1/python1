from PyStdVector2 import *
#from MyCellsDiffTypes_NoHeirs_py2 import *
from TableHeaders import *

class TableController2:
    def __init__(self, content, LineOfColHeader=[], ColOfLineHeader=[], TableHeader=[], ext_LC_0_CL_1=0, ine_LC_0_CL_1=0, vsh=0):
        if vsh==1:
            print("table controller constructor starts working")
        self.content=[]
        self.LineOfColHeader=[]
        self.ColOfLineHeader=[]
        self.TableHeader=[]
        self.LC_0_CL_1=0
        #def Set(self, content, LineOfColHeader=[], ColOfLineHeader=[], TableHeader=[], ext_LC_0_CL_1=0, ine_LC_0_CL_1=0):
        self.Set(content,       LineOfColHeader,     ColOfLineHeader,   TableHeader,    ext_LC_0_CL_1,   ine_LC_0_CL_1, vsh)
        if vsh==1:
            #print("checking:")
            #print("content:")
            #print(self.content)
            #print("LineOfColHeader:")
            #print(self.LineOfColHeader)
            #print("ColOfLineHeader:")
            #print(self.ColOfLineHeader)
            print("table controller constructor finishes working")

    def Set(self, content, LineOfColHeader=[], ColOfLineHeader=[], TableHeader=[], ext_LC_0_CL_1=0, ine_LC_0_CL_1=0, vsh=0):
        if vsh==1:
            print("Set starts working")
        self.SetContent(content, ext_LC_0_CL_1, ine_LC_0_CL_1, vsh)
        self.SetLineOfColHeader(LineOfColHeader)
        self.SetColOfLineHeader(ColOfLineHeader)
        self.SetTableHeaders(TableHeader)
        self.LC_0_CL_1=ine_LC_0_CL_1
        if vsh==1:
            print("Set finishes working")

    #def Set(self, content, HeaderRowExt=[], TableHeader=[], ext_LC_0_CL_1=0, ine_LC_0_CL_1=0):
    #    self.SetContent(content, ext_LC_0_CL_1, ine_LC_0_CL_1)
    #    if(ext_LC_0_CL_1==0):
    #        self.SetLineOfColHeader(HeaderRowExt)
    #    else:
    #        self.SetColOfLineHeader(HeaderRowExt)
    #    self.SetTableHeaders(TableHeader)
    #    self.LC_0_CL_1=LC_0_CL_1

    

    #def SetContentHeadered(self, content, ext_LC_0_CL_1=0, ine_LC_0_CL_1=0):
    #
    #def SetContentItself(self, content, ext_LC_0_CL_1=0, ine_LC_0_CL_1=0):
    #
    def SetContent(self, contentExt, ext_LC_0_CL_1=0, ine_LC_0_CL_1=0, vsh=0):
        contentCopied=copy.deepcopy(contentExt)
        Q=len(contentCopied)
        content=[]
        HdrRow=[]
        if(Q>0):
            if isinstance(contentCopied, list) and len(contentCopied)>0:
                if isinstance(contentCopied[1-1], list):
                    if isinstance(contentCopied[1-1][1-1], list) and not isinstance(contentCopied[1-1][2-1], list):#Cell Row Co Hdr
                        #content=[]
                        #HdrRow=[]
                        if vsh==1:
                            print("Cell Row Co Hdr, content then header")
                        for i in range(1, Q+1):
                            content.append(contentCopied[i-1][1-1])
                            HdrRow.append(contentCopied[i-1][2-1])
                        if ext_LC_0_CL_1==0:
                            self.LineOfColHeader=HdrRow
                        else:
                            self.ColOfLineHeader=HdrRow
                    if isinstance(contentCopied[1-1][2-1], list) and not isinstance(contentCopied[1-1][1-1], list):#Cell Row Co Hdr
                        #content=[]
                        #HdrRow=[]
                        if vsh==1:
                            print("Cell Row Co Hdr, header then content")
                        for i in range(1, Q+1):
                            content.append(contentCopied[i-1][2-1])
                            HdrRow.append(contentCopied[i-1][1-1])
                        if ext_LC_0_CL_1==0:
                            self.LineOfColHeader=HdrRow
                        else:
                            self.ColOfLineHeader=HdrRow
                    else:
                        if vsh==1:
                            print("simple 2D content")
                        content=contentCopied#copy was for content1
                    #
                    Lmin=Get2DArrayMinLength(content)
                    Lmax=Get2DArrayMaxLength(content)
                    if vsh==1:
                        print("Now dealing with content itself: Q="+str(Q)+" Lmin="+str(Lmin)+" Lmax="+str(Lmax))
                    #
                    if(ext_LC_0_CL_1==ine_LC_0_CL_1==0):
                        if vsh==1:
                            print("structures are same given and needed")
                        #self.content=[]
                        for i in range(1, Q+1):
                            #Lcur=Get2DArrayLengthN(content, i)
                            rowE=[]
                            for j in range(1, Lmin+1):
                                #for j in range(1, Lcur+1):
                                element=copy.deepcopy(content[i-1][j-1])
                                cell=DataCell(element)
                                rowE.append(cell)
                            self.content.append(rowE)
                    else:
                        #elif Lmin==Lmax:
                        if vsh==1:
                            #print("structures are different but given is rectangular")
                            print("structures are different but given is rectangular")
                        for i in range(1, Lmin+1):
                            #for i in range(1, Lmax+1):
                            rowE=[]
                            for j in range(1, Q+1):
                                element=copy.deepcopy(content[j-1][i-1])
                                cell=DataCell(element)
                                rowE.append(cell)
                            self.content.append(rowE)
                        #for i in range(1, Lmax+1):
                    #else:
                    #    if vsh==1:
                    #        print("structures are different but given is NOT rectangular, ignored")
                    #    for i in range(1, Lmin+1):
                    #        rowE=[]
                    #        for j in range(1, Q+1):
                    #            element=copy.deepcopy(content[j-1][i-1])
                    #            cell=DataCell(element)
                    #            rowE.append(cell)
                    #        self.content.append(rowE)
                else:#is not list
                    if vsh==1:
                        print("list element is not list")
                    if isinstance(content[1-1], DataCellRow):
                        if vsh==1:
                            print("content given is list of DataCellRow's")
                            print("def min length")
                        Lmin=0
                        for i in range(1, Q+1):
                            Lcur=content[i-1].GetLength()
                            if i==1 or (i>1 and Lcur<Lmin):
                                Lcur=Lmin
                                if vsh==1:
                                    print("i="+str(i)+" Lcur="+str(Lcur)+" Lmin="+str(Lmin))
                        if(ext_LC_0_CL_1==ine_LC_0_CL_1==0):
                            if vsh==1:
                                print("structures are same, DataCellRow's are external")
                            for i in range(1, Q+1):
                                rowE=[]
                                for j in range(1, Lmin+1):
                                    element=content[i-1].GetCell_AsCopy(j)
                                    cell=DataCell(element)#superflue, DataCellRow contains DataCells only
                                    rowE.append(cell)
                                self.content.append(rowE)
                        #
                    elif isinstance(content[1-1], DataCell):#content is 1D-list
                        if vsh==1:
                            print("content is 1D-list")
                        if(ext_LC_0_CL_1==ine_LC_0_CL_1==0):
                            if vsh==1:
                                print("structures are same, rows are external")
                            for i in range(1, Q+1):
                                rowE=[]
                                for j in range(1, Lmin+1):
                                    element=content[i-1].GetCell_AsCopy(j)
                                    cell=DataCell(element)#sflu
                                    rowE.append(cell)
                                self.content.append(rowE)
                        #
                        else:
                            if vsh==1:
                                print("structures are different,  every DataCelRow is internal")
                            rowE=[]
                            for i in range(1, Lmin+1):
                                for j in range(1, Q+1):
                                    element=content[j-1].GetCell_AsCopy(i)
                                    cell=DataCell(element)#sflu
                                    rowE.append(cell)
                            self.content.append(rowE)
                            self.LineOfColHeader=self.SetLineOfColHeader(HdrRow)
            else:
                #1DArray, 2DArray, ...
                pass
            #
        #
        self.LC_0_CL_1=ine_LC_0_CL_1==0
    #fn
        
    def SetLineOfColHeader(self, LineOfColHeader):
        if isinstance(LineOfColHeader, list):
            self.LineOfColHeader=[]
            L=len(LineOfColHeader)
            for i in range(1, L+1):
                element=copy.deepcopy(LineOfColHeader[i-1])
                cell=DataCell()
                cell.Set(element)
                self.LineOfColHeader.append(cell)
                

    def SetColOfLineHeader(self, ColOfLineHeader):
        if isinstance(ColOfLineHeader, list):
            self.ColOfLineHeader=[]
            L=len(ColOfLineHeader)
            for i in range(1, L+1):
                element=copy.deepcopy(ColOfLineHeader[i-1])
                cell=DataCell(element)
                self.ColOfLineHeader.append(cell)

    def SetTableHeaders(self, TableHeader="", LinesGeneralHeader="", ColumnsGeneralHeader=""):
        self.TableHeader=TableHeaders(TableHeader, LinesGeneralHeader, ColumnsGeneralHeader)
    #
    def GetQExtRows(self):
       return len(self.content)

    def GetQIneRows(self):
       return Get2DArrayMinLength(self.content)
    #
    def GetQLines(self):
        QExtRows=self.GetQExtRows()
        QIneRows=self.GetQIneRows()
        if self.LC_0_CL_1==0:
            QLines=QExtRows
            QColumns=QIneRows
        else:
            QLines=QIneRows
            QColumns=QExtRows
        return QLines

    def GetQColumns(self):
        QExtRows=self.GetQExtRows()
        QIneRows=self.GetQIneRows()
        if self.LC_0_CL_1==0:
            QLines=QExtRows
            QColumns=QIneRows
        else:
            QLines=QIneRows
            QColumns=QExtRows
        return QColumns

    def GetLC0CL1(self):
        return self.LC_0_CL_1
    #
    def SetStructureOtherwise(self):
        Lmax=Get2DArrayMaxLength(self.content)
        for i in range(1, Lmax+1):
            rowE=[]
            for j in range(1, Q+1):
                element=copy.deepcopy(content[j-1][i-1])
                cell=DataCell(element)
                rowE.append(cell)
            self.content.append(rowE)
        if self.LC_0_CL_1==0:
            self.LC_0_CL_1=1
        else:
            self.LC_0_CL_1=0
    #
    def GetCell_AsLink_ExtIne(self, ExtRowN, IneRowN):
        cell=0
        Q=len(self.content)
        Lmin=Get2DArrayMinLength(self.content)
        Lmax=Get2DArrayMaxLength(self.content)
        if ExtRowN>=1 and ExtRowN<=Q and IbeRowN>=1 and IneRowN<=Lmax:
            cell=self.content[ExtRowN-1][IneRowN-1]
        return cell

    def GetCell_AsCopy_ExtIne(self, ExtRowN, IneRowN):
        cell=0
        Q=len(self.content)
        Lmin=Get2DArrayMinLength(self.content)
        Lmax=Get2DArrayMaxLength(self.content)
        if ExtRowN>=1 and ExtRowN<=Q and IneRowN>=1 and IneRowN<=Lmax:
            cell=copy.deepcopy(self.content[ExtRowN-1][IneRowN-1])
        return cell
    #
    def GetCell_AsLink(self, LineN, ColN):
        if self.LC_0_CL_1==0:
            ExtRowN=LineN
            IneRowN=ColN
        else:
            ExtRowN=ColN
            IneRowN=LineN
        return self.GetCell_AsLink_ExtIne(ExtRowN, IneRowN)

    def GetCell_AsCopy(self, LineN, ColN):
        if self.LC_0_CL_1==0:
            ExtRowN=LineN
            IneRowN=ColN
        else:
            ExtRowN=ColN
            IneRowN=LineN
        #      GetCell_AsCopy_ExtIne
        return self.GetCell_AsCopy_ExtIne(ExtRowN, IneRowN)

    def GetCell_LineOfColHeader_AsLink(self, ColN):
        cell=0
        if self.LineOfColHeader!=[] and ColN>=1 and ColN<=len(self.LineOfColHeader):
            cell=self.LineOfColHeader[ColN-1]
        return cell

    def GetCell_LineOfColHeader_AsCopy(self, ColN):
        cell=0
        if self.LineOfColHeader!=[] and ColN>=1 and ColN<=len(self.LineOfColHeader):
            cell=copy.deepcopy(self.LineOfColHeader[ColN-1])
        return cell

    def GetCell_ColOfLineHeader_AsLink(self, LineN):
        cell=0
        if self.ColOfLineHeader!=[] and LineN>=1 and LineN<=len(self.ColOfLineHeader):
            cell=self.ColOfLineHeader[LineN-1]
        return cell

    def GetCell_ColOfLineHeader_AsCopy(self, LineN):
        cell=0
        if self.ColOfLineHeader!=[] and LineN>=1 and LineN<=len(self.ColOfLineHeader):
            cell=copy.deepcopy(self.ColOfLineHeader[LineN-1])
        return cell
    #
    def GetContentRowExt_AsList(self, ExtRowN):
        row=Get2DArrayExtRowN(self.content, ExtRowN)
        return row
    
    def GetContentRowExt_AsDataCellRow(self, ExtRowN):
        R=DataCellRow1()
        Q=len(self.content)
        if(ExtRowN>=1 and ExtRowN<=Q):
            row=DataCellRow1(self.content[ExtRowN-1])
            R=DataCellRow1(row)
        return R

    def GetContentRowIne_AsList(self, IneRowN):
        row=Get2DArrayIneRowN(self.content, IneRowN) 
        return row
    
    def GetContentRowIne_AsDataCellRow(self, IneRowN):
        R=DataCellRow1()
        row=Get2DArrayIneRowN(self.content, IneRowN)
        R=DataCellRow1(row)
        return R
        
    def GetContentLine_AsList(self, LineN):
        R=[]
        if self.LC_0_CL_1==0:
            ExtRowN=LineN
            IneRowN=ColN
            R=GetContentRowExt_AsList(ExtRowN)
        else:
            ExtRowN=ColN
            IneRowN=LineN
            R=GetContentRowIne_AsList(IneRowN)
        return R
    
    def GetContentLine_AsDataCellRow(self, LineN):
        R=DataCellRow1()
        if self.LC_0_CL_1==0:
            ExtRowN=LineN
            IneRowN=ColN
            R=GetContentRowExt_AsDataCellRow(ExtRowN)
        else:
            ExtRowN=ColN
            IneRowN=LineN
            R=GetContentRowIne_AsDataCellRow(IneRowN)
        return R

    def GetContentColumn_AsList(self, ColN):
        R=[]
        if self.LC_0_CL_1==0:
            ExtRowN=LineN
            IneRowN=ColN
            R=GetContentRowIne_AsList(IneRowN)
        else:
            ExtRowN=ColN
            IneRowN=LineN
            R=GetContentRowExt_AsList(ExtRowN)
        return R
    
    def GetContentColumn_AsDataCellRow(self, ColN):
        R=DataCellRow1()
        if self.LC_0_CL_1==0:
            ExtRowN=LineN
            IneRowN=ColN
            R=GetContentRowExt_AsDataCellRow(ExtRowN)
        else:
            ExtRowN=ColN
            IneRowN=LineN
            R=GetContentRowIne_AsDataCellRow(IneRowN)
        return R
    #
    def ToString(self, LineN, ColN, sBef="", sAft=""):
        cell=0
        s=""
        cell=self.GetCell_AsCopy(LineN, ColN)
        if isinstance(cell, DataCell):
            s=cell.ToString()
            s=sBef+s
            s=s+sAft
        return s
        
    def ToString_TableName(self, sBef="", sAft=""):
        s=""
        if isinstance(self.TableHeader, TableHeaders):
            s=self.TableHeader.ToString_TableHeader(sBef, sAft)
        return s

    def ToString_LinesGeneralName(self):
        s=""
        if isinstance(self.TableHeader, TableHeaders):
            s=self.TableHeader.ToString_LinesGeneralHeader()
        return s

    def ToString_ColumnsGeneralName(self):
        s=""
        if isinstance(self.TableHeader, TableHeaders):
            s=self.TableHeader.ToString_ColumnsGeneralHeader()
        return s

    def ToString_HeaderCorner(self, sBefLoCH="", sAftLoCH="", sBefCoLH="", sAftCoLH=""):
        s=""
        if isinstance(self.TableHeader, TableHeaders):
            s=self.TableHeader.ToString_Corner(sBefLoCH, sAftLoCH, sBefCoLH, sAftCoLH)
        return s

    def StringContentCellBef(self, LineN, ColN, TableReprSimple=[]):
        s=""
        TableHeader=self.ToString_TableName()
        LinesGeneralHeader=ToString_LinesGeneralName()
        ColumnsGeneralHeader=ToString_ColumnsGeneralName()
        LineHeaderItself=ToString_Cell_ColOfLineHeader(self, LineN)
        ColHeaderItself=ToString_Cell_LineOfColHeader(self, ColN)
        if TableReprSimple!=[]:
            LineNToShow=TableReprSimple.LineNToShow()
            ColNToShow=TableReprSimple.ColumnsNToShow()
            if TableReprSimple.ContentCellAs_Simple0_Matrix1_Fn2D2_L3_C4_LC5_CL6==0:
                pass
            if TableReprSimple.ContentCellAs_Simple0_Matrix1_Fn2D2_L3_C4_LC5_CL6==1:
                s=TableHeader+"("+str(LineNToShow)+", "+str(ColNToShow)+") = "
            if TableReprSimple.ContentCellAs_Simple0_Matrix1_Fn2D2_L3_C4_LC5_CL6==2:
                s=TableHeader+"("+LineHeaderItself+", "+ColHeaderItself+") = "
            if TableReprSimple.ContentCellAs_Simple0_Matrix1_Fn2D2_L3_C4_LC5_CL6==2:
                if TableReprSimple.ShowTableHeader==1:
                    s=TableHeader
                if TableReprSimple.ShowLineHeader==1 or TableReprSimple.ShowColumnHeader==1:
                s=s+"("
                if TableReprSimple.ShowLineHeader==1:
                    s=s+LinesGeneralHeader
                    if ShowLinesNumeration==1
                        s=s+str(
                s=s+LineHeader
                +"("+LineHeader+", "+ColHeader+") : "
        return s

    def StringContentCellAft(self, TableReprSimple):
        s=""

        return s

    def StringLineOfColHeaderCellBef(self, TableReprSimple):
        s=""

        return s

    def StringLineOfColHeaderCellAft(self, TableReprSimple):
        s=""

        return s

    def StringColOfLineHeaderCellBef(self, TableReprSimple):
        s=""

        return s

    def StringColOfLineHeaderCellAft(self, TableReprSimple):
        s=""

        return s
    
    
    def ToString_Cell_LineOfColHeader(self, ColN, sBef="", sAft=""):
        cell=0
        s=""
        cell=self.GetCell_LineOfColHeader_AsCopy(ColN)
        if isinstance(cell, DataCell):
            s=cell.ToString()
            s=sBef+s
            s=s+sAft
        return s

    def ToString_Cell_ColOfLineHeader(self, LineN, sBef="", sAft=""):
        cell=0
        s=""
        cell=self.GetCell_ColOfLineHeader_AsCopy(LineN)
        if isinstance(cell, DataCell):
            s=cell.ToString()
            s=sBef+s
            s=s+sAft
        return s

    def ToString_LineOfColHeader(self, delim=" ", sBef="", sAft=""):
        s=""
        QC=self.GetQColumns()
        if self.LineOfColHeader!=[]:
            for ColN in range(1, QC-1+1):
                s=s+self.ToString_Cell_LineOfColHeader(ColN, sBef, sAft)
                s=s+delim
            if QC>0:
                s=s+self.ToString_Cell_LineOfColHeader(QC, sBef, sAft)
        return s

    def ToString_HeaderLine(self, delim=" ", delimHdr=": ", sBef="", sAft="", sBefLoCH="", sAftLoCH="", sBefCoLH="", sAftCoLH=""):
        s=""
        sC=self.ToString_HeaderCorner(sBefLoCH, sAftLoCH, sBefCoLH, sAftCoLH)
        sL=self.ToString_LineOfColHeader(delim, sBef, sAft)
        if isinstance self.
        s=s+sC
        if sC!="" and sL!="":
            s=s+delimHdr
        s=s+sL
        return s
        
    def ToString_ContentLine(self, LineN, delim=" ", sBef="", sAft=""):
        s=""
        QC=self.GetQColumns()
        for i in range(1, QC-1+1):
            cell=self.GetCell_AsCopy(LineN, i)
            s=s+cell.ToString(sBef, sAft)
            s=s+delim
        if QC>0:
            cell=self.GetCell_AsCopy(LineN, i)
            s=s+cell.ToString(sBef, sAft)
        return s

    def ToString_Line(self, LineN, delim=" ", delimHdr=": ", sBef="", sAft="", sBefHdr="", sAftHdr=""):
        s=""
        sH=self.ToString_Cell_ColOfLineHeader(LineN, sBefHdr, sAftHdr)
        sL=self.ToString_ContentLine(LineN, delim, sBef, sAft)
        s=s+sH
        if sH!="" and sL!="":
            s=s+delimHdr
        s=s+sL
        return s
