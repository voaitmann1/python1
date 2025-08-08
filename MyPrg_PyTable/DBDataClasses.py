#
import copy
#
DBTypeN_SQLite=1
DBTypeN_MySql=2
DBTypeN_MsSqlSrv=3
DBTypeN_MSAccess2003=4
DBTypeN_MSAccess2007=5
#
class TDBTableDataSuppl:
    def __init__(self, DBHdr="", DBTypeName="",DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5=0, DBFileFullName=""):
        self.DBNameInDBCS=DBHdr
        self.DBTypeName=DBTypeName
        self.DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5=DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5
        self.DBFileFullName=DBFileFullName
#        
class TDBTableData:
    def __init__(self, TableNameInDB="", DBTableDataSuppl=[]):
        self.TableNameInDB=TableNameInDB
        self.DBTableDataSuppl=[]
        if not DBTableDataSuppl==[]:
            if self.DBTableDataSuppl==[]:
                self.DBTableDataSuppl=TDBTableDataSuppl()
            if isinstance(DBTableDataSuppl, TDBTableDataSuppl):
                self.DBTableDataSuppl=copy.deepcopy(DBTableDataSuppl)
            elif isinstance(DBTableDataSuppl, list):
                self.DBTableDataSuppl.DBNameInDBCS=str(DBTableDataSuppl[1-1])
                self.DBTableDataSuppl.DBTypeName=DBTableDataSuppl[2-1]
                self.DBTableDataSuppl.DBTypeN_SQLite_1_MySql_2_MsSqlSrv_3_MSAccess2003_4_MSAccess2007_5=int(DBTableDataSuppl[3-1])
                self.DBTableDataSuppl.DBFileFullName=str(DBTableDataSuppl[4-1])
#
#
class TDBItemsTableData:
    def __init__(self, ItemsTableName="", ItemsTableItemsFieldName="", ItemsTableKeyFieldName=""):
        self.ItemsTableName=ItemsTableName
        self.ItemsTableItemsFieldName=ItemsTableItemsFieldName
        self.ItemsTableKeyFieldName=ItemsTableKeyFieldName
#
#
class TDBFieldInfoSuppl:
    def __init__(self, FieldTypeN=0, FieldTypeName="", FieldLength=0, DBFieldCharacteristicsNumber=0, isKeyField=0, isCounter=0, isNotNull=0, isAutoIncrement=0):
        self.FieldTypeN=FieldTypeN#1
        self.FieldTypeName=FieldTypeName#2
        self.FieldLength=FieldLength#3
        self.DBFieldCharacteristicsNumber=DBFieldCharacteristicsNumber#4
        self.isKeyField=isKeyField#5
        self.isCounter=isCounter#6
        self.isNotNull=isNotNull#7
        self.isAutoIncrement=isAutoIncrement#8
#        
class TDBFieldInfo:
    def __init__(self, isToCreateDB=0):
        self.DBFieldNameToDBTable=""#
        if isToCreateDB==0:
            self.DBFieldInfoSuppl=[]#TDBFieldInfoSuppl()#
        else:#1
            self.DBFieldInfoSuppl=TDBFieldInfoSuppl()
