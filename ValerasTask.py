import copy
globalcount=0
class beta:
    i=0
    maximum=0
    #MyN=0
    def __init__(self):
        self.i=self.i+1
        #i=self.i
        self.MyN=i
        if self.maximum<i:
            self.maximum=i
        #if maximum<i:
        #     maximum=i
        global globalcount
        globalcount+=1
        #i=self.Count()
        print("object "+str(self.MyN)+" created, in all:"+str(i))
        print("i= "+str(self.i)+"="+str(i)+"; MyN= "+str(self.MyN)+" maximum="+str(self.maximum))#+str(self.get_Max())#+"="+str(maximum)

    @staticmethod
    def get_created_instances_count():
        return i

    #@staticmethod
    #def Count():
    #    self.i=i+1
    #    return i

    #@staticmethod #static method can't take arg self, et ac self nabl 
    #def get_created_instances_count1(self):
    #    return self.i

    def get_MyN(self):
        return self.MyN

    #@staticmethod
    #def get_Max(self):
    #    return self.maximum

    def __str__(self):
        global globalcount
        s="i= "+str(self.i)+"="+str(i)+" MyN= "+str(self.MyN)+";  maximum="+str(self.maximum)+"="+str(i)+"="+str(globalcount)+"="+str(self.get_created_instances_count())#+"="+str(self.get_created_instances_count1())#+" = "+str(maximum)#+str(self.get_Max())#+"="+str(maximum)
        return s

    def __del__(self):
        print("object "+str(self.MyN)+" deleted")
        if self.MyN==1:
            print("It is the last object being deleted! Maximum "+str(self.maximum)+"="+str(i)+"="+str(globalcount)+" objects were created")
        

X=[]
Q=4
print ("Creating objects:")
for i in range(1, Q+1):
    a=beta()
    X.append(copy.deepcopy(a))
Y=[]
Y.append(copy.deepcopy(X[3-1]))
#b=beta()
print ("Printing existing objects info:")
for i in range(1, Q+1):
    print(X[i-1].__str__())
print(Y[1-1].__str__())
print ("Deleting objects:")    
X=[]
Y=[]
#b.delete()
#delete(b)

