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
    #print("SeparatingSignN finishes working. s="+s)
    return s

class TableRepr_General:
    def __init__(self):
        self.ShowLineOfColHeader=1
        self.ShowColOfLineHeader=1
        self.ShowLinesGeneralHeader=0
        self.ShowColumnsGeneralHeader=0
        self.ShowLinesNumeration=0
        self.ShowColumnsNumeration=0
        self.LinesNumerationStart=0
        self.ColumnsNumerationStart=0
        self.LinesNumerationStep=1
        self.ColumnsNumerationStep=1

    def LineNToShow(self, LineN):
        return self.LinesNumerationStart+(LineN-1)*self.LinesNumerationStep

    def ColumnNToShow(self, ColN):
        return self.ColumnsNumerationStart+(ColN-1)*self.ColumnsNumerationStep

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

    def ToStringRowHeaderCellBef(self, Header, NToShow, GenHeader):
        s=""
        if self.HeaderAndN_GNH1_NGH2_HGN3_HNG4==1:
            if self.ShowGenHeader==1:
                s=s+SeparatingSignN(self.BefGH)
                s=s+GenHeader
                s=s+SeparatingSignN(self.AftGH)
            if self.ShowRowN==1:
                s=s+SeparatingSignN(self.BefN)
                s=s+str(NToShow)
                s=s+SeparatingSignN(self.AftN)
            if self.ShowHeader==1:
                s=s+SeparatingSignN(self.BefN)
                s=s+Header
                s=s+SeparatingSignN(self.AftN)
        elif self.HeaderAndN_GNH1_NGH2_HGN3_HNG4==2:
            if self.ShowRowN==1:
                s=s+SeparatingSignN(self.BefN)
                s=s+str(NToShow)
                s=s+SeparatingSignN(AftN)
            if self.ShowGenHeader==2:
                s=s+SeparatingSignN(self.BefGH)
                s=s+GenHeader
                s=s+SeparatingSignN(self.AftGH)
            if self.ShowHeader==1:
                s=s+SeparatingSignN(self.BefN)
                s=s+Header
                s=s+SeparatingSignN(self.AftN)
        elif self.HeaderAndN_GNH1_NGH2_HGN3_HNG4==3:
            if self.ShowHeader==1:
                s=s+SeparatingSignN(self.BefN)
                s=s+Header
                s=s+SeparatingSignN(self.AftN)
            if self.ShowGenHeader==2:
                s=s+SeparatingSignN(self.BefGH)
                s=s+GenHeader
                s=s+SeparatingSignN(self.AftGH)
            if self.ShowRowN==1:
                s=s+SeparatingSignN(self.BefN)
                s=s+str(NToShow)
                s=s+SeparatingSignN(self.AftN)
        elif self.HeaderAndN_GNH1_NGH2_HGN3_HNG4==4:
            if self.ShowHeader==1:
                s=s+SeparatingSignN(self.BefN)
                s=s+Header
                s=s+SeparatingSignN(self.AftN)
            if self.ShowRowN==1:
                s=s+SeparatingSignN(self.BefN)
                s=s+str(NToShow)
                s=s+SeparatingSignN(self.AftN)
            if self.ShowGenHeader==2:
                s=s+SeparatingSignN(self.BefGH)
                s=s+GenHeader
                s=s+SeparatingSignN(self.AftGH)
        return s

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
        self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8=1#5

    def GetContentCellBef(self, LineNToShow, ColNToShow, CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh=0):
        s=""
        if vsh==1:
            print("GetContentCellBef starts working")
            print("given:")
            print("LineNToShow="+str(LineNToShow)+" ColNToShow="+str(ColNToShow))
            print(" CellSelfText="+CellSelfText+" LHSelfText="+LHSelfText+" CHSelfText="+CHSelfText)
            print("LGHSelfText="+LGHSelfText+" CGHSelfText="+CGHSelfText+" THdrSelfText="+THdrSelfText)
            print("Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8="+str(self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8))
        LHdr=self.LineHdrParams.ToStringRowHeaderCellBef(LHSelfText, LineNToShow, LGHSelfText)
        CHdr=self.ColHdrParams.ToStringRowHeaderCellBef(CHSelfText, ColNToShow, CGHSelfText)
        if self.ShowTblHdr==1:
            s=s+THdrSelfText
            if vsh==1:
                print("THdrSelfText="+THdrSelfText+" s="+s)
        if self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8==0:
            s=s+SeparatingSignN(self.BefCnt)
            if vsh==1:
                print("self.BefCnt="+str(self.BefCnt)+" s="+s)
            s=s+CellSelfText
            if vsh==1:
                print("CellSelfText="+CellSelfText+" s="+s)
            s=s+SeparatingSignN(self.AftCnt)
            if vsh==1:
                print("self.AftCnt="+str(self.AftCnt)+" s="+s)
        elif self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8==1:
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
        elif self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8==2:
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
        elif self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8==3:
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
        elif self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8==4:
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
        elif self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8==5:
            s=s+SeparatingSignN(self.BefLH)
            if vsh==1:
                print("self.BefLH="+str(self.BefLH)+" s="+s)
            s=s+LHdr
            if vsh==1:
                print("LHdr="+LHdr+" s="+s)
            s=s+SeparatingSignN(self.AftLH)
            if vsh==1:
                print("self.AftLH="+str(self.AftLH)+" s="+s)
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
        elif self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8==6:
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
        elif self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8==7:
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
        elif self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8==8:
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
        self.ShowTblHdr=1
        #self.ShowLH=0
        #self.ShowCH=0
        self.BefLH=SeparCharNEmpty
        self.AftLH=SeparCharNEmpty
        self.BefCH=SeparCharNEmpty
        self.AftCH=SeparCharNEmpty
        self.BefCnt=SeparCharNEmpty
        self.AftCnt=SeparCharNEmpty
        self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8=0
    
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
        self.LineHdrParams.BefN=SeparCharNOpenBracket#(
        self.LineHdrParams.AftN=SeparCharNComma#,
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
        self.ColHdrParams.AftN=SeparCharNEqSgn#=
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
        self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8=5

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
        self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8=5

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
        self.Cnt0_LCnt1_CCnt2_CntL3_CntC4_LCCnt5_CLCnt6_CntLC7_CntCL8=6
        
class TableRepr:
    def __init__(self):
        self.general=TableRepr_General()
        self.LoCH=TableRepr_RowHeaderCell()
        self.CoLH=TableRepr_RowHeaderCell()
        self.Cont=TableRepr_ContentCell()

    def GetIfLineOfColHeaderToShow(self):
        y=0
        if isinstance(self.general, TableRepr_General):
            y=self.general.ShowLineOfColHeader()
        return y

    def GetIfColOfLineHeaderToShow(self):
        y=0
        if isinstance(self.general, TableRepr_General):
            y=self.general.ShowColOfLineHeader()
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

    def GetLineOfColHeaderCellBef(self, LineHeader, LineN, LinesGenHeader):
        s=""
        LineNToShow=self.CalcLineNToShow(LineN)
        if isinstance(self.LoCH, TableRepr_RowHeaderCell):
            s=self.LoCH.ToStringRowHeaderCellBef(self, LineHeader, LineNToShow, LinesGenHeader)
        return s

    def GetColOfLineHeaderCellBef(self, ColHeader, ColN, ColumnsGenHeader):
        s=""
        ColNToShow=self.CalcColumnNToShow(ColN)
        if isinstance(self.CoLH, TableRepr_RowHeaderCell):
            s=self.CoLH.ToStringRowHeaderCellBef(self, ColHeader, ColNToShow, ColumnsGenHeader)
        return s

    def GetContentCellBef(self, LineN, ColN, CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh=0):
        s=""
        LineNToShow=self.CalcLineNToShow(LineN)
        ColNToShow=self.CalcColumnNToShow(ColN)
        if isinstance(self.Cont, TableRepr_ContentCell):
            s=self.Cont.GetContentCellBef(LineNToShow, ColNToShow, CellSelfText, LHSelfText, CHSelfText, LGHSelfText, CGHSelfText, THdrSelfText, vsh)
        return s

    def SetAsSimple(self):
        #if isinstance(self.general, TableRepr_General):
        #    self.general.SetAsSimple()
        #if isinstance(self.LoCH, TableRepr_RowHeaderCell):
        #    self.LoCH.SetAsSimple()
        #if isinstance(self.CoLH, TableRepr_RowHeaderCell):
        #    self.CoLH.SetAsSimple()
        if isinstance(self.Cont, TableRepr_ContentCell):
            self.Cont.SetAsSimple()

    def SetAsMatrix(self):
        #if isinstance(self.general, TableRepr_General):
        #    self.general.SetAsMatrix()
        #if isinstance(self.LoCH, TableRepr_RowHeaderCell):
        #    self.LoCH.SetAsMatrix()
        #if isinstance(self.CoLH, TableRepr_RowHeaderCell):
        #    self.CoLH.SetAsMatrix()
        if isinstance(self.Cont, TableRepr_ContentCell):
            self.Cont.SetAsMatrix()

    def SetAsFn2D(self):
        #if isinstance(self.general, TableRepr_General):
        #    self.general.SetAsFn2D()
        #if isinstance(self.LoCH, TableRepr_RowHeaderCell):
        #    self.LoCH.SetAsFn2D()
        #if isinstance(self.CoLH, TableRepr_RowHeaderCell):
        #    self.CoLH.SetAsFn2D()
        if isinstance(self.Cont, TableRepr_ContentCell):
            self.Cont.SetAsFn2D()

    def SetAsFullInfo(self):
        #if isinstance(self.general, TableRepr_General):
        #    self.general.SetAsFullInfo()
        #if isinstance(self.LoCH, TableRepr_RowHeaderCell):
        #    self.LoCH.SetAsFullInfo()
        #if isinstance(self.CoLH, TableRepr_RowHeaderCell):
        #    self.CoLH.SetAsFullInfo()
        if isinstance(self.Cont, TableRepr_ContentCell):
            self.Cont.SetAsFullInfo()

