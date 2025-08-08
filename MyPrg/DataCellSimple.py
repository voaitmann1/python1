import math
import copy
#
#import PyStdVector2#.py
#import DBDataClasses
from DBDataClasses import *
from PyStdVector2 import *
from TableReprSimple import *
#
DataCell_Simple_TypeN=1
DataCell_ComboBoxOrMemo_TypeN=2
DataCell_DBTableHeader_TypeN=3
DataCell_ColHeader_DBFieldOrItems_TypeN=4
#
class DataCell_Simple:
    def GetType(self):          #2
         return DataCell_Simple_TypeN
    #    return 1 #1- simple, 3-combobox, 2-DBFldHdr
    def __init__(self, val=""): #1
        self.data=val
        #print("DataCell_Simple created")
        #print("val="+str(self.data))
        
    def GetVal(self, N=1): #3
        return self.data

    def GetItems(self):
        return self.data

    def GetItem(self, N=1): #4
        return self.data
     # ConcrType
    def GetFloatVal(self): #5
        return float(self.data)

    def GetIntVal(self): #6
        return int(self.data)

    def GetBoolVal(self): #7
        return bool(self.data)

    def GetStrVal(self): #8
        return str(self.data)

    # for combobox
    def GetActiveN(self): #for combobox-1
        return 1

    def GetActiveItem(self): #for combobox-2
        return self.data
    
    def SetActiveN(self, val): #for combobox-3
        zero=0
        #
    def SetActiveNByVal(self, val): #for combobox-4
        zero=0
        #
    def GetQItems(): #for combobox-5
        return 1

    def Set(self, val1="", val2=[], val3=[], val4=[]): #1
        self.data=val1

    def SetVal(self, val, N=0): #1
        self.data=val
    #
    def GetTableNameToDisplay(self):
         return ""

    def GetTableNameInDB(self):
         return ""

    def GetDBNameInDBCS(self):
         return ""

    def GetDBTypeName(self):
         return ""

    def GetDBTypeN(self):
        return 0

    def GetDBFileFullName(self):
        return ""
    #
    def GetDBTableDataToCreate(self):
        return []
    
    def GetDBTableData(self):
        return []
    #
    #
    def SetTableNameToDisplay(self, val):
        pass

    def SetTableNameInDB(self, val):
        pass
        
    def SetDBNameInDBCS(self, val):
        pass

    def SetDBTypeName(self, val):
        pass

    def SetDBTypeN(self, val):
        pass

    def SetDBFileFullName(self, val):
        pass

    def SetDBTableDataToCreate(self, val):
        pass
    def SetDBTableData(self, val):
        pass
            
    def SetColNameToDisplay(self, val):
        pass
    def SetDBFieldName(self, val):
        pass
    def SetFieldTypeN(self, val):
        pass
    def SetFieldTypeName(self, val):
        pass
    def SetFieldLength(self, val):
        pass
    def SetDBFieldCharacteristicsNumber(self, val):
        pass
    def SetIfIsKeyField(self, val):
        pass
    def SetIfIsCounter(self, val):
        pass
    def SetIfIsNotNull(self, val):
        pass
    def SetIfIsAutoIncrement(self, val):   
        pass
    #
    def SetItemsTableName(self, val):
        pass
    def SetItemsTableItemsFieldName(self, val):
        pass
    def SetItemsTableKeyFieldName(self, val):
        pass
    #
    def GetColNameToDisplay(self):
        return self.data
    def GetDBFieldName(self):
        s=""
        return s
    def GetFieldTypeN(self):
        r=0
        return r
    def GetFieldTypeName(self):
        r=0
        return r
    def GetFieldLength(self):
        r=0
        return r
    def GetDBFieldCharacteristicsNumber(self):
        r=0
        return r
    def GetIfIsKeyField(self):
        r=0
        return r
    def GetIfIsCounter(self):
        r=0
        return r
    def GetIfIsNotNull(self):
        r=0
        return r
    def GetIfIsAutoIncrement(self):   
        r=0
        return r
    #
    def GetItemsTableName(self):
        return ""
    def GetItemsTableItemsFieldName(self):
        return ""
    def GetItemsTableKeyFieldName(self):
        return ""
    #
    def ToString(self, sBef="", sAft=""):
        s=""
        if isinstance(self.data, str):
            s=self.data
            s=sBef+s
            s=s+sAft
        elif isinstance(self.data, float) or isinstance(self.data, int):
            s=str(self.data)
            s=sBef+s
            s=s+sAft
        return s

class DataCell_ComboboxOrMemo:
    def GetType(self):          #2
         return DataCell_ComboBoxOrMemo_TypeN
    #    return 1 #1- simple, 3-combobox, 2-DBFldHdr
    def __init__(self, val1, val2=0, vsh=0): #1
        self.items=[]
        self.data=0
        #print("DataCell_ComboboxOrMemo created")
        #print("val1=",val1," val2=",val2)
        if isinstance(val1, list):
            self.items=copy.deepcopy(val1)
            #print("list accepted")
        elif isinstance(val1, float) or isinstance(val1, int) or isinstance(val1, str):
            self.items=[]
            self.items.append(val1)
            #self.items.append(str(val1))
            #or could do so: else remain prev
            #print("one item only: ",self.items[1-1])
        #print("val1=",val1," val2=",val2)
        if isinstance(val2, int):
            self.SetActiveN(val2)
        else:
            self.data=1
        #print("val1=",val1," val2=",str(val2))
        #print("ActiveN="+str(self.GetActiveN())+" ActiveItem="+str(self.GetItem()))
        #print("constructor finishes working")
        
    def GetVal(self, N=1): #3
        return self.data

    def GetItems(self):
        return self.items

    def GetItem(self, N=0): #4
        R=0
        Q=len(self.items)
        if N==0:
            N=self.data        
        if(N>=1 and N<=Q):
            R=self.items[N-1]
        return R
        
     # ConcrType
    def GetFloatVal(self): #5
        return float(self.data)

    def GetIntVal(self): #6
        return int(self.data)

    def GetBoolVal(self): #7
        return bool(self.data)

    def GetStrVal(self): #8
        return str(self.data)

    # for combobox
    def GetActiveN(self): #for combobox-1
        return self.data

    def GetActiveItem(self): #for combobox-2
        return self.items[self.data]
    
    def SetActiveN(self, val, vsh=0): #for combobox-3
        if vsh==1:
            print("SetActiveN starts working")
            print("val="+str(val))
        Q=len(self.items)
        if vsh==1:
            print("Q="+str(Q)+" items")
        if(Q==0):
            self.data=0
            if vsh==1:
                print("Q=0="+str(Q)+"=>ActiveN=0="+str(self.data))
        else:
            if val>=1 and val<=Q:
                self.data=val
            else:
                self.data=1
        if vsh==1:
            print("ActiveN = "+str(self.data))
            print("SetActiveN finishes working")
        
    #
    def SetActiveNByVal(self, val): #for combobox-4
        Q=len(self.items)
        for i in range(1, Q+1):
            if self.items[i-1]==val:
                self.data=i
    #
    def GetQItems(self): #for combobox-5
        return len(self.items)

    def Set(self, val1, val2=1, val3=[], val4=[]): #1
        if isinstance(val1, list):
            self.cell=DataCell_ComboboxOrMemo(val1)
        elif isinstance(val, float) or isinstance(val1, int) or isinstance(val1, str):
            self.items=[]
            self.items.append(val1)
            #self.items.append(str(val1))
            #or could do so: else remain prev
        if isinstance(val2, int):
            self.cell.SetActiveN(val2)
        else:
            self.data=1

    def SetVal(self, val, N=0): #1
        Q=len(self.items)
        if N==0:
            N=Q
        if N>=1 and N<=Q:
            self.items[N-1]=val
    #
    def GetTableNameToDisplay(self):
        R=""
        if self.items!=[] and len(self.items)>1:
            R=self.items[1-1] 
        return R

    def GetTableNameInDB(self):
        R=""
        if self.items!=[] and len(self.items)>2:
            R=self.items[2-1] 
        return R

    def GetDBNameInDBCS(self):
        R=""
        if self.items!=[] and len(self.items)>3:
            R=self.items[3-1] 
        return R

    def GetDBTypeName(self):
        R=""
        if self.items!=[] and len(self.items)>4:
            R=self.items[4-1] 
        return R

    def GetDBTypeN(self):
        R=0
        if self.items!=[] and len(self.items)>5:
            R=int(self.items[5-1]) 
        return R

    def GetDBFileFullName(self):
        R=""
        if self.items!=[] and len(self.items)>6:
            R=self.items[6-1] 
        return R
    #
    def GetDBTableDataToCreate(self):
        return []
    
    def GetDBTableData(self):
        return []
    #
    def SetTableNameToDisplay(self, val):
        if len(self.items)<1:
            self.items.append(val)
        else:
            self.items[1-1]=val

    def SetTableNameInDB(self, val):
        while len(self.items)<2:
            self.items.append("")
        self.items[2-1]=val
        
    def SetDBNameInDBCS(self, val):
        while len(self.items)<3:
            self.items.append("")
        self.items[3-1]=val

    def SetDBTypeName(self, val):
        while len(self.items)<4:
            self.items.append("")
        self.items[4-1]=val

    def SetDBTypeN(self, val):
        while len(self.items)<5:
            self.items.append("")
        self.items[5-1]=val

    def SetDBFileFullName(self, val):
        while len(self.items)<6:
            self.items.append("")
        self.items[6-1]=val
    #
    def SetDBTableDataToCreate(self, val):
        if isinstance(val, list):
            if len(val)>=5:
                if len(self.items)==0:
                    self.items.append("")
                TableNameToDisplay=self.items[1-1]
                self.items=[]
                self.items.append(TableNameToDisplay)
                for i in range(1, 5+1):
                    self.items.append(val[i-1])
                    
    def SetDBTableData(self, val):
        if isinstance(val, list) and len(val)>=6:
            self.items=[]
            for i in range(1, 6+1):
                self.items.append(val[i-1])
    #
    def SetColNameToDisplay(self, val):
        if len(self.items)==0:
            self.items.append(val)
        else:
            self.items[1-1]=val
    def SetDBFieldName(self, val):
        while len(self.items)<2:
            self.items.append("")
        self.items[2-1]=val
    def SetFieldTypeN(self, val):
        while len(self.items)<3:
            self.items.append("")
        self.items[3-1]=val
    def SetFieldTypeName(self, val):
        while len(self.items)<4:
            self.items.append("")
        self.items[4-1]=val
    def SetFieldLength(self, val):
        while len(self.items)<5:
            self.items.append("")
        self.items[5-1]=val
    def SetDBFieldCharacteristicsNumber(self, val):
        while len(self.items)<6:
            self.items.append("")
        self.items[6-1]=val
    def SetIfIsKeyField(self, val):
        while len(self.items)<7:
            self.items.append("")
        self.items[7-1]=val
    def SetIfIsCounter(self, val):
        while len(self.items)<8:
            self.items.append("")
        self.items[8-1]=val
    def SetIfIsNotNull(self, val):
        while len(self.items)<9:
            self.items.append("")
        self.items[9-1]=val
    def SetIfIsAutoIncrement(self, val):   
        while len(self.items)<10:
            self.items.append("")
        self.items[10-1]=val
    #
    def SetItemsTableName(self, val):
        while len(self.items)<11:
            self.items.append("")
        self.items[11-1]=val
    def SetItemsTableItemsFieldName(self, val):
         while len(self.items)<12:
            self.items.append("")
         self.items[12-1]=val
    def GetItemsTableKeyFieldName(self, val):
         while len(self.items)<13:
            self.items.append("")
         self.items[13-1]=val
    #
    def GetColNameToDisplay(self):
        r=""
        if len(self.items)>=1:
            r=self.items[1-1]
        return r
    def GetDBFieldName(self):
        r=""
        if len(self.items)>=2:
            r=self.items[2-1]
        return r
    def GetFieldTypeN(self):
        r=0
        if len(self.items)>=3:
            r=self.items[3-1]
        return r
    def GetFieldTypeName(self):
        r=""
        if len(self.items)>=4:
            r=self.items[4-1]
        return r
    def GetFieldLength(self):
        r=0
        if len(self.items)>=5:
            r=self.items[5-1]
        return r
    def GetDBFieldCharacteristicsNumber(self):
        r=0
        if len(self.items)>=6:
            r=self.items[6-1]
        return r
    def GetIfIsKeyField(self):
        r=0
        if len(self.items)>=7:
            r=self.items[7-1]
        return r
    def GetIfIsCounter(self):
        r=0
        if len(self.items)>=8:
            r=self.items[8-1]
        return r
    def GetIfIsNotNull(self):
        r=0
        if len(self.items)>=9:
            r=self.items[9-1]
        return r
    def GetIfIsAutoIncrement(self):   
        r=0
        if len(self.items)>=10:
            r=self.items[10-1]
        return r
    #
    def GetItemsTableName(self):
        r=""
        if len(self.items)>=11:
            r=self.items[11-1]
        return r
    def GetItemsTableItemsFieldName(self):
        r=""
        if len(self.items)>=12:
            r=self.items[12-1]
        return r
    def GetItemsTableKeyFieldName(self):
        r=""
        if len(self.items)>=13:
            r=self.items[13-1]
        return r
    #
    def ToString(self, sBef="", sAft=""):
        s=""
        y=self.GetItem()
        if isinstance(y, str):
            s=y
            s=sBef+s
            s=s+sAft
        elif isinstance(y, float) or isinstance(y, int):
            s=str(self.data)
            s=sBef+s
            s=s+sAft
        return s

class DataCell_DBTableHeader:
    def GetType(self):          #2
         return DataCell_DBTableHeader_TypeN
    #    return 1 #1- simple, 3-combobox, 2-DBFldHdr
    def __init__(self, val1, val2=[], val3=[]): #1
        self.data=""
        self.DBTableData=[]
        if isinstance(val1, str):
            self.data=str(val1)
            if isinstance(val2, str):
                if self.DBTableData==[]:
                    self.DBTableData=TDBTableData()
                self.DBTableData.TableNameInDB=copy.deepcopy(val2)
                if isinstance(val3, list):
                    if self.DBTableData.DBTableDataSuppl==[]:
                        self.DBTableData.DBTableDataSuppl=TDBTableDataSuppl()
                    if len(val3)>=4:
                        self.DBTableData.DBTableDataSuppl=TDBTableDataSuppl()
                        self.DBTableData.DBTableDataSuppl.DBNameInDBCS=copy.deepcopy(val3[1-1])
                        self.DBTableData.DBTableDataSuppl.DBTypeName=copy.deepcopy(val3[2-1])
                        self.DBTableData.DBTableDataSuppl.DBTypeN=copy.deepcopy(int(val3[3-1]))
                        self.DBTableDataSuppl.DBFileFullName=copy.deepcopy(str(val3[4-1]))
                if isinstance(val3, TDBTableDataSuppl):
                    self.DBTableData.DBTableDataSuppl=TDBTableDataSuppl()
                    self.DBTableData.DBTableDataSuppl=copy.deepcopy(val3)
            elif isinstance(val2, TDBTableData):
                #self.DBTableData=TDBTableData()
                self.DBTableData=copy.deepcopy(val2)
            elif isinstance(val2, list) and len(val2)>0:
                self.DBTableData=TDBTableData()
                if len(val3)>=1:
                    self.DBTableData.TableNameInDB=val3[1-1]
                    if len(val3)>=5:
                        self.DBTableData.DBTableDataSuppl=TDBTableDataSuppl()
                        self.DBTableData.DBTableDataSuppl.DBNameInDBCS=copy.deepcopy(val3[2-1])
                        self.DBTableData.DBTableDataSuppl.DBTypeName=copy.deepcopy(val3[3-1])
                        self.DBTableData.DBTableDataSuppl.DBTypeN=copy.deepcopy(int(val3[4-1]))
                        self.DBTableDataSuppl.DBFileFullName=copy.deepcopy(str(val3[5-1]))
        elif isinstance(val1, list):
            if len(val1)>1:
                self.data=copy.deepcopy(val1[1-1])
                if len(val1)>2:
                    if self.DBTableData==[]:
                        self.DBTableData=TDBTableData()
                    self.DBTableData.TableNameInDB=copy.deepcopy(val1[2-1])
                    if len(val1)>3:
                        if self.DBTableData.DBTableDataSuppl==[]:
                            self.DBTableData.DBTableDataSuppl=TDBTableDataSuppl()
                        self.DBTableData.DBTableDataSuppl.DBNameInDBCS=copy.deepcopy(val1[3-1])
                        if len(val1)>4:
                            self.DBTableData.DBTableDataSuppl.DBTypeName=copy.deepcopy(val1[4-1])
                            if len(val1)>5:
                                self.DBTableData.DBTableDataSuppl.DBTypeN=copy.deepcopy(int(val1[5-1]))
                                if len(val1)>6:
                                    self.DBTableData.DBTableDataSuppl.DBFileFullName=copy.deepcopy(str(val1[6-1]))

    def GetVal(self, N=0, vsh=0): #3
        val=""
        if vsh==1:
            print("GetVal starts working")
        if N==0:
            if self.DBTableData!=[]:
                N=2
                if vsh==1:
                    print("DBTableData isn't empty=>N=2="+str(N))
            else:
                N=1
                if vsh==1:
                    print("DBTableData is empty=>N=1="+str(N))
        if N==1:
            val=self.data
        elif N==2:
            if self.DBTableData!=[]:
               val=copy.deepcopy(self.DBTableData.TableNameInDB)
        elif N==3:
            if self.DBTableData.DBTableDataSuppl!=[]:
                val=copy.deepcopy(self.DBTableData.DBTableDataSuppl.DBNameInDBCS)
        elif N==4:
            if self.DBTableData.DBTableDataSuppl!=[]:
                val=copy.deepcopy(self.DBTableData.DBTableDataSuppl.DBTypeName)
        elif N==5:
            if self.DBTableData.DBTableDataSuppl!=[]:
                val=copy.deepcopy(self.DBTableData.DBTableDataSuppl.DBTypeN)
        elif N==6:
            if self.DBTableData.DBTableDataSuppl!=[]:
                val=copy.deepcopy(self.DBTableData.DBTableDataSuppl.DBFileFullName)
        if vsh==1:
            print("N="+str(N)+" val="+str(val))
            print("GetVal finishes working")
        return val

    def GetItems(self):
        return []

    def GetItem(self, N=0): #4
        return self.GetVal(N)
     # ConcrType
    def GetFloatVal(self): #5
        return 0

    def GetIntVal(self): #6
        return 0

    def GetBoolVal(self): #7
        return bool(0)

    def GetStrVal(self): #8
        return self.GetVal()

    # for combobox
    def GetActiveN(self): #for combobox-1
        return 0

    def GetActiveItem(self): #for combobox-2
        return self.GetVal()
    
    def SetActiveN(self, val): #for combobox-3
        pass
        #
    def SetActiveNByVal(self, val): #for combobox-4
        pass
        #
    def GetQItems(): #for combobox-5
        y=1
        if self.DBTableData!=[]:
            if self.DBTableData.DBTableDataSuppl==[]:
                y=2
            else:
                y=self.data,
        return y
    
    def Set(self, val1, val2=[], val3=[], val4=[]): #1
        self.data=""
        self.DBTableData=[]
        if isinstance(val1, str):
            self.data=str(val1)
            if isinstance(val2, str):
                if self.DBTableData==[]:
                    self.DBTableData=TDBTableData()
                self.DBTableData.TableNameInDB=copy.deepcopy(val2)
                if isinstance(val3, list):
                    if self.DBTableData.DBTableDataSuppl==[]:
                        self.DBTableData.DBTableDataSuppl=TDBTableDataSuppl()
                    if len(val3)>=4:
                        self.DBTableData.DBTableDataSuppl=TDBTableDataSuppl()
                        self.DBTableData.DBTableDataSuppl.DBNameInDBCS=copy.deepcopy(val3[1-1])
                        self.DBTableData.DBTableDataSuppl.DBTypeName=copy.deepcopy(val3[2-1])
                        self.DBTableData.DBTableDataSuppl.DBTypeN=copy.deepcopy(int(val3[3-1]))
                        self.DBTableDataSuppl.DBFileFullName=copy.deepcopy(str(val3[4-1]))
                if isinstance(val3, TDBTableDataSuppl):
                    self.DBTableData.DBTableDataSuppl=TDBTableDataSuppl()
                    self.DBTableData.DBTableDataSuppl=copy.deepcopy(val3)
            elif isinstance(val2, TDBTableData):
                #self.DBTableData=TDBTableData()
                self.DBTableData=copy.deepcopy(val3)
            elif isinstance(val2, list) and len(val2)>0:
                self.DBTableData=TDBTableData()
                if len(val3)>=1:
                    self.DBTableData.TableNameInDB=val3[1-1]
                    if len(val3)>=5:
                        self.DBTableData.DBTableDataSuppl=TDBTableDataSuppl()
                        self.DBTableData.DBTableDataSuppl.DBNameInDBCS=copy.deepcopy(val3[2-1])
                        self.DBTableData.DBTableDataSuppl.DBTypeName=copy.deepcopy(val3[3-1])
                        self.DBTableData.DBTableDataSuppl.DBTypeN=copy.deepcopy(int(val3[4-1]))
                        self.DBTableDataSuppl.DBFileFullName=copy.deepcopy(str(val3[5-1]))
        elif isinstance(val1, list):
            if len(val1)>1:
                self.data=copy.deepcopy(val1[1-1])
                if len(val1)>2:
                    if self.DBTableData==[]:
                        self.DBTableData=TDBTableData()
                    self.DBTableData.TableNameInDB=copy.deepcopy(val1[2-1])
                    if len(val1)>3:
                        if self.DBTableData.DBTableDataSuppl==[]:
                            self.DBTableData.DBTableDataSuppl=TDBTableDataSuppl()
                        self.DBTableData.DBTableDataSuppl.DBNameInDBCS=copy.deepcopy(val1[3-1])
                        if len(val1)>4:
                            self.DBTableData.DBTableDataSuppl.DBTypeName=copy.deepcopy(val1[4-1])
                            if len(val1)>5:
                                self.DBTableData.DBTableDataSuppl.DBTypeN=copy.deepcopy(int(val1[5-1]))
                                if len(val1)>6:
                                    self.DBTableData.DBTableDataSuppl.DBFileFullName=copy.deepcopy(str(val1[6-1]))
        
        
    def SetVal(self, val, N=0): #1
        if N==1:
            self.data=val
        elif N==2:
            if self.DBTableData==[]:
               self.DBTableData=TDBTableData()
            self.DBTableData.TableNameInDB=copy.deepcopy(val)
        elif N==2:
            if self.DBTableData.DBTableDataSuppl==[]:
                self.DBTableData.DBTableDataSuppl=TDBTableDataSuppl()
                self.DBTableData.DBTableDataSuppl.DBNameInDBCS=copy.deepcopy(val)
        elif N==3:
            if self.DBTableData.DBTableDataSuppl==[]:
                self.DBTableData.DBTableDataSuppl=TDBTableDataSuppl()
                self.DBTableData.DBTableDataSuppl.DBTypeName=copy.deepcopy(val)
        elif N==4:
            if self.DBTableData.DBTableDataSuppl==[]:
                self.DBTableData.DBTableDataSuppl=TDBTableDataSuppl()
                self.DBTableData.DBTableDataSuppl.DBTypeN=copy.deepcopy(int(val))
        elif N==5:
            if self.DBTableData.DBTableDataSuppl==[]:
                self.DBTableData.DBTableDataSuppl=TDBTableDataSuppl()
                self.DBTableData.DBTableDataSuppl.DBFileFullName=copy.deepcopy(str(val))
    #
    def GetTableNameToDisplay(self):
        return self.data

    def GetTableNameInDB(self):
        s=""
        if self.DBTableData!=[]:
            s=self.DBTableData.TableNameInDB
        return s

    def GetDBNameInDBCS(self):
        s=""
        if self.DBTableData!=[]:
            if self.DBTableData.DBTableDataSuppl!=[]:
                s=self.DBTableData.DBTableDataSuppl.DBNameInDBCS
        return s

    def GetDBTypeName(self):
        s=""
        if self.DBTableData!=[]:
            if self.DBTableData.DBTableDataSuppl!=[]:
                s=self.DBTableData.DBTableDataSuppl.DBTypeName
        return s

    def GetDBTypeN(self):
        y=0
        if self.DBTableData!=[]:
            if self.DBTableData.DBTableDataSuppl!=[]:
                y=self.DBTableData.DBTableDataSuppl.DBTypeN
        return y

    def GetDBFileFullName(self):
        s=""
        if self.DBTableData!=[]:
            if self.DBTableData.DBTableDataSuppl!=[]:
                s=self.DBTableData.DBTableDataSuppl.DBFileFullName
        return s
    #
    def GetDBTableDataToCreate(self):
        r=[]
        if self.DBTableData!=[]:
            r=self.DBTableData.DBTableDataSuppl
        return r
    
    def GetDBTableData(self):
        return self.DBTableData
    #
    def SetTableNameToDisplay(self, val):
        self.data=val

    def SetTableNameInDB(self, val):
        if self.DBTableData!=[]:
            self.DBTableData=TDBTableData()
        self.DBTableData.TableNameInDB=val
        
    def SetDBNameInDBCS(self, val):
        if self.DBTableData!=[]:
            self.DBTableData=TDBTableData()
        if self.DBTableData.DBTableDataSuppl==[]:
            self.DBTableData.DBTableDataSuppl=TDBTableDataSuppl()
        self.DBTableData.DBTableDataSuppl.DBNameInDBCS=val

    def SetDBTypeName(self, val):
        if self.DBTableData!=[]:
            self.DBTableData=TDBTableData()
        if self.DBTableData.DBTableDataSuppl==[]:
            self.DBTableData.DBTableDataSuppl=TDBTableDataSuppl()
        self.DBTableData.DBTableDataSuppl.DBTypeName=val

    def SetDBTypeN(self, val):
        if self.DBTableData!=[]:
            self.DBTableData=TDBTableData()
        if self.DBTableData.DBTableDataSuppl==[]:
            self.DBTableData.DBTableDataSuppl=TDBTableDataSuppl()
        self.DBTableData.DBTableDataSuppl.DBTypeN=val

    def SetDBFileFullName(self, val):
        if self.DBTableData!=[]:
            self.DBTableData=TDBTableData()
        if self.DBTableData.DBTableDataSuppl==[]:
            self.DBTableData.DBTableDataSuppl=TDBTableDataSuppl()
        self.DBTableData.DBTableDataSuppl.DBFileFullName=val
    #
    def SetDBTableDataToCreate(self, val):
        if self.DBTableData==[]:
            self.DBTableData=TDBTableData()
        if isinstance(val, TDBTableDataSuppl):
            self.DBTableData.DBTableDataSuppl=copy.deepcopy(val)
        elif isinstance(val, list):
            if len(val)>=1:
                if self.DBTableData.DBTableDataSuppl==[]:
                    self.DBTableData.DBTableDataSuppl=TDBTableDataSuppl()
                self.DBTableData.DBTableDataSuppl.DBNameInDBCS=copy.deepcopy(val[1-1])
                if len(val)>=2:
                    self.DBTableData.DBTableDataSuppl.DBTypeName=copy.deepcopy(val[2-1])
                    if len(val)>=3:
                        self.DBTableData.DBTableDataSuppl.DBTypeN=copy.deepcopy(int(val[3-1]))
                        if len(val)>=4:
                            self.DBTableData.DBTableDataSuppl.DBFileFullName=copy.deepcopy(str(val[4-1]))

    def SetDBTableData(self, val):
        if isinstance(val, TDBTableData):
            self.DBTableData=copy.deepcopy(val)
        elif isinstance(val, list):
            if len(val)>=1:
                if self.DBTableData==[]:
                    self.DBTableData=TDBTableData()
                self.DBTableData.TableNameInDB=copy.deepcopy(val[1-1])
                if len(val)>=2:
                    if self.DBTableData.DBTableDataSuppl==[]:
                        self.DBTableData.DBTableDataSuppl=TDBTableDataSuppl()
                    self.DBTableData.DBTableDataSuppl.DBNameInDBCS=copy.deepcopy(val[2-1])
                    if len(val)>=23:
                        self.DBTableData.DBTableDataSuppl.DBTypeName=copy.deepcopy(val[3-1])
                        if len(val)>=4:
                            self.DBTableData.DBTableDataSuppl.DBTypeN=copy.deepcopy(int(val[4-1]))
                            if len(val)>=5:
                                self.DBTableData.DBTableDataSuppl.DBFileFullName=copy.deepcopy(str(val[5-1]))
    #
    def SetColNameToDisplay(self, val):
        pass
    def SetDBFieldName(self, val):
        pass
    def SetFieldTypeN(self, val):
        pass
    def SetFieldTypeName(self, val):
        pass
    def SetFieldLength(self, val):
        pass
    def SetDBFieldCharacteristicsNumber(self, val):
        pass
    def SetIfIsKeyField(self, val):
        pass
    def SetIfIsCounter(self, val):
        pass
    def SetIfIsNotNull(self, val):
        pass
    def SetIfIsAutoIncrement(self, val):   
        pass
    #
    def SetItemsTableName(self, val):
        pass
    def SetItemsTableItemsFieldName(self, val):
        pass
    def GetItemsTableKeyFieldName(self, val):
        pass
    #
    def GetColNameToDisplay(self):
        return self.data
    def GetDBFieldName(self):
        s=""
        return s
    def GetFieldTypeN(self):
        r=0
        return r
    def GetFieldTypeName(self):
        r=0
        return r
    def GetFieldLength(self):
        r=0
        return r
    def GetDBFieldCharacteristicsNumber(self):
        r=0
        return r
    def GetIfIsKeyField(self):
        r=0
        return r
    def GetIfIsCounter(self):
        r=0
        return r
    def GetIfIsNotNull(self):
        r=0
        return r
    def GetIfIsAutoIncrement(self):   
        r=0
        return r
    #
    def GetItemsTableName(self):
        return ""
    def GetItemsTableItemsFieldName(self):
        return ""
    def GetItemsTableKeyFieldName(self):
        return ""
    #
    def ToString(self, sBef="", sAft=""):
        s=""
        y=self.GetItem()
        if isinstance(y, str):
            s=y
            s=sBef+s
            s=s+sAft
        elif isinstance(y, float) or isinstance(y, int):
            s=str(self.data)
            s=sBef+s
            s=s+sAft
        return s


class DataCell_ColHeaderDBOrItems:
    def GetType(self):          #2
         return DataCell_Simple_TypeN
    #    return 1 #1- simple, 3-combobox, 2-DBFldHdr
    def __init__(self, val1="", val2=[], val3=[], val4=[]): #1
        self.data=val1#header
        self.DBFieldInfo=[]
        self.items=[]
        self.DBItemsTableData=[]
        self.data=val1
        if isinstance(val2, list):
            self.items=copy.deepcopy(val2)
        if isinstance(val3, TDBFieldInfo):
            self.DBFieldInfo=TDBFieldInfo()
            self.DBFieldInfo=copy.deepcopy(val3)
        elif isinstance(val3, list):
            if len(val3)>=1:
                self.DBFieldInfo=TDBFieldInfo()
                self.DBFieldInfo.DBFieldNameToDBTable=copy.deepcopy(str(val3[1-1]))
                if len(val3)>=9:
                    self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
                    self.DBFieldInfo.DBFieldInfoSuppl.FieldTypeN=int(val3[2-1])
                    self.DBFieldInfo.DBFieldInfoSuppl.FieldTypeName=str(val3[3-1])
                    elf.DBFieldInfo.DBFieldInfoSuppl.FieldLength=str(val3[4-1])
                    self.DBFieldInfo.DBFieldInfoSuppl.DBFieldCharacteristicsNumber=int(val3[5-1])
                    self.DBFieldInfo.DBFieldInfoSuppl.isKeyField=int(val3[6-1])
                    self.DBFieldInfo.DBFieldInfoSuppl.isCounter=int(val3[7-1])
                    self.DBFieldInfo.DBFieldInfoSuppl.isNotNull=int(val3[8-1])
                    self.DBFieldInfo.DBFieldInfoSuppl.isAutoIncrement=int(val3[9-1])
                    if len(val3>=12):
                        if self.DBItemsTableData==[]:
                            self.DBItemsTableData=TDBItemsTableData()
                        self.DBItemsTableData.ItemsTableName=str(val3[10-1])
                        self.DBItemsTableData.ItemsTableItemsFieldName=str(val3[11-1])
                        self.DBItemsTableData.ItemsTableKeyFieldName=str(val3[12-1])
        if isinstance(val4, TDBItemsTableData):
            self.DBItemsTableData=TDBItemsTableData()
            self.DBItemsTableData=copy.deepcopy(val4)
        elif isinstance(val4, list) and len(val4)>=3:
            self.DBItemsTableData=TDBItemsTableData()
            self.DBItemsTableData.ItemsTableName=str(val4[1-1])
            self.DBItemsTableData.ItemsTableItemsFieldName=str(val4[2-1])
            self.DBItemsTableData.ItemsTableKeyFieldName=str(val4[3-1])

    
    def GetVal(self, N=0): #3
        if N==0:
            if self.DBFieldInfo==[]:
                N=1
            else: #isinstance(self.DBFieldInfo, TDBFieldInfo)
                N=2
        if N==1:
            if isinstance(self.DBFieldInfo, TDBFieldInfo):
                val=copy.deepcopy(str(self.DBFieldInfo.DBFieldNameToDBTable))
            else:
                val=""
        if N==2:
            if isinstance(self.DBFieldInfo, TDBFieldInfo):
                if isinstance(self.DBFieldInfo.DBFieldInfoSuppl, TDBFieldInfoSuppl):
                    val=copy.deepcopy(str(self.DBFieldInfo.DBFieldInfoSuppl.FieldTypeN))
        if N==3:
            if isinstance(self.DBFieldInfo, TDBFieldInfo):
                if isinstance(self.DBFieldInfo.DBFieldInfoSuppl, TDBFieldInfoSuppl):
                    val=copy.deepcopy(str(self.DBFieldInfo.DBFieldInfoSuppl.FieldTypeName))
                else:
                    val=""
            else:
                val=""
        if N==4:
            if isinstance(self.DBFieldInfo, TDBFieldInfo):
                if isinstance(self.DBFieldInfo.DBFieldInfoSuppl, TDBFieldInfoSuppl):
                    val=copy.deepcopy(int(self.DBFieldInfo.DBFieldInfoSuppl.FieldLength))
                else:
                    val=""
            else:
                val=""

        if N==5:
            if isinstance(self.DBFieldInfo, TDBFieldInfo):
                if isinstance(self.DBFieldInfo.DBFieldInfoSuppl, TDBFieldInfoSuppl):
                    val=copy.deepcopy(int(self.DBFieldInfo.DBFieldInfoSuppl.DBFieldCharacteristicsNumber))
                else:
                    val=""
            else:
                val=""

        if N==6:
            if isinstance(self.DBFieldInfo, TDBFieldInfo):
                if isinstance(self.DBFieldInfo.DBFieldInfoSuppl, TDBFieldInfoSuppl):
                    val=copy.deepcopy(int(self.DBFieldInfo.DBFieldInfoSuppl.isKeyField))
                else:
                    val=0
            else:
                val=0

        if N==7:
            if isinstance(self.DBFieldInfo, TDBFieldInfo):
                if isinstance(self.DBFieldInfo.DBFieldInfoSuppl, TDBFieldInfoSuppl):
                    val=copy.deepcopy(int(self.DBFieldInfo.DBFieldInfoSuppl.isCounter))
                else:
                    val=0
            else:
                val=0

        if N==8:
            if isinstance(self.DBFieldInfo, TDBFieldInfo):
                if isinstance(self.DBFieldInfo.DBFieldInfoSuppl, TDBFieldInfoSuppl):
                    val=copy.deepcopy(int(self.DBFieldInfo.DBFieldInfoSuppl.isNotNull))
                else:
                    val=0
            else:
                val=0

        if N==9:
            if isinstance(self.DBFieldInfo, TDBFieldInfo):
                if isinstance(self.DBFieldInfo.DBFieldInfoSuppl, TDBFieldInfoSuppl):
                    val=copy.deepcopy(int(self.DBFieldInfo.DBFieldInfoSuppl.isAutoIncrement))
                else:
                    val=0
            else:
                val=0
        #
        if N==10:
            if isinstance(self.DBItemsTableData, TDBItemsTableData):
                val=copy.deepcopy(str(self.DBItemsTableData.ItemsTableName))
            else:
                val=""
        if N==11:
            if isinstance(self.DBItemsTableData, TDBItemsTableData):
                val=copy.deepcopy(str(self.DBItemsTableData.ItemsTableItemsFieldName))
            else:
                val=""
        if N==11:
            if isinstance(self.DBItemsTableData, TDBItemsTableData):
                val=copy.deepcopy(str(self.DBItemsTableData.ItemsTableKeyFieldName))
            else:
                val=""


    def GetItems(self):
        return self.items

    def GetItem(self, N=1): #4
        s=""
        if isinstance(self.items, list) and len(self.items)>0 and N>=1 and N<=len(self.items)>0:
            s=self.items[N-1]
        return s
     # ConcrType
    def GetFloatVal(self): #5
        return 0

    def GetIntVal(self): #6
        return 0

    def GetBoolVal(self): #7
        return bool(0)

    def GetStrVal(self): #8
        return self.GetVal()

    # for combobox
    def GetActiveN(self): #for combobox-1
        return 0

    def GetActiveItem(self): #for combobox-2
        return 0
    
    def SetActiveN(self, val): #for combobox-3
        pass
        #
    def SetActiveNByVal(self, val): #for combobox-4
        pass
        #
    def GetQItems(): #for combobox-5
        return 1

    def Set(self, val="", val2=[], val3=[], val4=[]): #1
        self.data=val#header
        self.DBFieldInfo=[]
        self.items=[]
        self.DBItemsTableData=[]
        self.data=va1l
        if isinstance(val2, list):
            self.items=copy.deepcopy(val2)
        if isinstance(val3, TDBFieldInfo):
            if self.DBFieldInfo==[]:
                self.DBFieldInfo=TDBFieldInfo()
            self.DBFieldInfo=copy.deepcopy(val3)
        elif isinstance(val3, list):
            if len(val3)>=1:
                if self.DBFieldInfo==[]:
                    self.DBFieldInfo=TDBFieldInfo()
                self.DBFieldInfo.DBFieldNameToDBTable=copy.deepcopy(str(val3[1-1]))
                if len(val3)>=9:
                    if self.DBFieldInfo.DBFieldInfoSuppl==[]:
                        self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
                    self.DBFieldInfo.DBFieldInfoSuppl.FieldTypeN=int(val3[2-1])
                    self.DBFieldInfo.DBFieldInfoSuppl.FieldTypeName=str(val3[3-1])
                    self.DBFieldInfo.DBFieldInfoSuppl.FieldLength=str(val3[4-1])
                    self.DBFieldInfo.DBFieldInfoSuppl.DBFieldCharacteristicsNumber=int(val3[5-1])
                    self.DBFieldInfo.DBFieldInfoSuppl.isKeyField=int(val3[6-1])
                    self.DBFieldInfo.DBFieldInfoSuppl.isCounter=int(val3[7-1])
                    self.DBFieldInfo.DBFieldInfoSuppl.isNotNull=int(val3[8-1])
                    self.DBFieldInfo.DBFieldInfoSuppl.isAutoIncrement=int(val3[9-1])
                    if len(val3>=12):
                        if self.DBItemsTableData==[]:
                            self.DBItemsTableData=TDBItemsTableData()
                        self.DBItemsTableData.ItemsTableName=str(val3[10-1])
                        self.DBItemsTableData.ItemsTableItemsFieldName=str(val3[11-1])
                        self.DBItemsTableData.ItemsTableKeyFieldName=str(val3[12-1])
        if isinstance(val4, TDBItemsTableData):
            if self.DBItemsTableData==[]:
                self.DBItemsTableData=TDBItemsTableData()
            self.DBItemsTableData=copy.deepcopy(val4)
        elif isinstance(val4, list) and len(val4)>=3:
            if self.DBItemsTableData==[]:
                self.DBItemsTableData=TDBItemsTableData()
            self.DBItemsTableData.ItemsTableName=str(val4[1-1])
            self.DBItemsTableData.ItemsTableItemsFieldName=str(val4[2-1])
            self.DBItemsTableData.ItemsTableKeyFieldName=str(val4[3-1])

    def SetVal(self, val, N=0): #1      
        if N==1:
            if self.DBFieldInfo==[]:
                self.DBFieldInfo=TDBFieldInfo()
            self.DBFieldInfo.DBFieldNameToDBTable=copy.deepcopy(str(val))
        if N==2:
            if self.DBFieldInfo==[]:
                self.DBFieldInfo=TDBFieldInfo()
            if self.DBFieldInfo.DBFieldInfoSuppl==[]:
                self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
            self.DBFieldInfo.FieldTypeN=copy.deepcopy(str(val))
        if N==3:
            if self.DBFieldInfo==[]:
                self.DBFieldInfo=TDBFieldInfo()
            if self.DBFieldInfo.DBFieldInfoSuppl==[]:
                self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
            self.DBFieldInfo.FieldTypeName=copy.deepcopy(str(val))
        if N==4:
            if self.DBFieldInfo==[]:
                self.DBFieldInfo=TDBFieldInfo()
            if self.DBFieldInfo.DBFieldInfoSuppl==[]:
                self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
            self.DBFieldInfo.FieldLength=copy.deepcopy(int(val))
        if N==5:
            if self.DBFieldInfo==[]:
                self.DBFieldInfo=TDBFieldInfo()
            if self.DBFieldInfo.DBFieldInfoSuppl==[]:
                self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
            self.DBFieldInfo.DBFieldCharacteristicsNumber=copy.deepcopy(int(val))
        if N==6:
            if self.DBFieldInfo==[]:
                self.DBFieldInfo=TDBFieldInfo()
            if self.DBFieldInfo.DBFieldInfoSuppl==[]:
                self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
            self.DBFieldInfo.isKeyField=copy.deepcopy(int(val))
        if N==7:
            if self.DBFieldInfo==[]:
                self.DBFieldInfo=TDBFieldInfo()
            if self.DBFieldInfo.DBFieldInfoSuppl==[]:
                self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
            self.DBFieldInfo.isCounter=copy.deepcopy(int(val))
        if N==8:
            if self.DBFieldInfo==[]:
                self.DBFieldInfo=TDBFieldInfo()
            if self.DBFieldInfo.DBFieldInfoSuppl==[]:
                self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
            self.DBFieldInfo.isNotNull=copy.deepcopy(int(val))
        if N==9:
            if self.DBFieldInfo==[]:
                self.DBFieldInfo=TDBFieldInfo()
            if self.DBFieldInfo.DBFieldInfoSuppl==[]:
                self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
            self.DBFieldInfo.isAutoIncrement=copy.deepcopy(int(val))
        #
        if N==10:
            if self.DBItemsTableData==[]:
                self.DBItemsTableData=TDBItemsTableData()
            self.DBItemsTableData.ItemsTableName=str(val)
        if N==11:
            if self.DBItemsTableData==[]:
                self.DBItemsTableData=TDBItemsTableData()
            self.DBItemsTableData.ItemsTableItemsFieldName=str(val)
        if N==12:
            if self.DBItemsTableData==[]:
                self.DBItemsTableData=TDBItemsTableData()
            self.DBItemsTableData.ItemsTableKeyFieldName=str(val)
        
                    
    #
    def GetTableNameToDisplay(self):
         return ""

    def GetTableNameInDB(self):
         return ""

    def GetDBNameInDBCS(self):
         return ""

    def GetDBTypeName(self):
         return ""

    def GetDBTypeN(self):
        return 0

    def GetDBFileFullName(self):
        return ""

    #
    def SetTableNameToDisplay(self, val):
        pass

    def SetTableNameInDB(self, val):
        pass
        
    def SetDBNameInDBCS(self, val):
        pass

    def SetDBTypeName(self, val):
        pass

    def SetDBTypeN(self, val):
        pass

    def SetDBFileFullName(self, val):
        pass
    #
    def SetColNameToDisplay(self, val):
        pass
        self.data=copy.deepcopy(str(val))
    def SetDBFieldName(self, val):
        if self.DBFieldInfo==[]:
            self.DBFieldInfo=TDBFieldInfo()
        self.DBFieldInfo.DBFieldNameToDBTable=copy.deepcopy(str(val))
    def SetFieldTypeN(self, val):
        if self.DBFieldInfo==[]:
            self.DBFieldInfo=TDBFieldInfo()
        if self.DBFieldInfo.DBFieldInfoSuppl==[]:
            self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
        self.DBFieldInfo.DBFieldInfoSuppl.FieldTypeN=copy.deepcopy(int(val))
    def SetFieldTypeName(self, val):
        if self.DBFieldInfo==[]:
            self.DBFieldInfo=TDBFieldInfo()
        if self.DBFieldInfo.DBFieldInfoSuppl==[]:
            self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
        self.DBFieldInfo.DBFieldInfoSuppl.FieldTypeName=copy.deepcopy(str(val))
    def SetFieldLength(self, val):
        if self.DBFieldInfo==[]:
            self.DBFieldInfo=TDBFieldInfo()
        if self.DBFieldInfo.DBFieldInfoSuppl==[]:
            self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
        self.DBFieldInfo.DBFieldInfoSuppl.FieldLength=copy.deepcopy(int(val))
    def SetDBFieldCharacteristicsNumber(self, val):
        if self.DBFieldInfo==[]:
            self.DBFieldInfo=TDBFieldInfo()
        if self.DBFieldInfo.DBFieldInfoSuppl==[]:
            self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
        self.DBFieldInfo.DBFieldInfoSuppl.DBFieldCharacteristicsNumber=copy.deepcopy(int(val))
    def SetIfIsKeyField(self, val):
        if self.DBFieldInfo==[]:
            self.DBFieldInfo=TDBFieldInfo()
        if self.DBFieldInfo.DBFieldInfoSuppl==[]:
            self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
        self.DBFieldInfo.DBFieldInfoSuppl.isKeyField=copy.deepcopy(int(val))
    def SetIfIsCounter(self, val):
        if self.DBFieldInfo==[]:
            self.DBFieldInfo=TDBFieldInfo()
        if self.DBFieldInfo.DBFieldInfoSuppl==[]:
            self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
        self.DBFieldInfo.DBFieldInfoSuppl.isCounter=copy.deepcopy(int(val))
    def SetIfIsNotNull(self, val):
        if self.DBFieldInfo==[]:
            self.DBFieldInfo=TDBFieldInfo()
        if self.DBFieldInfo.DBFieldInfoSuppl==[]:
            self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
        self.DBFieldInfo.DBFieldInfoSuppl.isNotNull=copy.deepcopy(int(val))
    def SetIfIsAutoIncrement(self, val):   
        if self.DBFieldInfo==[]:
            self.DBFieldInfo=TDBFieldInfo()
        if self.DBFieldInfo.DBFieldInfoSuppl==[]:
            self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
        self.DBFieldInfo.DBFieldInfoSuppl.isAutoIncrement=copy.deepcopy(int(val))
    #
    def SetItemsTableName(self, val):
        if self.DBItemsTableData==[]:
            self.DBItemsTableData=TDBItemsTableData()
        self.DBItemsTableData.ItemsTableName=copy.deepcopy(val)
    def SetItemsTableItemsFieldName(self, val):
        if self.DBItemsTableData==[]:
            self.DBItemsTableData=TDBItemsTableData()
        self.DBItemsTableData.ItemsTableItemsFieldName=val
    def SetItemsTableKeyFieldName(self, val):
        if self.DBItemsTableData==[]:
            self.DBItemsTableData=TDBItemsTableData()
        self.DBItemsTableData.ItemsTableKeyFieldName=val
    #
    def GetColNameToDisplay(self):
        return self.data
    def GetDBFieldName(self):
        s=""
        if self.DBFieldInfo!=[]:
            s=copy.deepcopy(self.DBFieldInfo.DBFieldNameToDBTable)
        return s
    def GetFieldTypeN(self):
        r=0
        if self.DBFieldInfo!=[] and self.DBFieldInfo.DBFieldInfoSuppl!=[]:
            r=self.DBFieldInfo.DBFieldInfoSuppl.FieldTypeN
        return r
    def GetFieldTypeName(self):
        r=""
        if self.DBFieldInfo!=[] and self.DBFieldInfo.DBFieldInfoSuppl!=[]:
            r=self.DBFieldInfo.DBFieldInfoSuppl.FieldTypeName
        return r
    def GetFieldLength(self):
        r=0
        if self.DBFieldInfo!=[] and self.DBFieldInfo.DBFieldInfoSuppl!=[]:
            r=self.DBFieldInfo.DBFieldInfoSuppl.FieldLength
        return r
    def GetDBFieldCharacteristicsNumber(self):
        r=0
        if self.DBFieldInfo!=[] and self.DBFieldInfo.DBFieldInfoSuppl!=[]:
            r=self.DBFieldInfo.DBFieldInfoSuppl.DBFieldCharacteristicsNumber
        return r
    def GetIfIsKeyField(self):
        r=0
        if self.DBFieldInfo!=[] and self.DBFieldInfo.DBFieldInfoSuppl!=[]:
            r=self.DBFieldInfo.DBFieldInfoSuppl.isKeyField
        return r
    def GetIfIsCounter(self):
        r=0
        if self.DBFieldInfo!=[] and self.DBFieldInfo.DBFieldInfoSuppl!=[]:
            r=self.DBFieldInfo.DBFieldInfoSuppl.isCounter
        return r
    def GetIfIsNotNull(self):
        r=0
        if self.DBFieldInfo!=[] and self.DBFieldInfo.DBFieldInfoSuppl!=[]:
            r=self.DBFieldInfo.DBFieldInfoSuppl.isNotNull
        return r
    def GetIfIsAutoIncrement(self):   
        r=0
        if self.DBFieldInfo!=[] and self.DBFieldInfo.DBFieldInfoSuppl!=[]:
            r=self.DBFieldInfo.DBFieldInfoSuppl.isAutoIncrement
        return r
    #
    def GetItemsTableName(self):
        s=""
        if isinstance(self.DBItemsTableData, TDBItemsTableData):
            s=self.DBItemsTableData.ItemsTableName
        return s
    def GetItemsTableItemsFieldName(self):
        s=""
        if isinstance(self.DBItemsTableData, TDBItemsTableData):
            s=self.DBItemsTableData.ItemsTableItemsFieldName
        return s
    def GetItemsTableKeyFieldName(self):
        s=""
        if isinstance(self.DBItemsTableData, TDBItemsTableData):
            s=self.DBItemsTableData.ItemsTableKeyFieldName
        return s
    #
    def ToString(self, sBef="", sAft=""):
        s=""
        if isinstance(self.data, str):
            s=self.data
            s=sBef+s
            s=s+sAft
        elif isinstance(self.data, float) or isinstance(self.data, int):
            s=str(self.data)
            s=sBef+s
            s=s+sAft
        return s

        
class DataCell:
    def GetType(self):          #2
         return self.cell.GetTypeN()
    #    return 1 #1- simple, 3-combobox, 2-DBFldHdr
    def __init__(self, val1="", val2=[], val3=[], val4=[], vsh=0): #1
        if isinstance(val1, DataCell):
            self.cell=copy.deepcopy(val1.cell)
        elif isinstance(val1, DataCell_Simple):
            self.cell=copy.deepcopy(val1)
        elif isinstance(val1, DataCell_ComboboxOrMemo):
            self.cell=copy.deepcopy(val1)
        elif not isinstance(val1, list) and val2==[] and val3==[] and val4==[]:
            self.cell=DataCell_Simple(val1)
        elif isinstance(val1, list) and isinstance(val2, int):
            self.cell=DataCell_ComboboxOrMemo(val1, val2, vsh)
        elif isinstance(val1, list):
            self.cell=DataCell_ComboboxOrMemo(val1, vsh)
            self.cell.SetActiveN(val2, vsh)
        elif isinstance(val1, str) and isinstance(val2, TDBTableData):
            self.cell=DataCell_DBTableHeader(val1, val2)
        elif isinstance(val1, str) and isinstance(val2, str) and isinstance(val3, TDBTableDataSuppl):
            self.cell=DataCell_DBTableHeader(val1, val2, val3)
        elif isinstance(val3, TDBFieldInfo):
            self.cell=DataCell_ColHeaderDBOrItems(val1, val2, val3, val4)
        elif isinstance(val2, TDBFieldInfo):
            self.cell=DataCell_ColHeaderDBOrItems(val1, val3, val2, val4)
        elif isinstance(val1, str) and isinstance(val2, list):
            self.cell=DataCell_ColHeaderDBOrItems(val1, val2, val3, val4)

        
    def SetCell_Simple(self, val1):
        self.cell=DataCell_Simple(val1)

    def SetCell_ComboboxOrMemo(self, val1=[], val2=1):
        self.cell=DataCell_ComboboxOrMemo(val1, val2)

    def SetCell_DBTableHeader(self, val1="", val2=[] , val3=[]):
        self.cell=DataCell_DBTableHeader(val1, val2, val3)

    def DataCell_ColHeaderDBOrItems(self, val1="", val2=[] , val3=[], val4=[]):
        self.cell=DataCell_DBTableHeader(val1, val2, val3, val4)
        if isinstance(val3, TDBFieldInfo):
            self.cell=DataCell_ColHeaderDBOrItems(val1, val2, val3, val4)
        elif isinstance(val2, TDBFieldInfo):
            self.cell=DataCell_ColHeaderDBOrItems(val1, val3, val2, val4)
        elif isinstance(val1, str) and isinstance(val2, list):
            self.cell=DataCell_ColHeaderDBOrItems(val1, val2, val3, val4)

        
    def GetVal(self, N=1): #3
        return self.cell.GetVal(N)

    def GetItems(self):
        return self.cell.GetItems()

    def GetItem(self, N=0): #4
        return self.cell.GetItem(N)
        
     # ConcrType
    def GetFloatVal(self): #5
        return self.cell.GetFloatVal()

    def GetIntVal(self): #6
        return self.cell.GetIntVal()

    def GetBoolVal(self): #7
        return self.cell.GetBoolVal()

    def GetStrVal(self): #8
        return self.cell.GetStrVal()

    # for combobox
    def GetActiveN(self): #for combobox-1
        return self.cell.GetActiveN()

    def GetActiveItem(self): #for combobox-2
        return self.cell.GetActiveItem()
    
    def SetActiveN(self, val): #for combobox-3
        self.cell.SetActiveN(val)
    #
    def SetActiveNByVal(self, val): #for combobox-4
        self.cell.SetActiveNByVal(val)
        #
    def GetQItems(self): #for combobox-5
        return self.cell.GetQItems()

    def Set(self, val1, val2=[], val3=[], val4=[]): #1
        if isinstance(val1, DataCell):
            self.cell=copy.deepcopy(val1.cell)
        elif isinstance(val1, DataCell_Simple):
            self.cell=copy.deepcopy(val1)
        elif isinstance(val1, DataCell_ComboboxOrMemo):
            self.cell=copy.deepcopy(val1)
        elif not isinstance(val1, list) and val2==[] and val3==[] and val4==[]:
            self.cell=DataCell_Simple(val1)
        elif isinstance(val1, list):
            self.cell=DataCell_ComboboxOrMemo(val1)
            self.cell.SetActiveN(val2)

    def SetVal(self, val, N=0): #1
        self.cell.SetVal(val, N)
        
    def GetTableNameToDisplay(self):
        return self.cell.GetTableNameToDisplay()

    def GetTableNameInDB(self):
        return self.cell.GetTableNameInDB()

    def GetDBNameInDBCS(self):
        return self.cell.GetDBNameInDBCS()

    def GetDBTypeName(self):
        return self.cell.GetDBTypeName()
    
    def GetDBTypeN(self):
        return self.cell.GetDBTypeN()

    def GetDBFileFullName(self):
        return self.cell.GetDBFileFullName()

    #
    def SetTableNameToDisplay(self, val):
        self.cell.SetTableNameToDisplay(val)

    def SetTableNameInDB(self, val):
        self.cell.SetTableNameInDB(val)
        
    def SetDBNameInDBCS(self, val):
        self.cell.SetDBNameInDBCS(val)

    def SetDBTypeName(self, val):
        self.cell.SetDBTypeName(val)

    def SetDBTypeN(self, val):
        self.cell.SetDBTypeN(val)

    def SetDBFileFullName(self, val):
        self.cell.SetDBFileFullName(val)

    #
    def SetColNameToDisplay(self, val):
        self.cell.SetColNameToDisplay(val)
    def SetDBFieldName(self, val):
        self.cell.SetDBFieldName(val)
    def SetFieldTypeN(self, val):
        self.cell.SetFieldTypeN(val)
    def SetFieldTypeName(self, val):
        self.cell.SetFieldTypeName(val)
    def SetFieldLength(self, val):
        self.cell.SetFieldLength(val)
    def SetDBFieldCharacteristicsNumber(self, val):
        self.cell.SetDBFieldCharacteristicsNumber(val)
    def SetIfIsKeyField(self, val):
        self.cell.SetIfIsKeyField(val)
    def SetIfIsCounter(self, val):
        self.cell.SetIfIsCounter(val)
    def SetIfIsNotNull(self, val):
        self.cell.SetIfIsNotNull(val)
    def SetIfIsAutoIncrement(self, val):   
        self.cell.SetIfIsAutoIncrement(val)
    #
    def SetItemsTableName(self, val):
        self.cell.SetItemsTableName(val)
    def SetItemsTableItemsFieldName(self, val):
        self.cell.SetItemsTableItemsFieldName(val)
    def SetItemsTableKeyFieldName(self, val):
        self.cell.SetItemsTableKeyFieldName(val)
    #
    def GetColNameToDisplay(self):
        return self.cell.GetColNameToDisplay()
    def GetDBFieldName(self):
        return self.cell.GetDBFieldName()
    def GetFieldTypeN(self):
        return self.cell.GetFieldTypeN()
    def GetFieldTypeName(self):
        return self.cell.GetFieldTypeName()
    def GetFieldLength(self):
        return self.cell.GetFieldLength()
    def GetDBFieldCharacteristicsNumber(self):
        return self.cell.GetDBFieldCharacteristicsNumber()
    def GetIfIsKeyField(self):
        return self.cell.GetIfIsKeyField()
    def GetIfIsCounter(self):
        return self.cell.GetIfIsCounter()
    def GetIfIsNotNull(self):
        return self.cell.GetIfIsNotNull()
    def GetIfIsAutoIncrement(self):   
        return self.cell.GetIfIsAutoIncrement()
    #
    def GetItemsTableName(self):
        return self.cell.GetItemsTableName()
    def GetItemsTableItemsFieldName(self):
        return self.cell.GetItemsTableItemsFieldName()
    def GetItemsTableKeyFieldName(self):
        return self.cell.GetItemsTableKeyFieldName()
    #
    
    def ToString(self, sBef="", sAft=""):
        return self.cell.ToString(sBef, sAft)

class DataCellRow:
    def __init__(self, row=[]):
        self.row=[]
        if isinstance(row, list):
            Q=len(row)
            for i in range (1, Q+1):
                val=copy.deepcopy(row[i-1])
                cell=DataCell(val)
                self.row.append(cell)
        else:
            val=copy.deepcopy(row)
            cell=DataCell(val)
            self.row.append(cell)

    def GetType(self, cellN):          #2
        r=0
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetType()
        return r

    def SetCell_Simple(self, cellN, val1):
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].SetCell_Simple(val1)

    def SetCell_ComboboxOrMemo(self, cellN, val1=[], val2=1):
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].SetCell_ComboboxOrMemo(val1, val2)

    def SetCell_DBTableHeader(self, cellN, val1="", val2=[] , val3=[]):
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].SetCell_DBTableHeader(self, val1, val2 , val3)

    def DataCell_ColHeaderDBOrItems(self, cellN, val1="", val2=[] , val3=[], val4=[]):
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].SetCell_DBTableHeader(self, val1, val2 , val3, val4)

        
    def GetVal(self, cellN, N=1): #3
        r=0
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetVal(N)
        return r

    def GetItems(self, cellN):
        r=0
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=row[cellN-1].GetItems()
        return r

    def GetItem(self, cellN, N=0): #4
        r=0
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetItem(N)
        return r
        
     # ConcrType
    def GetFloatVal(self, cellN): #5
        r=0
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetFloatVal()
        return r

    def GetIntVal(self, cellN): #6
        r=0
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=row[cellN-1].GetIntVal()
        return r

    def GetBoolVal(self, cellN): #7
        r=0
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetBoolVal()
        return r

    def GetStrVal(self, cellN): #8
        r=0
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetStrVal()
        return r

    # for combobox
    def GetActiveN(self, cellN): #for combobox-1
        r=0
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetActiveN()
        return r

    def GetActiveItem(self, cellN): #for combobox-2
        r=0
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetActiveItem()
        return r
    
    def SetActiveN(self, cellN, val): #for combobox-3
        r=0
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            self.row[cellN-1].SetActiveN(val)
        return r
    #
    def SetActiveNByVal(self, N, val): #for combobox-4
        r=0
        Q=len(self.row)
        if N>=1  and N <= Q:
            r=self.row[N-1].SetActiveNByVal(val)
        return r
        #
    def GetQItems(self, cellN): #for combobox-5
        r=0
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetQItems()
        return r

    def Set(self, cellN, val1, val2=[], val3=[], val4=[]): #1
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            self.row[cellN-1].Set(val1, val2, val3, val4)

    def SetVal(self, cellN, val, N=0): #1
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            self.row[cellN-1].SetVal(val, N)
        
    def GetTableNameToDisplay(self, cellN):
        r=""
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetTableNameToDisplay()
        return r

    def GetTableNameInDB(self, cellN):
        r=""
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetTableNameInDB()
        return r

    def GetDBNameInDBCS(self, cellN):
        r=""
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetDBNameInDBCS()
        return r

    def GetDBTypeName(self, cellN):
        r=""
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetDBTypeName()
        return r
    
    def GetDBTypeN(self, cellN):
        r=""
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetDBTypeN()
        return r

    def GetDBFileFullName(self, cellN):
        r=""
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetDBFileFullName()
        return r

    #
    def SetTableNameToDisplay(self, cellN, val):
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            self.row[cellN-1].SetTableNameToDisplay(val)

    def SetTableNameInDB(self, cellN, val):
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            self.row[cellN-1].SetTableNameInDB(val)
        
    def SetDBNameInDBCS(self, cellN, val):
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            self.row[cellN-1].SetDBNameInDBCS(val)

    def SetDBTypeName(self, cellN, val):
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            self.row[cellN-1].SetDBTypeName(val)

    def SetDBTypeN(self, cellN, val):
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            self.row[cellN-1].SetDBTypeN(val)

    def SetDBFileFullName(self, cellN, val):
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            self.row[cellN-1].SetDBFileFullName(val)

    #
    def SetColNameToDisplay(self, cellN, val):
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            self.row[cellN-1].SetColNameToDisplay(val)
    def SetDBFieldName(self, cellN, val):
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            self.row[cellN-1].SetDBFieldName(val)
    def SetFieldTypeN(self, cellN, val):
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            self.row[cellN-1].SetFieldTypeN(val)
    def SetFieldTypeName(self, cellN, val):
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            self.row[cellN-1].SetFieldTypeName(val)
    def SetFieldLength(self, cellN, val):
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            self.row[cellN-1].SetFieldLength(val)
    def SetDBFieldCharacteristicsNumber(self, cellN, val):
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            self.row[cellN-1].SetDBFieldCharacteristicsNumber(val)
    def SetIfIsKeyField(self, cellN, val):
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            self.row[cellN-1].SetIfIsKeyField(val)
    def SetIfIsCounter(self, cellN, val):
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            self.row[cellN-1].SetIfIsCounter(val)
    def SetIfIsNotNull(self, cellN, val):
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            self.row[cellN-1].SetIfIsNotNull(val)
    def SetIfIsAutoIncrement(self, cellN, val):   
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            self.row[cellN-1].SetIfIsAutoIncrement(val)
    #
    def SetItemsTableName(self, cellN, val):
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            self.row[cellN-1].SetItemsTableName(val)
    def SetItemsTableItemsFieldName(self, cellN, val):
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            self.row[cellN-1].SetItemsTableItemsFieldName(val)
    def SetItemsTableKeyFieldName(self, cellN, val):
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            self.row[cellN-1].SetItemsTableKeyFieldName(val)
    #
    def GetColNameToDisplay(self, cellN):
        r=""
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetColNameToDisplay()
        return r
    def GetDBFieldName(self, cellN):
        r=""
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetDBFieldName()
        return r
    def GetFieldTypeN(self, cellN):
        r=0
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetFieldTypeN()
        return r
    def GetFieldTypeName(self, cellN):
        r=""
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetFieldTypeName()
        return r
    def GetFieldLength(self, cellN):
        r=0
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetFieldLength()
        return r
    def GetDBFieldCharacteristicsNumber(self):
        r=0
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetDBFieldCharacteristicsNumber()
        return r
    def GetIfIsKeyField(self, cellN):
        r=0
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetIfIsKeyField()
        return r
    def GetIfIsCounter(self, cellN):
        r=0
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetIfIsCounter()
        return r
    def GetIfIsNotNull(self, cellN):
        r=0
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetIfIsNotNull()
        return r
    def GetIfIsAutoIncrement(self, cellN):   
        r=0
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetIfIsAutoIncrement()
        return r
    #
    def GetItemsTableName(self, cellN):
        r=""
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetItemsTableName()
        return r
    def GetItemsTableItemsFieldName(self, cellN):
        r=""
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetItemsTableItemsFieldName()
        return r
    def GetItemsTableKeyFieldName(self, cellN):
        r=""
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=self.row[cellN-1].GetItemsTableKeyFieldName()
        return r
    #
    def Set(self, row):
        self.row=[]
        if isinstance(row, DataCellRow):
            self.row=copy.deepcopy(row)
        elif isinstance(row, list):
            Q=len(row)
            for i in range(1, Q+1):
                val=copy.deepcopy(row[i-1])
                cell=DataCell(val)
                self.row.append(cell)
        else:
            val=copy.deepcopy(row)
            cell=DataCell(val)
            self.row.append(cell)
    #            
    def Add(self, val):
        x=copy.deepcopy(val)
        cell=DataCell(x)
        ArrayAdd(self.row, x)
    def Ins(self, cellN, val):
        x=copy.deepcopy(val)
        cell=DataCell(x)
        ArrayIns5(self.row, cellN, cell)
    def Del(self, cellN):
        Del1DArrayElement(self.row, cellN)
    def GetCell_AsLink(self, cellN):
        cell=[]
        Q=len(self.row)
        if cellN>=1 and cellN<=Q :
            cell=self.row[cellN-1]
        return cell
    def GetCell_AsCopy(self, cellN):
        cell=[]
        Q=len(self.row)
        if cellN>=1 and cellN<=Q :
            cell=copy.deepcopy(self.row[cellN-1])
        return cell
    def GetCell(self, cellN, AsLink0Copy1=1):
        cell=[]
        if AsLink0Copy1==0:
            cell=self.GetCell_AsLink(cellN)
        else:
            cell=self.GetCell_AsCopy(cellN)
        return cell
    def SetCell(self, cellN, val):
        Q=len(self.row)
        if cellN>=1 and cellN<=Q :
            self.row[cellN-1].Set(val)
    def SetCell(self, cellN, val1="", val2=[], val3=[], val4=[]):
        Q=len(self.row)
        if cellN>=1 and cellN<=Q :
            self.row[cellN-1].Set(val1, val2, val3, val4)
    def Swap(self, cell1N, cell2N):
        Swap1DArrayElements(self.row, cell1N, cell2N)
    def GetSize():
        return len(self.row)
    #
    def ToStringN(self, cellN, sBef="", sAft=""):
        r=""
        Q=len(self.row)
        if cellN>=1  and cellN <= Q:
            r=r+sBef
            r=self.row[cellN-1].ToString()
            r=r+sAft
        return r
       
    def ToString(self, delim="; ", sBef="", sAft=""):
        r=""
        Q=len(self.row)
        for i in range(1, Q-1+1):
            r=r+self.ToStringN(i, sBef, sAft)
            r=r+delim
        if Q>0:
            r=r+self.ToStringN(Q, sBef, sAft)
        return r
            

