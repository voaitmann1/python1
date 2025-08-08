#Goods
# Item\\ Param         Prise Quantity
# Smartphone Samsung J1  100   20
#
#Goods, Item N1: Smartphone Samsung J1: Param #1 - Price: 100
#Param #1 -Price (Goods, Item #1: Smartphone Samsung J1): 100
#Goods, Param #1 - Price (Item N1: Smartphone Samsung J1): 100
#Goods, 1: Smartphone Samsung J1 - Price: 100
#Price (Goods, 1: Smartphone Samsung J1): 100
#Goods, #1 Price (#1: Smartphone Samsung J1): 100

SeparCharNEmpty=0
SeparCharNSpace=1
SeparCharNComma=2
SeparCharNSemicolon=3
SeparCharNColon=4
SeparCharNMinus=5
SeparCharNEqSgn=6
SeparCharNShutBracket=7
SeparCharNOpenRectBracket=8
SeparCharNShutRectBracket=9
SeparCharNOpenBracket=10
SeparCharNDiezN=11
SeparCharNDot=12


def SeparatingSignN(N=0):
    #print("SeparatingSignN starts working. N="+str(N))
    s=""
    if N==SeparCharNSpace:
        s=" "
    if N==SeparCharNComma:
        s=","
    if N==SeparCharNSemicolon:
        s=";"
    if N==SeparCharNColon:
        s=":"
    if N==SeparCharNMinus:
        s="-"
    if N==SeparCharNEqSgn:
        s="="
    if N==SeparCharNShutBracket:
        s=")"
    if N==SeparCharNOpenRectBracket:
        s="["
    if N==SeparCharNShutRectBracket:
        s="]"
    if N==SeparCharNOpenBracket:
        s="("
    if N==SeparCharNDiezN:
        s="#"
    if N==SeparCharNDot:
        s="."
    #print("SeparatingSignN finishes working. s="+s)
    return s

class TableRepr_General:
    def __init__(self):
        self.ShowLineOfColHeader=1
        self.ShowColOfLineHeader=1
        #self.ShowLinesGeneralHeader=0
        #self.ShowColumnsGeneralHeader=0
        self.ShowLinesNumeration=0
        self.ShowColumnsNumeration=0
        self.LinesNumerationStart=0
        self.ColumnsNumerationStart=0
        self.LinesNumerationStep=1
        self.ColumnsNumerationStep=1

    def ToString(self):
        s=""
        s=s+" ShowLineOfColHeader="
        s=s+str(self.ShowLineOfColHeader)
        s=s+"; ShowColOfLineHeader="
        s=s+str(self.ShowColOfLineHeader)
        #s=s+"; ShowLinesGeneralHeader="
        #s=s+str(self.ShowLinesGeneralHeader)
        #s=s+"; ShowColumnsGeneralHeader="
        #s=s+str(self.ShowColumnsGeneralHeader)
        s=s+"; ShowLinesNumeration="
        s=s+str(self.ShowLinesNumeration)
        s=s+"; ShowColumnsNumeration="
        s=s+str(self.ShowColumnsNumeration)
        s=s+"; LinesNumerationStart="
        s=s+str(self.LinesNumerationStart)
        s=s+"; ColumnsNumerationStart="
        s=s+str(self.ColumnsNumerationStart)
        s=s+"; LinesNumerationStep="
        s=s+str(self.LinesNumerationStep)
        s=s+"; ColumnsNumerationStep="
        s=s+str(self.ColumnsNumerationStep)
        return s

    def LineNToShow(self, LineN):
        return self.LinesNumerationStart+(LineN-1)*self.LinesNumerationStep

    def ColumnNToShow(self, ColN):
        return self.ColumnsNumerationStart+(ColN-1)*self.ColumnsNumerationStep

    def SetAsSimple(self):
        #pass
        #no difference what to Set
        #self.ShowLineOfColHeader=1#may be 0 better
        #self.ShowColOfLineHeader=1#may be 0 better
        #self.ShowLinesGeneralHeader=0
        #self.ShowColumnsGeneralHeader=0
        self.ShowLinesNumeration=0
        self.ShowColumnsNumeration=0
        #self.LinesNumerationStart=1
        #self.ColumnsNumerationStart=1
        #self.LinesNumerationStep=1
        #self.ColumnsNumerationStep=1

    def SetAsMatrix(self):
        #numeration is vikt
        self.ShowLinesNumeration=1
        self.ShowColumnsNumeration=1
        #
        #self.ShowLineOfColHeader=1#may be 0 better
        #self.ShowColOfLineHeader=1#may be 0 better
        #self.ShowLinesGeneralHeader=0
        #self.ShowColumnsGeneralHeader=0
        #self.ShowLinesNumeration=1#above. ASc ce writes error, no indentatiob block
        self.ShowColumnsNumeration=1
        self.LinesNumerationStart=1
        self.ColumnsNumerationStart=1
        self.LinesNumerationStep=1
        self.ColumnsNumerationStep=1

    def SetAsFn2D(self):
        #self.ShowLineOfColHeader=1#may be 0 better
        #self.ShowColOfLineHeader=1#may be 0 better
        #self.ShowLinesGeneralHeader=0
        #self.ShowColumnsGeneralHeader=0
        self.ShowLinesNumeration=0
        self.ShowColumnsNumeration=0
        #self.LinesNumerationStart=1
        #self.ColumnsNumerationStart=1
        #self.LinesNumerationStep=1
        #self.ColumnsNumerationStep=1

    def SetAsFullInfo(self):
        self.ShowLineOfColHeader=1#may be 0 better
        self.ShowColOfLineHeader=1#may be 0 better
        #self.ShowLinesGeneralHeader=1
        #self.ShowColumnsGeneralHeader=1
        self.ShowLinesNumeration=1
        self.ShowColumnsNumeration=1
        self.LinesNumerationStart=1
        self.ColumnsNumerationStart=1
        self.LinesNumerationStep=1
        self.ColumnsNumerationStep=1

class TableRepr_RowHeaderCell:
    def __init__(self):
        self.ShowHeader=1#default
        self.ShowGenHeader=1
        self.ShowRowN=1
        self.HeaderAndN_GNH1_NGH2_HGN3_HNG4=1
        self.BefGH=SeparCharNEmpty#nil
        self.AftGH=SeparCharNEmpty#nil
        self.BefHdr=SeparCharNEmpty#nil
        self.AftHdr=SeparCharNEmpty#nil
        self.BefN=SeparCharNDiezN##
        self.AftN=SeparCharNMinus#-

    def ToString(self):
        s=""
        s=s+" ShowHeader="
        s=s+str(self.ShowHeader)
        s=s+" ShowGenHeader="
        s=s+str(self.ShowGenHeader)
        s=s+" ShowRowN="
        s=s+str(self.ShowRowN)
        s=s+" HeaderAndN_GNH1_NGH2_HGN3_HNG4="
        s=s+str(self.HeaderAndN_GNH1_NGH2_HGN3_HNG4)
        s=s+" BefGH="
        s=s+str(self.BefGH)
        s=s+"="
        s=s+SeparatingSignN(self.BefGH)
        s=s+" "
        s=s+" AftGH="
        s=s+str(self.AftGH)
        s=s+"="
        s=s+SeparatingSignN(self.AftGH)
        s=s+" "
        s=s+" BefHdr="
        s=s+str(self.BefHdr)
        s=s+"="
        s=s+SeparatingSignN(self.BefHdr)
        s=s+" "
        s=s+" AftHdr="
        s=s+str(self.AftHdr)
        s=s+"="
        s=s+SeparatingSignN(self.AftHdr)
        s=s+" "
        s=s+" BefN="
        s=s+str(self.BefN)
        s=s+"="
        s=s+SeparatingSignN(self.BefN)
        s=s+" "
        s=s+" AftN="
        s=s+str(self.AftN)
        s=s+"="
        s=s+SeparatingSignN(self.AftN)
        s=s+" "
        return s

    def ToStringRowHeaderCellByRepr(self, Header, NToShow, GenHeader, vsh=0):
        s=""
        c=""
        if vsh==1:
            print("ToStringRowHeaderCellByRepr starts working")
            print("Given: Header="+Header+" NToShow="+str(NToShow)+" GenHeader="+GenHeader)
        if self.HeaderAndN_GNH1_NGH2_HGN3_HNG4==1:
            if self.ShowGenHeader==1:
                c=""
                #
                #s=s+SeparatingSignN(self.BefGH)
                #s=s+str(GenHeader)
                #s=s+SeparatingSignN(self.AftGH)
                #
                c=c+SeparatingSignN(self.BefGH)
                c=c+str(GenHeader)
                c=c+SeparatingSignN(self.AftGH)
                #
                if vsh==1:
                    print("by GenHeader: c="+c)
                #
                s=s+c
            if self.ShowRowN==1:
                c=""
                #
                #s=s+SeparatingSignN(self.BefN)
                #s=s+str(NToShow)
                #s=s+SeparatingSignN(self.AftN)
                #
                c=c+SeparatingSignN(self.BefN)
                c=c+str(NToShow)
                c=c+SeparatingSignN(self.AftN)
                #
                if vsh==1:
                    print("by NToShow: c="+c)
                #
                s=s+c
            if self.ShowHeader==1:
                c=""
                #
                #s=s+SeparatingSignN(self.BefHdr)
                #s=s+str(Header)
                #s=s+SeparatingSignN(self.AftHdr)
                #
                s=s+SeparatingSignN(self.BefHdr)
                s=s+str(Header)
                s=s+SeparatingSignN(self.AftHdr)
                #
                if vsh==1:
                    print("by Header: c="+c)
                #
                s=s+c
        elif self.HeaderAndN_GNH1_NGH2_HGN3_HNG4==2:
            if self.ShowRowN==1:
                c=""
                #
                #s=s+SeparatingSignN(self.BefN)
                #s=s+str(NToShow)
                #s=s+SeparatingSignN(self.AftN)
                #
                c=c+SeparatingSignN(self.BefN)
                c=c+str(NToShow)
                c=c+SeparatingSignN(self.AftN)
                #
                if vsh==1:
                    print("by NToShow: c="+c)
                #
                s=s+c
            if self.ShowGenHeader==1:
                c=""
                #
                #s=s+SeparatingSignN(self.BefGH)
                #s=s+str(GenHeader)
                #s=s+SeparatingSignN(self.AftGH)
                #
                c=c+SeparatingSignN(self.BefGH)
                c=c+str(GenHeader)
                c=c+SeparatingSignN(self.AftGH)
                #
                if vsh==1:
                    print("by GenHeader: c="+c)
                #
                s=s+c
            if self.ShowHeader==1:
                c=""
                #
                #s=s+SeparatingSignN(self.BefHdr)
                #s=s+str(Header)
                #s=s+SeparatingSignN(self.AftHdr)
                #
                s=s+SeparatingSignN(self.BefHdr)
                s=s+str(Header)
                s=s+SeparatingSignN(self.AftHdr)
                #
                if vsh==1:
                    print("by Header: c="+c)
                #
                s=s+c
        elif self.HeaderAndN_GNH1_NGH2_HGN3_HNG4==3:
            if self.ShowHeader==1:
                c=""
                #
                #s=s+SeparatingSignN(self.BefHdr)
                #s=s+str(Header)
                #s=s+SeparatingSignN(self.AftHdr)
                #
                s=s+SeparatingSignN(self.BefHdr)
                s=s+str(Header)
                s=s+SeparatingSignN(self.AftHdr)
                #
                if vsh==1:
                    print("by Header: c="+c)
                #
                s=s+c
            if self.ShowGenHeader==1:
                c=""
                #
                #s=s+SeparatingSignN(self.BefGH)
                #s=s+str(GenHeader)
                #s=s+SeparatingSignN(self.AftGH)
                #
                c=c+SeparatingSignN(self.BefGH)
                c=c+str(GenHeader)
                c=c+SeparatingSignN(self.AftGH)
                #
                if vsh==1:
                    print("by GenHeader: c="+c)
                #
                s=s+c
            if self.ShowRowN==1:
                c=""
                #
                #s=s+SeparatingSignN(self.BefN)
                #s=s+str(NToShow)
                #s=s+SeparatingSignN(self.AftN)
                #
                c=c+SeparatingSignN(self.BefN)
                c=c+str(NToShow)
                c=c+SeparatingSignN(self.AftN)
                #
                if vsh==1:
                    print("by NToShow: c="+c)
                #
                s=s+c
        elif self.HeaderAndN_GNH1_NGH2_HGN3_HNG4==4:
            if self.ShowHeader==1:
                c=""
                #
                #s=s+SeparatingSignN(self.BefHdr)
                #s=s+str(Header)
                #s=s+SeparatingSignN(self.AftHdr)
                #
                s=s+SeparatingSignN(self.BefHdr)
                s=s+str(Header)
                s=s+SeparatingSignN(self.AftHdr)
                #
                if vsh==1:
                    print("by Header: c="+c)
                #
                s=s+c
            if self.ShowRowN==1:
                c=""
                #
                #s=s+SeparatingSignN(self.BefN)
                #s=s+str(NToShow)
                #s=s+SeparatingSignN(self.AftN)
                #
                c=c+SeparatingSignN(self.BefN)
                c=c+str(NToShow)
                c=c+SeparatingSignN(self.AftN)
                #
                if vsh==1:
                    print("by NToShow: c="+c)
                #
                s=s+c
            if self.ShowGenHeader==1:
                c=""
                #
                #s=s+SeparatingSignN(self.BefGH)
                #s=s+str(GenHeader)
                #s=s+SeparatingSignN(self.AftGH)
                #
                c=c+SeparatingSignN(self.BefGH)
                c=c+str(GenHeader)
                c=c+SeparatingSignN(self.AftGH)
                #
                if vsh==1:
                    print("by GenHeader: c="+c)
                #
                s=s+c
        if vsh==1:
            print("finally: "+s)
            print("ToStringRowHeaderCellByRepr finishes working")
        return s

    def SetAsSimple(self):
        self.ShowHeader=1
        self.ShowGenHeader=0
        self.ShowRowN=0
        self.HeaderAndN_GNH1_NGH2_HGN3_HNG4=1
        self.BefGH=SeparCharNEmpty
        self.AftGH=SeparCharNEmpty
        self.BefHdr=SeparCharNSpace#SeparCharNEmpty
        self.AftHdr=SeparCharNSpace#SeparCharNEmpty#SeparCharNSpace#
        self.BefN=SeparCharNEmpty
        self.AftN=SeparCharNEmpty

    def SetAsSimpleNumerated(self):#, firstN=1, step=1):#ce uz aic 
        self.SetAsSimple()
        #self.ShowHeader=1
        #self.ShowGenHeader=0
        self.ShowRowN=1
        #self.HeaderAndN_GNH1_NGH2_HGN3_HNG4=1
        #self.BefGH=SeparCharNEmpty
        #self.AftGH=SeparCharNEmpty
        #self.BefHdr=SeparCharNSpace#SeparCharNEmpty
        #self.AftHdr=SeparCharNSpace#SeparCharNSpace#SeparCharNEmpty
        #self.BefN=SeparCharNEmpty
        self.AftN=SeparCharNDot#SeparCharNShutBracket#SeparCharNComma#SeparCharNEmpty

    def SetAsEmpty(self):
        self.ShowHeader=0
        self.ShowGenHeader=0
        self.ShowRowN=0
        self.HeaderAndN_GNH1_NGH2_HGN3_HNG4=1
        self.BefGH=SeparCharNEmpty#nil
        self.AftGH=SeparCharNEmpty#nil
        self.BefHdr=SeparCharNEmpty#nil
        self.AftHdr=SeparCharNEmpty#nil
        self.BefN=SeparCharNEmpty##
        self.AftN=SeparCharNEmpty#-

    def SetAsPolynomeCoefsList(self):
        self.ShowHeader=1
        self.ShowGenHeader=1
        self.ShowRowN=1
        self.HeaderAndN_GNH1_NGH2_HGN3_HNG4=1
        self.BefGH=SeparCharNEmpty#nil
        self.AftGH=SeparCharNEmpty#nil
        self.BefHdr=SeparCharNEmpty#nil
        self.AftHdr=SeparCharNEmpty#nil
        self.BefN=SeparCharNEmpty##
        self.AftN=SeparCharNSpace#-

class TableRepr_ContentCell:
    def __init__(self):
        self.LineHdrParams=TableRepr_RowHeaderCell()
        self.ColHdrParams=TableRepr_RowHeaderCell()
        self.ShowTblHdr=0
        #self.ShowLH=0
        #self.ShowCH=0
        self.BefLH=SeparCharNEmpty
        self.AftLH=SeparCharNEmpty
        self.BefCH=SeparCharNEmpty
        self.AftCH=SeparCharNEmpty
        self.BefCnt=SeparCharNEmpty
        self.AftCnt=SeparCharNEmpty
        #self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8=1#5
        self.Cnt0_LCnt1_CCnt2_LCCnt3_CLCnt4_CntC5_CntL6_CntLC7_CntCL8=1#5

    def ToString_Slf(self):#content cell without its headers
        s=""
        #s=s+" LineHdrParams: "
        #s=s+self.LineHdrParams.ToString()
        #s=s+"; ColHdrParams: "
        #s=s+self.ColHdrParams.ToString()
        s=s+"; ShowTblHdr="
        s=s+str(self.ShowTblHdr)
        #self.ShowLH=0
        #self.ShowCH=0
        s=s+"; BefLH="
        s=s+str(self.BefLH)
        s=s+"="
        s=s+SeparatingSignN(self.BefLH)
        s=s+" "
        s=s+"; AftLH="
        s=s+str(self.AftLH)
        s=s+"="
        s=s+SeparatingSignN(self.AftLH)
        s=s+" "
        s=s+"; BefCH="
        s=s+str(self.BefCH)
        s=s+"="
        s=s+SeparatingSignN(self.BefCH)
        s=s+" "
        s=s+"; AftCH="
        s=s+str(self.AftCH)
        s=s+"="
        s=s+SeparatingSignN(self.AftCH)
        s=s+" "
        s=s+"; BefCnt="
        s=s+str(self.BefCnt)
        s=s+"="
        s=s+SeparatingSignN(self.BefCnt)
        s=s+" "
        s=s+"; AftCnt="
        s=s+str(self.AftCnt)
        s=s+"="
        s=s+SeparatingSignN(self.AftCnt)
        s=s+" "
        #self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8=1#5
        s=s+"; Cnt0_LCnt1_CCnt2_LCCnt3_CLCnt4_CntC5_CntL6_CntLC7_CntCL8="
        s=s+str(self.Cnt0_LCnt1_CCnt2_LCCnt3_CLCnt4_CntC5_CntL6_CntLC7_CntCL8)
        return s

    def ToString_CoLH(self):
        s=""
        s=s+" LineHdrParams: "
        s=s+self.LineHdrParams.ToString()
        return s
        
    def ToString_LoCH(self):
        s=""
        s=s+" ColHdrParams: "
        s=s+self.ColHdrParams.ToString()
        return s

    def ToString(self):#content cell AND its headers
        s=""
        s=s+" LineHdrParams: "
        s=s+self.LineHdrParams.ToString()
        s=s+"; ColHdrParams: "
        s=s+self.ColHdrParams.ToString()
        s=s+" ;"
        s=s+self.ToString_Slf()
        return s

    def GetContentCellByRepr(self, LineNToShow, ColNToShow, CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh=0):
        s=""
        if vsh==1:
            print("GetContentCellBef starts working")
            print("given:")
            print("LineNToShow="+str(LineNToShow)+" ColNToShow="+str(ColNToShow))
            print(" CellSelfText="+CellSelfText+" LHSelfText="+LHSelfText+" CHSelfText="+CHSelfText)
            print("LGHSelfText="+LGHSelfText+" CGHSelfText="+CGHSelfText+" THdrSelfText="+THdrSelfText)
            print("Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8="+str(self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8))
        LHdr=self.LineHdrParams.ToStringRowHeaderCellByRepr(LHSelfText, LineNToShow, LGHSelfText)
        CHdr=self.ColHdrParams.ToStringRowHeaderCellByRepr(CHSelfText, ColNToShow, CGHSelfText)
        if self.ShowTblHdr==1:
            s=s+THdrSelfText
            if vsh==1:
                print("THdrSelfText="+THdrSelfText+" s="+s)
        #if self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8==0:
        if self.Cnt0_LCnt1_CCnt2_LCCnt3_CLCnt4_CntC5_CntL6_CntLC7_CntCL8==0:
            s=s+SeparatingSignN(self.BefCnt)
            if vsh==1:
                print("self.BefCnt="+str(self.BefCnt)+" s="+s)
            s=s+CellSelfText
            if vsh==1:
                print("CellSelfText="+CellSelfText+" s="+s)
            s=s+SeparatingSignN(self.AftCnt)
            if vsh==1:
                print("self.AftCnt="+str(self.AftCnt)+" s="+s)
        #elif self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8==1:
        elif self.Cnt0_LCnt1_CCnt2_LCCnt3_CLCnt4_CntC5_CntL6_CntLC7_CntCL8==1:
            s=s+SeparatingSignN(self.BefLH)
            if vsh==1:
                print("self.BefLH="+self.BefLH+" s="+s)
            s=s+LHdr
            if vsh==1:
                print("LHdr="+LHdr+" s="+s)
            s=s+SeparatingSignN(self.AftLH)
            if vsh==1:
                print("self.AftLH="+str(self.AftLH)+" s="+s)
            s=s+SeparatingSignN(self.BefCnt)
            if vsh==1:
                print("self.BefCnt="+str(self.BefCnt)+" s="+s)
            s=s+CellSelfText
            if vsh==1:
                print("CellSelfText="+CellSelfText+" s="+s)
            s=s+SeparatingSignN(self.AftCnt)
            if vsh==1:
                print("self.AftCnt="+str(self.AftCnt)+" s="+s)
        #elif self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8==2:
        elif self.Cnt0_LCnt1_CCnt2_LCCnt3_CLCnt4_CntC5_CntL6_CntLC7_CntCL8==2:
            s=s+SeparatingSignN(self.BefCH)
            if vsh==1:
                print("self.BefCH="+self.BefCH+" s="+s)
            s=s+CHdr
            if vsh==1:
                print("CHdr="+CHdr+" s="+s)
            s=s+SeparatingSignN(self.AftCH)
            if vsh==1:
                print("self.AftCH="+str(self.AftCH)+" s="+s)
            s=s+SeparatingSignN(self.BefCnt)
            if vsh==1:
                print("self.BefCnt="+str(self.BefCnt)+" s="+s)
            s=s+CellSelfText
            if vsh==1:
                print("CellSelfText="+CellSelfText+" s="+s)
            s=s+SeparatingSignN(AftCnt)
            if vsh==1:
                print("self.AftCnt="+str(self.AftCnt)+" s="+s)
        #elif self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8==6:
        elif self.Cnt0_LCnt1_CCnt2_LCCnt3_CLCnt4_CntC5_CntL6_CntLC7_CntCL8==3:
            s=s+SeparatingSignN(self.BefLH)
            if vsh==1:
                print("self.BefLH="+str(self.BefLH)+" s="+s)
            s=s+LHdr
            if vsh==1:
                print("LHdr="+LHdr+" s="+s)
            s=s+SeparatingSignN(self.AftLH)
            if vsh==1:
                print("self.AftLH="+self.AftLH+" s="+s)
            s=s+SeparatingSignN(self.BefCH)
            if vsh==1:
                print("self.BefCH="+str(self.BefCH)+" s="+s)
            s=s+CHdr
            if vsh==1:
                print("CHdr="+CHdr+" s="+s)
            s=s+SeparatingSignN(self.AftCH)
            if vsh==1:
                print("self.AftCH="+str(self.AftCH)+" s="+s)
            s=s+SeparatingSignN(self.BefCnt)
            if vsh==1:
                print("self.BefCnt="+str(self.BefCnt)+" s="+s)
            s=s+CellSelfText
            if vsh==1:
                print("CellSelfText="+CellSelfText+" s="+s)
            s=s+SeparatingSignN(self.AftCnt)
            if vsh==1:
                print("self.AftCnt="+str(self.AftCnt)+" s="+s)
        #elif self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8==6:
        elif self.Cnt0_LCnt1_CCnt2_LCCnt3_CLCnt4_CntC5_CntL6_CntLC7_CntCL8==4:
            s=s+SeparatingSignN(self.BefCH)
            if vsh==1:
                print("self.BefCH="+str(self.BefCH)+" s="+s)
            s=s+CHdr
            if vsh==1:
                print("CHdr="+CHdr+" s="+s)
            s=s+SeparatingSignN(self.AftCH)
            if vsh==1:
                print("self.AftCH="+str(self.AftCH)+" s="+s)
            s=s+SeparatingSignN(self.BefLH)
            if vsh==1:
                print("self.BefLH="+str(self.BefLH)+" s="+s)
            s=s+LHdr
            if vsh==1:
                print("LHdr="+LHdr+" s="+s)
            s=s+SeparatingSignN(self.AftLH)
            if vsh==1:
                print("self.AftLH="+self.AftLH+" s="+s)
            s=s+SeparatingSignN(self.BefCnt)
            if vsh==1:
                print("self.BefCnt="+str(self.BefCnt)+" s="+s)
            s=s+CellSelfText
            if vsh==1:
                print("CellSelfText="+CellSelfText+" s="+s)
            s=s+SeparatingSignN(self.AftCnt)
            if vsh==1:
                print("self.AftCnt="+str(self.AftCnt)+" s="+s)
        #elif self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8==4:
        elif self.Cnt0_LCnt1_CCnt2_LCCnt3_CLCnt4_CntC5_CntL6_CntLC7_CntCL8==5:
            s=s+SeparatingSignN(self.BefCnt)
            if vsh==1:
                print("self.BefCnt="+str(self.BefCnt)+" s="+s)
            s=s+CellSelfText
            if vsh==1:
                print("CellSelfText="+CellSelfText+" s="+s)
            s=s+SeparatingSignN(self.AftCnt)
            if vsh==1:
                print("self.AftCnt="+str(self.AftCnt)+" s="+s)
            s=s+SeparatingSignN(self.BefCH)
            if vsh==1:
                print("self.BefCH="+str(self.BefCH)+" s="+s)
            s=s+CHdr
            if vsh==1:
                print("CHdr="+CHdr+" s="+s)
            s=s+SeparatingSignN(self.AftCH)
            if vsh==1:
                print("self.AftCH="+str(self.AftCH)+" s="+s)
        #elif self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8==3:
        elif self.Cnt0_LCnt1_CCnt2_LCCnt3_CLCnt4_CntC5_CntL6_CntLC7_CntCL8==6:
            s=s+SeparatingSignN(BefCnt)
            if vsh==1:
                print("self.BefCnt="+str(self.BefCnt)+" s="+s)
            s=s+CellSelfText
            if vsh==1:
                print("CellSelfText="+CellSelfText+" s="+s)
            s=s+SeparatingSignN(self.AftCnt)
            if vsh==1:
                print("self.AftCnt="+str(self.AftCnt)+" s="+s)
            s=s+SeparatingSignN(self.BefLH)
            if vsh==1:
                print("self.BefLH="+str(self.BefLH)+" s="+s)
            s=s+LHdr
            if vsh==1:
                print("LHdr="+LHdr+" s"+s)
            s=s+SeparatingSignN(self.AftLH)
            if vsh==1:
                print("self.AftLH="+self.AftLH+" s="+s)
        #elif self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8==7:
        elif self.Cnt0_LCnt1_CCnt2_LCCnt3_CLCnt4_CntC5_CntL6_CntLC7_CntCL8==7:
            s=s+SeparatingSignN(self.BefCnt)
            if vsh==1:
                print("self.BefCnt="+str(self.BefCnt)+" s="+s)
            s=s+CellSelfText
            if vsh==1:
                print("CellSelfText="+CellSelfText+" s="+s)
            s=s+SeparatingSignN(self.AftCnt)
            if vsh==1:
                print("self.AftCnt="+str(self.AftCnt)+" s="+s)
            s=s+SeparatingSignN(self.BefLH)
            if vsh==1:
                print("self.BefLH="+str(self.BefLH)+" s"+s)
            s=s+LHdr
            if vsh==1:
                print("LHdr="+LHdr+" s"+s)
            s=s+SeparatingSignN(self.AftLH)
            if vsh==1:
                print("self.AftLH="+str(self.AftLH)+" s="+s)
            s=s+SeparatingSignN(self.BefCH)
            if vsh==1:
                print("self.BefCH="+str(self.BefCH)+" s="+s)
            s=s+CHdr
            if vsh==1:
                print("CHdr="+CHdr+" s"+s)
            s=s+SeparatingSignN(self.AftCH)
            if vsh==1:
                print("self.AftCH="+str(self.AftCH)+" s="+s)
        #elif self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8==8:
        elif self.Cnt0_LCnt1_CCnt2_LCCnt3_CLCnt4_CntC5_CntL6_CntLC7_CntCL8==8:
            s=s+SeparatingSignN(self.BefCnt)
            if vsh==1:
                print("self.BefCnt="+str(self.BefCnt)+" s="+s)
            s=s+CellSelfText
            if vsh==1:
                print("CellSelfText="+CellSelfText+" s="+s)
            s=s+SeparatingSignN(self.AftCnt)
            if vsh==1:
                print("self.AftCnt="+str(self.AftCnt)+" s="+s)
            s=s+SeparatingSignN(self.BefCH)
            if vsh==1:
                print("self.BefCH="+str(self.BefCH)+" s="+s)
            s=s+CHdr
            if vsh==1:
                print("CHdr="+CHdr+" s"+s)
            s=s+SeparatingSignN(self.AftCH)
            if vsh==1:
                print("self.AftCH="+self.AftCH+" s"+s)
            s=s+SeparatingSignN(self.BefLH)
            if vsh==1:
                print("self.BefLH="+str(self.BefLH)+" s="+s)
            s=s+LHdr
            if vsh==1:
                print("LHdr="+LHdr+" s"+s)
            s=s+SeparatingSignN(self.AftLH)
            if vsh==1:
                print("self.AftLH="+str(self.AftLH)+" s="+s)
        return s

    
    def SetAsSimple(self):
        self.LineHdrParams=TableRepr_RowHeaderCell()
        self.ColHdrParams=TableRepr_RowHeaderCell()
        #
        self.ShowTblHdr=0#1
        #self.ShowLH=0
        #self.ShowCH=0
        self.BefLH=SeparCharNEmpty
        self.AftLH=SeparCharNEmpty
        self.BefCH=SeparCharNEmpty
        self.AftCH=SeparCharNEmpty
        self.BefCnt=SeparCharNEmpty
        self.AftCnt=SeparCharNEmpty
        #self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8=0
        self.Cnt0_LCnt1_CCnt2_LCCnt3_CLCnt4_CntC5_CntL6_CntLC7_CntCL8=0

    def SetAsSimpleNumerated(self):
        self.GetAsSimple()
    
    def SetAsMatrix(self):
        self.LineHdrParams=TableRepr_RowHeaderCell()
        #
        self.LineHdrParams.ShowHeader=0#default
        self.LineHdrParams.ShowGenHeader=0
        self.LineHdrParams.ShowRowN=1
        self.LineHdrParams.HeaderAndN_GNH1_NGH2_HGN3_HNG4=1
        self.LineHdrParams.BefGH=SeparCharNEmpty#nil
        self.LineHdrParams.AftGH=SeparCharNEmpty#nil
        self.LineHdrParams.BefHdr=SeparCharNEmpty#nil
        self.LineHdrParams.AftHdr=SeparCharNEmpty#nil
        self.LineHdrParams.BefN=SeparCharNEmpty#SeparCharNOpenBracket#(
        self.LineHdrParams.AftN=SeparCharNEmpty#SeparCharNComma#,
        #
        self.ColHdrParams=TableRepr_RowHeaderCell()
        #
        self.ColHdrParams.ShowHeader=0#default
        self.ColHdrParams.ShowGenHeader=0
        self.ColHdrParams.ShowRowN=1
        self.ColHdrParams.HeaderAndN_GNH1_NGH2_HGN3_HNG4=1
        self.ColHdrParams.BefGH=SeparCharNEmpty#nil
        self.ColHdrParams.AftGH=SeparCharNEmpty#nil
        self.ColHdrParams.BefHdr=SeparCharNEmpty#nil
        self.ColHdrParams.AftHdr=SeparCharNEmpty#nil
        self.ColHdrParams.BefN=SeparCharNEmpty#1_
        self.ColHdrParams.AftN=SeparCharNEmpty#SeparCharNEqSgn#=
        #
        self.ShowTblHdr=1
        #self.ShowLH=0
        #self.ShowCH=0
        self.BefLH=SeparCharNOpenBracket#(
        self.AftLH=SeparCharNComma#,
        self.BefCH=SeparCharNSpace#_
        self.AftCH=SeparCharNShutBracket#)
        self.BefCnt=SeparCharNEqSgn#=
        self.AftCnt=SeparCharNEmpty
        #self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8=5
        self.Cnt0_LCnt1_CCnt2_LCCnt3_CLCnt4_CntC5_CntL6_CntLC7_CntCL8=3

    def SetAsFn2D(self):
        self.LineHdrParams=TableRepr_RowHeaderCell()
        #
        self.LineHdrParams.ShowHeader=1#default
        self.LineHdrParams.ShowGenHeader=1
        self.LineHdrParams.ShowRowN=0
        self.LineHdrParams.HeaderAndN_GNH1_NGH2_HGN3_HNG4=1
        self.LineHdrParams.BefGH=SeparCharNEmpty#nil
        self.LineHdrParams.AftGH=SeparCharNEqSgn#nil
        self.LineHdrParams.BefHdr=SeparCharNEmpty#nil
        self.LineHdrParams.AftHdr=SeparCharNComma#nil
        self.LineHdrParams.BefN=SeparCharNEmpty#
        self.LineHdrParams.AftN=SeparCharNEmpty#
        #
        self.ColHdrParams=TableRepr_RowHeaderCell()
        #
        self.ColHdrParams.ShowHeader=1#default
        self.ColHdrParams.ShowGenHeader=1
        self.ColHdrParams.ShowRowN=0
        self.ColHdrParams.HeaderAndN_GNH1_NGH2_HGN3_HNG4=1
        self.ColHdrParams.BefGH=SeparCharNSpace#nil
        self.ColHdrParams.AftGH=SeparCharNEqSgn#nil
        self.ColHdrParams.BefHdr=SeparCharNEmpty#nil
        self.ColHdrParams.AftHdr=SeparCharNEmpty#nil
        self.ColHdrParams.BefN=SeparCharNEmpty#1_
        self.ColHdrParams.AftN=SeparCharNEmpty#=
        #
        #
        self.ShowTblHdr=1
        #self.ShowLH=0
        #self.ShowCH=0
        self.BefLH=SeparCharNOpenBracket#(
        self.AftLH=SeparCharNComma#,
        self.BefCH=SeparCharNSpace#_
        self.AftCH=SeparCharNShutBracket#)
        self.BefCnt=SeparCharNEqSgn#=
        self.AftCnt=SeparCharNEmpty
        #self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8=5
        self.Cnt0_LCnt1_CCnt2_LCCnt3_CLCnt4_CntC5_CntL6_CntLC7_CntCL8=3

    def SetAsFullInfo(self):
        self.LineHdrParams=TableRepr_RowHeaderCell()
        #
        self.LineHdrParams.ShowHeader=1#default
        self.LineHdrParams.ShowGenHeader=1
        self.LineHdrParams.ShowRowN=1
        self.LineHdrParams.HeaderAndN_GNH1_NGH2_HGN3_HNG4=1
        self.LineHdrParams.BefGH=SeparCharNEmpty#nil
        self.LineHdrParams.AftGH=SeparCharNMinus#nil
        self.LineHdrParams.BefN=SeparCharNEmpty#
        self.LineHdrParams.AftN=SeparCharNMinus#
        self.LineHdrParams.BefHdr=SeparCharNEmpty#nil
        self.LineHdrParams.AftHdr=SeparCharNComma#nil
        #
        self.ColHdrParams=TableRepr_RowHeaderCell()
        #
        self.ColHdrParams.ShowHeader=1#default
        self.ColHdrParams.ShowGenHeader=1
        self.ColHdrParams.ShowRowN=1
        self.ColHdrParams.HeaderAndN_GNH1_NGH2_HGN3_HNG4=1
        self.ColHdrParams.BefGH=SeparCharNEmpty#nil
        self.ColHdrParams.AftGH=SeparCharNMinus#nil
        self.ColHdrParams.BefHdr=SeparCharNEmpty#nil
        self.ColHdrParams.AftHdr=SeparCharNEmpty#nil
        self.ColHdrParams.BefN=SeparCharNEmpty#1_
        self.ColHdrParams.AftN=SeparCharNEmpty#=
        #
        self.ShowTblHdr=1
        #self.ShowLH=0
        #self.ShowCH=0
        self.BefLH=SeparCharNOpenBracket#(
        self.AftLH=SeparCharNComma#,
        self.BefCH=SeparCharNSpace#_
        self.AftCH=SeparCharNShutBracket#)
        self.BefCnt=SeparCharNColon#=
        self.AftCnt=SeparCharNEmpty
        #self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8=6
        self.Cnt0_LCnt1_CCnt2_LCCnt3_CLCnt4_CntC5_CntL6_CntLC7_CntCL8=4

    def SetAsCathegoriesOfGoods(self, usingGeneralNames=0, itemsNumeration=0, paramsNumeration=0, itemAsExampleOfParam=0, vsh=0):
        
        #pass
        #Goods
        # Item\\ Param         Prise Quantity
        # Smartphone Samsung J1  100   20
        #
        #Goods, Item N1: Smartphone Samsung J1: Param #1 - Price: 100 #!!
        #Param #1 -Price (Goods, Item #1: Smartphone Samsung J1): 100
        #Goods, 1: Smartphone Samsung J1 - Price: 100
        #Price (Goods, 1: Smartphone Samsung J1): 100
        #
        self.LineHdrParams=TableRepr_RowHeaderCell()
        #
        self.LineHdrParams.ShowHeader=1#default
        if usingGeneralNames==0:
            self.LineHdrParams.ShowGenHeader=0
        else:
            self.LineHdrParams.ShowGenHeader=1
        if itemsNumeration==0:
            self.LineHdrParams.ShowRowN=0
        else:
            self.LineHdrParams.ShowRowN=1
        self.LineHdrParams.HeaderAndN_GNH1_NGH2_HGN3_HNG4=1
        #self.LineHdrParams.BefGH=SeparCharNEmpty#nil
        #self.LineHdrParams.AftGH=SeparCharNMinus#nil
        #self.LineHdrParams.BefN=SeparCharNEmpty#
        #self.LineHdrParams.AftN=SeparCharNMinus#
        #self.LineHdrParams.BefHdr=SeparCharNEmpty#nil
        #self.LineHdrParams.AftHdr=SeparCharNComma#nil
        #
        self.ColHdrParams=TableRepr_RowHeaderCell()
        #
        self.ColHdrParams.ShowHeader=1#default
        if usingGeneralNames==0:
            self.ColHdrParams.ShowGenHeader=0
        else:
            self.ColHdrParams.ShowGenHeader=1
        if paramsNumeration==0:
            self.ColHdrParams.ShowRowN=0
        else:
            self.ColHdrParams.ShowRowN=1
        self.ColHdrParams.HeaderAndN_GNH1_NGH2_HGN3_HNG4=1
        #self.ColHdrParams.BefGH=SeparCharNEmpty#nil
        #self.ColHdrParams.AftGH=SeparCharNMinus#nil
        #self.ColHdrParams.BefHdr=SeparCharNEmpty#nil
        #self.ColHdrParams.AftHdr=SeparCharNEmpty#nil
        #self.ColHdrParams.BefN=SeparCharNEmpty#1_
        #self.ColHdrParams.AftN=SeparCharNEmpty#=
        #
        self.ShowTblHdr=1
        #self.ShowLH=0
        #self.ShowCH=0
        #self.BefLH=SeparCharNOpenBracket#(
        #self.AftLH=SeparCharNComma#,
        #self.BefCH=SeparCharNSpace#_
        #self.AftCH=SeparCharNShutBracket#)
        #self.BefCnt=SeparCharNColon#=
        #self.AftCnt=SeparCharNEmpty
        #self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8=6
        if itemAsExampleOfParam==0:
            self.Cnt0_LCnt1_CCnt2_LCCnt3_CLCnt4_CntC5_CntL6_CntLC7_CntCL8=4
            #
            self.BefCH=SeparCharNComma#_
            #
            #self.ColHdrParams.HeaderAndN_GNH1_NGH2_HGN3_HNG4=1
            self.ColHdrParams.BefGH=SeparCharNSpace#nil
            self.ColHdrParams.AftGH=SeparCharNSpace#nil
            self.ColHdrParams.BefN=SeparCharNDiezN#
            self.ColHdrParams.AftN=SeparCharNMinus#
            self.ColHdrParams.BefHdr=SeparCharNSpace#nil
            self.ColHdrParams.AftHdr=SeparCharNColon#nil
            #
            self.AftCH=SeparCharNSpace#)
            #
            #if self.ColHdrParams.ShowGenHeader==1:
            #    self.BefLH=SeparCharNSpace#(
            #else:
            #    self.BefLH=SeparCharNOpenBracket
            self.BefLH=SeparCharNSpace
            #
            #self.LineHdrParams.HeaderAndN_GNH1_NGH2_HGN3_HNG4=1
            self.LineHdrParams.BefGH=SeparCharNOpenBracket#nil
            self.LineHdrParams.AftGH=SeparCharNSpace#nil
            self.LineHdrParams.BefN=SeparCharNDiezN#
            self.LineHdrParams.AftN=SeparCharNMinus#
            self.LineHdrParams.BefHdr=SeparCharNSpace#nil
            self.LineHdrParams.AftHdr=SeparCharNShutBracket#nil
            #
            self.AftLH=SeparCharNColon#,
            #
            if self.ColHdrParams.ShowGenHeader==1:
                self.BefCnt=SeparCharNSpace#=
            else:
                self.BefCnt=SeparCharNOpenBracket
            self.AftCnt=SeparCharNEmpty
        else:
            self.Cnt0_LCnt1_CCnt2_LCCnt3_CLCnt4_CntC5_CntL6_CntLC7_CntCL8=3
            self.BefLH=SeparCharNComma#(#Goods,
            #
            #self.LineHdrParams.HeaderAndN_GNH1_NGH2_HGN3_HNG4=1
            self.LineHdrParams.BefGH=SeparCharNSpace#
            self.LineHdrParams.AftGH=SeparCharNSpace#
            self.LineHdrParams.BefN=SeparCharNDiezN#
            self.LineHdrParams.AftN=SeparCharNMinus#Goods, Item #1-
            self.LineHdrParams.BefHdr=SeparCharNSpace#nil
            self.LineHdrParams.AftHdr=SeparCharNColon#Goods, Item #1- Bike:
            #
            self.AftLH=SeparCharNSpace#,
            #
            self.BefCH=SeparCharNEmpty#_
            #
            #self.ColHdrParams.HeaderAndN_GNH1_NGH2_HGN3_HNG4=1
            self.ColHdrParams.BefGH=SeparCharNSpace#nil
            self.ColHdrParams.AftGH=SeparCharNSpace#nil
            self.ColHdrParams.BefN=SeparCharNDiezN#
            self.ColHdrParams.AftN=SeparCharNMinus#
            self.ColHdrParams.BefHdr=SeparCharNSpace#nil
            self.ColHdrParams.AftHdr=SeparCharNEmpty#Goods, Item #1: Bike: Param #1- -
            #
            self.AftCH=SeparCharNColon#)
            #
            self.BefCnt=SeparCharNSpace#=
            self.AftCnt=SeparCharNEmpty

    def SetAsCathegoriesOfGoods_ItemThenParam(self, usingGeneralNames=0, itemsNumeration=0, paramsNumeration=0, vsh=0):
        itemAsExampleOfParam=1
        self.SetAsCathegoriesOfGoods(self, usingGeneralNames, itemsNumeration, paramsNumeration, itemAsExampleOfParam, vsh)

    def SetAsCathegoriesOfGoods_ItemAsExampleOfParam(self, usingGeneralNames=0, itemsNumeration=0, paramsNumeration=0, vsh=0):
        itemAsExampleOfParam=1
        self.SetAsCathegoriesOfGoods(self, usingGeneralNames, itemsNumeration, paramsNumeration, itemAsExampleOfParam, vsh)

    def SetAsCathegoriesExampleAsConcreteGood(self):
        pass
        # Item2 - price: #5 smartphone Samsung J1: 100
        
    
class TableRepr:
    def __init__(self):
        self.general=TableRepr_General()
        self.LoCH=TableRepr_RowHeaderCell()
        self.CoLH=TableRepr_RowHeaderCell()
        self.Cont=TableRepr_ContentCell()
        #self.x=0
        #self.LoCH=TableRepr_RowHeaderCell()
        #self.general=TableRepr_General()

    def ToString_general(self):
        return self.general.ToString()

    def ToString_LoCH(self, vsh=1):
        return self.LoCH.ToString()
        
    def ToString_CoLH(self):
        return self.CoLH.ToString()
        
    def ToString_Cont_Slf(self):
        return self.Cont.ToString_Slf()

    def ToString_Cont_LoCH(self):
        return self.Cont.ToString_LoCH()
        #s="empty"
        #if isinstance(self.Cont, TableRepr_ContentCell):
        #    s="half-empty"
        #    if isinstance(self.Cont.ColHdrParams, TableRepr_RowHeaderCell):
        #        #s=self.Cont.ColHdrParams.ToString()# so works
        #        s=self.Cont.ToString_LoCH()#returns None
        #return s

    def ToString_Cont_CoLH(self):
        return self.Cont.ToString_CoLH()
        #s="empty"
        #if isinstance(self.Cont, TableRepr_ContentCell):
        #    s="half-empty"
        #    if isinstance(self.Cont.LineHdrParams, TableRepr_RowHeaderCell):
        #        #s=self.Cont.LineHdrParams.ToString()# so works
        #        s=self.Cont.ToString_CoLH()#returns None
        #return s

    def ShowToConsole(self):
        print("general:")
        print(self.ToString_general())
        print("LoCH:")
        print(self.ToString_LoCH())
        print("CoLH:")
        print(self.ToString_CoLH())
        print("Cont_Slf:")
        print(self.ToString_Cont_Slf())
        print("Cont_LoCH:")
        #s1=self.ToString_Cont_LoCH()
        #s2=self.Cont.ColHdrParams.ToString()
        print(self.ToString_Cont_LoCH())
        #print("s1=",s1)
        #print("s2=",s2)
        print("Cont_CoLH:")
        #s1=self.ToString_Cont_LoCH()
        #s2=self.Cont.LineHdrParams.ToString()
        print(self.ToString_Cont_CoLH())
        #print("s1=",s1)
        #print("s2=",s2)

    def GetIfLineOfColHeaderToShow(self):
        y=0
        if isinstance(self.general, TableRepr_General):
            y=self.general.ShowLineOfColHeader
        return y

    def GetIfColOfLineHeaderToShow(self):
        y=0
        if isinstance(self.general, TableRepr_General):
            y=self.general.ShowColOfLineHeader
        return y

    def CalcLineNToShow(self, LineN):
        y=0
        if isinstance(self.general, TableRepr_General):
            y=self.general.LineNToShow(LineN)
        return y

    def CalcColumnNToShow(self, ColN):
        y=0
        if isinstance(self.general, TableRepr_General):
            y=self.general.ColumnNToShow(ColN)
        return y

    def GetIfLinesToNumerate(self):
        y=0
        if isinstance(self.general, TableRepr_General):
            y=self.general.ShowLinesNumeration
        return y

    def GetIfColumnsToNumerate(self):
        y=0
        if isinstance(self.general, TableRepr_General):
            y=self.general.ShowColumnsNumeration
        return y

    #def GetLineOfColHeaderCellBef(self, LineHeader, LineN, LinesGenHeader):
    #    s=""
    #    LineNToShow=self.CalcLineNToShow(LineN)
    #    if isinstance(self.LoCH, TableRepr_RowHeaderCell):
    #        s=self.LoCH.ToStringRowHeaderCellBef(self, LineHeader, LineNToShow, LinesGenHeader)
    #    return s

    #def GetColOfLineHeaderCellBef(self, ColHeader, ColN, ColumnsGenHeader):
    #    s=""
    #    ColNToShow=self.CalcColumnNToShow(ColN)
    #    if isinstance(self.CoLH, TableRepr_RowHeaderCell):
    #        s=self.CoLH.ToStringRowHeaderCellBef(self, ColHeader, ColNToShow, ColumnsGenHeader)
    #    return s

    #def GetContentCellBef(self, LineN, ColN, CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh=0):
    #    s=""
    #    LineNToShow=self.CalcLineNToShow(LineN)
    #    ColNToShow=self.CalcColumnNToShow(ColN)
    #    if isinstance(self.Cont, TableRepr_ContentCell):
    #        s=self.Cont.GetContentCellBef(LineNToShow, ColNToShow, CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh)
    #    return s
    #
    #def GetContentCellAft(self, LineN, ColN, CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh=0):
    #    s=""
    #    LineNToShow=self.CalcLineNToShow(LineN)
    #    ColNToShow=self.CalcColumnNToShow(ColN)
    #    if isinstance(self.Cont, TableRepr_ContentCell):
    #        s=self.Cont.GetContentCellAft(LineNToShow, ColNToShow, CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh)
    #    return s

    def GetContentCellByRepr(self, LineN, ColN, CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh=0):
        s=""
        LineNToShow=self.CalcLineNToShow(LineN)
        ColNToShow=self.CalcColumnNToShow(ColN)
        if isinstance(self.Cont, TableRepr_ContentCell):
            s=self.Cont.GetContentCellByRepr(LineNToShow, ColNToShow, CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh)
        return s

    def GetLineOfColHeaderCellByRepr(self, ColN, LoCHCellSelfText, CGHSelfText, vsh=0):
        s=""
        if vsh==1:
            print("GetLineOfColHeaderCellByRepr starts working")
            print("given: ColN="+str(ColN)+" LoCHCellSelfText="+LoCHCellSelfText+" CGHSelfText="+CGHSelfText)
        ColNToShow=self.CalcColumnNToShow(ColN)
        if vsh==1:
            print("ColNToShow calculated: "+str(ColNToShow))
        if isinstance(self.general, TableRepr_General)and isinstance(self.LoCH, TableRepr_RowHeaderCell) and self.GetIfLineOfColHeaderToShow()==1:
            s=self.LoCH.ToStringRowHeaderCellByRepr(LoCHCellSelfText, ColNToShow, CGHSelfText, vsh)
        if vsh==1:
            print("finally: "+s)
            print("GetLineOfColHeaderCellByRepr finishes working")
        return s

    def GetColOfLineHeaderCellByRepr(self, LineN, CoLHCellSelfText, LGHSelfText, vsh=0):
        s=""
        if vsh==1:
            print("GetLineOfColHeaderCellByRepr starts working")
            print("given: LineN="+str(LineN)+" CoLHCellSelfText="+CoLHCellSelfText+" LGHSelfText="+LGHSelfText)
        
        LineNToShow=self.CalcLineNToShow(LineN)
        if isinstance(self.general, TableRepr_General)and isinstance(self.CoLH, TableRepr_RowHeaderCell) and self.GetIfColOfLineHeaderToShow()==1:
            s=self.CoLH.ToStringRowHeaderCellByRepr(CoLHCellSelfText, LineNToShow, LGHSelfText, vsh)
        return s    

    def SetAsSimple(self):
        if isinstance(self.general, TableRepr_General):
            self.general.SetAsSimple()
        if isinstance(self.LoCH, TableRepr_RowHeaderCell):
            self.LoCH.SetAsSimple()
        if isinstance(self.CoLH, TableRepr_RowHeaderCell):
            self.CoLH.SetAsSimple()
        if isinstance(self.Cont, TableRepr_ContentCell):
            self.Cont.SetAsSimple()

    def SetAsSimpleNumerated(self, LinesNumeration=1, ColumnsNumeration=1, FirstLineN=1, LinesStep=1, FirstColN=1, ColsStep=1):
        self.SetAsSimple()
        #if not isinstance(self.general, TableRepr_General):
        #    self.general=TableRepr_General()
        #
        self.general.ShowLinesNumeration=LinesNumeration
        self.general.ShowColumnsNumeration=ColumnsNumeration
        self.general.LinesNumerationStart=FirstLineN
        self.general.ColumnsNumerationStart=FirstColN
        self.general.LinesNumerationStep=LinesStep
        self.general.ColumnsNumerationStep=ColsStep
        #
        self.general.ShowLineOfColHeader=ColumnsNumeration
        self.general.ShowColOfLineHeader=LinesNumeration
        #
        self.LoCH.SetAsSimpleNumerated()
        self.CoLH.SetAsSimpleNumerated()

    def SetAsMatrix(self):
        if isinstance(self.general, TableRepr_General):
            self.general.SetAsMatrix()
        #if isinstance(self.LoCH, TableRepr_RowHeaderCell):
        #    self.LoCH.SetAsMatrix()
        #if isinstance(self.CoLH, TableRepr_RowHeaderCell):
        #    self.CoLH.SetAsMatrix()
        if isinstance(self.Cont, TableRepr_ContentCell):
            self.Cont.SetAsMatrix()

    def SetAsFn2D(self):
        if isinstance(self.general, TableRepr_General):
            self.general.SetAsFn2D()
        #if isinstance(self.LoCH, TableRepr_RowHeaderCell):
        #    self.LoCH.SetAsFn2D()
        #if isinstance(self.CoLH, TableRepr_RowHeaderCell):
        #    self.CoLH.SetAsFn2D()
        if isinstance(self.Cont, TableRepr_ContentCell):
            self.Cont.SetAsFn2D()

    def SetAsFullInfo(self):
        if isinstance(self.general, TableRepr_General):
            self.general.SetAsFullInfo()
        #if isinstance(self.LoCH, TableRepr_RowHeaderCell):
        #    self.LoCH.SetAsFullInfo()
        #if isinstance(self.CoLH, TableRepr_RowHeaderCell):
        #    self.CoLH.SetAsFullInfo()
        if isinstance(self.Cont, TableRepr_ContentCell):
            self.Cont.SetAsFullInfo()

    def SetAsCathegoriesOfGoods(self, usingGeneralNames=0, itemsNumeration=0, paramsNumeration=0, itemAsExampleOfParam=0, vsh=0):
        if isinstance(self.general, TableRepr_General):
            self.general.SetAsFullInfo()
        if isinstance(self.Cont, TableRepr_ContentCell):
            self.Cont.SetAsCathegoriesOfGoods(usingGeneralNames, itemsNumeration, paramsNumeration, itemAsExampleOfParam, vsh)

    def SetAsCathegoriesOfGoods_ItemThenParam(self, usingGeneralNames=0, itemsNumeration=0, paramsNumeration=0, vsh=0):
        itemAsExampleOfParam=0
        self.SetAsCathegoriesOfGoods(usingGeneralNames, itemsNumeration, paramsNumeration, itemAsExampleOfParam, vsh)

    def SetAsCathegoriesOfGoods_ItemAsExampleOfParam(self, usingGeneralNames=0, itemsNumeration=0, paramsNumeration=0, vsh=0):
        itemAsExampleOfParam=1
        self.SetAsCathegoriesOfGoods(usingGeneralNames, itemsNumeration, paramsNumeration, itemAsExampleOfParam, vsh)

    def SetAsPolynomeCoefsList(self):
        self.Cont.SetAsSimple()
        self.LoCH.SetAsSimple()
        self.general.ShowLinesNumeration=1
        self.general.ShowColumnsNumeration=1
        self.general.LinesNumerationStart=0
        self.general.ColumnsNumerationStart=0
        self.general.LinesNumerationStep=1
        self.general.ColumnsNumerationStep=1
        #
        self.general.ShowLineOfColHeader=1
        self.general.ShowColOfLineHeader=1
        #
        self.CoLH.SetAsPolynomeCoefsList()

