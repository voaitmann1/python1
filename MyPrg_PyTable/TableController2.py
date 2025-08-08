from PyStdVector2 import *
#from MyCellsDiffTypes_NoHeirs_py2 import *
from TableHeaders import *
from MyStringLib import *
from TableInfoClasses import *

class TableController2:
    def __init__(self, content=[], LineOfColHeader=[], ColOfLineHeader=[], TableHeader=[], ext_LC_0_CL_1=0, ine_LC_0_CL_1=0, vsh=0):
        if vsh==1:
            print("table controller constructor starts working")
        self.content=[]
        self.LineOfColHeader=[]
        self.ColOfLineHeader=[]
        self.TableHeader=[]
        self.LC_0_CL_1=0
        #def Set(self, content, LineOfColHeader=[], ColOfLineHeader=[], TableHeader=[], ext_LC_0_CL_1=0, ine_LC_0_CL_1=0):
        if content!=[]:
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

    #def Set_ByRowsWithHeaders(self, HeaderedContentRowsList, RowHeader=[],  TableHeader=[], ext_LC_0_CL_1=0, ine_LC_0_CL_1=0, vsh=0):
    #                                   if vsh==1:
    #        print("Set_WithHeaders starts working")
    #    InnerHeaderRow=[]
    #    PureContent=[]
    #    arow=[]
    #    content=copy.deepcopy(HeaderedContentRowsList)
    #    #einzeln header row
    #    if ext_LC_0_CL_1==0:
    #        self.SetColOfLineHeader(RowHeader)
    #        if vsh==1:
    #            print("ColOfLineHeader is set by ext RowHeader")
    #    else:
    #        self.SetLineOfColHeader(RowHeader)
    #        if vsh==1:
    #            print("LineOfColHeader is set by ext RowHeader")
    #    #Content rows and row of their headers
    #    if isinstance(content, list) and len(content)>0:
    #        if isinstance(content[1-1], list):
    #            if len(content[1-1])==2:
    #                if isinstance(content[1-1][1-1], list) and not isinstance(content[1-1][2-1], list):#row, header
    #                    Q=len(content)
    #                    count=0
    #                    for i in range(1, Q+1):
    #                        PureContent.append(content[i-1][1-1])
    #                        if content[i-1][2-1]!="":
    #                            count=count+1
    #                    if ext_LC_0_CL_1==0:
    #                        if count>0:
    #                            self.ColOfLineHeader=[]
    #                            for i in range(1, Q+1):
    #                                InnerHeaderRow.append(content[i-1][2-1])
    #                    else:
    #                        if count>0:
    #                            self.LineOfColHeader=[]
    #                            for i in range(1, Q+1):
    #                                InnerHeaderRow.append(content[i-1][2-1])
    #                elif not isinstance(content[1-1][1-1], list) and isinstance(content[1-1][2-1], list):#header, row
    #                    Q=len(content)
    #                    count=0
    #                    for i in range(1, Q+1):
    #                        PureContent.append(content[i-1][2-1])
    #                        if content[i-1][1-1]!="":
    #                            count=count+1
    #                    if ext_LC_0_CL_1==0:
    #                        if count>0:
    #                            self.ColOfLineHeader=[]
    #                            for i in range(1, Q+1):
    #                                InnerHeaderRow.append(content[i-1][1-1])
    #                        self.SetColOfLineHeader(InnerHeaderRow)
    #                    else:
    #                        if count>0:
    #                            self.LineOfColHeader=[]
    #                            for i in range(1, Q+1):
    #                                InnerHeaderRow.append(content[i-1][1-1])
    #                        self.SetLineOfColHeader(InnerHeaderRow)
    #                elif not isinstance(content[1-1][1-1], list) and not isinstance(content[1-1][2-1], list):#no header
    #                    if ext_LC_0_CL_1==0:
    #                        self.ColOfLineHeader=[]
    #                    else:
    #                        self.LineOfColHeader=[]
    #        elif isinstance(content[1-1], DataCellRowWithHeader):
    #            Q=len(content)
    #            count=0
    #            for i in range(1, Q+1):
    #                PureContent.append(content[i-1].row)
    #                if content[i-1][2-1]!="":
    #                    count=count+1
    #                    if ext_LC_0_CL_1==0:
    #                        if count>0:
    #                            self.ColOfLineHeader=[]
    #                            for i in range(1, Q+1):
    #                                InnerHeaderRow.append(content[i-1].header)
    #                            self.SetColOfLineHeader(InnerHeaderRow)
    #                    else:
    #                        if count>0:
    #                            self.LineOfColHeader=[]
    #                            for i in range(1, Q+1):
    #                                InnerHeaderRow.append(content[i-1].header)
    #                            self.SetLineOfColHeader(InnerHeaderRow)
    #    else:
    #        if vsh==1:
    #            print("content is not a list - table of 1 line and 1 column")
    #        if isinstance(content, DataCellRowWithHeader):
    #            PureContent.append(arow)
    #            InnerHeaderRow.append(content.header)
    #            if ext_LC_0_CL_1==0:
    #                self.ColOfLineHeader=[]
    #                self.SetColOfLineHeader(InnerHeaderRow)
    #            else:
    #                self.LineOfColHeader=[]
    #                self.SetLineOfColHeader(InnerHeaderRow)
    #        elif isinstance(content, DataCellRow):
    #            PureContent.append(content.row)
    #        else:
    #           arow.append(content)
    #            PureContent.append(arow)
    #            if ext_LC_0_CL_1==0:
    #                self.LineOfColHeader=[]#no headers
    #    #
    #    self.SetContent(PureContent, ext_LC_0_CL_1, ine_LC_0_CL_1, vsh)       
    #    self.SetTableHeaders(TableHeader)
    #    self.LC_0_CL_1=ine_LC_0_CL_1
    #    if vsh==1:
    #         print("Set_WithHeaders finishes working")

    def Set_By2DArray(self, arr2D, RowOfExtRowHeaderExistsNo0Yes1=0, RowOfIneRowHeaderExistsNo0Yes1=0, ext_LC_0_CL_1=0, ine_LC_0_CL_1=0, vsh=0):
        R=[]
        headers=[]
        corner=[]
        TableName=""
        ExtRowsGeneralName=""
        IneRowsGeneralName=""
        RowOfExtRowHeader=[]
        RowOfIneRowHeader=[]
        content=[]
        ContentLine=[]
        line=[]
        if vsh==1:
            print("Set_By2DArray starts working")
        data=copy.deepcopy(arr2D)
        if isinstance(data, list) and len(data)>0 and isinstance(data[1-1], list):
            Q=len(data)
            Lmin=Get2DArrayMinLength(data)#from PyStdVector2 import *
            Lmax=Get2DArrayMaxLength(data)#from PyStdVector2 import *
            if vsh==1:
                print("data is list of lists. Q="+str(Q)+" Lmin="+str(Lmin)+" Lmax="+str(Lmax))
            if RowOfExtRowHeaderExistsNo0Yes1==0 and RowOfIneRowHeaderExistsNo0Yes1==0:
                content=copy.deepcopy(data)
                if vsh==1:
                    print("content only, no headers")
            elif RowOfExtRowHeaderExistsNo0Yes1==0 and RowOfIneRowHeaderExistsNo0Yes1==1:
                content=data[2-1:len(data)]
                RowOfIneRowHeader=data[1-1]
                if vsh==1:
                    print("RowOfIneRowHeader - Exists, RowOfExtRowHeader - No")
                    print("RowOfIneRowHeader: ", RowOfIneRowHeader)
            elif RowOfExtRowHeaderExistsNo0Yes1==1 and RowOfIneRowHeaderExistsNo0Yes1==0:
                for i in range(1, Q+1):
                    line=copy.deepcopy(data[i-1])
                    #L=len(line)
                    #ContentLine=line[2-1:L]
                    ContentLine=line[2-1:Lmin]
                    content.append(ContentLine)
                    RowOfExtRowHeader.append(line[1-1])
                    if vsh==1:
                        print("RowOfExtRowHeaderExists - Exists, RowOfIneRowHeader - No")
                        print("RowOfExtRowHeader: ", RowOfExtRowHeader)
            else:
                line=copy.deepcopy(data[1-1])
                RowOfIneRowHeader=line[2-1:Lmin]
                for i in range(2, Q+1):
                    line=copy.deepcopy(data[i-1])
                    #L=len(line)
                    #ContentLine=line[2-1:L]
                    ContentLine=line[2-1:Lmin]
                    content.append(ContentLine)
                    RowOfExtRowHeader.append(line[1-1])
                #
                corner=copy.deepcopy(data[1-1][1-1])
                if vsh==1:
                    print("corner: ", corner)
                headers=ParseTableCorner(corner)
                if vsh==1:
                    print(" Headers: ", headers)
                TableName=headers[1-1]
                ExtRowsGeneralName=headers[2-1]
                IneRowsGeneralName=headers[3-1]
                if vsh==1:
                    print("RowOfExtRowHeaderExists & RowOfIneRowHeader - both exist")
                    print("RowOfExtRowHeader: ", RowOfExtRowHeader)
                    print("RowOfIneRowHeader: ", RowOfIneRowHeader)
        if ext_LC_0_CL_1==0:
            LineOfColHeader=copy.deepcopy(RowOfIneRowHeader)
            ColOfLineHeader=copy.deepcopy(RowOfExtRowHeader)
            LinesGeneralName=ExtRowsGeneralName
            ColumnsGeneralName=IneRowsGeneralName
        else:
            ColOfLineHeader=copy.deepcopy(RowOfIneRowHeader)
            LineOfColHeader=copy.deepcopy(RowOfExtRowHeader)
            ColumnsGeneralName=ExtRowsGeneralName
            LinesGeneralName=IneRowsGeneralName
        self.Set(content, LineOfColHeader, ColOfLineHeader, TableHeaders(TableName, LinesGeneralName, ColumnsGeneralName), ext_LC_0_CL_1, ine_LC_0_CL_1, vsh)   
        if vsh==1:
            print("Set_By2DArray finishes working")

    def Set_ByContentHeadered(self, contentHeaderedExt, RowOfIneRowHeader, tableHeaders, ext_LC_0_CL_1=0, ine_LC_0_CL_1=0, vsh=0):
        self.Set_By2DArray(contentHeaderedExt, 1, 0, ext_LC_0_CL_1, ine_LC_0_CL_1, vsh)
        if ext_LC_0_CL_1==0:
            self.SetLineOfColHeader(RowOfIneRowHeader)
        else:
            self.SetColOfLineHeader(RowOfIneRowHeader)
        self.SetTableHeaders(tableHeaders)
        self.LC_0_CL_1=ine_LC_0_CL_1

    def Set_ByContentHeadered1(self, contentExt, RowOfIneRowHeader, tableHeaders, ext_LC_0_CL_1=0, ine_LC_0_CL_1=0, vsh=0):        
        self.SetContentAndItsHeaders_Inner(contentExt, ext_LC_0_CL_1, ine_LC_0_CL_1, vsh)
        if ext_LC_0_CL_1==0:
            self.SetLineOfColHeader(RowOfIneRowHeader)
        else:
            self.SetColOfLineHeader(RowOfIneRowHeader)
        self.SetTableHeaders(tableHeaders)
        self.LC_0_CL_1=ine_LC_0_CL_1

    def Set_ByContent_AndSeparateHeaders(self, contentExt, RowOfExtRowHeader, RowOfIneRowHeader, tableHeaders, ext_LC_0_CL_1=0, ine_LC_0_CL_1=0, vsh=0):
        self.Set_By2DArray(contentExt, 0, 0, ext_LC_0_CL_1, ine_LC_0_CL_1, vsh)
        if ext_LC_0_CL_1==0:
            self.SetLineOfColHeader(RowOfIneRowHeader)
            self.SetColOfLineHeader(RowOfExtRowHeader)
        else:
            self.SetColOfLineHeader(RowOfIneRowHeader)
            self.SetLineOfColHeader(RowOfExtRowHeader)
        self.SetTableHeaders(tableHeaders)
        #self.SetContent(content, ext_LC_0_CL_1, ine_LC_0_CL_1, vsh)
        #self.LC_0_CL_1=ine_LC_0_CL_1

    def Set(self, content, LineOfColHeader=[], ColOfLineHeader=[], tableHeader=[], ext_LC_0_CL_1=0, ine_LC_0_CL_1=0, vsh=0):
        if vsh==1:
            print("Set starts working")
            print("Arguments:")
            print("Content:")
            print(content)
        self.SetContent(content, ext_LC_0_CL_1, ine_LC_0_CL_1, vsh)
        self.SetLineOfColHeader(LineOfColHeader)
        self.SetColOfLineHeader(ColOfLineHeader)
        self.SetTableHeaders(tableHeader)
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

    def GetQExtRows(self):
        return len(self.content)

    def GetQIneRows(self):
        Lmin=Get2DArrayMinLength(self.content)
        Lmax=Get2DArrayMaxLength(self.content)
        L=Lmin
        return L

    def GetQLines():
        QExtRows=self.GetQExtRows()
        QIneRows=self.GetQIneRows()
        if self.LC_not_CL==0:
            QLines=QExtRows
            Colunms=QIneRows
        else:
            QLines=QIneRows
            Colunms=QExtRows
        return QLines

    def GetQColumns():
        QExtRows=self.GetQExtRows()
        QIneRows=self.GetQIneRows()
        if self.LC_not_CL==0:
            QLines=QIneRows
            Colunms=QExtRows
        else:
            QLines=QExtRows
            Colunms=QIneRows
        return Colunms

    def GetSize(self):
        R=TableSize(self.GetQLines(), self.GetQColumns())
        return R
            

    #def SetContentHeadered(self, content, ext_LC_0_CL_1=0, ine_LC_0_CL_1=0):
    #
    #def SetContentItself(self, content, ext_LC_0_CL_1=0, ine_LC_0_CL_1=0):
    #
    def SetContent(self, contentExt, ext_LC_0_CL_1=0, ine_LC_0_CL_1=0, vsh=0):
        contentCopied=copy.deepcopy(contentExt)
        Q=len(contentCopied)
        HdrRow=[]
        content=[]
        if vsh==1:
            print("SetContent starts working")
            print(contentCopied)
            print("content[1]=",contentCopied[1-1])
        if(Q>0):
            if isinstance(contentCopied, list) and len(contentCopied)>0:
                if isinstance(contentCopied[1-1], list) and len(contentCopied[1-1])>1:
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
                elif isinstance(contentCopied[1-1], list) and len(contentCopied[1-1])==1:
                    if vsh==1:
                        print("list has single column")
                    for i in range(1, Q+1):
                        rowE=[]
                        element=contentCopied[i-1][1-1]
                        cell=DataCell(element)
                        rowE.append(cell)
                        self.content.append(rowE)
                else:#is not list
                    if vsh==1:
                        print("list element is not list")
                    content=contentCopied
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
        if ext_LC_0_CL_1!=ine_LC_0_CL_1:
            Transpose2DArray(self.content)
        #
        self.LC_0_CL_1=ine_LC_0_CL_1==0
        if vsh==1:
            print("SetContent finishes working")
    #fn
    def SetContentAndItsHeaders_Inner(self, contentExt, ext_LC_0_CL_1=0, ine_LC_0_CL_1=0, vsh=0):
        content=[]
        RowOfExtRowHeader1=[]
        RowOfExtRowHeader2=[]
        Q=0
        if vsh==1:
            print("SetContentAndItsHeaders_Inner starts working")
        contentCopied=copy.deepcopy(contentExt)
        if isinstance(contentCopied, list):
            if vsh==1:
                print("contentCopied is list")
            Q=len(contentCopied)
            if len(contentCopied)>0:
                if vsh==1:
                    print("Q=_str(Q)>0")
                if isinstance(contentCopied[1-1],list):
                    if vsh==1:
                        print("contentCopied[1] is list")
                    minL=Get2DArrayMinLength(contentCopied)
                    maxL=Get2DArrayMaxLength(contentCopied)
                    row=[]
                    if len(contentCopied[1-1])>0:
                        if vsh==1:
                            print("len(contentCopied[1])>0")
                        if len(contentCopied[1-1])==2:
                            if vsh==1:
                                print("len(contentCopied[1])==2")
                            if isinstance(contentCopied[1-1][1-1],list) and not isinstance(contentCopied[1-1][2-1],list):
                                if vsh==1:
                                    print("ContentCopied[1-1][1-1] is list, ContentCopied[1-1][2-1] is not list")
                                for i in range(1, Q+1):
                                    row1=[]
                                    row2=[]
                                    RowOfExtRowHeader1.append(contentCopied[i-1][2-1])
                                    element=copy.deepcopy(RowOfExtRowHeader1[i-1])
                                    cell=DataCell(element)
                                    RowOfExtRowHeader2.append(cell)
                                    #
                                    row1=copy.deepcopy(contentCopied[i-1][1-1])
                                    curL=len(row1)
                                    L=curL
                                    sL="";
                                    for j in range(1,L+1):
                                        element=copy.deepcopy(row1[j-1])
                                        cell=DataCell(element)
                                        row2.append(cell)
                                        sL=cell.ToString()+" "
                                    content.append(row2)
                                    if vsh==1:
                                        print("Row "+str(i)+" Header: "+cell.ToString()+" Content: "+sL)
                            elif not isinstance(contentCopied[1-1][1-1],list) and  isinstance(contentCopied[1-1][2-1],list):#
                                if vsh==1:
                                    print("ContentCopied[1-1][1-1] is not list, ContentCopied[1-1][2-1] is  list")
                                for i in range(1, Q+1):
                                    row1=[]
                                    row2=[]
                                    RowOfExtRowHeader1.append(contentCopied[i-1][1-1])
                                    element=copy.deepcopy(RowOfExtRowHeader1[i-1])
                                    cell=DataCell(element)
                                    RowOfExtRowHeader2.append(cell)
                                    #
                                    row1=copy.deepcopy(contentCopied[i-1][2-1])
                                    curL=len(row1)
                                    L=curL
                                    for j in range(1,L+1):
                                        element=copy.deepcopy(row1[j-1])
                                        cell=DataCell(element)
                                        row2.append(cell)
                                    content.append(row2)
                            elif not isinstance(contentCopied[1-1][1-1],list) and not isinstance(contentCopied[1-1][2-1],list):
                                for i in range(1, Q+1):
                                    row1=[]
                                    row2=[]
                                    row1=copy.deepcopy(contentCopied[i-1])
                                    curL=len(row1)
                                    L=curL
                                    for j in range(1,L+1):
                                        element=copy.deepcopy(row1[j-1])
                                        cell=DataCell(element)
                                        row2.append(cell)
                                    content.append(row2)
                        else:#  len(contentCopied[1-1])!=2:
                            for i in range(1, Q+1):
                                row1=[]
                                row2=[]
                                row1=copy.deepcopy(contentCopied[i-1])
                                curL=len(row1)
                                L=curL
                                for j in range(1,L+1):
                                    element=copy.deepcopy(row1[j-1])
                                    cell=DataCell(element)
                                    row2.append(cell)
                                content.append(row2)
                    else:#len(contentCopied[1-1])==0:
                        pass
                else:#not isinstance(contentCopied[1-1],list):
                    if isinstance(contentCopied[1-1],DataCellRowWithHeader):
                        for i in range(1, Q+1):
                            row1=[]
                            row2=[]
                            #
                            RowOfExtRowHeader2.append(contentCopied[i-1].header)
                            #
                            row1=copy.deepcopy(contentCopied[i-1].row)
                            curL=len(row1)
                            L=curL
                            for j in range(1,L+1):
                                element=copy.deepcopy(row1[j-1])
                                cell=DataCell(element)
                                row2.append(cell)
                            content.append(row2)
                    elif isinstance(contentCopied[1-1],DataCellRow):
                        for i in range(1, Q+1):
                            row1=[]
                            row2=[]
                            #
                            row1=copy.deepcopy(contentCopied[i-1].row)
                            curL=len(row1)
                            L=curL
                            for j in range(1,L+1):
                                element=copy.deepcopy(row1[j-1])
                                cell=DataCell(element)
                                row2.append(cell)
                            content.append(row2)
                    else:#rows ol length=1
                        for i in range(1, Q+1):
                            row1=[]
                            row2=[]
                            #
                            element=copy.deepcopy(contentCopied[i-1])
                            row1.append(element)
                            curL=len(row1)
                            L=curL
                            for j in range(1,L+1):
                                element=copy.deepcopy(row1[j-1])
                                cell=DataCell(element)
                                row2.append(cell)
                            content.append(row2)          
        else:#not isinstance(contentCopied, list):
            for i in range(1, Q+1):
                element=copy.deepcopy(contentCopied[i-1])
                row1.append(element)
                curL=len(row1)
                L=curL
                for j in range(1,L+1):
                    element=copy.deepcopy(row1[j-1])
                    cell=DataCell(element)
                    row2.append(cell)
                content.append(row2)
        #
        if content!=[]:
            if ext_LC_0_CL_1!=ine_LC_0_CL_1:
                Transpose2DArray(content)
            self.content=copy.deepcopy(content)
        if RowOfExtRowHeader2!=[]:
            if ext_LC_0_CL_1==0:    
                self.ColOfLineHeader=copy.deepcopy(RowOfExtRowHeader2)
            else:
                self.LineOfColHeader=copy.deepcopy(RowOfExtRowHeader2)
        if vsh==1:
            print("SetContentAndItsHeaders_Inner finishes working")        
   
        
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

    def SetTableHeaders(self, TableHeader="", LinesGeneralHeader="", ColumnsGeneralHeader="", vsh=0):
        self.TableHeader=TableHeaders(TableHeader, LinesGeneralHeader, ColumnsGeneralHeader, vsh)
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

    def GetStructRowOrderLC0CL1(self):
        return self.LC_0_CL_1
    
    def GetIf_LineOfColHeaderExists(self):
        R=0
        if self.LineOfColHeader!=0 and self.LineOfColHeader!=[]:
            R=1
        return R
    
    def GetIf_ColOfLineHeaderExists(self):
        R=0
        if self.ColOfLineHeader!=0 and self.ColOfLineHeader!=[]:
            R=1
        return R
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
    def GetContentRowExt_AsList_OfDataCells(self, ExtRowN):
        row=Get2DArrayExtRowN(self.content, ExtRowN)
        return row

    def GetContentRowExt_AsList_OfVals(self, ExtRowN):
        #row=Get2DArrayExtRowN(self.content, ExtRowN)
        #R=[]
        #Q=len(row)
        #for i in range(1, Q+1):
        #    cell=row[i-1]
        #    val=cell.GetVal()
        #    R.append(val)
        R=[]
        row=Get2DArrayExtRowN(self.content, ExtRowN)
        cellRow=DataCellRow(row)
        R=cellRow.GetContent_AsList_OfVals()
        return R

    def GetContentRowExt_AsList_OfCurItems(self, ExtRowN):
        #row=Get2DArrayExtRowN(self.content, ExtRowN)
        #R=[]
        #Q=len(row)
        #for i in range(1, Q+1):
        #    cell=row[i-1]
        #    curItem=cell.GetItem()
        #    R.append(curItem)
        R=[]
        row=Get2DArrayExtRowN(self.content, ExtRowN)
        cellRow=DataCellRow(row)
        R=cellRow.GetContent_AsList_OfCurItems()
        return R
    
    def GetContentRowExt_AsDataCellRow(self, ExtRowN):
        #R=DataCellRow1()
        #Q=len(self.content)
        #if(ExtRowN>=1 and ExtRowN<=Q):
        #    row=DataCellRow1(self.content[ExtRowN-1])
        #    R=DataCellRow1(row)
        R=DataCellRow()
        row=Get2DArrayExtRowN(self.content, ExtRowN)
        R.Set(row)
        return R

    def GetContentRowIne_AsList_OfDataCells(self, IneRowN):
        row=Get2DArrayIneRowN(self.content, IneRowN) 
        return row

    def GetContentRowIne_AsList_OfVals(self, IneRowN):
        row=Get2DArrayIneRowN(self.content, IneRowN)
        R=[]
        Q=len(row)
        for i in range(1, Q+1):
            cell=row[i-1]
            val=cell.GetVal()
            R.append(val)
        return R

    def GetContentRowIne_AsList_OfCurItems(self, IneRowN):
        row=Get2DArrayIneRowN(self.content, IneRowN)
        R=[]
        Q=len(row)
        for i in range(1, Q+1):
            cell=row[i-1]
            curItem=cell.GetItem()
            R.append(curItem)
        return R
    
    def GetContentRowIne_AsDataCellRow(self, IneRowN):
        R=DataCellRow1()
        row=Get2DArrayIneRowN(self.content, IneRowN)
        R=DataCellRow1(row)
        return R
        
    def GetContentLine_AsList_OfDataCells(self, LineN):
        R=[]
        if self.LC_0_CL_1==0:
            ExtRowN=LineN
            IneRowN=ColN
            R=self.GetContentRowExt_AsList_OfDataCells(ExtRowN)
        else:
            ExtRowN=ColN
            IneRowN=LineN
            R=self.GetContentRowIne_AsList_OfDataCells(IneRowN)
        return R

    def GetContentLine_AsList_OfVals(self, LineN):
        R=[]
        if self.LC_0_CL_1==0:
            ExtRowN=LineN
            #IneRowN=ColN
            R=self.GetContentRowExt_AsList_OfVals(ExtRowN)
        else:
            #ExtRowN=ColN
            IneRowN=LineN
            R=self.GetContentRowIne_AsList_OfVals(IneRowN)
        return R

    def GetContentLine_AsList_OfCurItems(self, LineN):
        R=[]
        if self.LC_0_CL_1==0:
            ExtRowN=LineN
            #IneRowN=ColN
            R=self.GetContentRowExt_AsList_OfCurItems(ExtRowN)
        else:
            ExtRowN=ColN
            #IneRowN=LineN
            R=self.GetContentRowIne_AsList_OfCurItems(IneRowN)
        return R

    def GetContentLineWithHeader_AsListNested_OfDataCells(self, LineN):
        R=[]
        hdr=""
        cnt=self.etContentLine_AsList_OfDataCells(LineN)
        if self.ColOfLineHeader!=[]:
            hdr=self.ColOfLineHeader[LineN-1]
        R=[hdr, cnt]
        return R

    def GetContentLineWithHeader_AsListNested_OfVals(self, LineN):
        R=[]
        #hdr=""
        hdrVal=""
        cnt=self.etContentLine_AsList_OfVals(LineN)
        if self.ColOfLineHeader!=[]:
            hdr=self.ColOfLineHeader[LineN-1]
            hdrVal=hdr.GetVal()
        R=[hdrVal, cnt]
        return R

    def GetContentLineWithHeader_AsListNested_OfCurItems(self, LineN):
        R=[]
        #hdr=""
        hdrVal=""
        cnt=self.etContentLine_AsList_OfCurItems(LineN)
        if self.ColOfLineHeader!=[]:
            hdr=self.ColOfLineHeader[LineN-1]
            hdrVal=hdr.GetItem()
        R=[hdrVal, cnt]
        return R
    
    def GetContentLine_AsDataCellRow(self, LineN):
        R=DataCellRow1()
        if self.LC_0_CL_1==0:
            ExtRowN=LineN
            #IneRowN=ColN
            R=self.GetContentRowExt_AsDataCellRow(ExtRowN)
        else:
            #ExtRowN=ColN
            IneRowN=LineN
            R=self.GetContentRowIne_AsDataCellRow(IneRowN)
        return R

    def GetContentColumn_AsList_OfDataCells(self, ColN):
        R=[]
        if self.LC_0_CL_1==0:
            #ExtRowN=LineN
            IneRowN=ColN
            R=self.GetContentRowIne_AsList_OfDataCells(IneRowN)
        else:
            #ExtRowN=ColN
            IneRowN=LineN
            R=self.GetContentRowExt_AsList_OfDataCells(ExtRowN)
        return R

    def GetContentColumn_AsList_OfVals(self, ColN):
        R=[]
        if self.LC_0_CL_1==0:
            #ExtRowN=LineN
            IneRowN=ColN
            R=self.GetContentRowIne_AsList_OfVals(IneRowN)
        else:
            ExtRowN=ColN
            #IneRowN=LineN
            R=self.GetContentRowExt_AsList_OVals(ExtRowN)
        return R

    def GetContentColumn_AsList_OfCurItems(self, ColN):
        R=[]
        if self.LC_0_CL_1==0:
            #ExtRowN=LineN
            IneRowN=ColN
            R=self.GetContentRowIne_AsList_OfCurItems(IneRowN)
        else:
            ExtRowN=ColN
            #IneRowN=LineN
            R=self.GetContentRowExt_AsList_OCurItems(ExtRowN)
        return R

    def GetContentColumnWithHeader_AsListNested_OfDataCells(self, ColN):
        R=[]
        cnt=self.GetContentColumn_AsList_OfDataCells(ColN) 
        hdr=""
        if self.LineOfColHeader!=[]:
            hdr=self.LineOfColHeader_OfDataCells[ColN-1]
        R=[hdr, cnt]
        return R

    def GetContentColumnWithHeader_AsListNested_OfVals(self, ColN):
        R=[]
        cnt=self.GetContentColumn_AsList_OfVals(ColN) 
        #hdr=""
        hdrVal=""
        if self.LineOfColHeader!=[]:
            hdr=self.LineOfColHeader_OfDataCells[ColN-1]
            hdrVal=hdr.GetVal()
        R=[hdrVal, cnt]
        return R

    def GetContentColumnWithHeader_AsListNested_OfCurItems(self, ColN):
        R=[]
        cnt=self.GetContentColumn_AsList_OfCurItems(ColN) 
        #hdr=""
        hdrVal=""
        if self.LineOfColHeader!=[]:
            hdr=self.LineOfColHeader_OfDataCells[ColN-1]
            hdrVal=hdr.GetItem()
        R=[hdrVal, cnt]
        return R
    
    def GetContentColumn_AsDataCellRow(self, ColN):
        R=DataCellRow1()
        if self.LC_0_CL_1==0:
            #ExtRowN=LineN
            IneRowN=ColN
            R=self.GetContentRowExt_AsDataCellRow(ExtRowN)
        else:
            ExtRowN=ColN
            #IneRowN=LineN
            R=self.GetContentRowIne_AsDataCellRow(IneRowN)
        return R

    def GetContent(self):
        return self.content

    def GetContent_Vals(self):
        content=[]
        Q=len(self.content)
        if self.LC_0_CL_1==0:
            for i in range(1, Q+1):
                row=self.GetContentLine_AsList_OfVals(i)
                content.append(row)
        else:
            for i in range(1, Q+1):
                row=GetContentColumn_AsList_OfVals(i)
                content.append(row)
        return content

    def GetContent_CurItems(self):
        content=[]
        Q=len(self.content)
        if self.LC_0_CL_1==0:
            for i in range(1, Q+1):
                row=self.GetContentLine_AsList_OfCurItems(i)
                content.append(row)
        else:
            for i in range(1, Q+1):
                row=self.GetContentColumn_AsList_OfCurItems(i)
                content.append(row)
        return content
            

    def GetLine_WithHeader(self, LineN):
        R=[]
        if LineN>=1 and LineN<=self.GetQLines():
            row=self.GetContentLine_AsDataCellRow(LineN)
            if self.ColOfLineHeader==[]:
                header=""
            else:
                header=GetCell_ColOfLineHeader_AsCopy(LineN)
            R=DataCellRowWithHeader(row, header)
        return R

    def GetColumn_WithHeader(self, ColN):
        R=[]
        if ColN>=1 and ColN<=self.GetQColumns():
            row=self.GetContentColumn_AsDataCellRow(ColN)
            if self.LineOfColHeader==[]:
                header=""
            else:
                header=GetCell_LineOfColHeader_AsCopy(ColN)
            R=DataCellRowWithHeader(row, header)
        return R

    def GetLineOfColHeader_WithGeneralName(self):
        R=[]
        if self.LineOfColHeader!=[] and isinstance(self.LineOfColHeader, list) and len(self.LineOfColHeader)>0:
            row=copy.deepcopy(self.LineOfColHeader)
            if self.TableHeader==[] and isinstance(self.TableHeader, TableHeaders) and isinstance(self.TableHeader.ColumnsGeneralHeader, DataCell):
                header=copy.deepcopy(self.TableHeader.ColumnsGeneralHeader)
            else:
                header=""
            R=DataCellRowWithHeader(row, header)
        return R

    def GetColOfLineHeader_WithGeneralName(self):
        R=[]
        if self.ColOfLineHeader!=[] and isinstance(self.ColOfLineHeader, list) and len(self.ColOfLineHeader)>0:
            row=copy.deepcopy(self.ColOfLineHeader)
            if self.TableHeader==[] and isinstance(self.TableHeader, TableHeaders) and isinstance(self.TableHeader.LinesGeneralHeader, DataCell):
                header=copy.deepcopy(self.TableHeader.LinesGeneralHeader)
            else:
                header=""
            R=DataCellRowWithHeader(row, header)
        return R

    #def GetCellSurrounding(self, LineN, ColN, Repr=[]):
    #    if LineN>=1 and LineN<=self.GetQLines() and ColN>=1 and ColN<=self.GetQColumns():
    #        cell=self.GetCell_AsCopy(LineN, ColN)
    #        cellTxt=str(self.cell.GetVal())
    #        if self.LineOfColHeaderCell!=[]:
    #            #cell=self.self.LineOfColHeaderCell[ColN-1]
    #            LineOfColHeaderCellText=self.ToString_Cell_LineOfColHeader(ColN)
    #        elif isinstance(Repr, TableRepr) and isinstance(Repr.general, TableRepr_General) and Repr.general.ShowColumnsGeneralHeader==1:
    #            pass
            
    #
    #def ToString(self, LineN, ColN, sBef="", sAft=""):
    #    cell=0
    #    s=""
    #    cell=self.GetCell_AsCopy(LineN, ColN)
    #    if isinstance(cell, DataCell):
    #        s=cell.ToString()
    #        s=sBef+s
    #        s=s+sAft
    #    return s
        
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
    #
    def ToString_Cell(self, LineN, ColN, tblRepr=[], vsh=0):
        s=""
        #LineN
        #ColN
        CellSelfText=""
        LHSelfText=""
        CHSelfText=""
        LGHSelfTex=""
        CGHSelfText=""
        THdrSelfText=""
        LNToShow=LineN
        CNToShow=ColN
        if vsh==1:
            print("ToString_Cell starts working")
            if isinstance(tblRepr.general, TableRepr_General):
                print(tblRepr.general.ToString())
            else:
                print("General repr not defined")
            #if isinstance(tblRepr.LoCH, TableRepr_RowHeaderCell):
            #    print(tblRepr.LoCH.ToString())
            #else:
            #    print("LoCH repr not defined")
            if isinstance(tblRepr.CoLH, TableRepr_RowHeaderCell):
                print(tblRepr.CoLH.ToString())
            else:
                print("CoLH repr not defined")
            if isinstance(tblRepr.LoCH, TableRepr_RowHeaderCell):
                print(tblRepr.LoCH.ToString())
            else:
                print("LoCH repr not defined")
            if isinstance(tblRepr.Cont, TableRepr_ContentCell):
                print(tblRepr.Cont.ToString())
            else:
                print("Cont repr not defined")
        if isinstance(tblRepr, TableRepr):
            LNToShow=tblRepr.CalcLineNToShow(LineN)
            CNToShow=tblRepr.CalcColumnNToShow(ColN)
            if vsh==1:
                print("tblRepr is TableRepr")
                print("rows numbers to represent: L="+str(LNToShow)+" C="+str(CNToShow))
        if isinstance(self.TableHeader, TableHeaders):
            cell=self.TableHeader.GetTableHeader()
            if cell!="" and isinstance(cell, DataCell):
                THdrSelfText=cell.ToString()
            else:
                THdrSelfText=cell#==""
            if vsh==1:
                print("THdrSelfText="+THdrSelfText)
            cell=self.TableHeader.GetLinesGeneralHeader()
            if cell!="" and isinstance(cell, DataCell):
                LGHSelfText=cell.ToString()
            else:
                LGHSelfText=cell#==""
            if vsh==1:
                print("LGHSelfText="+LGHSelfText)
            cell=self.TableHeader.GetColumnsGeneralHeader()
            if cell!="" and isinstance(cell, DataCell):
                CGHSelfText=cell.ToString()
            else:
                CGHSelfText=cell#==""
            if vsh==1:
                print("CGHSelfText="+CGHSelfText)
        if LineN==0  and ColN>=1 and ColN<=self.GetQColumns():#LineOfColHeader
            s=self.ToString_Cell_LineOfColHeader(self, ColN, tblRepr, vsh=0)
        elif ColN==0 and LineN>=1 and LineN<=self.GetQLines():#ColOfLineHeader
            s=self.ToString_Cell_ColOfLineHeader(self, LineN, tblRepr, vsh=0) 
        elif LineN>=1 and LineN<=self.GetQLines() and ColN>=1 and ColN<=self.GetQColumns():
            cell=self.GetCell_AsCopy(LineN, ColN)
            CellSelfText=cell.ToString()
            if self.LineOfColHeader!=[]:
                CHSelfText=self.LineOfColHeader[ColN-1].ToString()
            elif isinstance(tblRepr, TableRepr) and isinstance(tblRepr.general, TableRepr_General) and tblRepr.general.ShowLineOfColHeader==1 and isinstance(tblRepr.LoCH, TableRepr_RowHeaderCell):
                CHSelfText=tblRepr.GetLineOfColHeaderCellByRepr(ColN, "", CNToShow, CGHSelfText)
            if self.ColOfLineHeader!=[]:
                LHSelfText=self.ColOfLineHeader[LineN-1].ToString()
            elif isinstance(tblRepr, TableRepr) and isinstance(tblRepr.general, TableRepr_General) and tblRepr.general.ShowLineOfColHeader==1 and isinstance(tblRepr.LoCH, TableRepr_RowHeaderCell):
                LHSelfText=tblRepr.GetColOfLineHeaderCellByRepr(LineN, "", LNToShow, LGHSelfTex)
            if isinstance(tblRepr, TableRepr):
                s=tblRepr.GetContentCellByRepr(LineN, ColN, CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh=0)
            else:
                s=cell.ToString()
            if vsh==1:
                print("s= "+s)
                print("ToString_Cell finishes working")
        return s

    #def StringContentCellAft(self, TableReprSimple):
    #   s=""
    #   
    ##    return s
    #
    #def StringLineOfColHeaderCellBef(self, TableReprSimple):
    #    s=""
    #
    #    return s
    #
    #def StringLineOfColHeaderCellAft(self, TableReprSimple):
    #    s=""
    #
    #    return s
    #
    #def StringColOfLineHeaderCellBef(self, TableReprSimple):
    #    s=""
    #
    #    return s
    #
    #def StringColOfLineHeaderCellAft(self, TableReprSimple):
    #    s=""
    #
    #    return s
    #
    #
    #def LineOfColHeaderCellSurrounding
    
    def ToString_Cell_LineOfColHeader(self, ColN, Repr=[], vsh=0):
        cell=0
        s=""
        rs=""
        LoCHCellSelfText=""
        CGHSelfText=""
        if vsh==1:
            print("ToString_Cell_LineOfColHeader starts working") 
        if self.LineOfColHeader!=[]:
            cell=self.GetCell_LineOfColHeader_AsCopy(ColN)
            if isinstance(cell, DataCell):
                LoCHCellSelfText=cell.ToString()
                #s=sBef+s
                #s=s+sAft
                if vsh==1:
                    print("Cell_LineOfColHeader own text, without supplememts: "+LoCHCellSelfText)
        else:
            if vsh==1:
                print("LineOfColHeader does not exist: self text is empty: "+LoCHCellSelfText)
        if isinstance(self.TableHeader, TableHeaders):
            cell=self.TableHeader.GetColumnsGeneralHeader()
            if cell!="" and isinstance(cell, DataCell):
                CGHSelfText=cell.ToString()
                if vsh==1:
                    print("ColumnsGeneralHeader: "+CGHSelfText)
            else:
                CGHSelfText=cell
                if vsh==1:
                    print("ColumnsGeneralHeader is empty")
            #cell=self.TableHeader.GetTableHeader()
            #LGHSelfText=cell.ToString()
        if isinstance(Repr, TableRepr) and isinstance(Repr.general, TableRepr_General) and Repr.general.ShowLineOfColHeader==1 and isinstance(Repr.LoCH, TableRepr_RowHeaderCell):
            s=Repr.GetLineOfColHeaderCellByRepr(ColN, LoCHCellSelfText, CGHSelfText, vsh)
            if vsh==1:
                print("Representation rules are defined")
                Repr.ShowToConsole()
        else:
            s=LoCHCellSelfText
            if vsh==1:
                print("Representation rules are not defined")
        if vsh==1:
            print("Finally: "+s)
            print("ToString_Cell_LineOfColHeader finishes working")
        return s

    def ToString_Cell_ColOfLineHeader(self, LineN, tblRepr=[], vsh=0):#
        cell=0
        s=""
        CoLHCellSelfText=""
        LGHSelfText=""
        if vsh==1:
            print("ToString_Cell_ColOfLineHeader starts working")
        if self.LineOfColHeader!=[]:
            cell=self.GetCell_ColOfLineHeader_AsCopy(LineN)
            if isinstance(cell, DataCell):
                CoLHCellSelfText=cell.ToString()
                #s=sBef+s
                #s=s+sAft
                if vsh==1:
                    print("Cell_ColOfLineHeader own text, without supplememts: "+CoLHCellSelfText)
        else:
            if vsh==1:
                print("ColOfLineHeader does not exist")
        if vsh==1:
            print(" CoLH Cell's surrounding:")
        if isinstance(self.TableHeader, TableHeaders):
            cell=self.TableHeader.GetLinesGeneralHeader()
            if cell!="" and isinstance(cell, DataCell):
                LGHSelfText=cell.ToString()
                if vsh==1:
                    print("Lines general header: "+LGHSelfText)
            else:
                LGHSelfText=cell
                if vsh==1:
                    print("Lines general header is empty")
            #cell=self.TableHeader.GetTableHeader()
            #LGHSelfText=cell.ToString()
        if isinstance(tblRepr, TableRepr) and isinstance(tblRepr.general, TableRepr_General) and isinstance(tblRepr.CoLH, TableRepr_RowHeaderCell) and tblRepr.general.ShowColOfLineHeader==1 and isinstance(tblRepr.LoCH, TableRepr_RowHeaderCell):
            s=tblRepr.GetColOfLineHeaderCellByRepr(LineN, CoLHCellSelfText, LGHSelfText,  vsh)
            if vsh==1:
                print("Representation rules are defined")
                tblRepr.ShowToConsole()
        else:
            s=CoLHCellSelfText
            if vsh==1:
                print("Representation rules are NOT defined")
        if vsh==1:
            print("Finally: "+s)
            print("ToString_Cell_ColOfLineHeader finishes working")
        return s

    def ToString_LineOfColHeader(self, delim=" ", tblRepr=[], vsh=0):
        s=""
        QC=self.GetQColumns()
        if vsh==1:
            print("ToString_Cell_ColOfLineHeader starts working") 
        if self.LineOfColHeader!=[]:
            for ColN in range(1, QC-1+1):
                s=s+self.ToString_Cell_LineOfColHeader(ColN, tblRepr, vsh)
                s=s+delim
            if QC>0:
                s=s+self.ToString_Cell_LineOfColHeader(QC, tblRepr, vsh)
        return s

    def ToString_HeaderLine(self, delim=" ", delimHdr=": ", tblRepr=[], vsh=0):
        s=""
        #sBefLoCH=""
        #sAftLoCH=""
        #sBefCoLH=""
        #sAftCoLH=""
        sC=self.ToString_HeaderCorner()#sBefLoCH, sAftLoCH, sBefCoLH, sAftCoLH)
        #sL=self.ToString_LineOfColHeader(delim, sBef, sAft)
        sL=self.ToString_LineOfColHeader(delim, tblRepr, vsh)
        #if isinstance self.
        s=s+sC
        if sC!="" and sL!="":
            s=s+delimHdr
        s=s+sL
        return s
        
    def ToString_ContentLine(self, LineN, delim=" ", tblRepr=[], vsh=0):
        s=""
        QC=self.GetQColumns()
        for i in range(1, QC-1+1):
            #cell=self.GetCell_AsCopy(LineN, i)
            #s=s+cell.ToString(sBef, sAft)
            s=s+self.ToString_Cell(LineN, i, tblRepr, vsh)
            s=s+delim
        if QC>0:
            #cell=self.GetCell_AsCopy(LineN, QC)
            #s=s+cell.ToString(sBef, sAft)
            s=s+self.ToString_Cell(LineN, QC, tblRepr, vsh)
        return s

    def ToString_Line(self, LineN, delim=" ", delimHdr=": ", tblRepr=[], vsh=0):
        s=""
        if vsh==1:
            print("ToString_Line starts working")
            print("Line header")
        sHdr=self.ToString_Cell_ColOfLineHeader(LineN, tblRepr, vsh)
        if vsh==1:
            print("LH="+sHdr)
            print("Line Content:")
        sCnt=self.ToString_ContentLine(LineN, delim, tblRepr, vsh)
        if vsh==1:
            print("CL="+sCnt)
        s=s+sHdr
        if sHdr!="" and sCnt!="":
            s=s+delimHdr
        s=s+sCnt
        if vsh==1:
            print("Finally: "+s)
            print("ToString_Line finishes working")
        return s

    def MaxColOfLineHeaderLen(TableReprSimple=[]):
        Lmax=0
        lens=[]
        if LineOfColHeader!=[]:
            QL=self.GetQLines()
            for i in range(1,QL+1):
                L=len(ToString_Cell_ColOfLineHeader(i))
                #if((i==1) or (i>1 and L>Lmax)):#inv syntax - but here syntax s'gut, ma above wa no bracket
                #if i==1 or (i>1 and L>Lmax):#inv syntax - but here syntax s'gut, ma above wa no bracket
                if i==1 or (i>1 and L>Lmax):
                    Lmax=L
        return Lmax

    def MaxColLen(ColN, TableReprSimple=[]):
        Lmax=0
        lens=[]
        if ColN>=1 and ColN<=self.GetQColumns():
            QL=self.GetQLines()
            for i in range(1,QL+1):
                L=len(StringContentCellBef(i, ColN, TableReprSimple))
                if i==1 or (i>1 and L>Lmax):
                    Lmax=L
        return Lmax

    def MaxColWithHdrLen(ColN, TableReprSimpleExt=[]):# not finished!
        Lmax=0
        lens=[]
        if ColN>=1 and ColN<=self.GetQColumns():
            QL=self.GetQLines()
            for i in range(1,QL+1):
                L=len(StringContentCellBef(i, ColN, TableReprSimple))
                if i==1 or (i>1 and L>Lmax):
                    Lmax=L
            LMaxCont=Lmax
            if self.LinOfColHeader!=0 or (TableReprSimpleExt!=[] and TableReprSimpleExt.GetIfLineOfColHeaderToShow()==1):
                psss#s=self.
        return Lmax


    #def GetContent_AsDataCells(self):
    #    return self.content 
    #
    #def GetContent_AsDataVals(self):
    #    content=[]
    #    row=[]
    #    QL=self.GetQLines()
    #    QC=self.etQColumns()
    #    if self.LC_0_CL_1==0:
    #        for i in range(1, QL+1):
    #            row=self. GetContentLine_AsList_OfVals(i)
    #            content.append(row)
    #    else:
    #        for i in range(1, QC+1):
    #            row=self. GetContentColumn_AsList_OfVals(i)
    #            content.append(row)
    #    return content
    #
    #def GetContent_AsDataCurItems(self):
    #   content=[]
    #    row=[]
    #    QL=self.GetQLines()
    #    QC=self.etQColumns()
    #    if self.LC_0_CL_1==0:
    #        for i in range(1, QL+1):
    #            row=self.GetContentLine_AsList_OfCurItems(i)
    #            content.append(row)
    #    else:
    #        for i in range(1, QC+1):
    #            row=self.GetContentColumn_AsList_OfCurItems(i)
    #           content.append(row)
    #     return content

    def ShowToConsole(self, delim=" ", delimHdr=": ", tblRepr=[], vsh=0):
        print(self.ToString_TableName())
        #print("HL:",self.ToString_HeaderLine(delim, delimHdr))
        print(self.ToString_HeaderLine(delim, delimHdr))
        QL=self.GetQLines()
        for i in range(1, QL+1):
            #print(i," ", self.ToString_Line(i, delim, delimHdr, tblRepr, vsh))
            print(self.ToString_Line(i, delim, delimHdr, tblRepr, vsh))
        print("(QLines="+str(QL)+")")

    #
    #def PrepareDataForTableColumn_IniV(self, rowCntExt=[], header="", DfltVal="", AddNotOtherAction=1, QToAddForEmpty=1, vsh=0):
    #    if vsh==1:
    #        print("PrepareDataForTableColumn starts working")
    #       QColumns=self.GetQColumns()
    #    rowLen=self.GetQLines()
    #    cellRow=DataCellRowWithHeader(rowCntExt, header)
    #    if vsh==1:
    #        print("Data for Column:")
    #        print(cellRow.ToString())
    #    rowToSet=[]
    #    dfltCell=DataCell(DfltVal)
    #    extL=cellRow.GetLength()
    #    #colToSet=cellRow.GetContent_AsList_OfCells()
    #    if QColumns==0:
    #        if AddNotOtherAction==1:
    #            if extL==0:
    #                for i in range(1, QToAddForEmpty+1):
    #                    rowToSet.append(dfltCell)
    #            else:
    #                cellRow.SetSize(rowLen, DfltVal)
    #                rowToSet=cellRow.GetContent_AsList_OfCells()
    #    else:
    #        if extL==0:
    #            for i in range(1, rowLen+1):
    #                rowToSet.append(dfltCell)
    #        else:
    #            cellRow.SetSize(rowLen, DfltVal)
    #            rowToSet=cellRow.GetContent_AsList_OfCells()
    #    if vsh==1:
    #        print("PrepareDataForTableColumn finishes working")
    #    return rowToSet

    def PrepareDataForTableColumn_HdrdCellRow(self, rowCntExt=[], header="", DfltVal="", AddNotOtherAction=1, QToAddForEmpty=1, vsh=0):
        if vsh==1:
            print("PrepareDataForTableColumn starts working")
        QColumns=self.GetQColumns()
        rowLen=self.GetQLines()
        cellRow=DataCellRowWithHeader(rowCntExt, header)
        if vsh==1:
            print("Data for Column:")
            print(cellRow.ToString())
        rowToSet=[]
        dfltCell=DataCell(DfltVal)
        extL=cellRow.GetLength()
        #colToSet=cellRow.GetContent_AsList_OfCells()
        if QColumns==0:
            if AddNotOtherAction==1:
                if extL==0:
                    for i in range(1, QToAddForEmpty+1):
                        rowToSet.append(dfltCell)
                    cellRow=DataCellRowWithHeader(rowToSet, header)
                else:
                    cellRow.SetSize(rowLen, DfltVal)
                    #rowToSet=cellRow.GetContent_AsList_OfCells()
        else:
            if extL==0:
                for i in range(1, rowLen+1):
                    rowToSet.append(dfltCell)
                cellRow=DataCellRowWithHeader(rowToSet, header)
            else:
                cellRow.SetSize(rowLen, DfltVal)
                #rowToSet=cellRow.GetContent_AsList_OfCells()
        if vsh==1:
            print("PrepareDataForTableColumn finishes working")
        return cellRow

    def PrepareDataForTableColumn_NestedListOfCells(self, rowCntExt=[], header="", DfltVal="", AddNotOtherAction=1, QToAddForEmpty=1, vsh=0):
        if vsh==1:
            print("PrepareDataForTableColumn starts working")
        cellRow=self.PrepareDataForTableColumn_HdrdCellRow(rowCntExt, header, DfltVal, AddNotOtherAction, QToAddForEmpty, vsh)
        contentRow=cellRow.GetContent_AsList_OfCells()
        hdrCell=cellRow.GetCell_AsCopy_header()
        if vsh==1:
            print("PrepareDataForTableColumn finishes working")
        return [hdrCell, contentRow]

    #def ExtractRowContentAsStrListFromPreparedData(self, preparedList):

    #def ExtractRowHeaderFromPreparedData(self, preparedList):
        

    #def PrepareDataForTableColumnContent(self, rowCntExt=[], header="", DfltVal="", AddNotOtherAction=1, QToAddForEmpty=1, vsh=0):
            #HeaderedColumn=PrepareDataForTableColumnGeneral(self, rowCntExt=[], header="", DfltVal="", AddNotOtherAction=1, QToAddForEmpty=1, vsh=0)
               
    def SetColumn(self, ColN, rowCntExt=[], header="", DfltVal="", QToAddForEmpty=1, vsh=0):
        QColumns=self.GetQColumns()
        hdrCell=DataCell(header)
        if QColumns==0 and ColN==1:
            #rowToSet=self.PrepareDataForTableColumn(self, rowCntExt, header, DfltVal, 1, QToAddForEmpty, vsh)
            rowToSet=PrepareDataForTableColumn_NestedListOfCells(rowCntExt, header, DfltVal, 1, QToAddForEmpty, vsh)
            contentRow=rowToSet[2-1]
            headerCell=rowToSet[1-1]
            if self.LC_0_CL_1==1:
                self.content.append(contentRow)
            else:
                L=len(rowToSet)
                for i in range(1, L+1):
                    row=[]
                    cell=contentRow[i-1]
                    row.append(cell)
                    self.content.append(row)
            #if self.LineOfColHeader==[] and header!="":
            if self.LineOfColHeader==[] and headerCell.GetStrVal()!="":
                #self.LineOfColHeader.append(hdrCell)
                self.__SetValToLineOfColHeaderIfPossible(ColN, valExt, vsh)
        elif ColN>=1 and ColN<=QColumns and QColumns>0:
            #rowToSet=self.PrepareDataForTableColumn(self, rowCntExt, header, DfltVal, 0, 0, vsh)
            rowToSet=PrepareDataForTableColumn_NestedListOfCells(rowCntExt, header, DfltVal, 0, 0, vsh)
            contentRow=rowToSet[2-1]
            headerCell=rowToSet[1-1]
            if self.LC_0_CL_1==1:
                self.content[ColN-1]=contentRow
            else:
                Set2DArrayIneRowN(self.content, contentRow, ColN, DfltVal, 0)
            #if self.LineOfColHeader==[] and header!="":
            if self.LineOfColHeader!=[] and headerCell.GetStrVal()!="":
                #self.LineOfColHeader[ColN-1]=copy.deepcopy(hdrCell)
                self.__SetValToLineOfColHeaderIfPossible(ColN, valExt, vsh)
                #def __SetValToLineOfColHeaderIfPossible(self, ColN, valExt, vsh=0):
                
    def AddEmptyColumn(self, DfltVal="", QToAddForEmpty=1, CreateHdrIfEmpty=1, vsh=0):
        rowToSet=PrepareDataForTableColumn([], "", DfltVal, 1, QToAddForEmpty, vsh)
        if self.LC_0_CL_1==1:
            self.content.append(rowToSet)
        else:
            Add2DArrayIneRow(self.content, rowToSet, DfltVal, 0)
        if self.LineOfolHeader!=[] or(self.GetQColumns()==1 and self.LineOfolHeader==[] and CreateHdrIfEmpty==1):
            cell=DataCell(DfltVal)
            self.LineOfolHeader.append(cell)
        
    def AddColumn(self, rowCntExt=[], header="", DfltVal="", QToAddForEmpty=1, vsh=0):
        if vsh==1:
            print("AddColumn starts working")
        #rowToSet=self.PrepareDataForTableColumn(rowCntExt, header, DfltVal, 1, QToAddForEmpty, vsh)
        rowToSet=self.PrepareDataForTableColumn_NestedListOfCells(rowCntExt, header, DfltVal, 1, QToAddForEmpty, vsh)
        contentRow=rowToSet[2-1]
        headerCell=rowToSet[1-1]
        if vsh==1:
            print("Q colunms before: "+str(self.GetQColumns()))
        if self.LC_0_CL_1==1:
            self.content.append(contentRow)
            if vsh==1:
                print("CL. simply added")
        else:
            Add2DArrayIneRow(self.content, contentRow, DfltVal, 0, vsh)
            if vsh==1:
                print("LC. used fn from library")
        if vsh==1:
            print("Q colunms after: "+str(self.GetQColumns()))
        if vsh==1:
            print("content:")
            print(self.content)
            print("Now header")
        QColunms=self.GetQColumns()
        colN=QColunms
        hdr=headerCell.GetStrVal()
        #__NewValUniqueForLineOfColHeader(self, valExt, colN, vsh=0):
        #self.__AddValToLineOfColHeaderIfPossible(header, colN, vsh)
        self.__AddValToLineOfColHeaderIfPossible(hdr, vsh)
        if vsh==1:
            print("AddColumn finishes working")
            
    def InsColumn(self, ColN, rowCntExt=[], header="", DfltVal="", vsh=0):
        rowToSet=PrepareDataForTableColumn(rowCntExt, header, DfltVal, 0, 0, vsh)
        QColumns=self.GetQColumns()
        if ColN>=1 and ColN<=QColumns and QColumns>0:
            if self.LC_0_CL_1==1:
                Ins2DArrayExtRow(self.content, ColN, rowToSet, DfltVal, 0, vsh)
            else:
                Ins2DArrayIneRow(self.content, ColN, rowToSet, DfltVal)
            self.__InsValToLineOfColHeaderIfPossible(header)

    def DelColumn(self, ColN, QCellsAferDelLastLine=1, DfltVal=""):
        QColumns=self.GetQColumns()
        if ColN>=1 and ColN<=QColumns and QColumns>0:
            colLength=self.GetQLines()
            if ColN==1 and QCellsAferDelLastLine==1:
                cell=DataCell(DfltVal)
                del ((self.content[1-1])[:])
                self.content[1-1].append(cell)
            else:
                if self.LC_0_CL_1==1:
                    Del2DArrayExtRowN(self.content, LineN)
                else:
                    Del2DArrayIneRowN(self.content, LineN, vsh)
            if self.LineOfColHeader!=[]:
                del self.LineOfColHeader[ColN-1]

    def PrepareDataForTableLine(self, rowCntExt=[], header="", DfltVal="", AddNotOtherAction=1, QToAddForEmpty=1, vsh=0):
        QLines=self.GetQQLine()
        rowLen=self.GetQColumns()
        cellRow=DataCellRowWithHeader(rowCntExt, header)
        rowToSet=[]
        dfltCell=DataCell(DfltVal)
        extL=cellRow.GetLength()
        #colToSet=cellRow.GetContent_AsList_OfCells()
        if QLines==0:
            if AddNotOtherAction==1:
                if extL==0:
                    for i in range(1, QToAddForEmpty+1):
                        rowToSet.append(dfltCell)
                else:
                    cellRow.SetSize(rowLen, DfltVal)
                    rowToSet=cellRow.GetContent_AsList_OfCells()
        else:
            if extL==0:
                for i in range(1, rowLen+1):
                    rowToSet.append(dfltCell)
            else:
                cellRow.SetSize(rowLen, DfltVal)
                rowToSet=cellRow.GetContent_AsList_OfCells()
        return rowToSet
        
    def SetLine(self, LineN, rowCntExt=[], header="", DfltVal="", QToAddForEmpty=1, vsh=0):
        QLines=self.GetQLines()
        hdrCell=DataCell(header)
        if QLines==0 and LineN==1:
            rowToSet=self.PrepareDataForTableColumn(self, rowCntExt, header, DfltVal, 1, QToAddForEmpty, vsh)
            if self.LC_0_CL_1==0:
                self.content.append(rowToSet)
            else:
                L=len(rowToSet)
                for i in range(1, L+1):
                    row=[]
                    cell=colToSet[i-1]
                    row.append(cell)
                    self.content.append(row)
            if self.ColOfLineHeader==[] and header!="":
                self.ColOfLineHeader.append(hdrCell)
        elif LineN>=1 and LineN<=QLines and QLines>0:
            rowToSet=self.PrepareDataForTableColumn(self, rowCntExt, header, DfltVal, 0, 0, vsh)
            if self.LC_0_CL_1==0:
                self.content[LineN-1]=rowToSet
            else:
                Set2DArrayIneRowN(self.content, rowToSet, LineN, DfltVal, 0)
            if self.LineOfColHeader==[] and header!="":
                self.LineOfColHeader[ColN-1]=copy.deepcopy(hdrCell)

    def AddEmptyLine(self, DfltVal="", QToAddForEmpty=1, CreateHdrIfEmpty=1, vsh=0):
        rowToSet=PrepareDataForTableColumn([], "", DfltVal, 1, QToAddForEmpty, vsh)
        if self.LC_0_CL_1==0:
            self.content.append(rowToSet)
        else:
            Add2DArrayIneRow(self.content, rowToSet, DfltVal, 0)
        if self.ColOfLineHeader!=[] or(self.GetQColumns()==1 and self.ColOfLineHeader==[] and CreateHdrIfEmpty==1):
            cell=DataCell(DfltVal)
            self.ColOfLineHeader.append(cell)
            

    def AddLine(self, rowCntExt=[], header="", DfltVal="", QToAddForEmpty=1, vsh=0):
        rowToSet=PrepareDataForTableColumn(rowCntExt, header, DfltVal, 1, QToAddForEmpty, vsh)
        if self.LC_0_CL_1==0:
            self.content.append(rowToSet)
        else:
            Add2DArrayIneRow(self.content, rowToSet, DfltVal, 0)
        self.__AddValToColOfLineHeaderIfPossible(header)

    def InsLine(self, LineN, rowCntExt=[], header="", DfltVal="", vsh=0):
        rowToSet=self.PrepareDataForTableColumn(rowCntExt, header, DfltVal, 0, 0, vsh)
        QLines=self.GetQLines()
        if LineN>=1 and LineN<=QLines and QLines>0:
            if self.LC_0_CL_1==0:
                Ins2DArrayExtRow(self.content, LineN, rowToSet, DfltVal, 0, vsh)
            else:
                Ins2DArrayIneRow(self.content, LineN, rowToSet, DfltVal)
            self.__InsValToColOfLineHeaderIfPossible(header)

    def DelLine(self, LineN, QCellsAferDelLastLine=1, DfltVal=""):
        QLines=self.GetQLines()
        if LineN>=1 and LineN<=QLines and QLines>0:
            lineLength=self.GetQColumns()
            if LineN==1 and QCellsAferDelLastLine==1:
                cell=DataCell(DfltVal)
                del ((self.content[1-1])[:])
                self.content[1-1].append(cell)
            else:
                if self.LC_0_CL_1==0:
                    Del2DArrayExtRowN(self.content, LineN)
                else:
                    Del2DArrayIneRowN(self.content, LineN, vsh)
            if self.ColOfLineHeader!=[]:
                del self.ColOfLineHeader[LineN-1]

    def Transpose(self):
        Transpose2DArray(self.content)
        ColOfLineHeader=self.LineOfColHeader
        LineOfColHeader=self.ColOfLineHeader
        self.LineOfColHeader=LineOfColHeader
        self.ColOfLineHeader=ColOfLineHeader
        if isinstance(self.TableHeader, TableHeaders):
            self.TableHeader.Transpose()

    def Get_LineOfColHeader_AsListOfStrVals(self):
        ExistingStrValList=[]
        if self.LineOfColHeader!=[]:
            L=len(self.LineOfColHeader)
            for i in range(1, L+1):
                strVal=str(self.LineOfColHeader[i-1].GetVal())
                ExistingStrValList.append(strVal)
        return ExistingStrValList

    def Get_ColOfLineHeader_AsListOfStrVals(self):
        ExistingStrValList=[]
        if self.ColOfLineHeader!=[]:
            L=len(self.ColOfLineHeader)
            for i in range(1, L+1):
                strVal=str(self.ColOfLineHeader[i-1].GetVal())
                ExistingStrValList.append(strVal)
        return  ExistingStrValList 

    def __NewValUniqueForLineOfColHeader(self, valExt, colN, vsh=0):
        val=copy.deepcopy(str(valExt))
        if vsh==1:
            print("__NewValUniqueForLineOfColHeader starts working")
            print("val came: ",val)
        ExistingStrValList=self.Get_LineOfColHeader_AsListOfStrVals()
        if vsh==1:
            print("ExistingStrValList: ",ExistingStrValList)
            print("starting library function: ")
        #   NewValUniqueFor1DArray(arr,               val, N,     sBef="", sAft="", vsh=0)
        val=NewValUniqueFor1DArray(ExistingStrValList, val, colN, "_C_",   "",      vsh)
        if vsh==1:
            print("val result: ",val)
            print("__NewValUniqueForLineOfColHeader finishes working")
        return val

    def __NewValUniqueForColOfLineHeader(self, valExt, lineN, vsh=0):
        val=copy.deepcopy(str(valExt))
        if vsh==1:
            print("__NewValUniqueForColOfLineHeader starts working")
            print("val came: ",val)
        ExistingStrValList=self.Get_ColOfLineHeader_AsListOfStrVals()
        if vsh==1:
            print("ExistingStrValList: ",ExistingStrValList)
        #def __NewValUniqueForLineOfColHeader(self, valExt, colN, vsh=0):
        val=NewValUniqueFor1DArray(ExistingStrValList, val, lineN, "_L_", "")
        if vsh==1:
            print("val result: ",val)
            print("__NewValUniqueForColOfLineHeader finishes working")
        return val

    def __AddValToLineOfColHeaderIfPossible(self, valExt, vsh=0):
        if vsh==1:
            print("__AddValToLineOfColHeaderIfPossible starts working")
        QColumns=self.GetQColumns()
        if vsh==1:
            print("QColumns="+str(QColumns))
        if not (QColumns>0 and self.LineOfColHeader==[]):
            if vsh==1:
                print("it is allowed to add Col Header")
            val=self.__NewValUniqueForLineOfColHeader( valExt, QColumns, vsh)
            if vsh==1:
                print("val to add:")
                print(str(val))
            cell=DataCell(val)
            self.LineOfColHeader.append(val)
        else:
            if vsh==1:
                print("not allowed to add Col Header")
        if vsh==1:
            #print("val result: ",val)
            print("__AddValToLineOfColHeaderIfPossible finishes working")

    def __InsValToLineOfColHeaderIfPossible(self, ColN, valExt, vsh=0):
        if vsh==1:
            print()
        QColumns=self.GetQColumns()
        if ColN>=1 and ColN<=QColumns and QColumns>0 and self.LineOfColHeader!=[]:
            val=self.__NewValUniqueForLineOfColHeader( valExt, ColN)
            cell=DataCell(val)
            ArrayIns5(self.LineOfColHeader, ColN, val)

    def __SetValToLineOfColHeaderIfPossible(self, ColN, valExt, vsh=0):
        QColumns=self.GetQColumns()
        if ColN>=1 and ColN<=QColumns and QColumns>0 and self.LineOfColHeader!=[]:
            val=self.__NewValUniqueForLineOfColHeader( valExt, ColN)
            cell=DataCell(val)
            self.LineOfColHeader[ColN-1].Set(val)
        elif ColN==1 and QColumns==0 and valExt!="" and self.LineOfColHeader==[]:
            val=self.__NewValUniqueForLineOfColHeader( valExt, ColN)
            cell=DataCell(val)
            self.LineOfColHeader.append(cell)

    def __AddValToColOfLineHeaderIfPossible(self, valExt, vsh=0):
        QLines=self.GetQQLines()
        if not (QLines>0 and self.ColOfLineHeader==[]):
            val=self.__NewValUniqueForColOfLineHeader( valExt, QColumns)
            cell=DataCell(val)
            self.ColOfLineHeader.append(val)

    def __InsValToColOfLineHeaderIfPossible(self, LineN, valExt, vsh=0):
        QLines=self.GetQLines()
        if LineN>=1 and LineN<=QLines and QLines>0 and self.ColOfLineHeader!=[]:
            val=self.__NewValUniqueForLineOfColHeader( valExt, LineN)
            cell=DataCell(val)
            ArrayIns5(self.ColOfLineHeader, LineN, val)

    def __SetValToColOfLineHeaderIfPossible(self, LineN, valExt, vsh=0):
        QLines=self.GetQLines()
        if LineN>=1 and LineN<=QLines and QLines>0 and self.ColOfLineHeader!=[]:
            val=self.__NewValUniqueForLineOfColHeader( valExt, LineN)
            cell=DataCell(val)
            self.ColOfLineHeader[LineN-1].Set(val)
           
        
                    
        

    
