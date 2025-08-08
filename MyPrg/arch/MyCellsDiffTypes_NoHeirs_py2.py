# -*- coding: cp1251 -*-
import math
import copy
#
import PyStdVector#.py
import DBDataClasses 
#
DataCell_Simple_TypeN=1
DataCell_ComboBoxOrMemo_TypeN=2
DataCell_DBTableHeader_TypeN=3
DataCell_ColHeader_DBFieldOrItems_TypeN=4
#

# Functions of DataCell:
#
# Nrs bo letters 11 excluding 9-10
# #for combobox-1-5
# #for database-0-3
# #ColDBHeaderItems-1-23 except 3
# #DBTableHdr-1-16
# #to represent-1-2
#
#
#Functions of My1DArray:
#


#  field\cell   |     item          |      suppl
#------------------------------------------------------
#Simple         |  value:  not []   |        -
#ComboboxOrMemo |  items:       []  |  activeN: not []      
#DBFldHdr       |  items:       []  |     names: []

#  field\cell   |   data            |   names
#--------------------------------------------------
#Simple         |  value:   not []  |     -
#ComboboxOrMemo |  activeN: not []  |  items: []       
#DBFldHdr       |  items:       []  |  names: []

#  field\cell    |   data            |   items     | DBFldInf
#-------------------------------------------------------------
# Simple         |  value:   not []  |     -       |    -
# ComboboxOrMemo |  activeN: not []  |  items: []  |    -    
# DBFldHdr       |  names:       []  |  items: []  |  int []
#
#  field\cell    |   GetVal()         
#------------------------------------
# Simple         |  return data
# ComboboxOrMemo |  GetItem(N)     
# DBFldHdr       |  GetName(N)
#                |              

 

class DataCell_Simple:
    def GetType(self):          #2
         return 1
    #    return 1 #1- simple, 3-combobox, 2-DBFldHdr
    def __init__(self, val=""): #1
        self.data=val
    def GetVal(self, N=1): #3
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

    def GetQNames(): # for database-0
        return 1

    # for database
    def GetName(self, N=1): # for database-1
        return self.GetVal(N)

    def SetName(self, names, N=0): # for database-2
        self.data = names
        
    def SetItem(self, items, N=0): # for database-3
        self.SetName(items,N)

    #
    def Set(self, var1=[], var2=[], var3=[], var4=[]): #11
        self.data = var1
    #
    #
    #SetName - above
    #
    # functions of DB FieldHeaderOrItems
    #
    def GetDBFieldInfo(self): #ColDBHeaderItems-1
        return 0
           
    def GetDBItemsTblInfo(self): #ColDBHeaderItems-2
        return 0
    #
    def SetDBFieldInfo(self, DBFldInfo): #ColDBHeaderItems-4
        pass
    
    def SetDBItemsTblInfo(self, DBItemsTblInfo): #ColDBHeaderItems-5
        pass 
                
    # def SetItems - united in SetItem below
    #
    #
    def GetColNameToDisplay(self): #ColDBHeaderItems-6
        return ""
           
    def GetDBFieldNameToDisplay(self): #ColDBHeaderItems-7
        return ""

    def GetFieldTypeN(self): #ColDBHeaderItems-8
        return 0

    def GetFieldTypeName(self): #ColDBHeaderItems-9
        return ""

    def GetFieldLength(self): #ColDBHeaderItems-10
        return 0

    def GetDBFieldCharacteristicsNumber(self): #ColDBHeaderItems-11
        return 0

    def GetIfIsKeyField(self): #ColDBHeaderItems-12
        return 0

    def GetIfIsNotNull(self): #ColDBHeaderItems-13
        return 0

    def GetIfIsCounter(self): #ColDBHeaderItems-13
        return 0

    def GetIfIsAutoIncrement(self): #ColDBHeaderItems-14
        return 0
    #
    def SetColNameToDisplay(self, name): #ColDBHeaderItems-15
        pass

    def SetDBFieldName(self, name): #ColDBHeaderItems-16
        pass

    def SetFieldTypeN(self, n): #ColDBHeaderItems-17
        pass

    def SetFieldTypeName(self, name): #ColDBHeaderItems-18
        pass

    def SetFieldLength(self, n): #ColDBHeaderItems-19
        pass

    def SetDBFieldCharacteristicsNumber(self, CharacteristicsNumber): #ColDBHeaderItems-20
        pass

    def SetIfIsKeyField(self, isKeyField):  #ColDBHeaderItems-21
        pass

    def SetIfIsNotNull(self, isNotNull):  #ColDBHeaderItems-22
        pass

    def SetIfIsCounter(self, isCounter):  #ColDBHeaderItems-22
        pass

    def SetIfIsAutoIncrement(self, isAutoIncrement):  #ColDBHeaderItems-23
        pass
    #
    #functions of DBTableHeader 
    #
    def GetDBTableDataSuppl(self): #DBTableHdr-1
        return []

    def GetDBTableData(self): #DBTableHdr-2
        return []

    def GetDBTableNameToDisplay(self): #DBTableHdr-3
        return ""

    def GetDBTableNameInDB(self): #DBTableHdr-4
        return ""

    def GetDBNameInDBCS(self): #DBTableHdr-5
        return ""

    def GetDBTypeName(self): #DBTableHdr-6
        return ""

    def GetDBTypeN(self): #DBTableHdr-7
        return 0

    def GetDBFileFullName(self): #DBTableHdr-8
        return ""
    #
    def SetDBTableDataSuppl(self, DBTableDataSuppl):  #DBTableHdr-9
        pass

    def SetDBTableData(self, DBTableData): #DBTableHdr-10
        pass

    def SetDBTableNameToDisplay(self, TableNameToDisplay): #DBTableHdr-11
        pass

    def SetDBTableNameInDB(self, DBTableNameInDB): #DBTableHdr-12
        pass

    def SetDBNameInDBCS(self, DBNameInDBCS): #DBTableHdr-13
        pass

    def SetDBTypeName(self, DBTypeName): #DBTableHdr-14
        pass

    def SetDBTypeN(self, DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5): #DBTableHdr-15
        pass
    
    def SetDBFileFullName(self, DBFileFullName): #DBTableHdr-16
        pass
    #    
    #   
    def ToString(self, str_bef="", str_aft=""):  # represent-1
        #return "cell id="+str(id(self))+" content: "+str(self.GetName())+" "
        return str_bef+str(self.GetName())+str_aft

    def __str__(): #represent-2
        return str(self.GetName())

   


class DataCell_ComboboxOrMemo:
    def GetType(self): #2
         return DataCell_ComboboxOrMemoTypeN
    #    return 1 #1- simple, 3-combobox, , 2-DBFldHdr
    def __init__(self, data=1, items=[]):
        self.data=data#1
        self.items=items#[]
    #def __init__(self):
    #    DataCell_Simple.__init__(self)#self.data=""
    #    self.items=[]
    def GetVal(self, N=0): #3
        #return self.data
        if N<=0 or N>self.data:
            N=self.data
        #return self.GetItem( self.data)#self.items[self.data-1]
        return self.GetItem(N)

    def GetItem(self, N=0): #4
        R = 0
        if isinstance(self.items, list):
            #Q = MyLibPy2.ArrayLength(self.items)
            Q = len(self.items)
            if N >= 1 and N <= Q:
                R = self.items[N - 1]
            else:
                R = self.items[self.data-1]
        else:
            R = self.items[self.data-1]
        return R

    # ConcrType
    def GetFloatVal(self): #5
        return float(GetVal(self))

    def GetIntVal(self): #6
        return int(GetVal(self))

    def GetBoolVal(self): #7
        return bool(GetVal(self))#here must be own function!

    def GetStrVal(self): #8
        return str(self.GetVal())
   
    # for combobox
    def GetActiveN(self): #for combobox-1
        return self.data

    def GetActiveItem(self): #for combobox-2
        return self.items[self.data-1]

    def SetActiveN(self, val): #for combobox-3
        N=int(val)
        #Q=MyLibPy2.ArrayLength(self.items)
        Q=len(self.items)
        if N>=1 and N<=Q:
            self.data=N

    def SetActiveNByVal(self, val): #for combobox-4
        N=0
        for item in items:
            N+=1
            if val==items:
                self.data=N

    def GetQItems(): #for combobox-5
        R = 0
        if not isinstance(self.items, list):
            R = 1
        else:
            R = MyLib.ArrayLength(self.items)
        return R

    def GetQNames():  # for database-0
        return self.GetQItems()

    def GetName(self, N=0):  # for database-1
        return self.GetItem(N)

    # for database
    def SetName(self, names, N=0): # for database-2
        self.SetItem(names, N)
           
    def SetItem(self, items, N=0):  # for database-3
        Q=MyLibPy2.ArrayLength(self.items)
        if isinstance(items, list):
           self.items = items
        else:
           if N>=1 and N<=Q:
               self.items[N-1]=items

    def Set(self, var1=[], var2=[], var3=[], var4=[]): #11
        #DataCell_Simple.Set(var1, var2, var3)
        self.data=var1
        self.items = var2
    #
    # functions of DB FieldHeaderOrItems
    #
    def GetDBFieldInfo(self): #ColDBHeaderItems-1
        return 0
           
    def GetDBItemsTblInfo(self): #ColDBHeaderItems-2
        return 0
    #
    def SetDBFieldInfo(self, DBFldInfo): #ColDBHeaderItems-4
        pass
    
    def SetDBItemsTblInfo(self, DBItemsTblInfo): #ColDBHeaderItems-5
        pass 
                
    # def SetItems - united in SetItem below
    #
    #
    def GetColNameToDisplay(self): #ColDBHeaderItems-6
        return ""
           
    def GetDBFieldNameToDisplay(self): #ColDBHeaderItems-7
        return ""

    def GetFieldTypeN(self): #ColDBHeaderItems-8
        return 0

    def GetFieldTypeName(self): #ColDBHeaderItems-9
        return ""

    def GetFieldLength(self): #ColDBHeaderItems-10
        return 0

    def GetDBFieldCharacteristicsNumber(self): #ColDBHeaderItems-11
        return 0

    def GetIfIsKeyField(self): #ColDBHeaderItems-12
        return 0

    def GetIfIsNotNull(self): #ColDBHeaderItems-13
        return 0

    def GetIfIsCounter(self): #ColDBHeaderItems-13
        return 0

    def GetIfIsAutoIncrement(self): #ColDBHeaderItems-14
        return 0
    #
    def SetColNameToDisplay(self, name): #ColDBHeaderItems-15
        pass

    def SetDBFieldName(self, name): #ColDBHeaderItems-16
        pass

    def SetFieldTypeN(self, n): #ColDBHeaderItems-17
        pass

    def SetFieldTypeName(self, name): #ColDBHeaderItems-18
        pass

    def SetFieldLength(self, n): #ColDBHeaderItems-19
        pass

    def SetDBFieldCharacteristicsNumber(self, CharacteristicsNumber): #ColDBHeaderItems-20
        pass

    def SetIfIsKeyField(self, isKeyField):  #ColDBHeaderItems-21
        pass

    def SetIfIsNotNull(self, isNotNull):  #ColDBHeaderItems-22
        pass

    def SetIfIsCounter(self, isCounter):  #ColDBHeaderItems-22
        pass

    def SetIfIsAutoIncrement(self, isAutoIncrement):  #ColDBHeaderItems-23
        pass
    #
    # functions of DBTableHeader
    #
    def GetDBTableDataSuppl(self): #DBTableHdr-1
        return []

    def GetDBTableData(self): #DBTableHdr-2
        return []

    def GetDBTableNameToDisplay(self): #DBTableHdr-3
        return ""

    def GetDBTableNameInDB(self): #DBTableHdr-4
        return ""

    def GetDBNameInDBCS(self): #DBTableHdr-5
        return ""

    def GetDBTypeName(self): #DBTableHdr-6
        return ""

    def GetDBTypeN(self): #DBTableHdr-7
        return 0
    
    def GetDBFileFullName(self): #DBTableHdr-8
        return ""
    #
    def SetDBTableDataSuppl(self, DBTableDataSuppl):  #DBTableHdr-9
        pass

    def SetDBTableData(self, DBTableData): #DBTableHdr-10
        pass

    def SetDBTableNameToDisplay(self, TableNameToDisplay): #DBTableHdr-11
        pass

    def SetDBTableNameInDB(self, DBTableNameInDB): #DBTableHdr-12
        pass

    def SetDBNameInDBCS(self, DBNameInDBCS): #DBTableHdr-13
        pass

    def SetDBTypeName(self, DBTypeName): #DBTableHdr-14
        pass

    def SetDBTypeN(self, DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5): #DBTableHdr-15
        pass
    
    def SetDBFileFullName(self, DBFileFullName): #DBTableHdr-16
        pass
    #
    #
    def ToString(self):  # new 2021-08-12 # to represent-1
        #return "cell id="+str(id(self))+" content: "+str(self.GetName())+" "
        return str(self.GetName())

    def __str__(self): # to represent-2
        return ToString()
    #
    #

class DataCell_DBTableHeader:
    def GetType(self): #2
        return DataCell_DBTableHeader_TypeN
    #    return 1 #1- simple, 3-combobox, , 2-DBFldHdr
    #def __init__(self):
    #    self.DBFldInfo=[]
    def __init__(self, data="", DBTableData=[]): #1
        self.data=""
        self.DBTableData=[]
        #
        self.Set(data, DBTableData)                  

    def GetVal(self, N=0): #3
        #return self.data
        if N<=0 or N>self.data:
            N=self.data
        #return self.GetItem( self.data)#self.items[self.data-1]
        return self.GetItem(N)

    def GetItem(self, N=0): #4
        R = 0
        if isinstance(self.items, list):
            #Q = MyLibPy2.ArrayLength(self.items)
            Q = len(self.items)
            if N >= 1 and N <= Q:
                R = self.items[N - 1]
            else:
                R = self.items[self.data-1]
        else:
            R = self.items[self.data-1]
        return R

    # ConcrType
    def GetFloatVal(self): #5
        return float(GetVal(self))

    def GetIntVal(self): #6
        return int(GetVal(self))

    def GetBoolVal(self): #7
        return bool(GetVal(self))#here must be own function!

    def GetStrVal(self): #8
        return str(self.GetVal())
   
    # for combobox
    def GetActiveN(self): #for combobox-1
        return self.data

    def GetActiveItem(self): #for combobox-2
        return self.items[self.data-1]

    def SetActiveN(self, val): #for combobox-3
        N=int(val)
        Q=MyLibPy2.ArrayLength(self.items)
        if N>=1 and N<=self.Q:
            self.data=N

    def SetActiveNByVal(self, val): #for combobox-4
        N=0
        for item in items:
            N+=1
            if val==items:
                self.data=N

    def GetQItems(): #for combobox-5
        R = 0
        if not isinstance(self.items, list):
            R = 1
        else:
            R = MyLib.ArrayLength(self.items)
        return R

    def GetQNames():  # for database-0
        return self.GetQItems()

    def GetName(self, N=0):  # for database-1
        return self.GetItem(N)

    # for database
    def SetName(self, names, N=0): # for database-2
        self.SetItem(names, N)
           
    def SetItem(self, items, N=0):  # for database-3
        Q=MyLibPy2.ArrayLength(self.items)
        if isinstance(items, list):
           self.items = items
        else:
           if N>=1 and N<=Q:
               self.items[N-1]=items

    def Set(self, data="", DBTableData=[]):#11
        self.SetName(data)
        self.SetDBTableData(DBTableData)
    #
    # functions of DB FieldHeaderOrItems
    #
    def GetDBFieldInfo(self): #ColDBHeaderItems-1
        return 0
           
    def GetDBItemsTblInfo(self): #ColDBHeaderItems-2
        return 0
    #
    def SetDBFieldInfo(self, DBFldInfo): #ColDBHeaderItems-4
        pass
    
    def SetDBItemsTblInfo(self, DBItemsTblInfo): #ColDBHeaderItems-5
        pass 
    #            
    # def SetItems - united in SetItem below
    #
    #
    def GetColNameToDisplay(self): #ColDBHeaderItems-6
        return ""
           
    def GetDBFieldNameToDisplay(self): #ColDBHeaderItems-7
        return ""

    def GetFieldTypeN(self): #ColDBHeaderItems-8
        return 0

    def GetFieldTypeName(self): #ColDBHeaderItems-9
        return ""

    def GetFieldLength(self): #ColDBHeaderItems-10
        return 0

    def GetDBFieldCharacteristicsNumber(self): #ColDBHeaderItems-11
        return 0

    def GetIfIsKeyField(self): #ColDBHeaderItems-12
        return 0

    def GetIfIsNotNull(self): #ColDBHeaderItems-13
        return 0

    def GetIfIsCounter(self): #ColDBHeaderItems-13
        return 0

    def GetIfIsAutoIncrement(self): #ColDBHeaderItems-14
        return 0
    #
    def SetColNameToDisplay(self, name): #ColDBHeaderItems-15
        pass

    def SetDBFieldName(self, name): #ColDBHeaderItems-16
        pass

    def SetFieldTypeN(self, n): #ColDBHeaderItems-17
        pass

    def SetFieldTypeName(self, name): #ColDBHeaderItems-18
        pass

    def SetFieldLength(self, n): #ColDBHeaderItems-19
        pass

    def SetDBFieldCharacteristicsNumber(self, CharacteristicsNumber): #ColDBHeaderItems-20
        pass

    def SetIfIsKeyField(self, isKeyField):  #ColDBHeaderItems-21
        pass

    def SetIfIsNotNull(self, isNotNull):  #ColDBHeaderItems-22
        pass

    def SetIfIsCounter(self, isCounter):  #ColDBHeaderItems-22
        pass

    def SetIfIsAutoIncrement(self, isAutoIncrement):  #ColDBHeaderItems-23
        pass
    #
    # functions of DBTableHeader
    #
    def GetDBTableDataSuppl(self): #DBTableHdr-1
        R=[]
        if not self.DBTableData==[]:
            #if not self.DBTableData.DBTableDataSuppl==[]:
            R=self.DBTableData.DBTableDataSuppl
        return R

    def GetDBTableData(self): #DBTableHdr-2
        return self.DBTableData

    def GetDBTableNameToDisplay(self): #DBTableHdr-3
        return self.data#TableNameToDisplay

    def GetDBTableNameInDB(self): #DBTableHdr-4
        R=[]
        if not self.DBTableData==[]:
            #if not self.DBTableData.DBTableDataSuppl==[]:
            R=self.DBTableData.TableNameInDB
        return R

    def GetDBNameInDBCS(self): #DBTableHdr-5
        R=[]
        if not self.DBTableData==[]:
            if not self.DBTableData.DBTableDataSuppl==[]:
                R=self.DBTableData.DBTableDataSuppl.DBNameInDBCS
        return R

    def GetDBTypeName(self): #DBTableHdr-6
        R=[]
        if not self.DBTableData==[]:
            if not self.DBTableData.DBTableDataSuppl==[]:
                R=self.DBTableData.DBTableDataSuppl.DBTypeName
        return R

    def GetDBTypeN(self): #DBTableHdr-7
        R=[]
        if not self.DBTableData==[]:
            if not self.DBTableData.DBTableDataSuppl==[]:
                R=self.DBTableData.DBTableDataSuppl.DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5
        return R

    def GetDBFileFullName(self): #DBTableHdr-8
        R=[]
        if not self.DBTableData==[]:
            if not self.DBTableData.DBTableDataSuppl==[]:
                R=self.DBTableData.DBTableDataSuppl.DBFileFullName
        return R
    #
    def SetDBTableDataSuppl(self, DBTableDataSuppl):  #DBTableHdr-9
        R=[]
        if self.DBTableData==[]:
            self.DBTableData=TDBTableData()
        if isinstance(DBTableDataSuppl, TDBTableDataSuppl):
            self.DBTableData.DBTableDataSuppl=copy.deepcopy(DBTableDataSuppl)
        elif isinstance(DBTableDataSuppl, list):
            self.DBTableData.DBTableDataSuppl=TDBTableDataSuppl()
            #
            self.DBTableDataSuppl.DBNameInDBCS=str(DBTableDataSuppl[1-1])
            self.DBTableDataSuppl.DBTypeName=DBTableDataSuppl[2-1]
            self.DBTableDataSuppl.DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5=int(DBTableDataSuppl[3-1])
            self.DBTableDataSuppl.DBFileFullName=str(DBTableDataSuppl[4-1]) 

    def SetDBTableData(self, DBTableData): #DBTableHdr-10
        if isinstance(DBTableData, TDBTableData):
            self.DBTableData=copy.deepcopy(DBTableData)
        elif isinstance(DBTableData, list):
            if len(DBTableData)>0:
                if self.DBTableData==[]:
                    self.DBTableData=copy.deepcopy(DBTableData)
                self.DBTableData.TableNameInDB=DBTableData[1-1]
                if len(DBTableData)>5:
                    if self.DBTableData.DBTableDataSuppl==[]:
                        self.DBTableData.DBTableDataSuppl=TDBTableDataSuppl()
                    self.DBTableDataSuppl.DBNameInDBCS=str(DBTableDataSuppl[2-1])
                    self.DBTableDataSuppl.DBTypeName=DBTableDataSuppl[3-1]
                    self.DBTableDataSuppl.DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5=int(DBTableDataSuppl[4-1])
                    self.DBTableDataSuppl.DBFileFullName=str(DBTableDataSuppl[5-1])
                        
    def SetDBTableNameToDisplay(self, TableNameToDisplay): #DBTableHdr-11
        self.data=TableNameToDisplay

    def SetDBTableNameInDB(self, DBTableNameInDB): #DBTableHdr-12
        if self.DBTableData==[]:
            self.DBTableData=TDBTableData()
        self.DBTableData.TableNameInDB=DBTableNameInDB

    def SetDBNameInDBCS(self, DBNameInDBCS): #DBTableHdr-13
        if self.DBTableData==[]:
            self.DBTableData=TDBTableData()
        if self.DBTableData.DBTableDataSuppl==[]:
            self.DBTableData.DBTableDataSuppl=TDBTableDataSuppl()
        self.DBTableData.DBTableDataSuppl.DBNameInDBCS=DBNameInDBCS

    def SetDBTypeName(self, DBTypeName): #DBTableHdr-14
        if self.DBTableData==[]:
            self.DBTableData=TDBTableData()
        if self.DBTableData.DBTableDataSuppl==[]:
            self.DBTableData.DBTableDataSuppl=TDBTableDataSuppl()
        self.DBTableData.DBTableDataSuppl.DBTypeName=DBTypeName

    def SetDBTypeN(self, DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5): #DBTableHdr-15
        if self.DBTableData==[]:
            self.DBTableData=TDBTableData()
        if self.DBTableData.DBTableDataSuppl==[]:
            self.DBTableData.DBTableDataSuppl=TDBTableDataSuppl()
        self.DBTableData.DBTableDataSuppl.DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5=DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5

    def SetDBFileFullName(self, DBFileFullName): #DBTableHdr-16
        if self.DBTableData==[]:
            self.DBTableData=TDBTableData()
        if self.DBTableData.DBTableDataSuppl==[]:
            self.DBTableData.DBTableDataSuppl=TDBTableDataSuppl()
        self.DBTableData.DBTableDataSuppl.DBFileFullName=DBFileFullName
        #
        #
        ##
class DataCell_ColHeader_DBFieldOrItems:
    def GetType(self): #2
        return DataCell_ColHeader_DBFieldOrItems_TypeN
    #    return 1 #1- simple, 3-combobox, , 2-DBFldHdr
    #def __init__(self):
    #    self.DBFldInfo=[]
    def __init__(self, data="", items=[], DBFldInfo=[], DBItemsTblInfo=[]): #1
        self.TDBFieldInfo=[]
        self.items=[]
        self.DBItemsTblInfo=[]
        self.data=""#self.ColName=""
        #
        self.Set(data, items, DBFldInfo, DBItemsTblInfo)
    #
    #
    def GetVal(self): #3
        return self.GetName(self)

    def GetItem(self, N=0): #4
        R = 0
        if isinstance(self.items, list):
            #Q = MyLibPy2.ArrayLength(self.items)
            Q = len(self.items)
            if N >= 1 and N <= Q:
                R = self.items[N - 1]
        else:
            R = self.items[self.data-1]
        return R

    # ConcrType
    def GetFloatVal(self): #5
        return float(GetVal(self))

    def GetIntVal(self): #6
        return int(GetVal(self))

    def GetBoolVal(self): #7
        return bool(GetVal(self))#here must be own function!

    def GetStrVal(self): #8
        return str(self.GetVal())
   
    # for combobox
    def GetActiveN(self): #for combobox-1
        return 0

    def GetActiveItem(self): #for combobox-2
        return self.GetItem(0)

    def SetActiveN(self, val): #for combobox-3
        zero=0
        #

    def SetActiveNByVal(self, val): #for combobox-4
        pass
        #if isinstance(self.item, list) and self.item.count(val) > 0:
        #    self.SupplInf = self.item.index(val)

    def GetQItems():  #for combobox-5
        R = 0
        if not isinstance(self.items, list):
            R = 1
        else:
            R = MyLibPy2.ArrayLength(self.items)
        return R

    def GetQNames(): #for database-0
        R = 0
        if not isinstance(self.data, list):
            R = 1
        else:
            R = MyLibPy2.ArrayLength(self.data)
        return R

     # for database
    def GetName(self): # for database-1
        s=self.data#s=self.ColName
        if not self.DBFieldInfo==[]:
           s=self.DBFieldInfo.DBFieldNameToDBTable
        return s

    def SetName(self, names, N=0): # here very special #ColDBHeaderItems-3   #for database-2
        # N remains 0
        if isinstance(names, list):
            self.ColName=names[1-1]
            if len(names)>1:
                if self.DBFieldInfo==[]:
                    self.DBFieldInfo=TDBFieldInfo()
                self.DBFieldInfo.DBFieldNameToDBTable=str(data[2-1])
           
    def SetItem(self, items, N=0): #for database-3
        Q=MyLibPy2.ArrayLength(self.items)
        if isinstance(items, list):
            self.items = items
        else:
            if N>=1 and N<=Q:
                self.items[N-1]=items

    #
    def Set(self, var1=[], var2=[], var3=[], var4=[]): #11
        self.SetName(var1)
        self.SetItem(var2)
        self.SetDBFieldInfo(var3)#self.SetDBFieldInfo(DBFldInfo)
        self.SetDBItemsTblInfo(var4)#self.SetDBItemsTblInfo(DBItemsTblInfo)
    
    #
    # functions of DB FieldHeaderOrItems
    #     
    def GetDBFieldInfo(self): #ColDBHeaderItems-1
        return self.GetDBFieldInfo
           
    def GetDBItemsTblInfo(self): #ColDBHeaderItems-2
        return self.DBItemsTblInfo
    #
    #
    def SetDBFieldInfo(self, DBFldInfo): #ColDBHeaderItems-4
        self.DBFieldInfo=[]
        if not DBFldInfo==[]:
            if isinstance(DBFldInfo, TDBFieldInfo):
                self.DBFieldInfo=copy.deepcopy(DBFldInfo)
            elif isinstance(DBFldInfo, list):
                if len(DBFldInfo)>0:
                    if self.DBFieldInfo==[]:
                        self.DBFieldInfo=TDBFieldInfo()
                    self.DBFieldInfo.DBFieldNameToDBTable=str(DBFieldInfo[1-1])
                    if len(self.DBFieldInfo)>=8:
                        #self.DBFieldInfo alrerady created
                        if self.DBFieldInfo.DBFieldInfoSuppl==[]:
                            self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
                        self.DBFieldInfo.DBFieldInfoSuppl.FieldTypeN=int(DBFldInfo[2-1])
                        self.DBFieldInfo.DBFieldInfoSuppl.FieldTypeName=str(DBFldInfo[3-1])
                        self.DBFieldInfo.DBFieldInfoSuppl.FieldLength=int(DBFldInfo[4-1])
                        self.DBFieldInfo.DBFieldInfoSuppl.DBFieldCharacteristicsNumber=int(DBFldInfo[5-1])
                        self.DBFieldInfo.DBFieldInfoSuppl.isKeyField=int(DBFldInfo[6-1])
                        self.DBFieldInfo.DBFieldInfoSuppl.isCounter=int(DBFldInfo[7-1])
                        self.DBFieldInfo.DBFieldInfoSuppl.isAutoIncrement=int(DBFldInfo[8-1])

    def SetDBItemsTblInfo(self, DBItemsTblInfo): #ColDBHeaderItems-5
        self.DBItemsTblInfo=[]
        if not DBItemsTblInfo==[]:
            self.DBItemsTblInfo=self.TDBItemsTblInfo()
            if isinstance(DBItemsTblInfo, TDBItemsTblInfo):
                self.DBItemsTblInfo=copy.deepcopy(DBItemsTblInfo)
            elif isinstance(DBItemsTblInfo, list):
                # self.DBItemsTblInfo already created
                self.DBItemsTblInfo.ItemsTableName=DBItemsTblInfo[1-1]
                self.ItemsTableItemsFieldName=DBItemsTblInfo[2-1]
                self.ItemsTableKeyFieldName=DBItemsTblInfo[3-1] 
                
    # def SetItems - united in SetItem below
    #
    #
    def GetColNameToDisplay(self): #ColDBHeaderItems-6
        return self.data#self.ColName
           
    def GetDBFieldNameToDisplay(self): #ColDBHeaderItems-7
        s=""
        if not self.DBFieldInfo==[]:
           s=self.DBFieldInfo.DBFieldNameToDBTable
        return s

    def GetFieldTypeN(self): #ColDBHeaderItems-8
        R=0
        if not self.DBFieldInfo==[] and not self.DBFieldInfo.DBFieldInfoSuppl==[]:
            R=self.DBFieldInfo.DBFieldInfoSuppl.FieldTypeN
        return R

    def GetFieldTypeName(self): #ColDBHeaderItems-9
        R=""
        if not self.DBFieldInfo==[] and not self.DBFieldInfo.DBFieldInfoSuppl==[]:
            R=self.DBFieldInfo.DBFieldInfoSuppl.FieldTypeName
        return R

    def GetFieldLength(self): #ColDBHeaderItems-10
        R=0
        if not self.DBFieldInfo==[] and not self.DBFieldInfo.DBFieldInfoSuppl==[]:
            R=self.DBFieldInfo.DBFieldInfoSuppl.FieldLength
        return R

    def GetDBFieldCharacteristicsNumber(self): #ColDBHeaderItems-11
        R=0
        if not self.DBFieldInfo==[] and not self.DBFieldInfo.DBFieldInfoSuppl==[]:
            R=self.DBFieldInfo.DBFieldInfoSuppl.DBFieldCharacteristicsNumber
        return R

    def GetIfIsKeyField(self): #ColDBHeaderItems-12
        R=0
        if not self.DBFieldInfo==[] and not self.DBFieldInfo.DBFieldInfoSuppl==[]:
            R=self.DBFieldInfo.DBFieldInfoSuppl.isKeyField
        return R

    def GetIfIsNotNull(self): #ColDBHeaderItems-13
        R=0
        if not self.DBFieldInfo==[] and not self.DBFieldInfo.DBFieldInfoSuppl==[]:
            R=self.DBFieldInfo.DBFieldInfoSuppl.isNotNull
        return R

    def GetIfIsCounter(self): #ColDBHeaderItems-13
        R=0
        if not self.DBFieldInfo==[] and not self.DBFieldInfo.DBFieldInfoSuppl==[]:
            R=self.DBFieldInfo.DBFieldInfoSuppl.isCounter
        return R

    def GetIfIsAutoIncrement(self): #ColDBHeaderItems-14
        R=0
        if not self.DBFieldInfo==[] and not self.DBFieldInfo.DBFieldInfoSuppl==[]:
            R=self.DBFieldInfo.DBFieldInfoSuppl.isAutoIncrement
        return R
    #
    def SetColNameToDisplay(self, name): #ColDBHeaderItems-15
        self.data=name#self.ColName=name

    def SetDBFieldName(self, name): #ColDBHeaderItems-16
        s=""
        if self.DBFieldInfo==[]:
            self.DBFieldInfo=TDBFieldInfo()
        self.DBFieldInfo.DBFieldNameToDBTable=name

    def SetFieldTypeN(self, n): #ColDBHeaderItems-17
        if self.DBFieldInfo==[]:
            self.DBFieldInfo=TDBFieldInfo()
            if self.DBFieldInfo.DBFieldInfoSuppl==[]:
                self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
            self.DBFieldInfo.DBFieldInfoSuppl.FieldTypeN=n

    def SetFieldTypeName(self, name): #ColDBHeaderItems-18
        if self.DBFieldInfo==[]:
            self.DBFieldInfo=TDBFieldInfo()
            if self.DBFieldInfo.DBFieldInfoSuppl==[]:
                self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
            self.DBFieldInfo.DBFieldInfoSuppl.FieldTypeName=name

    def SetFieldLength(self, n): #ColDBHeaderItems-19
        if self.DBFieldInfo==[]:
            self.DBFieldInfo=TDBFieldInfo()
            if self.DBFieldInfo.DBFieldInfoSuppl==[]:
                self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
            self.DBFieldInfo.DBFieldInfoSuppl.FieldLength=n

    def SetDBFieldCharacteristicsNumber(self, CharacteristicsNumber): #ColDBHeaderItems-20
        if self.DBFieldInfo==[]:
            self.DBFieldInfo=TDBFieldInfo()
            if self.DBFieldInfo.DBFieldInfoSuppl==[]:
                self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
            self.DBFieldInfo.DBFieldInfoSuppl.FieldLength=CharacteristicsNumber

    def SetIfIsKeyField(self, isKeyField):  #ColDBHeaderItems-21
        if self.DBFieldInfo==[]:
            self.DBFieldInfo=TDBFieldInfo()
            if self.DBFieldInfo.DBFieldInfoSuppl==[]:
                self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
            self.DBFieldInfo.DBFieldInfoSuppl.isKeyField=isKeyField

    def SetIfIsNotNull(self, isNotNull):  #ColDBHeaderItems-22
        if self.DBFieldInfo==[]:
            self.DBFieldInfo=TDBFieldInfo()
            if self.DBFieldInfo.DBFieldInfoSuppl==[]:
                self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
            self.DBFieldInfo.DBFieldInfoSuppl.isNotNull=isNotNull

    def SetIfIsCounter(self, isCounter):  #ColDBHeaderItems-22
        if self.DBFieldInfo==[]:
            self.DBFieldInfo=TDBFieldInfo()
            if self.DBFieldInfo.DBFieldInfoSuppl==[]:
                self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
            self.DBFieldInfo.DBFieldInfoSuppl.isCounter=isCounter

    def SetIfIsAutoIncrement(self, isAutoIncrement):  #ColDBHeaderItems-23
        if self.DBFieldInfo==[]:
            self.DBFieldInfo=TDBFieldInfo()
            if self.DBFieldInfo.DBFieldInfoSuppl==[]:
                self.DBFieldInfo.DBFieldInfoSuppl=TDBFieldInfoSuppl()
            self.DBFieldInfo.DBFieldInfoSuppl.isAutoIncrement=isAutoIncrement
   
    #
    # functions of DBTableHeader
    #
    def GetDBTableDataSuppl(self): #DBTableHdr-1
        return []

    def GetDBTableData(self): #DBTableHdr-2
        return []

    def GetDBTableNameToDisplay(self): #DBTableHdr-3
        return ""

    def GetDBTableNameInDB(self): #DBTableHdr-4
        return ""

    def GetDBNameInDBCS(self): #DBTableHdr-5
        return ""

    def GetDBTypeName(self): #DBTableHdr-6
        return ""

    def GetDBTypeN(self): #DBTableHdr-7
        return 0

    def GetDBFileFullName(self): #DBTableHdr-8
        return ""
    #
    def SetDBTableDataSuppl(self, DBTableDataSuppl):  #DBTableHdr-9
        pass

    def SetDBTableData(self, DBTableData): #DBTableHdr-10
        pass

    def SetDBTableNameToDisplay(self, TableNameToDisplay): #DBTableHdr-11
        pass

    def SetDBTableNameInDB(self, DBTableNameInDB): #DBTableHdr-12
        pass

    def SetDBNameInDBCS(self, DBNameInDBCS): #DBTableHdr-13
        pass

    def SetDBTypeName(self, DBTypeName): #DBTableHdr-14
        pass

    def SetDBTypeN(self, DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5): #DBTableHdr-15
        pass
    
    def SetDBFileFullName(self, DBFileFullName): #DBTableHdr-16
        pass
                   

    def ToString(self):  # new 2021-08-12
        #return "cell id="+str(id(self))+" content: "+str(self.GetName())+" "
        return str(self.GetName()) + " "
    #
    def __str__(self):
       return ToString()
        #
        ##
#---------------------------------------------------------------------------

class DataCell:
    def __init__(self, var1=[], var2=[], var3=[], var4=[]): #1
        #self.cell=[]#!else dataCell instance has no attribute cell
        #self.cell=DataCell_Simple()
        if isinstance(var1, DataCell):
            self.cell=copy.deepcopy(var1.cell)
        #
        elif isinstance(var1, DataCell_Simple) or isinstance(var1, DataCell_ComboboxOrMemo) or isinstance(var1, DataCell_ColHeader_DBFieldOrItems) or isinstance(var1, DataCell_DBTableHeader):
            self.cell=copy.deepcopy(var1)
        #
        elif not isinstance(var1, list)  and var2==[]and var3==[] and var4==[]:
            self.cell=DataCell_Simple(var1)
        #
        elif isinstance(var1, list) and var2==[] and var3==[] and var4==[]:
            self.cell=DataCell_ComboboxOrMemo(var1)
        elif isinstance(var1, list) and isinstance(var2, int) and var3==[] and var4==[]:
            self.cell=DataCell_ComboboxOrMemo(var1)
            self.cell.SetActiveN(var2)
        elif isinstance(var1, int) and isinstance(var2, list) and var3==[] and var4==[]:
            self.cell=DataCell_ComboboxOrMemo(var2)
            self.cell.SetActiveN(var1)
        #
        elif isinstance(var1, str) and isinstance(var2, TDBTableData) and var3==[] and var4==[]:
            self.cell=DataCell_DBTableHeader(var1, var2)
        #
        elif isinstance(var1, str) and isinstance(var2, TDBFieldInfo) and var3==[] and var4==[]:
            self.cell=DataCell_DBTableHeader(var1, var2, var3, var4)
        #    
        self.Set(var1, var3, var2, var4)#ob no need to delete old obj as in C++
                   
    def Set_Simple(self,var1): #1-11-1
        self.cell=DataCell_Simple()
        self.cell.Set(var1)
    def Set_ComboboxOrMemo(self,var1, var2):  #1-11-2
        self.cell=DataCell_ComboboxOrMemo()
        self.cell.Set(var1, var2)
    def Set_DBTableHeader(self,var1, var2, var3):  #1-11-3
        self.cell=DataCell_DBTableHeader()
        self.cell.Set(var1, var2, var3)
    def Set_ColHdr_DBFldOrItems(self, var1, var2=[], var3=[], var4=[]):  #1-11-3
        self.cell=DataCell_ColHeader_DBFieldOrItems()
        self.cell.Set(var1, var2, var3)

    def Set(self, var1, var2=[], var3=[], var4=[]): #11
        if var2==[] and var3==[] and var4==[]:
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
                self.Set_Simple(var1)
            else:
                self.Set_Simple(0)
    #
    def GetType(self): #2
        return self.cell.GetType()
    
    def GetVal(self, N=1): #3
        return self.cell.GetVal(self, N)

    def GetItem(self, N=1): #4
        return self.cell.GetItem(self, N)

    # ConcrType
    def GetFloatVal(self): #5
        return float(self.cell.GetFloatVal())

    def GetIntVal(self): #6
        return int(self.cell.GetIntVal())

    def GetBoolVal(self): #7
        return bool(self.cell.GetBoolVal())

    def GetStrVal(self): #8
        return str(self.cell.GetStrVal())

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
    def GetQItems(): #for combobox-5
        return self.cell.GetQItems()

    def GetQNames(): # for database-0
        return self.cell.GetQNames()

    # for database
    def GetName(self, N=1): # for database-1
        return self.cell.GetName(N)

    def SetName(self, names, N=0): # for database-2
        self.cell.SetName(names, N)
        
    def SetItem(self, items, N=0): # for database-3
        self.cell.SetItem(items, N)

    #
    def Set(self, var1=[], var2=[], var3=[], var4=[]): #11
        self.cell.Set(var1, var2, var3, var4)
    #
    #
    #SetName - above
    #
    # functions of DB FieldHeaderOrItems
    #
    def GetDBFieldInfo(self): #ColDBHeaderItems-1
        return self.cell.GetDBFieldInfo()
           
    def GetDBItemsTblInfo(self): #ColDBHeaderItems-2
        return self.cell.GetDBItemsTblInfo()
    #
    def SetDBFieldInfo(self, DBFldInfo): #ColDBHeaderItems-4
        self.cell.SetDBFieldInfo(DBFldInfo)
    
    def SetDBItemsTblInfo(self, DBItemsTblInfo): #ColDBHeaderItems-5
        self.cell.SetDBItemsTblInfo(DBItemsTblInfo) 
                
    # def SetItems - united in SetItem below
    #
    #
    def GetColNameToDisplay(self): #ColDBHeaderItems-6
        return self.cell.GetColNameToDisplay()
           
    def GetDBFieldNameToDisplay(self): #ColDBHeaderItems-7
        return self.cell.GetDBFieldNameToDisplay()

    def GetFieldTypeN(self): #ColDBHeaderItems-8
        return self.cell.GetFieldTypeN()

    def GetFieldTypeName(self): #ColDBHeaderItems-9
        return self.cell.GetFieldTypeName()

    def GetFieldLength(self): #ColDBHeaderItems-10
        return self.cell.GetFieldLength()

    def GetDBFieldCharacteristicsNumber(self): #ColDBHeaderItems-11
        return self.cell.GetDBFieldCharacteristicsNumber()

    def GetIfIsKeyField(self): #ColDBHeaderItems-12
        return self.cell.GetIfIsKeyField()

    def GetIfIsCounter(self): #ColDBHeaderItems-13
        return self.cell.GetIfIsCounter()

    def GetIfIsNotNull(self): #ColDBHeaderItems-13
        return self.cell.GetIfIsNotNull()

    def GetIfIsAutoIncrement(self): #ColDBHeaderItems-14
        return self.cell.GetIfIsAutoIncrement()
    #
    def SetColNameToDisplay(self, name): #ColDBHeaderItems-15
        self.cell.SetColNameToDisplay(name)

    def SetDBFieldName(self, name): #ColDBHeaderItems-16
        self.cell.SetDBFieldName(name)

    def SetFieldTypeN(self, n): #ColDBHeaderItems-17
        self.cell.SetFieldTypeN(n)

    def SetFieldTypeName(self, name): #ColDBHeaderItems-18
        self.cell.SetFieldTypeName(name)

    def SetFieldLength(self, n): #ColDBHeaderItems-19
        self.cell.SetFieldLength(n)

    def SetDBFieldCharacteristicsNumber(self, CharacteristicsNumber): #ColDBHeaderItems-20
        self.cell.SetDBFieldCharacteristicsNumber(CharacteristicsNumber)

    def SetIfIsKeyField(self, isKeyField):  #ColDBHeaderItems-21
        self.cell.SetIfIsKeyField(isKeyField)

    def SetIfIsNotNull(self, isNotNull):  #ColDBHeaderItems-22
        self.cell.SetIfIsCounter(isNotNull)

    def SetIfIsCounter(self, isCounter):  #ColDBHeaderItems-22
        self.cell.SetIfIsCounter(isCounter)

    def SetIfIsAutoIncrement(self, isAutoIncrement):  #ColDBHeaderItems-23
        self.cell.SetIfIsAutoIncrement(isAutoIncrement)
    #
    # functions of DBTableHeader
    #
    def GetDBTableDataSuppl(self): #DBTableHdr-1
        return self.cell.GetDBTableDataSuppl()

    def GetDBTableData(self): #DBTableHdr-2
        return self.cell.GetDBTableData()

    def GetDBTableNameToDisplay(self): #DBTableHdr-3
        return self.cell.GetDBTableNameToDisplay()

    def GetDBTableNameInDB(self): #DBTableHdr-4
        return self.cell.GetDBTableNameInDB()

    def GetDBNameInDBCS(self): #DBTableHdr-5
        return self.cell.GetDBNameInDBCS()

    def GetDBTypeName(self): #DBTableHdr-6
        return self.cell.GetDBTypeName()

    def GetDBTypeN(self): #DBTableHdr-7
        return self.cell.GetDBTypeN()

    def GetDBFileFullName(self): #DBTableHdr-8
        return self.cell.GetDBFileFullName()
    #
    def SetDBTableDataSuppl(self, DBTableDataSuppl):  #DBTableHdr-9
        self.cell.SetDBTableDataSuppl(DBTableDataSuppl)

    def SetDBTableData(self, DBTableData): #DBTableHdr-10
        self.cell.SetDBTableData(DBTableData)

    def SetDBTableNameToDisplay(self, TableNameToDisplay): #DBTableHdr-11
        self.cell.SetDBTableNameToDisplay(TableNameToDisplay)

    def SetDBTableNameInDB(self, DBTableNameInDB): #DBTableHdr-12
        self.cell.SetDBTableNameInDB(DBTableNameInDB)

    def SetDBNameInDBCS(self, DBNameInDBCS): #DBTableHdr-13
        self.cell.SetDBNameInDBCS(DBNameInDBCS)

    def SetDBTypeName(self, DBTypeName): #DBTableHdr-14
        self.cell.SetDBTypeName(DBTypeName)

    def SetDBTypeN(self, DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5): #DBTableHdr-15
        self.cell.SetDBTypeN(DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5)
    
    def SetDBFileFullName(self, name): #DBTableHdr-16
        self.cell.SetDBFileFullName(name)
    #    
    #   
    def ToString(self, str_bef="", str_aft=""):  # represent-1
        #return "cell id="+str(id(self))+" content: "+str(self.GetName())+" "
        return str_bef+str(self.GetName())+str_aft

    def __str__(): #represent-2
        return str(self.GetName())
        
    def ToString_Info(self):  # represent-3 #says invalid sybtax, et here s' all gut, ma in fn ef wa ne satq )s
        return "DataCell Type="+str(self.GetTypeN())+" id="+str(id(self))+" val="+str(self.GetVal())
    
#-----------------------------------------------------------------------


class DataCellRow:
    #row = []
    def __init__(self):
        self.row = []
        
        
    def GetCell(self, cellN=0):
        R = 0
        #Q = self.ArrayLength(self.row)
        Q = len(self.row)
        if cellN >= 1 and cellN <= Q:
            R = self.row[cellN - 1]
        #elif cellN==0:
        #    R=self.header
        return R
    
    def Set(self, arr, header=0):
        #Q=MyLibPy2.ArrayLength(arr)
        #print("DataCellRow.Set starts working")
        #print("Adding ",Q, " items")
        #
        self.row=copy.deepcopy(arr)
        self.header=copy.deepcopy(header)
        #Q=MyLibPy2.ArrayLength(arr)
        #print("DataCellRow.Set finishes working")

    def SetCell(self, N, val):
        if N>=1 and N<=self.GetLength():
            cell=DataCell(val)
            self.row[N-1].Set(val)

    #def GetHeader(self):
    #    return self.header

    def GetLength(self):
        #return MyLibPy2.ArrayLength(self.row)
        return len(self.row)

    def GetLengthN(self, cellN):
        R=0
        if cellN>=1 and cellN<=Q:
            R=self.row[cellN-1].GetQItems()
        elif cellN==0 and self.header!=0:
            R=self.header.GetLength()
        return R

    def GetName(self, NameN=1, CellN=0):
        R = ""
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    R=self.row[N-1].GetName(NameN)
        #elif cellN==0:
        #    R=self.header.GetName(NameN)
        cell=self.GetCell(cellN)
        if isinstace(cell, DataCell):
            R=cell.GetName(NameN)
        return R

    def GetQItems(self, cellN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        if cellN>=1 and CellN<=Q:
            R=self.row[N-1].GetQItems()
        #elif CellN==0:
        #    R=self.header.GetQItems()
        return R

    def GetQNames(self, cellN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    R=self.row[N-1].GetQNames()
        if cellN>=1 and CellN<=Q:
            R=self.row[cellN-1].GetQNames()
        #elif cellN==0 and isinstance(self.header, DataCell):
        #    R=self.header.GetQNames()
        return R

    def GetTypeN(self, cellN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    R=self.row[N-1].GetType()
        if cellN>=1 and cellN<=Q:
            R=self.row[N-1].GetTypeN()
        #elif cellN==0 and isinstance(self.header, DataCell):
        #    R=self.header.GetTypeN()
        return R

    def GetActiveN(self, cellN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    R=self.row[N-1].GetActiveN()
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetActiveN()
        return R

    def GetActiveItem(self, cellN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    R=self.row[N-1].GetActiveItem()
        if cellN>=1 and cellN<=Q:
            R=self.row[N-1].GetActiveItem()
        #elif cellN==0 and isinstance(self.header, DataCell):
        #    R=self.header.GetActiveItem()
        return R

   

    def SetActiveNByVal(self, cellN, val):
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        if cellN>=1 and cellN<=Q:
            self.row[cellN-1].SetActiveNByVal(val)
        #elif cellN==0:
        #    self.header.SetActiveNByVal(val)
    
    def GetVal(self, cellN=0, valN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            #if cellN>=0 and cellN<=Q:
            activeN=self.GetActiveNOfN(cellN)
            cellLength=self.GetLengthN(cellN)
            if valN<=0 or valN>cellLength:
                valN=activeN
            R=cell.GetVal(valN)
        return R

    def GetItem(self, cellN, valN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            #activeN=self.GetActiveNOfN(cellN)
            #cellLength=self.GetLengthN(cellN)
            activeN=cell.GetActiveN()
            cellLength=cell.GetLengthN(cellN)
            if valN<=0 or valN>cellLength:
                valN=activeN
            R=self.row[cellN-1].GetItem(valN)
        return R


    def GetFloatVal(self, cellN=0):
        R=0
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetFloatVal()
        return R

    def GetIntVal(self, cellN=0):
        R=0
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetIntVal()
        return R

    def GetBoolVal(self, cellN, valN=0):
        R=0
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetBoolVal()
        return R

    def GetStrVal(self, cellN, valN=0):
        R=0
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetStrVal()
        return R
        
        
    def SetName(self, names, cellN=0, nameN=0):
        Q=len(self.row)
        #i#f(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    self.row[cellN-1].SetName(names, nameN)
        if cellN>=1 and cellN<=Q:
            self.row[cellN-1].SetName(names, nameN)
        #elif:
        #    self.header.SetName(names, nameN)
        return R
        
    def SetItem(self, cellN, names, itemN=0):
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        if cellN>=1 and cellN<=0:
            self.row[cellN-1].SetItem(names, itemN)
        elif cellN==0:
            self.header.SetItem(names, itemN)
            
     

    def Add(self, cellExt):
        cell=copy.deepcopy(cellExt)
        #ArrayAdd(self.row, cell)
        self.row.append(cell)

    def InsN(self, cellExt, N=0):
        row=[]
        Q=len(self.row)
        cell=copy.deepcopy(cellExt)
        #if N==0:
        #    N=Q
        #if N==1 or N==0:
        #    self.row.append(cell)
        #else:
        if N>=1 and N<=Q:
            for i in range(1, N-1+1):
                row.append(self.row[i-1])
            row.append(cell)
            for i in range(N, Q+1):
                row.append(self.row[i-1])
            self.row=row

    def DelN(self, N=0):
        row=[]
        Q=len(self.row)
        cell=copy.deepcopy(cellExt)
        if N==0:
            N=Q
        if N>=1 and N<=Q:
            for i in range(1, N-1+1):
                row.append(self.row[i-1])
            row.append(cell)
            for i in range(N, Q+1):
                row.append(self.row[i-1])
        

    def GetFieldType(self, cellN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        activeN=self.GetActiveNOfN(cellN)
        cellLength=self.GetLengthN(cellN)
        #if cellN>0:
        cell=GetCell(cellN)
            #activeN=self.GetActiveNOfN(cellN)
            #cellLength=self.GetLengthN(cellN)
            #R=self.row[cellN-1].GetFieldType()
        if isinstance(cell, DataCell):
            R=cell.GetFieldType()
        return R

    def GetFieldWidth(self, cellN):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #activeN=self.GetActiveNOfN(cellN)
        #cellLength=self.GetLengthN(cellN)
        #R=self.row[cellN-1].GetFieldWidth()
        cell=GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetFieldWidth()
        return R

    def GetFieldLength(self, cellN):
        R=0
        Q=len(self.row)
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetFieldLength()
        return R

    def GetFieldType(self, cellN):
        R=0
        Q=len(self.row)
        cell=GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetFieldType()
        return R


    def SetFieldType(self, cellN, TypeN):
        Q=len(self.row)
        if cellN>=1 and cellN<=Q:
            self.row[cellN-1].SetFieldType(TypeN)
        

    def SetFieldWidth(self, cellN, val):
        Q=len(self.row)
        if cellN>=1 and cellN<=Q:
            self.row[cellN-1].SetFieldWidth(val)
        #elif cellN==0:
        #    self.header.SetFieldWidth(val)

    def SetFieldChateristics(self, val, cellN=0):
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        if cellN>=1 and cellN<=Q:
            self.row[cellN-1].SetFieldChateristics(val)
        #elif cellN==0:
        #    self.header.SetFieldChateristics(val)



    def ToStringN(self, cellN=0):
        R=""
        Q=len(self.row)
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.ToString()
        return R


    def ToString(self, str_btw=" "):
        #Q=MyLibPy2.ArrayLength(self.row)
        R = ""
        R = "Row #"+str(id(self))+": "+str(Q)+" elements: "
        #Q=MyLibPy2.ArrayLength(self.row)
        Q=len(self.row)
        for i in range(1, Q):#seems Q not including, ce for 1..Q-1
            R=R+self.row[i-1].ToString()
            R=R+str_btw
        if Q>0:
            R=R+self.row[Q-1].ToString()
        return R

    def ToString(self, separator=" ", ShowHeaderLine=0):
        R = ""
        if(ShowHeaderLine!=0):
            R = "Row #"+str(id(self))+": "+str(Q)+" elements: "
            R=R+separator
        Q=len(self.row)
        for i in range(1, Q-1+1):
            R=R+self.ToStringN(i)
            R=R+separator
        if Q>0:
            R=R+self.ToStringN(Q)
        return R

    def __str__(self):
        return self.ToString()
#DataCellRow

   


class DataCellRowWithHeader:
    #row = []
    def __init__(self, row=[], header=0):
        #self.row = []
        if(isinstance(row, DataCellRow)):
            self.row =copy.deepcopy(row)
        elif(isinstance(row, list)):
            self.row=DataCellRow(copy.deepcopy(row))
        else:
            self.row = DataCellRow()
        self.header=header#0
        
    def GetCell(self, cellN=0):
        R = 0
        #Q = self.ArrayLength(self.row)
        Q = len(self.row)
        if cellN >= 1 and cellN <= Q:
            #R = self.row[cellN - 1]
            R = self.row.GetCell(cellN)
        elif cellN==0:
            R=self.header
        return R
    
    def Set(self, row, header=0):
        #Q=MyLibPy2.ArrayLength(arr)
        #print("DataCellRow.Set starts working")
        #print("Adding ",Q, " items")
        #
        if(isinstance(row, DataCellRow)):
            self.row =copy.deepcopy(row)
        elif isinstance(row, list):
            self.row=DataCellRow(copy.deepcopy(row))
        self.header=copy.deepcopy(header)
        #Q=MyLibPy2.ArrayLength(arr)
        #print("DataCellRow.Set finishes working")

    def GetHeader(self):
        return self.header

    def GetLength(self):
        #return MyLibPy2.ArrayLength(self.row)
        return len(self.row)

    def GetLengthN(self, cellN):
        R=0
        if cellN==0 and self.header!=0:
            R=self.header.GetLength()
        elif cellN>=1 and cellN<=Q:
            R=self.row.GetQItems(cellN)
        return R

    def GetName(self, NameN=1, CellN=0):
        R = ""
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    R=self.row[N-1].GetName(NameN)
        #elif cellN==0:
        #    R=self.header.GetName(NameN)
        cell=self.GetCell(cellN)
        if isinstace(cell, DataCell):
            R=cell.GetName(NameN)
        return R

    def GetQItems(self, cellN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        if cellN>=1 and CellN<=Q:
            #R=self.row[N-1].GetQItems()
            R=self.row.GetQItems(cellN)
        elif CellN==0:
            R=self.header.GetQItems()
        return R

    def GetQNames(self, cellN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    R=self.row[N-1].GetQNames()
        if cellN>=1 and CellN<=Q:
            #R=self.row[cellN-1].GetQNames()
            R=self.row.GetQNames(CellN)
        elif cellN==0 and isinstance(self.header, DataCell):
            R=self.header.GetQNames()
        return R

    def GetTypeN(self, cellN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    R=self.row[N-1].GetType()
        if cellN>=1 and cellN<=Q:
            #R=self.row[N-1].GetTypeN()
            R=self.row.GetTypeN(cellN)
        elif cellN==0 and isinstance(self.header, DataCell):
            R=self.header.GetTypeN()
        return R

    def GetActiveN(self, cellN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    R=self.row[N-1].GetActiveN()
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetActiveN()
        return R

    def GetActiveItem(self, cellN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    R=self.row[N-1].GetActiveItem()
        if cellN>=1 and cellN<=Q:
            #R=self.row[N-1].GetActiveItem()
            R=self.row[N-1].GetActiveItem(cellN)
        elif cellN==0 and isinstance(self.header, DataCell):
            R=self.header.GetActiveItem()
        return R

   

    def SetActiveNByVal(self, cellN, val):
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        if cellN>=1 and cellN<=Q:
            #self.row[cellN-1].SetActiveNByVal(val)
            self.row.SetActiveNByVal(cellN, val)
        elif cellN==0:
            self.header.SetActiveNByVal(val)
    
    def GetVal(self, cellN=0, valN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            #if cellN>=0 and cellN<=Q:
            activeN=self.GetActiveNOfN(cellN)
            cellLength=self.GetLengthN(cellN)
            if valN<=0 or valN>cellLength:
                valN=activeN
            R=cell.GetVal(valN)
        return R

    def GetItem(self, cellN, valN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            #activeN=self.GetActiveNOfN(cellN)
            #cellLength=self.GetLengthN(cellN)
            activeN=cell.GetActiveN()
            cellLength=cell.GetLengthN(cellN)
            if valN<=0 or valN>cellLength:
                valN=activeN
            R=self.row[cellN-1].GetItem(valN)
        return R


    def GetFloatVal(self, cellN=0):
        R=0
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetFloatVal()
        return R

    def GetIntVal(self, cellN=0):
        R=0
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetIntVal()
        return R

    def GetBoolVal(self, cellN, valN=0):
        R=0
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetBoolVal()
        return R

    def GetStrVal(self, cellN, valN=0):
        R=0
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetStrVal()
        return R
        
        
    def SetName(self, names, cellN=0, nameN=0):
        Q=len(self.row)
        #i#f(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    self.row[cellN-1].SetName(names, nameN)
        if cellN>=1 and cellN<=Q:
            self.row[cellN-1].SetName(names, nameN)
        else:
            self.header.SetName(names, nameN)
        return R
        

    def SetItem(self, cellN, names, itemN=0):
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        if cellN>=1 and cellN<=0:
            #self.row[cellN-1].SetItem(names, itemN)
            self.row.SetItem(cellN, names, itemN)
        elif cellN==0:
            self.header.SetItem(names, itemN)
            
            

    def Add(self, cell):
        self.row.Add(cell)

    def InsN(self, cell, N=0):
        self.row.InsN(cell, N)

    def DelN(self, N=0):
        self.DelN(N)
       

    def GetFieldType(self, cellN=0):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        activeN=self.GetActiveNOfN(cellN)
        cellLength=self.GetLengthN(cellN)
        #if cellN>0:
        cell=GetCell(cellN)
            #activeN=self.GetActiveNOfN(cellN)
            #cellLength=self.GetLengthN(cellN)
            #R=self.row[cellN-1].GetFieldType()
        if isinstance(cell, DataCell):
            R=cell.GetFieldType()
        return R

    def GetFieldWidth(self, cellN):
        R=0
        Q=len(self.row)
        if(cellN<=0 or cellN>Q):
            cellN=Q#cellN=1
        #if cellN>0:
        #activeN=self.GetActiveNOfN(cellN)
        #cellLength=self.GetLengthN(cellN)
        #R=self.row[cellN-1].GetFieldWidth()
        cell=GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetFieldWidth()
        return R

    def GetFieldLength(self, cellN):
        R=0
        Q=len(self.row)
        if(cellN<=0 or cellN>Q):
            cellN=Q#cellN=1
        if cellN>0:
        #    activeN=self.GetActiveNOfN(cellN)
        #    cellLength=self.GetLengthN(cellN)
        #    R=self.row[cellN-1].GetFieldLength()
            cell=GetCell(cellN)
            if isinstance(cell, DataCell):
                R=cell.GetFieldLength()
        return R

    def GetFieldType(self, cellN):
        R=0
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    activeN=self.GetActiveNOfN(cellN)
        #    cellLength=self.GetLengthN(cellN)
        #    R=self.row[cellN-1].GetFieldType()
        cell=GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.GetFieldType()
        return R



    def SetFieldType(self, cellN, TypeN):
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    self.row[cellN-1].SetFieldType(TypeN)
        if cellN>=1 and cellN<=Q:
            #self.row[cellN-1].SetFieldType(TypeN)
            self.row.SetFieldType(cellN, TypeN)
        elif cellN==0:
            self.header.SetFieldType(TypeN)

    def SetFieldWidth(self, cellN, val):
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        #    self.row[cellN-1].SetFieldWidth(val)
        if cellN>=1 and cellN<=Q:
            self.row.SetFieldWidth(cellN, val)
        elif cellN==0:
            self.header.SetFieldWidth(val)

    def SetFieldChateristics(self, val, cellN=0):
        Q=len(self.row)
        #if(cellN<=0 or cellN>Q):
        #    cellN=Q#cellN=1
        #if cellN>0:
        if cellN>=1 and cellN<=Q:
            self.row.SetFieldChateristics(val, cellN)
        elif cellN==0:
            self.header.SetFieldChateristics(val)



    def HeaderToString(self):
        R=""
        if(isinstance(self.header,DataCell)):
             R=self.header.ToString()
        return R


    def ToStringN(self, cellN=0):
        R=""
        Q=len(self.row)
        cell=self.GetCell(cellN)
        if isinstance(cell, DataCell):
            R=cell.ToString()
        return R


    def ToString(self, sep_row=" ", sep_hdr=" ", ShowHeaderLine=0):
        #Q=MyLibPy2.ArrayLength(self.row)
        R = ""
        if(ShowHeaderLine>0):
            R = "Row #"+str(id(self))+": "+str(Q)+" elements: "
        #Q=MyLibPy2.ArrayLength(self.row)
        R=R+self.HeaderToString()
        R=R+sep_hdr
        Q=len(self.row)
        for i in range(1, Q):#seems Q not including, ce for 1..Q-1
            R=R+self.ToStringN(cellN)
            R=R+str_btw
        if Q>0:
            R=R+self.row[Q-1].ToString()
        return R

    def ToString(self, separator=" ", SepMain=": "):
        R = ""
        R = "Row #"+str(id(self))+": "+str(Q)+" elements: "
        R=R+ToStringN(0) # maybe 
        R=R+SepMain
        Q=len(self.row)
        for i in range(1, Q-1+1):
            R=R+ToStringN(i)
            R=R+separator
        R=R+ToStringN(Q)
        return R

    def __str__(self):
        return self.ToString()








#class TableHeaders:
#    def __init__(self, TableHeader="", LinesGeneralHeader="", ColumnsGeneralHeader=""):
#        self.TableHeader=""
#        self.LinesGeneralHeader=""
#        self.ColumnsGeneralHeader=""
#        self.Set(TableHeader, LinesGeneralHeader, ColumnsGeneralHeader)
#
#    def Set(self, TableHeader="", LinesGeneralHeader="", ColumnsGeneralHeader=""):
#        self.SetTableHeader(seTableHeader)
#        self.SetLinesGeneralHeader(LinesGeneralHeader)
#        self.SetColumnsGeneralHeader(ColumnsGeneralHeader)
#        
#    def SetTableHeader(self, val):
#        if isinstance(val, DataCell):
#            self.TableHeader=copy.deepcopy(val)
#        else:
#            self.TableHeader=DataCell(val)
#
#    def SetLinesGeneralHeader(self, val):
#        if isinstance(val, DataCell):
#            self.LinesGeneralHeader=copy.deepcopy(val)
#       else:
#            self.LinesGeneralHeader=DataCell(val)
#
#    def SetColumnsGeneralHeader(self, val):
#        if isinstance(val, DataCell):
#            self.ColumnsGeneralHeader=copy.deepcopy(val)
#        else:
#            self.ColumnsGeneralHeader=DataCell(val)
#    
#    #
#    def GetTableHeader(self):
#        return self.TableHeader
#
#    def GetLinesGeneralHeader(self, val):
#        return self.LinesGeneralHeader
#
#    def GetColumnsGeneralHeader(self, val):
#        return self.LinesGeneralHeader
#    #
#
#    def GetTableName(self):
#        return self.TableHeader.GetName()
#
#    def GetLinesGeneralName(self):
#        return self.LinesGeneralHeader.GetName()
#
#    def GetColumnsGeneralName(self):
#        return self.ColumnsGeneralHeader.GetName()
#
#    def GetLinesGeneralName_FieldName(self):
#        return self.LinesGeneralHeader.GetName(2-1)
#
#    def GetColumnsGeneralName_FieldName(self):
#        return self.ColumnsGeneralHeader.GetName(2-1)
#
#    def GetDBTableName(self):
#        return self.TableHeader.GetName(2-1)
#
#    def GetTable_DBGeneralName(self):
#        return self.TableHeader.GetName(3-1)
#
#    def GetTable_DBPath(self):
#        return self.TableHeader.GetName(4-1)
#
#    #
#    
#    def SetTableName(self, val):
#        self.TableHeader.SetName(val)
#
#    def SetLinesGeneralName(self, val):
#        self.LinesGeneralHeader.SetName(val)
#
#    def SetColumnsGeneralName(self, val):
#        self.ColumnsGeneralHeader.SetName(val)
#
#    def SetLinesGeneralName_FieldName(self, val):
#        self.LinesGeneralHeader.SetName(val, 2-1)
#
#    def SetColumnsGeneralName_FieldName(self, val):
#        self.ColumnsGeneralHeader.SetName(val, 2-1)
#
#    def SetDBTableName(self, val):
#        self.TableHeader.SetName(val, 2-1)
#
#    def SetTable_DBGeneralName(self, val):
#        self.TableHeader.SetName(val, 3-1)
#
#       def SetTable_DBPath(self, val):
#        self.TableHeader.SetName(val, 4-1)
#
#    def Transpose(self):
#        buf=copy.deepcopy(self.LinesGeneralHeader)
#        self.LinesGeneralHeader=copy.deepcopy(self.ColumnsGeneralHeader)
#        elf.ColumnsGeneralHeader=copy.deepcopy(buf)

             

class Table:
    def __init__(self, rows=[], RowsAreColumns0Lines1=1, LineOfColHeader=[], ColOfLineHeader=[], TableHeader=0, LinesGeneralHeader=0, ColumnsGeneraklHeader=0, InnerStruct_LC_not_CL_1_VV_0=0,): 
        self.content=[]
        #self.content=
        self.LineOfColHeader=[]
        self.ColOfLineHeader=[]
        self.TableHeader=DataCell()
        self.LinesGeneralHeader=DataCell()
        self.ColumnsGeneralHeader=DataCell()
        self.LC_not_CL=true
        self.Set(rows, RowsAreColumns0Lines1, LineOfColHeader, ColOfLineHeader, TableHeader, LinesGeneralHeader, ColumnsGeneraklHeader, InnerStruct_LC_not_CL_1_VV_0)

    def GetCell(self, LineN, ColN):
        cell=0
        if LineN==0 and ColN>0 and len(self.LineOfColHeader)>0:
            if ColN<len(self.LineOfColHeader):
                cell=self.LineOfColHeader[ColN-1]
        elif LineN>0 and ColN==0 and len(self.ColOfLineHeader)>0:
            if LineN<len(self.ColOfLineHeader):
                cell=self.ColOfLineHeader[LineN-1]
        elif LineN>0 and ColN>0:
            if(self.LC_not_CL):
                ExtRowN=LineN
                IneRowN=ColN
            else:
                IneRowN=LineN
                ExtRowN=ColN
            #if ExtRowN<=len(content):
            #    curRow=content[ExtRowN-1]
            #    if IneRowN<=len(curRow):
            #        cell=curRow[IneRowN-1]
            if ExtRowN>=1 and ExtRowN<=len(self.content) and IneRowN>=1 and IneRowN<=len(self.content[1-1]):
                cell=self.content[ExtRowN-1][IneRowN-1]
        return cell

    def SetCell(self, cellExt, LineN, ColN):
        #cell=copy.deepcopy(cellExt)
        if LineN==0 and ColN>0 and len(self.LineOfColHeader)>0:
            if ColN<len(self.LineOfColHeader):
                self.LineOfColHeader[ColN-1]=copy.deepcopy(cell)
        elif LineN>0 and ColN==0 and len(self.ColOfLineHeader)>0:
            if LineN<len(self.ColOfLineHeader):
                self.ColOfLineHeader[LineN-1]=copy.deepcopy(cell)
        elif LineN>0 and ColN>0:
            if(self.LC_not_CL):
                ExtRowN=LineN
                IneRowN=ColN
            else:
                IneRowN=LineN
                ExtRowN=ColN
            if ExtRowN>=1 and ExtRowN<=len(self.content) and IneRowN>=1 and IneRowN<=len(self.content[1-1]):
                self.content[ExtRowN-1][IneRowN-1]=copy.deepcopy(cellExt)

    def Set(self, rows, RowsAreColumns0Lines1, LineOfColHeader=[], ColOfLineHeader=[], TableHeader=0, LinesGeneralHeader=0, ColumnsGeneraklHeader=0, InnerStruct_LC_not_CL_1_VV_0=0): 
        QRows=len(rows)
        L=len(rows[1-1])
        LoCH_L=len(LineOfColHeader)
        CoLH_L=len(ColOfLineHeader)
        self.content=[]
        self.LineOfColHeader=[]
        self.ColOfLineHeader=[]
        #if InnerStruct_LC_not_CL_1_VV_0==RowsAreColumns0Lines1:
        #    if RowsAreColumns0Lines1==1:
        #        self.content=[]
        #        QRows=len(rows)
        #        for i in range(1, QRows+1):
        #            row=copy.deepcopy(rows[i-1])
        #            self.content.append(row)
        #    else:
        #        for i in range(1,L+1):
        #            row=[]
        #            for j in range(1,QRows+1):
        #                cur=copy.deepcopy(LineOfColHeader[i-1])
        #                row.append(cur)
        #            self.content.append(copy.deepcopy(row))
        #    if InnerStruct_LC_not_CL_1_VV_0==0:
        #        QLines=len(self.content)
        #        QColumns=len(self.content[1-1])
        #    else:
        #        QColumns=len(self.content)
        #        QLines=len(self.content[1-1])
        self.SetContent(rows, RowsAreColumns0Lines1, InnerStruct_LC_not_CL_1_VV_0)    
        #         
        if LoCH_L>0:
            if LoCH_L>QColumns:
                for i in range(1, QColumns+1):
                    cur=copy.deepcopy(LineOfColHeader[i-1])
                    self. LineOfColHeader.append(cur)
            elif LoCH_L<QColumns:
                for i in range(1, LoCH_L+1):
                    cur=copy.deepcopy(LineOfColHeader[i-1])
                    self.LineOfColHeader.append(cur)
                for i in range(LoCH_L+1, QColumns+1):
                    cur=DataCell()
                    self.LineOfColHeader.append(copy.deepcopy(cur))
            else:
                self.LineOfColHeader=copy.deepcopy(LineOfColHeader)
        #
        if CoLH_L>0:
            if CoLH_L>QLines:
                for i in range(1, QLines+1):
                    cur=copy.deepcopy(ColOfLineHeader[i-1])
                    self. ColOfLineHeader.append(cur)
            elif CoLH_L<QLines:
                for i in range(1, LoCH_L+1):
                    cur=copy.deepcopy(ColOfLineHeader[i-1])
                    self.ColOfLineHeader.append(cur)
                for i in range(LoCH_L+1, QLines+1):
                    cur=DataCell()
                    self.ColOfLineHeader.append(copy.deepcopy(cur))
            else:
                self.ColOfLineHeader=copy.deepcopy(ColOfLineHeader)
        #     
        if TableHeader!=0:
            if isinstance(TableHeader, DataCell):
                self.TableHeader=copy.deepcopy(TableHeader)
            elif isinstance(TableHeader, list) or isinstance(TableHeader, str):
                self.TableHeader=DataCell(TableHeader)
            else:
                self.TableHeader=0
        #
        if LinesGeneralHeader!=0:
            if isinstance(LinesGeneralHeader, DataCell):
                self.LinesGeneralHeader=copy.deepcopy(LinesGeneralHeader)
            elif isinstance(LinesGeneralHeader, list) or isinstance(LinesGeneralHeader, str):
                self.LinesGeneralHeader=DataCell(LinesGeneralHeader)
            else:
                self.LinesGeneralHeader=0
        #
        if ColumnsGeneralHeader!=0:
            if isinstance(ColumnsGeneralHeader, DataCell):
                self.ColumnsGeneralHeader=copy.deepcopy(ColumnsGeneralHeader)
            elif isinstance(ColumnsGeneralHeader, list) or isinstance(ColumnsGeneralHeader, str):
                self.ColumnsGeneralHeader=DataCell(ColumnsGeneralHeader)
            else:
                self.LinesGeneralHeader=0
        #
        self.LC_not_CL=InnerStruct_LC_not_CL_1_VV_0
        #if WriteInfoNo0Yes1==1:
        #     self.info=new TableInfo()
        #     self.info.QLines=QLines

    def GetQExtRows(self):
        return len(self.content)

    def GetQIneRows(self):
        QIneRows=0
        QExtRows=len(self.content)
        if QExtRows>0:
             QIneRows=len(self.content[1-1])
        return QIneRows

    def GetQLines(self):
        QIneRows=self.GetQIneRows()
        QExtRows=self.GetQExtRows()
        if self.self.LC_not_CL==1:
            QLines=QExtRows
        else:
            QLines=QIneRows
        return QLines

    def GetQColumns(self):
        QIneRows=self.GetQIneRows()
        QExtRows=self.GetQExtRows()
        if self.self.LC_not_CL==0:
            QColumns=QExtRows
        else:
            QColumns=QIneRows
        return QLines

    def GetLineHeaderCellN(self, LineN):
        cell=0
        Q=len(self.ColOfLineHeader)
        if Q>0 and LineN>=1 and LineN<=Q:
            cell=self.ColOfLineHeader[LineN-1]
        return cell

    def GetColumHeaderCellN(self, ColN):
        cell=0
        Q=len(self.LineOfColHeader)
        if Q>0 and ColN>=1 and ColN<=Q:
            cell=self.LineOfColHeader[ColN-1]
        return cell
            
    def SwapCells(self, LineN1, ColN1, LineN2, ColN2):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if LineN1>=1 and LineN1<=QLines and ColN1>=1 and ColN1<=QColumns and    LineN2>=1 and LineN2<=QLines and ColN2>=1 and ColN2<=QColumns:
            #cellBuf=self.GetCell(LineN2, ColN2)
            #self.SetCell(self.GetCell(LineN1, ColN1), LineN2, ColN2)
            #self.SetCell(cellBuf, LineN1, ColN1)
            #
            cell1=self.GetCell(LineN1, ColN1)
            cell2=self.GetCell(LineN2, ColN2)
            self.SetCell(cell1, LineN2, ColN2)
            self.SetCell(cell2, LineN1, ColN1)

    def SwapLines(self, Line1N, Line2N):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if Line1N>=1 and Line1N<=QLines and Line2N>=1 and Line2N<=QLines:
            for i in range(1, QColumns+1):
                self.SwapCells(Line1N, i, Line2N, i)

    def SwapColumns(self, Col1N, Col2N):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if Col1N>=1 and Col1N<=QColumns and Col2N>=1 and Col2N<=QColumns:
            for i in range(1, QLines+1):
                self.SwapCells(i, Col1N, i, Col2N)

    def SwapLineNWithHeaderLine(self, LineN):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if len(self.LineOfColHeader)>0 and LineN>=1 and LineN<=QLines:
            for i in range(1, QColumns+1):
                hdrCell=copy.deepcopy(self.LineOfColHeader[i-1])
                cntCell=GetCell(LineN, i)
                self.LineOfColHeader[i-1]=copy.deepcopy(cntCell)
                self.SetCel(hdrCell, LineN, i)

    def SwapColNWithHeaderLine(self, ColN):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if len(self.ColOfLineHeader)>0 and ColN>=1 and ColN<=QColumns:
            for i in range(1, QLines+1):
                hdrCell=copy.deepcopy(self.ColOfLineHeader[i-1])
                cntCell=GetCell(i, ColN)
                self.ColOfLineHeader[i-1]=copy.deepcopy(cntCell)
                self.SetCel(hdrCell, i, ColN)

    def OrderVisaVersaLines(self):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if(QLines%2==0):
            N=QLines
        else:
            N=QLines-1
        for i in range(1, N+1):
            N1=i
            N2=QLines+i-1
            self.SwapLines(N1, N2)

    def OrderVisaVersaColumns(self):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if(QLines%2==0):
            N=QColumns
        else:
            N=QColumns-1
        for i in range(1, N+1):
            N1=i
            N2=QColumns+i-1
            self.SwapColumns(N1, N2)

    def OrderVisaVersaLineN(self, N):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if N>=0 and N<=QColumns:
            if(QColumns%2==0):
                N=QColumns
            else:
                N=QColumns-1
            for i in range(1, N+1):
                N1=i
                N2=QColumns+i-1
                self.SwapCells(N, N1, N, N2)

    def OrderVisaVersaColumnN(self, N):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if N>=0 and N<=QColumns:
            if(QLines%2==0):
                N=QLines
            else:
                N=QLines-1
            for i in range(1, N+1):
                N1=i
                N2=QLines+i-1
                self.SwapCells(N1, N, N2, N)

    def OrderVisaVersaHeaderLine(self):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if len(self.LineOfColHeader)>0:
            if(QColumns%2==0):
                N=QColumns
            else:
                N=QColumns-1
        for i in range(1, N+1):
            N1=i
            N2=QColumns+i-1
            cell1=copy.deepcopy(self.LineOfColHeader[N1-1])
            cell2=copy.deepcopy(self.LineOfColHeader[N2-1])
            self.LineOfColHeader[N1-1]=copy.deepcopy(cell2)
            self.LineOfColHeader[N2-1]=copy.deepcopy(cell1)

    def OrderVisaVersaHeaderColumn(self):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if len(self.ColOfLineHeader)>0:
            if(QColumns%2==0):
                N=QLines
            else:
                N=QLines-1
        for i in range(1, N+1):
            N1=i
            N2=QLines+i-1
            cell1=copy.deepcopy(self.ColOfLineHeader[N1-1])
            cell2=copy.deepcopy(self.ColOfLineHeader[N2-1])
            self.ColOfLineHeader[N1-1]=copy.deepcopy(cell2)
            self.ColOfLineHeader[N2-1]=copy.deepcopy(cell1)

    def AddLine(self, row):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if self.LC_not_CL==1:
            self.content.append(row)
        else:
            for i in range(1, QColumns+1):
                self.content[i-1].append(row[i-1])

    def AddColumn(self, row):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if self.LC_not_CL==1:
            for i in range(1, QLines+1):
                self.content[i-1].append(row[i-1])
        else:
            self.content.append(row)

    def InsLineN(self, row, N):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        content=[]
        if self.LC_not_CL==1:
            for i in range(1, N-1+1):
                CurLine=self.GetLine(i)
                content.append(CurLine)
            content.append(row)#into Nth pos
            for i in range(N, QLines+1):
                CurLine=self.GetLine(i)
                content.append(CurLine)
        else:
            for i in range(1, QColumns+1):
                CurRow=[]
                for j in range(1, N-1+1):
                    cell=self.GetCell(j, i)
                    CurRow.append(copy.deepcopy(cell))
                for j in range(1, N-1+1):
                    cell=row[j-1]
                    CurRow.append(copy.deepcopy(cell))
                for j in range(N, QLines+1):
                    cell=self.GetCell(j, i)
                    CurRow.append(copy.deepcopy(cell))
                content.append(CurRow)

    def InsColumnN(self, row, N):
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        content=[]
        if self.LC_not_CL==0:
            for i in range(1, N-1+1):
                CurCol=self.GetColumn(i)
                content.append(CurCol)
            content.append(row)#into Nth pos
            for i in range(N, QLines+1):
                CurCol=self.GetColumn(i)
                content.append(CurCol)
        else:
            for i in range(1, QLines+1):
                CurRow=[]
                for j in range(1, N-1+1):
                    cell=self.GetCell(j, i)
                    CurRow.append(copy.deepcopy(cell))
                for j in range(1, N-1+1):
                    cell=row[j-1]
                    CurRow.append(copy.deepcopy(cell))
                for j in range(N, QColumns+1):
                    cell=self.GetCell(j, i)
                    CurRow.append(copy.deepcopy(cell))
                content.append(CurRow)
                

    def Transpose(self):
        content=[]
        #QExtRows=self.GetQExtRows()
        #QIneRows=self.GetQIneRows()
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        #for i in range(1, QIneRows+1):
        #for i in range(1, QIneRows+1):  
            #for i in range(1, QIneRows+1):
            #CurExtRow=[]
            #for j in range(1, QExtRows+1):
                #cell=
        for i in range(1, QColumns+1):  
            CurExtRow=[]
            for j in range(1, QLines+1):
                cell=GetCell(j, i)
                CurExtRow.append(copy.deepcopy(cell))
            content.append(copy.deepcopy(CurExtRow))
        self.content=content
        #
        buf=self.LineOfColHeader
        self.LineOfColHeader=self.ColOfLineHeader
        self.ColOfLineHeader=buf
            
        
    def GetLineN(self, LineN):
        row=DataCellRow()
        QLines=self.GetQLines()
        if LineN>=0 and LineN<=QLines:
             if LineN==0 and len(self.LineOfColHeader)>0:
                 for i in range(1, QLines+1):
                     #cell=GetCell(LineN, i)#also abl
                     cell=self.LineOfColHeader[i-1]
                     row.Add(cell)
             else:
                 for i in range(1, QLines+1):
                     cell=GetCell(LineN, i)
                     row.Add(cell)
        return row

    def GetColumnN(self, ColN):
        row=DataCellRow()
        QColumns=self.GetQColumns()
        if ColN>=0 and ColN<=QColumns:
             if ColN==0 and len(self.ColOfLineHeader)>0:
                 for i in range(1, QLines+1):
                     #cell=GetCell(LineN, i)#also abl
                     cell=self.ColOfLineHeader[i-1]
                     row.Add(cell)
             else:
                 for i in range(1, QColumns+1):
                     cell=GetCell(ColN, i)
                     row.Add(cell)
        return row

    # RowsAreColumns0Lines1 InnerStruct_LC_not_CL_1_VV_0=0
    def SetContent(rows, LinesNotCols=1, LC_not_CL=1):
        if isinstance(rows, list) and len(rows)>0 and len(rows[1-1])>0:
            self.LC_not_CL=LC_not_CL
            self.content=[]
            if LinesNotCols==LC_not_CL:
                for row in rows:
                    self.content.Append(row)
            else:
                #QIneRows=(MyLibPy2.DefExtrRowLensIn2DArr(rows))[2-1]
                QIneRows=0
                QExtRows=len(rows)
                QIneRows=len(rows[1-1])
                for i in range(1, QIneRows+1):
                    CurExtRow=[]
                    for j in range(1, QExtRows+1):
                        cell=row[j-1][i-1]
                        CurExtRow.append(cell)
                    self.content.append(CurExtRow)


    def ToString(self, LineN, ColN):
        R=""
        cell=self.GetCell(LineN, ColN)
        if isinstance(cell, DataCell):
            R=cell.ToString()
        return R

    def CornerToString(self):
        s=""
        s=s+str(self.LinesGeneralHeader.GetName())
        if self.LinesGeneralHeader.GetName()!="" and self.ColumnsGeneralHeader.GetName()!="":
             s=s+"\\"
        s=s+str(self.ColumnsGeneralHeader.GetName())
        return s

    def HeaderLineToString(self, sep_hdr=" ", sep_row=" "):
        s=self.CornerToString()
        s=s+sep_hdr
        QColumns=self.GetQColumns()
        for i in range(1, QColumns-1+1):
            cell=GetColumHeaderCellN(i)
            s=s+cell.ToString()
            s=s+sep_row
        if QColumns>0:
            cell=GetColumHeaderCellN(QColumns)
            s=s+cell.ToString()
        return s

    def LineToString(self, LineN, sep_hdr=" ", sep_row=" "):
        s=""
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if LineN==0:
            s=HeaderLineToString(sep_hdr, sep_row)
        elif LineN<=QLines:
            cell=GetLineHeaderCellN(self, LineN)
            s=cell.ToString()
            if s!="":
                s=s+sep_hdr
            if QColumns>0:
                for i in range(1, QColumns-1+1):
                    cell=self.GetCell(LineN, i)
                    s=s+sell.ToString()
                cell=self.GetCell(LineN, QColumns)
                s=s+sell.ToString()
        return s
                        
                        
class Table1:
    def __init__(self, content=[], LineOfColHeader=[], ColOfLineHeader=[], Headers=0, C_not_CL=1):
        self.Set(content, LineOfColHeader, ColOfLineHeader, TableHeader, LinesGeneralHeader, ColumnsGeneralHeader, LC_not_CL)

    def Set(self, content=[], LineOfColHeader=[], ColOfLineHeader=[], TableHeader="", LinesGeneralHeader="", ColumnsGeneralHeader="", LC_not_CL=1):
        SetContent(content)
        #
        SetLineOfColHeader(LineOfColHeader)
        SetColOfLineHeader(ColOfLineHeader)
        if TableHeader==""and LinesGeneralHeader==""and ColumnsGeneralHeader=="":
            self.Headers=0
        else:
            self.Headers=TableHeaders(TableHeader, LinesGeneralHeader, ColumnsGeneralHeader)
        self.LC_not_CL=LC_not_CL

    def SetContent(self, content):
        if isinstance(content, My2DArray1):
           self.content=copy.deepcopy(content)
        else:
            self.content=My2DArray1()
            self.content=Set(content)
    
    def SetLineOfColHeader(self, LineOfColHeader):
        if isinstance(LineOfColHeader, My1DArray):
            self.LineOfColHeader=copy.deepcopy(LineOfColHeader)
        else:
            self.LineOfColHeader=My1DArray()
            self.LineOfColHeader.Set(LineOfColHeader)
    
    def SetColOfLineHeader(self, ColOfLineHeader):
        if isinstance(ColOfLineHeader, My1DArray):
            self.ColOfLineHeader=copy.deepcopy(ColOfLineHeader)
        else:
            self.ColOfLineHeader=My1DArray()
            self.ColOfLineHeader.Set(ColOfLineHeader)

    def SetTableHeaders(self, TableHeader="", LinesGeneralHeader="", ColumnsGeneralHeader=""):
        self.TableHeader=TableHeader(TableHeader, LinesGeneralHeader, ColumnsGeneralHeader)

    def SetTableHeader(self, TableHeader):
        self.Headers.SetTableHeader(TableHeader)

    def SetLinesGeneralHeader(self, LinesGeneralHeader):
        self.Headers.SetLinesGeneralHeader(LinesGeneralHeader)

    def SetLinesGeneralHeader(self, ColumnsGeneralHeader):
        self.Headers.SetColumnsGeneralHeader(ColumnsGeneralHeader)

    def GetContent(self):
        return self.content

    def GetContentAsList(self):
        return content.data

    def GetLineOfColHeader(self):
        return self.LineOfColHeader

    def GetLineOfColHeaderAsList(self):
        return self.LineOfColHeader.row

    def GetColOfLineHeader(self):
        return self.ColOfLineHeader

    def GetColOfLineHeaderAsList(self):
        return self.ColOfLineHeader.row

    def GetTableHeaders(self):
        return self.Headers

    def GetIf_LC_not_CL(self):
        return self.LC_not_CL

    def GetCell_LineOfColHeader(self, N):
        L=0
        cell=0
        if isinstance(self.LineOfColHeader, My1DArray):
            L=self.LineOfColHeader.GetLength()
            if L>0:
                cell=self.LineOfColHeader.GetElement(N)
        elif ((isinstance(self.LineOfColHeader, list)) and (len(self.LineOfColHeader)>=N)):
            cell=self.LineOfColHeader[N-1]    
        return cell

    def GetCell_ColOfLineHeader(self, N):
        L=0
        cell=0
        if isinstance(self.ColOfLineHeader, My1DArray):
            L=self.ColOfLineHeader.GetLength()
            if L>0:
                cell=self.ColOfLineHeader.GetElement(N)
        elif ((isinstance(self.ColOfLineHeader, list)) and (len(self.ColOfLineHeader)>=N)):
            cell=self.LineOfColHeader[N-1]           
        return cell

    def GetContentElement(self, ExtRowN, IneRowN):
        R=0
        if ExtRowN>=1 and IneRowN>=1:
            if isinstance(self.content, My2DArray) and ExtRowN<=self.content.GetLength() and IneRowN<=self.content.GetLengthOfInnerRow(ExtRowN):
                R=self.content.GetElement(ExtRowN, IneRowN)
            elif isinstance(self.content, list) and ExtRowN<=len(self.content) and IneRowN<=len(self.content[ExtRowN-1]):
                R=self.content[ExtRowN-1][IneRowN-1]
        return R
            
    def GetCell(self, LineN, ColN):
        cell=0
        if(LineN==0 and ColN>0):
            cell=self.GetCell_LineOfColHeader(ColN)
        elif(LineN>=0 and ColN==0):
            cell=self.GetCell_ColOfLineHeader(LineN)
        else:
            if self.LC_not_CL==1:
                ExtRowN =LineN
                IneRowN=ColN
            else:
                ExtRowN =ColN
                IneRowN=LineN
            cell=self.GetContentElement(ExtRowN, IneRowN)
        return cell
    
    def SetCell_LineOfColHeader(self, valExt, N, ExistingVal_Allowed0Forbidden1=0):
        #if(not(isinatance(self.LineOfColHeader, My1DArray))):
        #    self.LineOfColHeader=My1DArray()
        val=copy.deepcopy(valExt)
        cell=DataCell(val)
        if isinstance(self.LineOfColHeader, My1DArray):
            self.LineOfColHeader.SetElement(cell, N, ExistingVal_Allowed0Forbidden1)
        elif (isinstance(self.LineOfColHeader, list) and len(self.LineOfColHeader)>=N):
            self.LineOfColHeader[N-1]=cell
       
    def SetCell_ColOfLineHeader(self, val, N):
        if(not(isinatance(self.ColOfLineHeader, My1DArray))):
           self.ColOfLineHeader=My1DArray()
           
    def SetContentElement(self, cellExt, ExtRowN=1, IneRowN=1):
        if ExtRowN>=1 and IneRowN>=1:
            if isinstance(self.content, My2DArray):
                if ExtRowN<=self.content.GetLength() and IneRowN<=len(self.content[ExtRowN-1]):
                    self.content.SetElement(ExtRowN, IneRowN)
                #else NOP, add rows, not sngl element
            elif isinstance(self.content, list):
                if ExtRowN<=len(self.content) and IneRowN<=len(self.content[ExtRowN-1]):
                    elf.content[ExtRowN-1][IneRowN-1]=copy.deepcopy(cellExt)
                #else NOP, add rows, not sngl element

    def SetCell(self, cellExt, LineN, ColN):
        cell=copy.deepcopy(cellExt)
        if(LineN==0 and ColN>0):
            cell=self.SetCell_LineOfColHeader(cell, ColN)
        elif(LineN>=0 and ColN==0):
            cell=self.SetCell_ColOfLineHeader(cell, LineN)
        else:
            if self.LC_not_CL==1:
                ExtRowN =LineN
                IneRowN=ColN
            else:
                ExtRowN =ColN
                IneRowN=LineN
            #self.content.SetElement(cell, ExtRowN, IneRowN)
            self.SetContentElement(cell, ExtRowN, IneRowN)
    #
    
    def GetQExtRows(self):
        return self.content.GetLength()

    def GetQIneRows(self):
        return self.content.GetLengthOfInnerRow()

    def GetQLines(self):
        QIneRows=self.GetQIneRows()
        QExtRows=self.GetQExtRows()
        if self.self.LC_not_CL==1:
            QLines=QExtRows
        else:
            QLines=QIneRows
        return QLines

    def GetQColumns(self):
        QIneRows=self.GetQIneRows()
        QExtRows=self.GetQExtRows()
        if self.self.LC_not_CL==0:
            QColumns=QExtRows
        else:
            QColumns=QIneRows
        return QLines   
    #
    #def GetMinLength(self):#ne test'd
    #    LE=len(self.row)
    #    Lmin=0
    #    for i in range(1, L+1):
    #       LI=len(self.row[i-1])
    #       if i==1 or (i>1 and LI<Lmin):
    #           Lmin=LI
    #    return Lmin
    #
    #def GetMaxLength(self):#ne test'd
    #   LE=len(self.row)
    #   Lmax=0
    #   for i in range(1, L+1):
    #     LI=len(self.row[i-1])
    #     if i==1 or (i>1 and LI>Lmax):
    #         Lmax=LI
    #  return Lmax
    #

    def GetExtRow(self, N):
        row=My1DArray()
        Q=self.content.GetLength()
        if(N>1 and N<=Q):
            cell=self.content

    #

    def SetExtRow(self, rowExt, N, RowHeaderExt=0, Preserve_WholeRect0_NewRowLen1=0):
        if N>=1:
            
            #
            if isinstance(self.content, My2DArray):
                if N<=self.content.GetSize():
                    self.content.SetExtRow(row, N, Preserve_WholeRect0_NewRowLen1)
                #else NOP, add row first
            elif isinstance(self.content, list):
                if N<=self.content.GetSize():
                    LOld=len(self.content[N-1])
                    LNew=len(row)
                    if LOld<=LNew:
                        LMin=LOld
                    else:
                        LMin=LNew
                    if len(row)==len(self.content[N-1]):
                        for i in range(1, LOld+1):
                            cell=copy.deepcopy(rowExt[i-1])
                            self.content[N-1][i-1]=copy.deepcopy(cell)
                    else:
                        L=len(self.content)
                        content=[]
                        for i in range(1, N-1+1):
                            row=copy.deepcopy(self.content[i-1])
                            content.append(row)
                        if Preserve_WholeRect0_NewRowLen1==1:
                            content.append(copy.deepcopy(rowExt))
                        else:
                            row=[]
                            for i in range(1, LMin+1):
                                cell=copy.depcopy(rowExt[i-1])
                                row.append(cell)
                            if LMin==LNew:
                                for i in range(LMin+1, LNew+1):
                                    cell=copy.depcopy(rowExt[i-1])
                                    row.append(cell)
                            else:
                                for i in range(LMin+1, LNew+1):
                                    cell=DataCell()
                                    row.append(cell)
                        for i in range(N+1, L+1):
                            row=copy.deepcopy(self.content[i-1])
                            content.append(row)
                        self.content=content
                        
    def AddExtRow(self, rowExt, RowHeaderExt=0, Preserve_WholeRect0_NewRowLen1=0):
        if isinstance(self.content, My2DArray):
            self.content.AddExtRow(row, Preserve_WholeRect0_NewRowLen1)
        elif isinstance(self.content, list):
            L=len(self.content)
            if L==0:
                self.content.append(copy.deepcopy(rowExt))
            else:
                LOld=len(self.content[L-1])
                cell=DataCell()
                for i in range(1, LOld+1):
                    rowErst.append(cell)
                self.content.append(rowErst)
                self.SetExtRow(rowExt, N, RowHeaderExt, Preserve_WholeRect0_NewRowLen1)
     
    def AddIneRow(self, rowExt, LineHeaderExt=0, Preserve_WholeRect0_NewRowLen1=0):
        if isinstance(self.content, My2DArray):
            self.content.AddIneRow(row)
        elif isinstance(self.content, list):
            rowFirst=[]
            L=len(self.content)
            if L==0:
                for i in range(1, len(row)+1):
                    rowFirst=[]
                    cell=copy.deepcopy(rowExt[i-1])
                    rowFirst.append(cell)
                    self.content.append(rowFirst)
            else:
                LOld=len(self.content[L-1])
                LNew=len(rowExt)
                if LOld<=LNew:#<=
                    for i in range(1, LOld+1):
                        cell=copy.deepcopy(rowExt[i-1])
                        self.content[i-1].append(cell)
                else:#LOld>LNew
                    for i in range(1, LNew+1):
                        cell=copy.deepcopy(rowExt[i-1])
                        self.content[i-1].append(cell)
                    if Preserve_WholeRect0_NewRowLen1==1:
                        cell=DataCell()
                        for i in range(LNew+1, LOld+1):
                            self.content[i-1].append(copy.deepcopy(cell))
                        
    def InsExtRow(self, N, rowExt, RowHeaderExt=0, Preserve_WholeRect0_NewRowLen1=0):                    
        if N>=1:
            if isinstance(self.ColOfLineHeader,My1DArray) and self.ColOfLineHeader.GetLength()>=N:
                ExistingVal_Allowed0Forbidden1=1
                #self.ColOfLineHeader.Add(self, elementExt, ExistingVal_Allowed0Forbidden1)
            #
            if isinstance(self.content, My2DArray) and N<=self.content.GetLength():
                self.content.InsExtRow(self, rowExt, N, Preserve_WholeRect0_NewRowLen1, 0)
            elif isinstance(self.content, list) and N<=len(self.content):
                content=[]
                L=len(self.content)
                for i in range(1, N-1+1):
                    row=copy.deepcopy(self.content[i-1])
                    content.append(row)
                    #content.append(copy.deepcopy(self.content[i-1]))
                #Inserting ext row. 
                if len(self.content[N-1])==len(rowExt) or Preserve_WholeRect0_NewRowLen1==1:
                    row=copy.deepcopy(rowExt)
                    content.append(row)
                    #content.append(copy.deepcopy(rowExt)
                else:
                    LOld=len(self.content[L-1])
                    LNew=len(rowExt)
                    if LOld<=LNew:
                        LMin=LOld
                    else:
                        LMin=LNew
                    row=[]
                    for i in range(1, LMin+1):
                        cell=copy.deepcopy(rowExt[i-1])
                        row.append.cell
                    if LNew<LOld:
                        cell=DataCell()
                        for i in range(LMin+1, LOld):
                            cell=copy.deepcopy(rowExt[i-1])
                            row.append(cell)
                    else:
                        for i in range(LMin+1, LOld):
                            cell=copy.deepcopy(rowExt[i-1])
                            row.append(cell)
                #
                for i in range(N, L+1):
                    content.append(copy.deepcopy(self.content[i-1]))
                self.content=content

    def InsExtRow(self, N, rowExt, RowHeaderExt=0, Preserve_WholeRect0_NewRowLen1=0):                    
        if N>=1:

            #
            if isinstance(self.content, My2DArray) and N<=self.content.GetLength():
                self.content.InsExtRow(self, rowExt, N, Preserve_WholeRect0_NewRowLen1, 0)
            elif isinstance(self.content, list) and N<=len(self.content):
                content=[]

    #
        
    def GetTableHeader(self):
        R=""
        if isinstance(self.Headers, TableHeaders):
            R=self.Headers.TableHeader
        return R

    def GetLinesGeneralHeader(self):
        R=""
        if isinstance(self.Headers, TableHeaders):
            R=self.Headers.LinesGeneralHeader
        return R

    def GetColumnsGeneralHeader(self):
        R=""
        if isinstance(self.Headers, TableHeaders):
            R=self.Headers.ColumnsGeneralHeader
        return R

    
    def SetTableHeader(self, TableHeader):
        if isinstance(self.Headers, TableHeaders):
            self.Headers.Set
        return R

    def GetLinesGeneralHeader(self):
        R=""
        if isinstance(self.Headers, TableHeaders):
            R=self.Headers.LinesGeneralHeader
        return R

    def GetColumnsGeneralHeader(self):
        R=""
        if isinstance(self.Headers, TableHeaders):
            R=self.Headers.ColumnsGeneralHeader
        return R

    #

    def ToString_LineOfColHeaderCell(self, ColN):
        cell=self.GetLineOfColHeaderCellN(ColN)
        s=cell.ToString()
        return s

    def ToString_ColOfLineHeaderCell(self, LineN):
        cell=self.GetColOfLineHeaderCellN(LineN)
        s=cell.ToString()
        return s
    
    def ToString_Cell(self, LineN, ColN):
        s=""
        if(LineN==0 and ColN>0):
            s=ToString_LineOfColHeaderCell(ColN)
        elif(LineN>0 and ColN==0):
            s=ToString_ColOfLineHeaderCell(LineN)
        else:
            cell=self.GetCell(LineN, ColN)
            s=cell.ToString()
        return s

    def ToString_Corner(self):
        s=""
        if isinstance(self.Headers, TableHeaders):
            LinesGeneralName=self.Headers.GetTableName()
            sLoCH=self.Headers.GetLinesGeneralName()
            sCoLH=self.Headers.GetColumnsGeneralName()
            if sCoLH!="" and sLoCH!="":
                s=sLoCH+"\\"+sCoLH
            else:
                s=s+sLoCH+sCoLH
        return s

    def ToString_LineOfColHeader(self, SepRow="; "):#SepHdr=": ", SepRow="; "):
        s=""
        sc=""
        #sHdr=self.ToString_Corner()
        #s=s+sHdr
        #if s!="":
        #    s=s+SepHdr
        if isinstance (self.LineOfColHeader, My1DArray):
            Q=self.LineOfColHeader.GetLength()
            for i in range(1, Q-1+1):
                cell=GetCell_LineOfColHeader(i)
                sc=cell.ToString()
                s=s+sc
                s=s+SepRow
            if Q>0:
                cell=GetCell_LineOfColHeader(i)
                sc=cell.ToString()
                s=s+sc
        elif isinstance(self.LineOfColHeader, list):
            Q=len(self.LineOfColHeader)
            for i in range(1, Q-1+1):
                cell=LineOfColHeader[i-1]
                sc=cell.ToString()
                s=s+sc
                s=s+SepRow
            if Q>0:
                cell=LineOfColHeader[Q-1]
                sc=cell.ToString()
                s=s+sc
        return s

    #def ToString_ColOfLineHeader(self, SepRow="; "):#SepHdr=": ", SepRow="; "):
    #    s=""
    #    sc=""
    #    #sHdr=self.ToString_Corner()
    #    #s=s+sHdr
    #    #if s!="":
    #    #    s=s+SepHdr
    #    if(isinstance self.ColOfLineHeader, My1DArray):
    #        Q=self.ColOfLineHeader.GetLength()
    #        for i in range(1, Q-1+1):
    #            cell=GetCell_ColOfLine(i)
    #            sc=cell.ToString()
    #            s=s+sc
    #            s=s+SepRow
    #        if Q>0:
    #            cell=ColOfLineHeader(i)
    #            sc=cell.ToString()
    #            s=s+sc
    #    elif isinstance(self.ColOfLineHeader, list):
    #        Q=len(self.LineOfColHeader)
    #        for i in range(1, Q-1+1):
    #            cell=ColOfLineHeader[i-1]
    #            sc=cell.ToString()
    #            s=s+sc
    #            s=s+SepRow
    #        if Q>0:
    #            cell=ColOfLineHeader[Q-1]
    #            sc=cell.ToString()
    #            s=s+sc
    #    return s
        
    def ToString_Line(self, N=1, SepRow="; "):
        s=""
        QLines=self.GetQLines()
        QColumns=self.GetQColumns()
        if N==0:
            s=ToString_LineOfColHeader(SepRow)
        elif N>=1 and N<=QLines and QColumns>0:
            if(QColumns>1):
                for i in range(1,QColumns-1+1):
                    cell=self.GetCell(N, i)
                    s=s+cell.ToString()
                    s=s+SepRow
                cell=self.GetCell(N, QColumns)
                s=s+cell.ToString()
            else:
                cell=self.GetCell(N, 1)
                s=s+cell.ToString()
        return s

    def ToString_LineOfColHeader_WithCorner(self, SepRow="; ", SepHdr=": "):
        s=""
        s=s+self.ToString_Corner()
        if s!="":
            s=s+SepHdr
        s=s+ToString_LineOfColHeader(SepRow)
        return s

    def ToString_Line_WithHeader(self, LineN=1, SepRow="; ", SepHdr=": "):
        s=""
        s=s+self.ToString_ColOfLineHeaderCell(LineN)
        if s!="":
            s=s+SepHdr
        s=s+ToString_Line(LineN, SepRow)
        return s

    def ShowConsole(self, SepRow="; ", SepHdr=": "):
        QLines=self.GetQLines()
        print(self.GetTableName())
        print(self.ToString_LineOfColHeader_WithCorner(SepRow, SepHdr))
        for i in range(1, QLines+1):
            print(self.ToString_Line_WithHeader(self, LineN, SepRow, SepHdr))

    #

    def Transpose(self):
        buf=copy.deepcopy(self.LineOfColHeader)
        self.LineOfColHeader=copy.deepcopy(self.ColOfLineHeader)
        self.ColOfLineHeader=copy.deepcopy(buf)
        #
        if isinstance(self.Headers, TableHeaders):
            self.Headers.Transpose()
        #
        if isinstance(self.content, My2DArray):
            self.content.Transpose()
        
#--------------------------------------------------------------------------------------------

class DataCellRow1:
    def __init__(self, row=[]): #1, #My1DArray-#1
        self.row=My1DArray()
        self.Set(row)
    #
    # funstions from My1DArray
    #
    def GetLength(self): #My1DArray-#18
        return self.row.GetLength()
    
    def SetCell(self, N, data): #3, #My1DArray-#5
        if N>=1 and N<=self.GetLength():
            cell=DataCell(val)
            self.row[N-1]=copy.deepcopy(cell)

    def Set(self, row): #My1DArray-#2 #seems #3 no need
        L=0
        self.row.Clear()
        if isinstance(row, DataCellRow1):
            L=row.GetLength()
            for i in range(1, L+1):
                cell=copy.deepcopy(row.GelCell(i))
                self.row.Add(cell)
        elif isinstance(row, My1DArray):
            L=row.GetLength()
            for i in range(1, L+1):                       
                val=copy.deepcopy(row.GetElement(i))
                cell=DataCell(val)
                self.row.Add(cell)
        elif isinstance(row, list):
            L=len(row)#var1, var3, var2, var4 ? what is this?
            for i in range(1, L+1):                       
                cell=DataCell(row[i-1])
                self.row.Add(cell)

    def GetCellN_AsLink(self, N): #->My1DArray-#25
        R=0
        L=self.GetLength()
        if N>=1 and N<=L:
            R=self.row.GetElement_AsLink(N)
        return R

    def GetCellN_AsCopy(self, N): #->My1DArray-#26
        R=0
        L=self.GetLength()
        if N>=1 and N<=L:
            R=self.row.GetElement_AsCopy(N)
        return R

    def GetCellN(self, N, Link0Copy1=0): #->My1DArray-#4
        R=0
        L=self.GetLength()
        if N>=1 and N<=L:
            R=self.row.GetElement(N, )
        return R

    def SetCellN(self, N, data):#->My1DArray-#5
        if N>=1 and N<=MaxInt:
            if isinstance(data, DataCell):
                self.row[N-1]=copy.deepcopy(data)
            elif isinstance(data, list) and len(data)==4:
                val1=data[1-1]
                val2=data[2-1]
                val3=data[3-1]
                val4=data[4-1]
                self.row[N-1].Set(val1,val2, val3, val4)
            else:
                self.row[N-1].Set(data)
                
    def Add(self, cellExt, ExistingVal_Allowed0Forbidden1=0): #->My1DArray-#6
        if isinstance(cellExt, DataCell):
            cell=copy.deepcopy(cellExt)
        else:
            cell=DataCell()
            cell.Set(cellExt)
        self.row.Add(cell, ExistingVal_Allowed0Forbidden1)

    def Ins(self, N, cellExt, ExistingVal_Allowed0Forbidden1=0): #My1DArray-#7,8
        L=self.GetLength()
        if N>=1 and N<=L:
            if isinstance(cellExt, DataCell):
                cell=copy.deepcopy(cellExt)
            else:
                cell=DataCell()
                cell.Set(cellExt)
        self.row.Ins(cell, N, ExistingVal_Allowed0Forbidden1)

    def Del(self, N): #->My1DArray-#9
        self.row.Del(N)

    def Clear(self): #->My1DArray-#10
        self.row.Clear()
    #
    #
    def SeekFirst(self, val, FromN=1):#copied et mod'd, ob "=" for cells is special #->My1DArray-#11
        N=0
        Q=len(self.row)
        ToN=0
        if ToN<1 or ToN>Q:
           ToN=Q
        count=0
        #for i in range(FromN,ToN):
        for i in range(FromN,ToN+1):
            if self.row[i-1]==val:
                count=count+1
                if count==1:
                    N=i+1
                    N=i
        return N
    #
    def SeekLast(self, val, ToN=0): #copied et mod'd, ob "=" for cells is special #->My1DArray-#12
        N=0
        Q=len(self.row)
        count=0
        FromN=1
        if ToN<1 or ToN>Q:
            ToN=Q
        #for i in range(FromN,ToN):
        for i in range(FromN,ToN+1):
            if self.row[i-1]==val:
                N=i+1
                N=i
        return N
    #
    def Seek(self, val, NLim=0, FirstNotLast=1): #copied et mod'd, ob "=" for cells is special #->My1DArray-#13
        N=0
        Q=len(self.row)
        #
        if FirstNotLast==1:
            FromN=NLim
            ToN=0
        else:
            FromN=1
            ToN=NLim
        #
        if FromN<1 or FromN>Q:
            FromN=1
        if ToN<1 or ToN>Q:
            ToN=Q
        if FirstNotLast==1:
            N=self.SeekFirst(val, FromN)
        else:
            N=self.SeekLast(val, TomN)
        #
        return N
    #
    def DelFirstElement(self, val):  #->My1DArray-#14
        if isinstance(cellExt, DataCell):
            cell=copy.deepcopy(cellExt)
        else:
            cell=DataCell()
            cell.Set(cellExt)
        self.row.DelFirstElement(cell)
    #
    def DelLastElement(self, val):  #->My1DArray-#15
        if isinstance(cellExt, DataCell):
            cell=copy.deepcopy(cellExt)
        else:
            cell=DataCell()
            cell.Set(cellExt)
        self.row.DelLastElement(cell)
    #
    def Swap(self, N1, N2): #->My1DArray-#15
        self.row.Swap(N1, N2)

    def Reverse(self): #My1DArray-17
        self.Reverse()
    #My1DArray-18 - above
    def SetLength(self, L, DefaultVal=0): #My1DArray-19
        DefaultCell=DataCell(DefaultVal)
        self.row.SetLength(L, DefaultCell)

    def GetSubRow(self, N1, N2):  #My1DArray-20
        self.row.GetSubRow(N1, N2) 
                                     
    def ToString_Element(self, N, sBef="", sAft=""): #21
        R=""
        if N>=1 and N<=self.GetLength():
            cell=self.GetCell(N)
            R=sBef+cell.ToString()+sAft
        return R

    def ToString_Element_Info(self, N): #22
        sInf="Element "+str(N)+" doesn't exist "
        if N>=1 and N<=self.GetLength():
            sInf="(DataCell TypeN="+str(self.GetTypeN())+" id="+id(self)+" val="+str(self.GetVal())+") "
        return sInf
    #
    #Functions of DataCell
    #
    def Set_Simple(self, N, var1, ExistingVal_Allowed0Forbidden1=0): #1-11-1
        Q=self.GetLength()
        if N>=1 and N<=Q:
            #self.row[N-1]=DataCell_Simple()
            #self.row[N-1].Set(var1)
            cell=DataCell_Simple(var1)
            #cell.Set(var1)
            self.row.SetElement(cell, N, ExistingVal_Allowed0Forbidden1) 
    def Set_ComboboxOrMemo(self, N, var1, var2):  #1-11-2
        Q=self.GetLength()
        if N>=1 and N<=Q:
            #self.row[N-1]=DataCell_ComboboxOrMemo()
            #self.row[N-1].Set(var1, var2)
            cell=DataCell_ComboboxOrMemo(var1, var2)
            #cell.Set(var1, var2)
            self.row.SetElement(cell, N, ExistingVal_Allowed0Forbidden1)
    def Set_DBTableHeader(self, N, var1, var2, var3, ExistingVal_Allowed0Forbidden1=0):  #1-11-3
        Q=self.GetLength()
        if N>=1 and N<=Q:
            #self.row[N-1]=DataCell_DBTableHeader()
            #self.row[N-1].Set(var1, var2, var3)
            cell=DataCell_DBTableHeader(var1, var2, var3)
            #cell.Set(var1, var2, var3)
            self.row.SetElement(cell, N, ExistingVal_Allowed0Forbidden1)
    def Set_ColHdr_DBFldOrItems(self, N, var1, var2=[], var3=[], var4=[], ExistingVal_Allowed0Forbidden1=0):  #1-11-3
        Q=self.GetLength()
        if N>=1 and N<=Q:
            #self.row[N-1]=DataCell_ColHeader_DBFieldOrItems()
            #self.row[N-1].Set(var1, var2, var3)
            cell=DataCell_ColHeader_DBFieldOrItems(var1, var2, var3, var4)
            #cell.Set(var1, var2, var3, var4)
            self.row.SetElement(cell, N, ExistingVal_Allowed0Forbidden1)
    def Set(self, N, var1, var2=[], var3=[], var4=[], ExistingVal_Allowed0Forbidden1=0): #11
        Q=self.GetLength()
        if N>=1 and N<=Q:
            #cell=row[N-1].Set(var1, var2, var3, var4)
            cell=DataCell(var1, var2, var3, var4)
            #cell.Set(var1, var2, var3, var4)
            self.row.SetElement(cell, N, ExistingVal_Allowed0Forbidden1)
    #
    def GetType(self, N): #2
        R=0
        Q=self.GetLength()
        if N>=1 and N<=Q:
            cell=self.row.GetElement_AsCopy(N)
            #can't row[N-1] 
            R=cell.GetType()
        return R
    
    def GetVal(self, ElementN, ValN=1): #3
        R=0
        Q=self.GetLength()
        if ElementN>=1 and ElementN<=Q:
            cell=self.row.GetElement_AsCopy(ElementN)
            #can't row[N-1] 
            R=cell.GetVal(ValN)
        return R

    def GetItem(self, ElementN, ValN=1): #4
        R=0
        Q=self.GetLength()
        if ElementN>=1 and ElementN<=Q:
            cell=self.row.GetElement_AsCopy(ElementN)
            #can't row[N-1] 
            R=cell.GetItem(ValN)
        return R

    # ConcrType
    def GetFloatVal(self, N): #5
        R=0
        Q=self.GetLength()
        if N>=1 and N<=Q:
            cell=self.row.GetElement_AsCopy(N)
            #can't row[N-1] 
            R=cell.GetFloatVal()
        return R

    def GetIntVal(self, N): #6
        R=0
        Q=self.GetLength()
        if N>=1 and N<=Q:
            cell=self.row.GetElement_AsCopy(N)
            #can't row[N-1] 
            R=cell.GetIntVal()
        return R

    def GetBoolVal(self, N): #7
        R=0
        Q=self.GetLength()
        if N>=1 and N<=Q:
            cell=self.row.GetElement_AsCopy(N)
            #can't row[N-1] 
            R=cell.GetBoolVal()
        return R

    def GetStrVal(self, N): #8
        R=0
        Q=self.GetLength()
        if N>=1 and N<=Q:
            cell=self.row.GetElement_AsCopy(N)
            #can't row[N-1] 
            R=cell.GetStrVal()
        return R

    # for combobox
    def GetActiveN(self, N): #for combobox-1
        R=0
        Q=self.GetLength()
        if N>=1 and N<=Q:
            cell=self.row.GetElement_AsCopy(N)
            #can't row[N-1] 
            R=cell.GetActiveN()
        return R

    def GetActiveItem(self, N): #for combobox-2
        R=0
        Q=self.GetLength()
        if N>=1 and N<=Q:
            cell=self.row.GetElement_AsCopy(N)
            #can't row[N-1] 
            R=cell.GetActiveItem()
        return R
    
    def SetActiveN(self, N, val): #for combobox-3
        Q=self.GetLength()
        if N>=1 and N<=Q:
            #cell=row[N-1].Set(var1, var2, var3, var4)
            cell=self.GetElement_AsLink(N)
            #cell=self.GetElement_AsCopy(N)
            cell.SetActiveN(val)
            #self.row.SetElement(cell, N)
    #
    def SetActiveNByVal(self, val): #for combobox-4
        Q=self.GetLength()
        if N>=1 and N<=Q:
            #cell=row[N-1].Set(var1, var2, var3, var4)
            cell=self.GetElement_AsLink(N)
            #cell=self.GetElement_AsCopy(N)
            cell.SetActiveNByVal(val)
            #self.row.SetElement(cell, N)
    #
    def GetQItems(): #for combobox-5
        R=0
        Q=self.GetLength()
        if N>=1 and N<=Q:
            cell=self.row.GetElement_AsCopy(N)
            #can't row[N-1] 
            R=cell.GetQItems()
        return R

    def GetQNames(): # for database-0
        R=0
        Q=self.GetLength()
        if N>=1 and N<=Q:
            cell=self.row.GetElement_AsCopy(N)
            #can't row[N-1] 
            R=cell.GetQNames()
        return R

    # for database
    def GetName(self, N=1): # for database-1
        R=0
        Q=self.GetLength()
        if N>=1 and N<=Q:
            cell=self.row.GetElement_AsCopy(N)
            #can't row[N-1] 
            R=cell.GetName(N)
        return R

    def SetName(self, ElementN, names, NameN=0): # for database-2
        Q=self.GetLength()
        if ElementN>=1 and ElementN<=Q:
            #cell=row[N-1].Set(var1, var2, var3, var4)
            cell=self.GetElement_AsLink(ElementN)
            #cell=self.GetElement_AsCopy(N)
            cell.SetName(names, NameN)
            #self.row.SetElement(cell, N)
        
    def SetItem(self, items, itemN=0): # for database-3
        Q=self.GetLength()
        if N>=1 and N<=Q:
            #cell=row[N-1].Set(var1, var2, var3, var4)
            cell=self.GetElement_AsLink(ElementN)
            #cell=self.GetElement_AsCopy(N)
            cell.SetItem(items, itemN)
            #self.row.SetElement(cell, N)

    #
    def Set(self, N, var1=[], var2=[], var3=[], var4=[]): #11
        Q=self.GetLength()
        if N>=1 and N<=Q:
            #cell=row[N-1].Set(var1, var2, var3, var4)
            cell=self.GetElement_AsLink(ElementN)
            #cell=self.GetElement_AsCopy(N)
            cell.Set(items, var1, var2, var3, var4)
            #self.row.SetElement(cell, N)
    #
    #
    #SetName - above
    #
    # functions of DB FieldHeaderOrItems
    #
    def GetDBFieldInfo(self, ColN): #ColDBHeaderItems-1
        R=0
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsCopy(ColN)
            #can't row[ColN-1] 
            R=cell.GetDBFieldInfo(ColN)
        return R
           
    def GetDBItemsTblInfo(self, ColN): #ColDBHeaderItems-2
        R=0
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsCopy(ColN)
            #can't row[ColN-1] 
            R=cell.GetDBItemsTblInfo(ColN)
        return R
    #
    def SetDBFieldInfo(self, ColN, DBFldInfo): #ColDBHeaderItems-4
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsLink(ColN)
            #can't row[ColN-1] 
            cell.SetDBFieldInfo(DBFldInfo)
    
    def SetDBItemsTblInfo(self, ColN, DBItemsTblInfo): #ColDBHeaderItems-5
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsLink(ColN)
            #can't row[ColN-1] 
            cell.SetDBItemsTblInfo(DBItemsTblInfo) 
                
    # def SetItems - united in SetItem below
    #
    #
    def GetColNameToDisplay(self, ColN): #ColDBHeaderItems-6
        R=0
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsCopy(ColN)
            #can't row[ColN-1] 
            R=cell.GetColNameToDisplay(ColN)
        return R
           
    def GetDBFieldNameToDisplay(self, ColN): #ColDBHeaderItems-7
        R=0
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsCopy(ColN)
            #can't row[ColN-1] 
            R=cell.GetDBFieldNameToDisplay()
        return R

    def GetFieldTypeN(self, ColN): #ColDBHeaderItems-8
        R=0
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsCopy(ColN)
            #can't row[ColN-1] 
            R=cell.GetFieldTypeN()
        return R

    def GetFieldTypeName(self, ColN): #ColDBHeaderItems-9
        R=0
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsCopy(ColN)
            #can't row[ColN-1] 
            R=cell.GetFieldTypeName()
        return R

    def GetFieldLength(self, ColN): #ColDBHeaderItems-10
        R=0
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsCopy(ColN)
            #can't row[ColN-1] 
            R=cell.GetFieldLength()
        return R

    def GetDBFieldCharacteristicsNumber(self, ColN): #ColDBHeaderItems-11
        R=0
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsCopy(ColN)
            #can't row[ColN-1] 
            R=cell.GetDBFieldCharacteristicsNumber()
        return R

    def GetIfIsKeyField(self, ColN): #ColDBHeaderItems-12
        R=0
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsCopy(ColN)
            #can't row[ColN-1] 
            R=cell.GetIfIsKeyField()
        return R

    def GetIfIsCounter(self, ColN): #ColDBHeaderItems-13
        R=0
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsCopy(ColN)
            #can't row[ColN-1] 
            R=cell.GetIfIsCounter()
        return R

    def GetIfIsAutoIncrement(self, ColN): #ColDBHeaderItems-14
        R=0
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsCopy(ColN)
            #can't row[ColN-1] 
            R=cell.GetIfIsAutoIncrement()
        return R
    #
    def SetColNameToDisplay(self, ColN, name): #ColDBHeaderItems-15
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsLink(ColN)
            #can't row[ColN-1] 
            cell.SetColNameToDisplay(name)
    
    def SetDBFieldName(self, ColN, name): #ColDBHeaderItems-16
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsLink(ColN)
            #can't row[ColN-1] 
            cell.SetDBFieldName(name)
    
    def SetFieldTypeN(self, ColN, n): #ColDBHeaderItems-17
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsLink(ColN)
            #can't row[ColN-1] 
            cell.SetFieldTypeN(n)
    
    def SetFieldTypeName(self, ColN, name): #ColDBHeaderItems-18
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsLink(ColN)
            #can't row[ColN-1] 
            cell.SetFieldTypeName(name)

    def SetFieldLength(self, ColN, n): #ColDBHeaderItems-19
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsLink(ColN)
            #can't row[ColN-1] 
            cell.SetFieldLength(n)

    def SetDBFieldCharacteristicsNumber(self, ColN, CharacteristicsNumber): #ColDBHeaderItems-20
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsLink(ColN)
            #can't row[ColN-1] 
            cell.SetDBFieldCharacteristicsNumber(CharacteristicsNumber)

    def SetIfIsKeyField(self, ColN, isKeyField):  #ColDBHeaderItems-21
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsLink(ColN)
            #can't row[ColN-1] 
            cell.SetDBFieldCharacteristicsNumber(CharacteristicsNumber)

    def SetIfIsCounter(self, ColN, isCounter):  #ColDBHeaderItems-22
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsLink(ColN)
            #can't row[ColN-1] 
            cell.SetIfIsCounter(isCounter)

    def SetIfIsAutoIncrement(self, ColN, isAutoIncrement):  #ColDBHeaderItems-23
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsLink(ColN)
            #can't row[ColN-1] 
            cell.SetIfIsAutoIncrement(isAutoIncrement)

    def SetIfIsNotNull(self, ColN, isNotNull):  #ColDBHeaderItems-23
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsLink(ColN)
            #can't row[ColN-1] 
            cell.SetIfIsNotNull(isNotNull)
    #
    # functions of DBTableHeader
    #
    def GetDBTableDataSuppl(self, CellN): #DBTableHdr-1
        R=0
        Q=self.GetLength()
        if CellN>=1 and CellN<=Q:
            cell=self.row.GetElement_AsCopy(CellN)
            #can't row[ColN-1] 
            R=cell.GetDBTableDataSuppl()
        return R

    def GetDBTableData(self, CellN): #DBTableHdr-2
        R=0
        Q=self.GetLength()
        if CellN>=1 and CellN<=Q:
            cell=self.row.GetElement(CellN)
            #can't row[ColN-1] 
            R=cell.GetDBTableDataSuppl()
        return R

    def GetDBTableNameToDisplay(self, CellN): #DBTableHdr-3
        R=0
        Q=self.GetLength()
        if CellN>=1 and CellN<=Q:
            cell=self.row.GetElement(CellN)
            #can't row[ColN-1] 
            R=cell.GetDBTableDataSuppl()
        return R

    def GetDBTableNameInDB(self, CellN): #DBTableHdr-4
        R=0
        Q=self.GetLength()
        if CellN>=1 and CellN<=Q:
            cell=self.row.GetElement(CellN)
            #can't row[ColN-1] 
            R=cell.GetDBTableNameInDB()
        return R

    def GetDBNameInDBCS(self, CellN): #DBTableHdr-5
        R=0
        Q=self.GetLength()
        if CellN>=1 and CellN<=Q:
            cell=self.row.GetElement(CellN)
            #can't row[ColN-1] 
            R=cell.GetDBNameInDBCS()
        return R

    def GetDBTypeName(self, CellN): #DBTableHdr-6
        R=0
        Q=self.GetLength()
        if CellN>=1 and CellN<=Q:
            cell=self.row.GetElement(CellN)
            #can't row[ColN-1] 
            R=cell.GetDBTypeName()
        return R

    def GetDBTypeN(self, CellN): #DBTableHdr-7
        R=0
        Q=self.GetLength()
        if CellN>=1 and CellN<=Q:
            cell=self.row.GetElement(CellN)
            #can't row[ColN-1] 
            R=cell.GetDBTypeN()
        return R

    def GetDBFileFullName(self, CellN): #DBTableHdr-8
        R=0
        Q=self.GetLength()
        if CellN>=1 and CellN<=Q:
            cell=self.row.GetElement(CellN)
            #can't row[ColN-1] 
            R=cell.GetDBFileFullName()
        return R
    #
    def SetDBTableDataSuppl(self, CellN, DBTableDataSuppl):  #DBTableHdr-9
        Q=self.GetLength()
        if CellN>=1 and CellN<=Q:
            cell=self.row.GetElement_AsLink(CellN)
            #can't row[ColN-1] 
            cell.SetDBTableDataSuppl(DBTableDataSuppl)
     
    def SetDBTableData(self, CellN, DBTableData): #DBTableHdr-10
        Q=self.GetLength()
        if CellN>=1 and CellN<=Q:
            cell=self.row.GetElement(CellN)
            #can't row[ColN-1] 
            cell.SetDBTableData(DBTableData)
     
    def SetDBsbleNameToDisplay(self, CellN, TableNameToDisplay): #DBTableHdr-11
        self.cell.SetDBTableNameToDisplay(TableNameToDisplay)

    def SetDBTableNameInDB(self, CellN, DBTableNameInDB): #DBTableHdr-12
        self.cell.SetDBTableNameInDB(DBTableNameInDB)

    def SetDBNameInDBCS(self, CellN, DBNameInDBCS): #DBTableHdr-13
        self.cell.SetDBNameInDBCS(DBNameInDBCS)

    def SetDBTypeName(self, CellN, DBTypeName): #DBTableHdr-14
        self.cell.SetDBTypeName(DBTypeName)

    def SetDBTypeN(self, CellN, DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5): #DBTableHdr-15
        self.cell.SetDBTypeN(DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5)
    
    def SetDBFileFullName(self, CellN, name): #DBTableHdr-16
        self.cell.SetDBFileFullName(name)
    #    
    #   
    def ToString_Element(self, N, str_bef="", str_aft=""):  # represent-1
        s=""
        #return "cell id="+str(id(self))+" content: "+str(self.GetName())+" "
        Q=self.ToString()
        if N>=1 and N<=Q:
            cell=self.GetElement(N)
            s=sell.ToString(str_bef, str_aft)
        return s

    #def __str__(): #represent-2
    #    return str(self.GetName()
        
    def ToString_Info_Element(self, N):  # represent-3
        return "DataCell Type="+str(self.GetTypeN())+" id="+str(id(self))+" val="+str(self.GetVal())    

    def ToString(self, delim=" ", str_bef="", str_aft=""):
        s=""
        Q=self.ToString()
        for i in range(1, Q):
            s=s+ToString_Element(self, i, str_bef, str_aft)
            s=s+delim
        if Q>0:
            s=s+ToString_Element(self, Q, str_bef, str_aft)

    def ToString_Info(self, delim=" ", str_bef="", str_aft=""):
        s="DataCellRow id="+str(id(self))+" L="+str(self.GetLength())+delim
        Q=self.ToString()
        for i in range(1, Q):
            s=s+ToString_Info_Element(self, i, str_bef, str_aft)
            s=s+delim
        if Q>0:
            s=s+ToString_Info_Element(self, Q, str_bef, str_aft)

#..............................................................................                    

class DataCellRowWithHeader1:
    def __init__(self, row, header):
        #self.row=DataCellRow1(row)
        self.row=My1DArray(row)
        self.header=DataCell(header)
    #
    # funstions from My1DArray
    #
    def GetLength(self): #My1DArray-#18
        return self.row.GetLength()
    
    def SetCell(self, N, data): #3, #My1DArray-#5
        if N>=1 and N<=self.GetLength():
            cell=DataCell(val)
            self.row[N-1]=copy.deepcopy(cell)

    def Set(self, row): #My1DArray-#2 #seems #3 no need
        L=0
        self.row.Clear()
        if isinstance(row, DataCellRow1):
            L=row.GetLength()
            for i in range(1, L+1):
                cell=copy.deepcopy(row.GelCell(i))
                self.row.Add(cell)
        elif isinstance(row, My1DArray):
            L=row.GetLength()
            for i in range(1, L+1):                       
                val=copy.deepcopy(row.GetElement(i))
                cell=DataCell(val)
                self.row.Add(cell)
        elif isinstance(row, list):
            L=len(row)#var1, var3, var2, var4
            for i in range(1, L+1):                       
                cell=DataCell(row[i-1])
                self.row.Add(cell)

    def GetCellN_AsLink(self, N): #->My1DArray-#25
        R=0
        L=self.GetLength()
        if N>=1 and N<=L:
            R=self.row.GetElement_AsLink(N)
        return R
    
    def GetCellN_AsCopy(self, N): #->My1DArray-#26
        R=0
        L=self.GetLength()
        if N>=1 and N<=L:
            R=self.row.GetElement_AsCopy(N)
        return R
    
    def GetCellN(self, N, Link0Copy1=0): #->My1DArray-#4
        R=0
        L=self.GetLength()
        if N>=1 and N<=L:
            R=self.row.GetElement(N, )
        return R

    def SetCellN(self, N, data):#->My1DArray-#5
        if N>=1 and N<=MaxInt:
            if isinstance(data, DataCell):
                self.row[N-1]=copy.deepcopy(data)
            elif isinstance(data, list) and len(data)==4:
                val1=data[1-1]
                val2=data[2-1]
                val3=data[3-1]
                val4=data[4-1]
                self.row[N-1].Set(val1,val2, val3, val4)
            else:
                self.row[N-1].Set(data)
                
    def Add(self, cellExt, ExistingVal_Allowed0Forbidden1=0): #->My1DArray-#6
        if isinstance(cellExt, DataCell):
            cell=copy.deepcopy(cellExt)
        else:
            cell=DataCell()
            cell.Set(cellExt)
        self.row.Add(cell, ExistingVal_Allowed0Forbidden1)

    def Ins(self, N, cellExt, ExistingVal_Allowed0Forbidden1=0): #My1DArray-#7,8
        L=self.GetLength()
        if N>=1 and N<=L:
            if isinstance(cellExt, DataCell):
                cell=copy.deepcopy(cellExt)
            else:
                cell=DataCell()
                cell.Set(cellExt)
        self.row.Ins(cell, N, ExistingVal_Allowed0Forbidden1)

    def Del(self, N): #->My1DArray-#9
        self.row.Del(N)

    def Clear(self): #->My1DArray-#10
        self.row.Clear()
    #
    #
    def SeekFirst(self, val, FromN=1):#copied et mod'd, ob "=" for cells is special #->My1DArray-#11
        N=0
        Q=len(self.row)
        ToN=0
        if ToN<1 or ToN>Q:
            ToN=Q
        count=0
        #for i in range(FromN,ToN):
        for i in range(FromN,ToN+1):
            if self.row[i-1]==val:
                count=count+1
                if count==1:
                    N=i+1
                    N=i
        return N
    #
    def SeekLast(self, val, ToN=0): #copied et mod'd, ob "=" for cells is special #->My1DArray-#12
        N=0
        Q=len(self.row)
        count=0
        FromN=1
        if ToN<1 or ToN>Q:
            ToN=Q
        #for i in range(FromN,ToN):
        for i in range(FromN,ToN+1):
            if self.row[i-1]==val:
                N=i+1
                N=i
        return N
    #
    def Seek(self, val, NLim=0, FirstNotLast=1): #copied et mod'd, ob "=" for cells is special #->My1DArray-#13
        N=0
        Q=len(self.row)
        #
        if FirstNotLast==1:
            FromN=NLim
            ToN=0
        else:
            FromN=1
            ToN=NLim
        #
        if FromN<1 or FromN>Q:
            FromN=1
        if ToN<1 or ToN>Q:
            ToN=Q
        if FirstNotLast==1:
            N=self.SeekFirst(val, FromN)
        else:
            N=self.SeekLast(val, TomN)
        #
        return N
    #
    def DelFirstElement(self, val):  #->My1DArray-#14
        if isinstance(cellExt, DataCell):
            cell=copy.deepcopy(cellExt)
        else:
            cell=DataCell()
            cell.Set(cellExt)
        self.row.DelFirstElement(cell)
    #
    def DelLastElement(self, val):  #->My1DArray-#15
        if isinstance(cellExt, DataCell):
            cell=copy.deepcopy(cellExt)
        else:
            cell=DataCell()
            cell.Set(cellExt)
        self.row.DelLastElement(cell)
    #
    def Swap(self, N1, N2): #->My1DArray-#15
        self.row.Swap(N1, N2)

    def Reverse(self): #My1DArray-17
        self.Reverse()
    #My1DArray-18 - above
    def SetLength(self, L, DefaultVal=0): #My1DArray-19
        DefaultCell=DataCell(DefaultVal)
        self.row.SetLength(L, DefaultCell)

    def GetSubRow(self, N1, N2):  #My1DArray-20
        self.row.GetSubRow(N1, N2) 
                                     
    def ToString_Element(self, N, sBef="", sAft=""): #21
        R=""
        if N>=1 and N<=self.GetLength():
            cell=self.GetCell(N)
            R=sBef+cell.ToString()+sAft
        return R

    def ToString_Element_Info(self, N): #22
        sInf="Element "+str(N)+" doesn't exist "
        if N>=1 and N<=self.GetLength():
            sInf="(DataCell TypeN="+str(self.GetTypeN())+" id="+id(self)+" val="+str(self.GetVal())+") "
        return sInf
    #
    #Functions of DataCell
    #
    def Set_Simple(self, N, var1, ExistingVal_Allowed0Forbidden1=0): #1-11-1
        Q=self.GetLength()
        if N>=1 and N<=Q:
            #self.row[N-1]=DataCell_Simple()
            #self.row[N-1].Set(var1)
            cell=DataCell_Simple(var1)
            #cell.Set(var1)
            self.row.SetElement(cell, N, ExistingVal_Allowed0Forbidden1) 
    def Set_ComboboxOrMemo(self, N, var1, var2):  #1-11-2
        Q=self.GetLength()
        if N>=1 and N<=Q:
            #self.row[N-1]=DataCell_ComboboxOrMemo()
            #self.row[N-1].Set(var1, var2)
            cell=DataCell_ComboboxOrMemo(var1, var2)
            #cell.Set(var1, var2)
            self.row.SetElement(cell, N, ExistingVal_Allowed0Forbidden1)
    def Set_DBTableHeader(self, N, var1, var2, var3, ExistingVal_Allowed0Forbidden1=0):  #1-11-3
        Q=self.GetLength()
        if N>=1 and N<=Q:
            #self.row[N-1]=DataCell_DBTableHeader()
            #self.row[N-1].Set(var1, var2, var3)
            cell=DataCell_DBTableHeader(var1, var2, var3)
            #cell.Set(var1, var2, var3)
            self.row.SetElement(cell, N, ExistingVal_Allowed0Forbidden1)
    def Set_ColHdr_DBFldOrItems(self, N, var1, var2=[], var3=[], var4=[], ExistingVal_Allowed0Forbidden1=0):  #1-11-3
        Q=self.GetLength()
        if N>=1 and N<=Q:
            #self.row[N-1]=DataCell_ColHeader_DBFieldOrItems()
            #self.row[N-1].Set(var1, var2, var3)
            cell=DataCell_ColHeader_DBFieldOrItems(var1, var2, var3, var4)
            #cell.Set(var1, var2, var3, var4)
            self.row.SetElement(cell, N, ExistingVal_Allowed0Forbidden1)
    def Set(self, N, var1, var2=[], var3=[], var4=[], ExistingVal_Allowed0Forbidden1=0): #11
        Q=self.GetLength()
        if N>=1 and N<=Q:
            #cell=row[N-1].Set(var1, var2, var3, var4)
            cell=DataCell(var1, var2, var3, var4)
            #cell.Set(var1, var2, var3, var4)
            self.row.SetElement(cell, N, ExistingVal_Allowed0Forbidden1)
    #
    def GetType(self, N): #2
        R=0
        Q=self.GetLength()
        if N>=1 and N<=Q:
            cell=self.row.GetElement_AsCopy(N)
            #can't row[N-1] 
            R=cell.GetType()
        return R
    
    def GetVal(self, ElementN, ValN=1): #3
        R=0
        Q=self.GetLength()
        if ElementN>=1 and ElementN<=Q:
            cell=self.row.GetElement_AsCopy(ElementN)
            #can't row[N-1] 
            R=cell.GetVal(ValN)
        return R

    def GetItem(self, ElementN, ValN=1): #4
        R=0
        Q=self.GetLength()
        if ElementN>=1 and ElementN<=Q:
            cell=self.row.GetElement_AsCopy(ElementN)
            #can't row[N-1] 
            R=cell.GetItem(ValN)
        return R

    # ConcrType
    def GetFloatVal(self, N): #5
        R=0
        Q=self.GetLength()
        if N>=1 and N<=Q:
            cell=self.row.GetElement_AsCopy(N)
            #can't row[N-1] 
            R=cell.GetFloatVal()
        return R

    def GetIntVal(self, N): #6
        R=0
        Q=self.GetLength()
        if N>=1 and N<=Q:
            cell=self.row.GetElement_AsCopy(N)
            #can't row[N-1] 
            R=cell.GetIntVal()
        return R

    def GetBoolVal(self, N): #7
        R=0
        Q=self.GetLength()
        if N>=1 and N<=Q:
            cell=self.row.GetElement_AsCopy(N)
            #can't row[N-1] 
            R=cell.GetBoolVal()
        return R

    def GetStrVal(self, N): #8
        R=0
        Q=self.GetLength()
        if N>=1 and N<=Q:
            cell=self.row.GetElement_AsCopy(N)
            #can't row[N-1] 
            R=cell.GetStrVal()
        return R

    # for combobox
    def GetActiveN(self, N): #for combobox-1
        R=0
        Q=self.GetLength()
        if N>=1 and N<=Q:
            cell=self.row.GetElement_AsCopy(N)
            #can't row[N-1] 
            R=cell.GetActiveN()
        return R

    def GetActiveItem(self, N): #for combobox-2
        R=0
        Q=self.GetLength()
        if N>=1 and N<=Q:
            cell=self.row.GetElement_AsCopy(N)
            #can't row[N-1] 
            R=cell.GetActiveItem()
        return R
    
    def SetActiveN(self, N, val): #for combobox-3
        Q=self.GetLength()
        if N>=1 and N<=Q:
            #cell=row[N-1].Set(var1, var2, var3, var4)
            cell=self.GetElement_AsLink(N)
            #cell=self.GetElement_AsCopy(N)
            cell.SetActiveN(val)
            #self.row.SetElement(cell, N)
    #
    def SetActiveNByVal(self, val): #for combobox-4
        Q=self.GetLength()
        if N>=1 and N<=Q:
            #cell=row[N-1].Set(var1, var2, var3, var4)
            cell=self.GetElement_AsLink(N)
            #cell=self.GetElement_AsCopy(N)
            cell.SetActiveNByVal(val)
            #self.row.SetElement(cell, N)
    #
    def GetQItems(self, N): #for combobox-5
        R=0
        Q=self.GetLength()
        if N>=1 and N<=Q:
            cell=self.row.GetElement_AsCopy(N)
            #can't row[N-1] 
            R=cell.GetQItems()
        return R

    def GetQNames(self, N): # for database-0
        R=0
        Q=self.GetLength()
        if N>=1 and N<=Q:
            cell=self.row.GetElement_AsCopy(N)
            #can't row[N-1] 
            R=cell.GetQNames()
        return R

    # for database
    def GetName(self, N=1): # for database-1
        R=0
        Q=self.GetLength()
        if N>=1 and N<=Q:
            cell=self.row.GetElement_AsCopy(N)
            #can't row[N-1] 
            R=cell.GetName(N)
        return R

    def SetName(self, ElementN, names, NameN=0): # for database-2
        Q=self.GetLength()
        if ElementN>=1 and ElementN<=Q:
            #cell=row[N-1].Set(var1, var2, var3, var4)
            cell=self.GetElement_AsLink(ElementN)
            #cell=self.GetElement_AsCopy(N)
            cell.SetName(names, NameN)
            #self.row.SetElement(cell, N)
        
    def SetItem(self, items, itemN=0): # for database-3
        Q=self.GetLength()
        if N>=1 and N<=Q:
            #cell=row[N-1].Set(var1, var2, var3, var4)
            cell=self.GetElement_AsLink(ElementN)
            #cell=self.GetElement_AsCopy(N)
            cell.SetItem(items, itemN)
            #self.row.SetElement(cell, N)

    #
    def Set(self, N, var1=[], var2=[], var3=[], var4=[]): #11
        Q=self.GetLength()
        if N>=1 and N<=Q:
            #cell=row[N-1].Set(var1, var2, var3, var4)
            cell=self.GetElement_AsLink(ElementN)
            #cell=self.GetElement_AsCopy(N)
            cell.Set(items, var1, var2, var3, var4)
            #self.row.SetElement(cell, N)
    #
    #
    #SetName - above
    #
    # functions of DB FieldHeaderOrItems
    #
    def GetDBFieldInfo(self, ColN): #ColDBHeaderItems-1
        R=0
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsCopy(ColN)
            #can't row[ColN-1] 
            R=cell.GetDBFieldInfo(ColN)
        return R
           
    def GetDBItemsTblInfo(self, ColN): #ColDBHeaderItems-2
        R=0
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsCopy(ColN)
            #can't row[ColN-1] 
            R=cell.GetDBItemsTblInfo(ColN)
        return R
    #
    def SetDBFieldInfo(self, ColN, DBFldInfo): #ColDBHeaderItems-4
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsLink(ColN)
            #can't row[ColN-1] 
            cell.SetDBFieldInfo(DBFldInfo)
    
    def SetDBItemsTblInfo(self, ColN, DBItemsTblInfo): #ColDBHeaderItems-5
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsLink(ColN)
            #can't row[ColN-1] 
            cell.SetDBItemsTblInfo(DBItemsTblInfo) 
                
    # def SetItems - united in SetItem below
    #
    #
    def GetColNameToDisplay(self, ColN): #ColDBHeaderItems-6
        R=0
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsCopy(ColN)
            #can't row[ColN-1] 
            R=cell.GetColNameToDisplay(ColN)
        return R
           
    def GetDBFieldNameToDisplay(self, ColN): #ColDBHeaderItems-7
        R=0
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsCopy(ColN)
            #can't row[ColN-1] 
            R=cell.GetDBFieldNameToDisplay()
        return R

    def GetFieldTypeN(self, ColN): #ColDBHeaderItems-8
        R=0
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsCopy(ColN)
            #can't row[ColN-1] 
            R=cell.GetFieldTypeN()
        return R

    def GetFieldTypeName(self, ColN): #ColDBHeaderItems-9
        R=0
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsCopy(ColN)
            #can't row[ColN-1] 
            R=cell.GetFieldTypeName()
        return R

    def GetFieldLength(self, ColN): #ColDBHeaderItems-10
        R=0
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsCopy(ColN)
            #can't row[ColN-1] 
            R=cell.GetFieldLength()
        return R

    def GetDBFieldCharacteristicsNumber(self, ColN): #ColDBHeaderItems-11
        R=0
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsCopy(ColN)
            #can't row[ColN-1] 
            R=cell.GetDBFieldCharacteristicsNumber()
        return R

    def GetIfIsKeyField(self, ColN): #ColDBHeaderItems-12
        R=0
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsCopy(ColN)
            #can't row[ColN-1] 
            R=cell.GetIfIsKeyField()
        return R

    def GetIfIsCounter(self, ColN): #ColDBHeaderItems-13
        R=0
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsCopy(ColN)
            #can't row[ColN-1] 
            R=cell.GetIfIsCounter()
        return R
    
    def GetIfIsNotNull(self, ColN): #ColDBHeaderItems-13
        R=0
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsCopy(ColN)
            #can't row[ColN-1] 
            R=cell.GetIfIsNotNull()
        return R

    def GetIfIsAutoIncrement(self, ColN): #ColDBHeaderItems-14
        R=0
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsCopy(ColN)
            #can't row[ColN-1] 
            R=cell.GetIfIsAutoIncrement()
        return R
    #
    def SetColNameToDisplay(self, ColN, name): #ColDBHeaderItems-15
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsLink(ColN)
            #can't row[ColN-1] 
            cell.SetColNameToDisplay(name)
    
    def SetDBFieldName(self, ColN, name): #ColDBHeaderItems-16
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsLink(ColN)
            #can't row[ColN-1] 
            cell.SetDBFieldName(name)
    
    def SetFieldTypeN(self, ColN, n): #ColDBHeaderItems-17
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsLink(ColN)
            #can't row[ColN-1] 
            cell.SetFieldTypeN(n)
    
    def SetFieldTypeName(self, ColN, name): #ColDBHeaderItems-18
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsLink(ColN)
            #can't row[ColN-1] 
            cell.SetFieldTypeName(name)

    def SetFieldLength(self, ColN, n): #ColDBHeaderItems-19
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsLink(ColN)
            #can't row[ColN-1] 
            cell.SetFieldLength(n)

    def SetDBFieldCharacteristicsNumber(self, ColN, CharacteristicsNumber): #ColDBHeaderItems-20
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsLink(ColN)
            #can't row[ColN-1] 
            cell.SetDBFieldCharacteristicsNumber(CharacteristicsNumber)

    def SetIfIsKeyField(self, ColN, isKeyField):  #ColDBHeaderItems-21
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsLink(ColN)
            #can't row[ColN-1] 
            cell.SetDBFieldCharacteristicsNumber(CharacteristicsNumber)

    def SetIfIsCounter(self, ColN, isCounter):  #ColDBHeaderItems-22
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsLink(ColN)
            #can't row[ColN-1] 
            cell.SetIfIsCounter(isCounter)

    def SetIfIsAutoIncrement(self, ColN, isAutoIncrement):  #ColDBHeaderItems-23
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsLink(ColN)
            #can't row[ColN-1] 
            cell.SetIfIsAutoIncrement(isAutoIncrement)

    def SetIfIsNotNull(self, ColN, isNotNull):  #ColDBHeaderItems-23
        Q=self.GetLength()
        if ColN>=1 and ColN<=Q:
            cell=self.row.GetElement_AsLink(ColN)
            #can't row[ColN-1] 
            cell.SetIfIsNotNull(isNotNull)
    #
    # functions of DBTableHeader - no need
    #
    #def GetDBTableDataSuppl(self, CellN): #DBTableHdr-1
    #    R=0
    #    Q=self.GetLength()
    #    if CellN>=1 and CellN<=Q:
    #        cell=self.row.GetElement_AsCopy(CellN)
   #         #can't row[ColN-1] 
    #        R=cell.GetDBTableDataSuppl()
    #    return R

    #def GetDBTableData(self, CellN): #DBTableHdr-2
    #    R=0
    #    Q=self.GetLength()
    #    if CellN>=1 and CellN<=Q:
    #        cell=self.row.GetElement(CellN)
    #        #can't row[ColN-1] 
    #        R=cell.GetDBTableDataSuppl()
    #    return R

    #def GetDBTableNameToDisplay(self, CellN): #DBTableHdr-3
    #    R=0
    #    Q=self.GetLength()
    #    if CellN>=1 and CellN<=Q:
    #        cell=self.row.GetElement(CellN)
    #        #can't row[ColN-1] 
    #        R=cell.GetDBTableDataSuppl()
    #    return R

    #def GetDBTableNameInDB(self, CellN): #DBTableHdr-4
    #    R=0
    #    Q=self.GetLength()
    #    if CellN>=1 and CellN<=Q:
    #        cell=self.row.GetElement(CellN)
    #        #can't row[ColN-1] 
    #        R=cell.GetDBTableNameInDB()
    #    return R

    #def GetDBNameInDBCS(self, CellN): #DBTableHdr-5
    #    R=0
    #    Q=self.GetLength()
    #    if CellN>=1 and CellN<=Q:
    #        cell=self.row.GetElement(CellN)
    #        #can't row[ColN-1] 
    #        R=cell.GetDBNameInDBCS()
    #    return R

    #def GetDBTypeName(self, CellN): #DBTableHdr-6
    #    R=0
    #    Q=self.GetLength()
    #    if CellN>=1 and CellN<=Q:
    #        cell=self.row.GetElement(CellN)
    #        #can't row[ColN-1] 
    #        R=cell.GetDBTypeName()
    #    return R

    #def GetDBTypeN(self, CellN): #DBTableHdr-7
    #    R=0
    #    Q=self.GetLength()
    #    if CellN>=1 and CellN<=Q:
    #        cell=self.row.GetElement(CellN)
    #        #can't row[ColN-1] 
    #        R=cell.GetDBTypeN()
    #    return R

    #def GetDBFileFullName(self, CellN): #DBTableHdr-8
    #    R=0
    #    Q=self.GetLength()
    #    if CellN>=1 and CellN<=Q:
    #        cell=self.row.GetElement(CellN)
    #        #can't row[ColN-1] 
    #        R=cell.GetDBFileFullName()
    #    return R
    #
    #def SetDBTableDataSuppl(self, CellN, DBTableDataSuppl):  #DBTableHdr-9
    #    Q=self.GetLength()
    #    if CellN>=1 and CellN<=Q:
    #        cell=self.row.GetElement_AsLink(CellN)
    #        #can't row[ColN-1] 
    #        cell.SetDBTableDataSuppl(DBTableDataSuppl)
     
    #def SetDBTableData(self, CellN, DBTableData): #DBTableHdr-10
    #    Q=self.GetLength()
    #    if CellN>=1 and CellN<=Q:
    #        cell=self.row.GetElement(CellN)
    #        #can't row[ColN-1] 
    #        cell.SetDBTableData(DBTableData)
     
    #def SetDBs+bleNameToDisplay(self, CellN, TableNameToDisplay): #DBTableHdr-11
    #    self.cell.SetDBTableNameToDisplay(TableNameToDisplay)

    #def SetDBTableNameInDB(self, CellN, DBTableNameInDB): #DBTableHdr-12
    #    self.cell.SetDBTableNameInDB(DBTableNameInDB)

    #def SetDBNameInDBCS(self, CellN, DBNameInDBCS): #DBTableHdr-13
    #    self.cell.SetDBNameInDBCS(DBNameInDBCS)

    #def SetDBTypeName(self, CellN, DBTypeName): #DBTableHdr-14
    #    self.cell.SetDBTypeName(DBTypeName)

    #def SetDBTypeN(self, CellN, DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5): #DBTableHdr-15
    #    self.cell.SetDBTypeN(DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5)
    
    #def SetDBFileFullName(self, CellN, name): #DBTableHdr-16
    #    self.cell.SetDBFileFullName(name)
    #    
    #   
    def ToString_Element(self, N, str_bef="", str_aft=""):  # represent-1
        s=""
        #return "cell id="+str(id(self))+" content: "+str(self.GetName())+" "
        Q=self.ToString()
        if N>=1 and N<=Q:
            cell=self.GetElement(N)
            s=sell.ToString(str_bef, str_aft)
        return s

    #def __str__(): #represent-2
    #    return str(self.GetName()
        
    def ToString_Info_Element(self, N):  # represent-3
        return "DataCell Type="+str(self.GetTypeN())+" id="+str(id(self))+" val="+str(self.GetVal())    

    def ToString(self, delim=" ", str_bef="", str_aft=""):
        s=""
        Q=self.ToString()
        for i in range(1, Q):
            s=s+ToString_Element(self, i, str_bef, str_aft)
            s=s+delim
        if Q>0:
            s=s+ToString_Element(self, Q, str_bef, str_aft)

    def ToString_Info(self, delim=" ", str_bef="", str_aft=""):
        s="DataCellRow id="+str(id(self))+" L="+str(self.GetLength())+delim
        Q=self.ToString()
        for i in range(1, Q):
            s=s+ToString_Info_Element(self, i, str_bef, str_aft)
            s=s+delim
        if Q>0:
            s=s+ToString_Info_Element(self, Q, str_bef, str_aft)                                  
    #
    # 
    #
    #Functions for Row Header Cell
    #
    #Functions of DataCell except TableHeader functions
    #
    def Set_Simple_Hdr(self, var1, ExistingVal_Allowed0Forbidden1=0): #1-11-1
        self.Header.Set_Simple(var1) 
    def Set_ComboboxOrMemo_Hdr(self, var1, var2):  #1-11-2
         self.Header.Set_ComboboxOrMemo(var1, var2) 
    def Set_DBTableHeader_Hdr(self, var1, var2, var3, ExistingVal_Allowed0Forbidden1=0):  #1-11-3
        self.Header.Set_DBTableHeader(var1, var2, var3)
    def Set_ColHdr_DBFldOrItems_Hdr(self,var1, var2=[], var3=[], var4=[], ExistingVal_Allowed0Forbidden1=0):  #1-11-3
        self.Header.Set_DBTableHeader(var1, var2, var3, var4)
    def Set_Hdr(self, var1, var2=[], var3=[], var4=[], ExistingVal_Allowed0Forbidden1=0): #11
        self.Header.Set(var1, var2, var3, var4)
    #
    def GetElement_Link_Hdr(self):
        return self.Header
    def GetElement_Copy_Hdr(self):
        cell=[]
        if isinstance(self.Header, DataCell):
            cell=copy.deepcopy(self.Header)
        return cell
    def GetElement_Hdr(self, Link0Copy1=0):
        R=0
        if Link0Copy1==0:
            R=self.GetElement_Link_Hdr()
        else:
            R=self.GetElement_Copy_Hdr()
        return R
    #
    def GetType_Hdr(self): #2
        R=0
        if isinstance(self.Header, DataCell):
            R=self.Header.GetType()
        return R
    
    def GetVal_Hdr(self, ValN=1): #3
        R=0
        if isinstance(self.Header, DataCell):
            R=self.Header.GetVal(ValN)
        return R

    def GetItem_Hdr(self, ValN=1): #4
        R=0
        if isinstance(self.Header, DataCell):
            R=self.Header.GetItem(ValN)
        return R

    # ConcrType
    def GetFloatVal_Hdr(self): #5
        R=0
        if isinstance(self.Header, DataCell):
            R=self.Header.GetFloatVal()
        return R

    def GetIntVal_Hdr(self): #6
        return self.Header.GetIntVal()

    def GetBoolVal_Hdr(self): #7
        return self.Header.GetBoolVal()

    def GetStrVal_Hdr(self): #8
        return self.Header.GetStrVal()

    # for combobox
    def GetActiveN_Hdr(self): #for combobox-1
        return self.Header.GetActiveN()

    def GetActiveItem_Hdr(self): #for combobox-2
        return self.Header.GetActiveItem()
    
    def SetActiveN_Hdr(self, val): #for combobox-3
        self.Header.HeaderSetActiveN(val)
    #
    def SetActiveNByVal_Hdr(self, val): #for combobox-4
        self.Header.HeaderSetActiveNByVal(val)
    #
    def GetQItems_Hdr(self): #for combobox-5
        return self.Header.GetQItems()

    def GetQNames_Hdr(self): # for database-0
        R=0
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            cell=self.Header
            #can't row[N-1] 
            R=cell.GetQNames()
        return R

    # for database
    def GetName_Hdr(self, N=1): # for database-1
        R=0
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            cell=self.Header
            #can't row[N-1] 
            R=cell.GetName(N)
        return R

    def SetName_Hdr(self, names, NameN=0): # for database-2
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            #cell=row[N-1].Set(var1, var2, var3, var4)
            cell=self.Header
            #cell=self.GetElement_AsCopy(N)
            cell.SetName(names, NameN)
            #self.row.SetElement(cell, N)
        
    def SetItem_Hdr(self, items, itemN=0): # for database-3
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            #cell=row[N-1].Set(var1, var2, var3, var4)
            cell=self.Header
            #cell=self.GetElement_AsCopy(N)
            cell.SetItem(items, itemN)
            #self.row.SetElement(cell, N)

    #
    def Set_Hdr(self, var1=[], var2=[], var3=[], var4=[]): #11
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            #cell=row[N-1].Set(var1, var2, var3, var4)
            cell=self.Header
            #cell=self.GetElement_AsCopy(N)
            cell.Set(items, var1, var2, var3, var4)
            #self.row.SetElement(cell, N)
    #
    #
    #SetName - above
    #
    # functions of DB FieldHeaderOrItems
    #
    def GetDBFieldInfo_Hdr(self): #ColDBHeaderItems-1
        R=0
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            cell=self.Header
            #can't row[ColN-1] 
            R=cell.GetDBFieldInfo()
        return R
           
    def GetDBItemsTblInfo_Hdr(self): #ColDBHeaderItems-2
        R=0
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            cell=self.Header
            #can't row[ColN-1] 
            R=cell.GetDBItemsTblInfo()
        return R
    #
    def SetDBFieldInfo_Hdr(self, DBFldInfo): #ColDBHeaderItems-4
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            cell=self.Header
            #can't row[ColN-1] 
            cell.SetDBFieldInfo(DBFldInfo)
    
    def SetDBItemsTblInfo_Hdr(self, DBItemsTblInfo): #ColDBHeaderItems-5
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            cell=self.Header
            #can't row[ColN-1] 
            cell.SetDBItemsTblInfo(DBItemsTblInfo) 
                
    # def SetItems - united in SetItem below
    #
    #
    def GetColNameToDisplay_Hdr(self): #ColDBHeaderItems-6
        R=0
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            cell=self.Header
            #can't row[ColN-1] 
            R=cell.GetColNameToDisplay()
        return R
           
    def GetDBFieldNameToDisplay_Hdr(self): #ColDBHeaderItems-7
        R=0
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            cell=self.Header
            #can't row[ColN-1] 
            R=cell.GetDBFieldNameToDisplay()
        return R

    def GetFieldTypeN_Hdr(self): #ColDBHeaderItems-8
        R=0
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            cell=self.Header
            #can't row[ColN-1] 
            R=cell.GetFieldTypeN()
        return R

    def GetFieldTypeName_Hdr(self, ColN): #ColDBHeaderItems-9
        R=0
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            cell=self.Header
            #can't row[ColN-1] 
            R=cell.GetFieldTypeName()
        return R

    def GetFieldLength_Hdr(self): #ColDBHeaderItems-10
        R=0
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            cell=self.Header
            #can't row[ColN-1] 
            R=cell.GetFieldLength()
        return R

    def GetDBFieldCharacteristicsNumber_Hdr(self): #ColDBHeaderItems-11
        R=0
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            cell=self.Header
            #can't row[ColN-1] 
            R=cell.GetDBFieldCharacteristicsNumber()
        return R

    def GetIfIsKeyField_Hdr(self): #ColDBHeaderItems-12
        R=0
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            cell=self.Header
            #can't row[ColN-1] 
            R=cell.GetIfIsKeyField()
        return R

    def GetIfIsCounter_Hdr(self): #ColDBHeaderItems-13
        R=0
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            cell=self.Header
            #can't row[ColN-1] 
            R=cell.GetIfIsCounter()
        return R

    def GetIfIsAutoIncrement_Hdr(self): #ColDBHeaderItems-14
        R=0
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            cell=self.Header
            #can't row[ColN-1] 
            R=cell.GetIfIsAutoIncrement()
        return R

    def GetIfIsNotNull_Hdr(self): #ColDBHeaderItems-14
        R=0
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            cell=self.Header
            #can't row[ColN-1] 
            R=cell.GetIfIsNotNull()
        return R
    #
    def SetColNameToDisplay_Hdr(self, name): #ColDBHeaderItems-15
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            cell=self.Header
            #can't row[ColN-1] 
            cell.SetColNameToDisplay(name)
    
    def SetDBFieldName_Hdr(self, name): #ColDBHeaderItems-16
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            cell=self.Header
            #can't row[ColN-1] 
            cell.SetDBFieldName(name)
    
    def SetFieldTypeN_Hdr(self, n): #ColDBHeaderItems-17
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            cell=self.Header
            #can't row[ColN-1] 
            cell.SetFieldTypeN(n)
    
    def SetFieldTypeName_Hdr(self, name): #ColDBHeaderItems-18
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            cell=self.Header
            #can't row[ColN-1] 
            cell.SetFieldTypeName(name)

    def SetFieldLength_Hdr(self, n): #ColDBHeaderItems-19
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            cell=self.Header
            #can't row[ColN-1] 
            cell.SetFieldLength(n)

    def SetDBFieldCharacteristicsNumber_Hdr(self, CharacteristicsNumber): #ColDBHeaderItems-20
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            cell=self.Header
            #can't row[ColN-1] 
            cell.SetDBFieldCharacteristicsNumber(CharacteristicsNumber)

    def SetIfIsKeyField_Hdr(self, isKeyField):  #ColDBHeaderItems-21
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            cell=self.Header
            #can't row[ColN-1] 
            cell.SetDBFieldCharacteristicsNumber(CharacteristicsNumber)

    def SetIfIsCounter_Hdr(self, isCounter):  #ColDBHeaderItems-22
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            cell=self.Header
            #can't row[ColN-1] 
            cell.SetIfIsCounter(isCounter)

    def SetIfIsAutoIncrement_Hdr(self, isAutoIncrement):  #ColDBHeaderItems-23
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            cell=self.Header
            #can't row[ColN-1] 
            cell.SetIfIsAutoIncrement(isAutoIncrement)

    def SetIfIsNotNull_Hdr(self, isNotNull):  #ColDBHeaderItems-23
        Q=self.GetLength()
        if isinstance(self.Header, DataCell):
            cell=self.Header
            #can't row[ColN-1] 
            cell.SetIfIsNotNull(isNotNull)


    def ToString_Info_RowElement(self, N):  # represent-3
        s=""
        Q=len(self.row)
        if N<=1 and N>=L:
            cell=self.row[N-1]
            s="DataCell Type="+str(self.GetTypeN())+" id="+str(id(self))+" val="+str(self.GetVal())
        return s

    def ToString_Info_RowHdr(self):  # represent-3
        s=""
        if isinstance(self.header, DataCell):
             s="DataCell Type="+str(self.header.GetTypeN())+" id="+str(id(self.header))+" val="+str(self.header.GetVal())                         
        return s

    def ToString_RowElement(self, N, str_bef="", str_aft=""):
        s=""
        Q=self.ToString()
        if N<=1 and N>=Q:
            s=self.row[N-1].ToString(str_bef, str_aft)
        return s

    def ToString(self, delim=" ", str_bef="", str_aft=""):
        s=""
        Q=self.ToString()
        for i in range(1, Q):
            s=s+ToString_RowElement(i, str_bef, str_aft)
            s=s+delim
        if Q>0:
            s=s+ToString_Element(Q, str_bef, str_aft)

    def ToString_Info(self, delim=" ", str_bef="", str_aft=""):
        s="DataCellRow id="+str(id(self))+" L="+str(self.GetLength())+delim
        Q=self.ToString()
        for i in range(1, Q):
            s=s+ToString_Info_Element(i, str_bef, str_aft)
            s=s+delim
        if Q>0:
            s=s+ToString_Info_Element(Q, str_bef, str_aft)
        s=s+" Header: "
        s=s+ToString_Info_RowHdr(Q, str_bef, str_aft)
        return s
