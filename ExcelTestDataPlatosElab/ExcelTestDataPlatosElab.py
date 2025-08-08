import pandas as pd
df=pandas.DataFrame




class RequestCfg:
    def __init__(self, MFlToCalc=1, VerdictLoc_AfJeUnit1_AcoAfAllUnits2=1, MFlWriteTo_ColsAfIniData=3):
        self.MFlToCalc=MFlToCalc
        self.VerdictsLage_AfJeUnit1_AcoAfAllUnits2=VerdictsLage_AfJeUnit1_AcoAfAllUnits2
        self.MFlWriteTo_ColsAfIniData=MFlWriteTo_ColsAfIniData

class RequestData:
    def __init__(self, tColN, fuelRestColN, dt_sec=0):
        self.tColN=TColN
        self.fuelRestColN=fuelRestColN
        self.dt_sec=dt_sec
        self.mFlToCalc=mFlToCalc

class OneUnitPart:
    def __init__(self, ColN, UnitName, dVal, minVal=0, maxVal=0, dValDefined=1, minValDefined=0, maxValDefined=0):
        self.ColN=ColN
        self.UnitName=UnitName
        self.dVal=dVal
        self.minVal=minVal
        self.maxVal=maxVal
        self.dValDefined=dValDefined
        self.minValDefined=minValDefined
        self.maxValDefined=maxValDefined

    def CheckVal(val):
        pass

class FullRequest:
    def __init__(self, units, requestData):
        self.units=units
        self.requestData=requestData

    def getQUnits(self):
        return len(self.units)

    def getUnitNByName(self, unitName):
        RN=0
        QUnits=self.getQUnits()
        for i in range(1, QUnits+1):
            if unitName=self.units[i-1].UnitName:
                RN=i
        return RN

#class Data

def ParseTimeStrToTimeIndex(timeStr):
    hStr=timeStr[1-1:2+1-1]
    mStr=timeStr[3-1:4+1-1]
    sStr=timeStr[7-1:8+1-1]
    L=len(timeStr)
    if L>8:
        msStr=timeStr[10-1:]
        tIndex=0
        h=int(hStr)
        m=int(mStr)
        s=int(msStr)
        ms=int(msStr)
        msOrd=len(msStr)
    timeIndex=3600*h+60*m+s
    if msOrd>0:
        for i in range(msOrd):
            timeIndex*=10
        timeIndex+=ms
    return timeIndex, msOrd

#class ColNs:
#    def __init__(self, requestData, distBtwData):
#        self.QUnits=len(requestData.units)
#        self.unitNValColN=[]
#        self.unitNCheckColN=[]
#        self.mFlColN=0
#        self.fuelRestColN=0
#        selt.timeColN=0
#        self.lastIniDataColN=0
#        self.GeneralVerdictColN=0

def getDataFrame(fileName, path, requestData):
    df=pd.read_excel(path+"\\"+fileName)
    return df

def getMinTimeIndexAndOrd(df, requestData):
    tColN=requestData.requestData.tColN
    minTimeStr=df[tColN-1][1-1]
    nxtTimeStr=df[tColN-1][2-1]
    minTimeIndex, msOrd=ParseTimeStrToTimeIndex(minTimeStr)
    nxtTimeIndex, msOrd=ParseTimeStrToTimeIndex(nxtTimeStr)
    return minTimeIndex, msOrd

def getQLinesInOneSecond(df, requestData):
    minTimeIndex, msOrd = ParseTimeStrToTimeIndex(minTimeStr)
    nxtTimeIndex, msOrd = ParseTimeStrToTimeIndex(nxtTimeStr)

def getTimeRow(df, requestData):
    return df[requestData.requestData.tColN-1]

def getFuelRestRow(df, requestData):
    return df[requestData.requestData.tColN-1]

def getQUnits(requestData):
    return len(requestData.units)
        
def getUnitRowN(df, requestData, unitN):
    rowN=requestData.units[unitN-1].ColN
    return df[rowN-1]

def getUnitRowByName(df, requestData, unitName):
    rowN=requestData.getUnitNByName(unitName)
    return df[rowN-1]

def getFinTime(startTime, durationSec, 
    
        

class Row:
    def __init__(self, startTimeStr, finTimeStr, unitsRows, requestData):#, requestData):
        self.startTimeStr= startTimeStr
        self.finTimeStr=finTimeStr
        self.unitsRows=unitsRows
        #self.requestData=requestData
        self.startTimeIndex, self.msOrd=self.ParseTimeStrToTimeIndex(startTimeStr)
        self.finTimeIndex, self.msOrd=self.ParseTimeStrToTimeIndex(finTimeStr)
        #self.checkVals=[]
        self.checkUnits=[]
        self.checkMins=[]
        self.checkMaxs=[]
        self.checkDiffs=[]
        self.mins=[]
        self.maxs=[]
        self.diffs=[]
        QUnits=len(self.unitsRows)
        QVals=len(self.unitsRows[1-1])
        for i in range(QUnits):
            self.mins.append(0)
            self.maxs.append(0)
            self.diffs.append(0)
            self.checkMins.append(0)
            self.checkMaxs.append(0)
            self.checkDiffs.append(0)
            self.checkUnits.append(0)
            for j in range(1, QVals+1):
                curVal=self.unitsRows[i][j-1]#ce cols!
                if j==1 or curVal<self.mins[i]:
                    self.mins[i]=curVal
                if j==1 or curVal>self.maxs[i]:
                    self.maxs[i]=curVal
            self.diffs[i]=self.maxs[i]-self.mins[i]
            if requestData.units[i].minValDefined==0 and self.mins[i]>requestData.units[i].minVal:
                self.checkMins[i]=0
            else:
                self.checkMins[i]=1
            if requestData.units[i].maxValDefined==0 and self.maxs[i]>requestData.units[i].maxVal:
                self.checkMaxs[i]=0
            else:
                self.checkMaxs[i]=1
            if requestData.units[i].dValDefined==0 and self.diffs[i]>requestData.units[i].dVal:
                self.checkDiffs[i]=0
            else:
                self.checkDiffs[i]=1
            self.checkUnits[i]=self.checkMins[i]*self.checkMaxs[i]*self.checkDiffs[i]

    def getDuration(self):
        return

#read file
#form rows fron df
def FormRow(df, tToStart, curDuration):
    
                 
