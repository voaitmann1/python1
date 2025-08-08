import copy
globalMax=0
globalCur=0
class beta:
    staticCur=0
    staticMax=0
    def __init__(self):
        self.__class__.staticCur+=1
        self.__class__.staticMax+=1
        self.curN=self.__class__.staticMax
        print("Object created: "+self.__str__())

    @staticmethod
    def CountCreated():
        return localMax

    def __str__(self):
        return "Object: "+str(self.curN)+" Exists now: "+str(self.__class__.staticCur)+" Existed max: "+str(self.__class__.staticMax)

    def __del__(self):
        self.__class__.staticCur-=1
        print("object deleted: "+self.__str__())
        if self.__class__.staticCur==1:
            print("It is the last object being deleted!"+" Exists now: "+str(self.__class__.staticCur)+" Existed max: "+str(self.__class__.staticMax))

X=[]
Q=4
print ("Creating objects:")
for i in range(1, Q+1):
    a=beta()
    X.append(copy.deepcopy(a))
    X.append(a)
Y=[]
Y.append(copy.deepcopy(X[3-1]))
Y.append(X[3-1])
b=beta()
print ("Printing existing objects info:")
for i in range(1, Q+1):
    print(X[i-1].__str__())
print(Y[1-1].__str__())
print ("Deleting objects:")    
X=[]
Y=[]
