import copy
from PyStdVector2 import *

class StringParams:
    def __init__():
        self.inLength=6
        self.QHidden=0
        self.bef=""
        self.aft=""
        self.AlignL1R2CL3CR4=1
        self.FillAft="."
        self.FillBef=" "
        self.MarkBef=" "
        self.MarkAft=" "

def MyStrLJust(data, inLength, FillAft=".", FillBef=" "):
    L=len(data)
    d=inLength-L


#def StringFormat(data, inLength, QHidden, AlignL1R2CL3CR4, FillAft=".", FillBef=" ", vsh=0):
    #def StringFormat(data, bef, aft, inLength, QHidden, AlignL1R2CL3CR4, FillAft=".", FillBef=" ", vsh=0):
def StringFormat(data, inLength, QHidden, AlignL1R2CL3CR4, FillAft=".", FillBef=" ", BefCut="<", AftCut=">", BefNonCut=" ", AftNonCut=" ", BefMark="+", AftMark=" ", vsh=0):
    R=""
    if vsh==1:
        print("StringFormat starts working")
    q=len(data)
    if vsh==1:
        print("q=",q," QHidden=",QHidden)
    #StrToPlace=bef+data+aft
    #StrToPlace=bef+data[QHidden:]+aft
    bef=""
    aft=""
    StrFull=bef+data+aft
    #StrFull=bef+data+aft
    #StrFull=data
    StrToPlace=StrFull[int(QHidden):int(QHidden+1+inLength-1)]
    #Li=ArrayLength(StrToPlace)
    Li1=len(StrToPlace)
    if vsh==1:
        print("q=",q," StrFull=",StrFull," StrToPlace=",StrToPlace," QHidden=",QHidden," Li1=",Li1)
    #if Li>=inLength:
    #if Li1>=inLength:
    #    StrToPlace= StrFull[int(QHidden):int(inLength)]
    #    if vsh==1:
    #        print(" Li1=",Li1,">=inLength=",inLength," R=",R)
    #else:
    if vsh==1:
        print("justifying")
    if AlignL1R2CL3CR4==1:
        R=StrToPlace.ljust(inLength, FillAft)  
    elif AlignL1R2CL3CR4==2:
        R=StrToPlace.rjust(inLength, FillBef)    
    elif AlignL1R2CL3CR4==3:
        R=StrToPlace.center(inLength, FillBef) 
    elif AlignL1R2CL3CR4==4:
        R=StrToPlace.center(inLength, FillBef)
    if vsh==1:
        print("R=",R)
        print("marking cut sides")
    if QHidden==0:
        R=BefNonCut+R
    else:
        R=BefCut+R
    if vsh==1:
        print("QHidden=",QHidden)
        print("R=",R)
    HiddenAft=(q-QHidden)-Li1
    #HiddenAft=Li1-q
    #if HiddenAft<0:
    #    HiddenAft=0
    if vsh==1:
        print("whole: ",data," cut: ",StrToPlace)
        print("HiddenAft=",HiddenAft)
    if HiddenAft>0:
        R=R+AftCut
    else:
        R=R+AftNonCut
    if vsh==1:
        print("R=",R)
        print("marking:")
    R=BefMark+R+AftMark
    if vsh==1:
        print("finally: R=",R)
        print("StringFormat finishes working")
    return R

def StringFormat1(data, inLength, QHidden, bef="", aft="", AlignL1R2CL3CR4=1, FillAft=".", FillBef=" ", MarkBef=" ", MarkAft=" "):
    R=""
    q=len(data)
    #StrToPlace=bef+data+aft
    #StrToPlace=bef+data[QHidden:]+aft
    StrFull=bef+data+aft
    StrToPlace=StrFull[QHidden:]
    Li=ArrayLength(StrToPlace)
    if Li>=inLength:
        R= StrFull[QHidden:inLength]  
    else:
        if AlignL1R2CL3CR4==1:
            pass
        elif AlignL1R2CL3CR4==2:
            pass   
        elif AlignL1R2CL3CR4==3:
            R=StrToPlace.center(inLength, bef) 
        elif AlignL1R2CL3CR4==4:
            R=StrToPlace.center(inLength, bef)


def StringFormat2(data, paramsExt=[]):
    if(paramsExt==[]):
        params=StringParams()
    elif isinstance(paramsExt, StringParams):
        params=paramsExt
    inLength=params.inLength
    QHidden=params.QHidden
    bef=params.bef
    aft=params.aft
    AlignL1R2CL3CR4=params.AlignL1R2CL3CR4
    FillAft=params.FillAft
    FillBef=params.FillBef
    MarkBef=params.MarkBef
    MarkAft=params.MarkAft
    #
    s=StringFormat1(data, inLength, QHidden, bef, aft, AlignL1R2CL3CR4, FillAft, FillBef, MarkBef, MarkAft)
    return s

def ParseTableCorner(data, vsh=0):
    R=[]
    TableName=""
    LinesGeneralName=""
    ColumnsGeneralName=""
    Q=len(data)
    NColon=0
    NSlash=0
    CountColons=0
    CountSlashes=0
    if vsh==1:
        print("ParseTableCorner starts working")
    if isinstance(data, str) and len(data)>0:
        if vsh==1:
            print("data=", data, "L=", len(data))
            print("Analyzing every character:")
        for i in range(1, Q+1):
            s=data[i-1:i-1+1]
            if vsh==1:
                print(i, " ", s)
            #if s=="\\":
            if s=='\\':
                NSlash=i
                CountSlashes=CountSlashes+1
            if s==":":
                NColon=i
                CountColons=CountColons+1
        if vsh==1:
            print("so:")
        if vsh==1:
            print("CountColons=", CountColons, " CountSlashes=", CountSlashes, " NColon=", NColon, " NSlash=", NSlash)
        if CountColons>1 or CountSlashes>1 or (NSlash>0 and NSlash<NColon):
            pass
            if vsh==1:
                print("non-readable format, not a corner")
        elif NColon==0 and NSlash==0:
            TableName=copy.deepcopy(data)
            if vsh==1:
                print("no delimiters: table name only")
        elif NColon==0 and NSlash==1:
            ColumnsGeneralName=data[1+1-1: Q]
            if vsh==1:
                print("first slash - CGN")
        elif NColon==0 and NSlash==Q:
            LinesGeneralName=data[1-1: Q-1]
            if vsh==1:
                print("last slash, no colon - CGN")
        elif NColon==Q and NSlash==0:
            TableName=data[1-1: Q-1]
            if vsh==1:
                print("last colon, no slash  - TN")
        else:
            #if NSlash!=1:
            TableName=data[1-1:NColon-1]
            #if NSlash>0:
            LinesGeneralName=data[NColon+1-1: NSlash-1]
            ColumnsGeneralName=data[NSlash+1-1: Q]
        if vsh==1:
            print("ParseTableCorner finishes working")
        R=[TableName, LinesGeneralName, ColumnsGeneralName]
    return R
    
def Parse2DStrArrayAsTable(source, RowOfExtRowHeaderExistsNo0Yes1, RowOfIneRowHeaderExistsNo0Yes1):
    R=[]
    Headers=[]
    corner=[]
    TableName=""
    LinesGeneralName=""
    ColumnsGeneralName=""
    RowOfExtRowHeader=[]
    RowOfIneRowHeader=[]
    content=[]
    ContentLine=[]
    line=[]
    data=copy.deepcopy(source)
    if isinstance(data, list) and len(data)>0 and isinstance(data[1-1], list):
        Q=len(data)
        Lmin=Get2DArrayMinLength(data)#from PyStdVector2 import *
        if RowOfExtRowHeaderExistsNo0Yes1==0 and RowOfIneRowHeaderExistsNo0Yes1==0:
            content=copy.deepcopy(data)
        elif RowOfExtRowHeaderExistsNo0Yes1==0 and RowOfIneRowHeaderExistsNo0Yes1==1:
            content=data[2-1:len(data)]
            RowOfIneRowHeader=data[1-1]
        elif RowOfExtRowHeaderExistsNo0Yes1==1 and RowOfIneRowHeaderExistsNo0Yes1==0:
            for i in range(1, Q+1):
                line=copy.deepcopy(data[i-1])
                #L=len(line)
                #ContentLine=line[2-1:L]
                ContentLine=line[2-1:Lmin]
                content.append(ContentLine)
                RowOfExtRowHeader.append(line[1-1])
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
            Headers=ParseTableCorner(corner)
            TableName=Headers[1-1]
            LinesGeneralName=Headers[2-1]
            ColumnsGeneralName=Headers[3-1]
        R=[content, RowOfExtRowHeader, RowOfIneRowHeader, Headers]
        R=[["content",content],
           ["RowOfExtRowHeader",RowOfExtRowHeader],
           ["RowOfIneRowHeader",RowOfIneRowHeader],
           ["TableName",TableName],
           ["LinesGeneralName",LinesGeneralName],
           ["ColumnsGeneralName",ColumnsGeneralName]]
    return R
            
        
