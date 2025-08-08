class beta:
    staticCur=0
    staticMax=0
    def __init__(self):
        self.__class__.staticCur+=1
        self.__class__.staticMax+=1
        self.curN=self.__class__.staticMax
        print("object created: "+self.__str__())#to comment

    def __str__(self):
        return "Object: "+str(self.curN)+" Exists now: "+str(self.__class__.staticCur)+" Existed max: "+str(self.__class__.staticMax)

    def __del__(self):
        self.__class__.staticCur-=1
        print("object deleted: "+self.__str__())#to comment
        if self.__class__.staticCur==1:
            print("It is the last object being deleted!"+" Exists now: "+str(self.__class__.staticCur)+" Existed max: "+str(self.__class__.staticMax))

X=[]
Q=4
print ("Creating objects:")#to comment
for i in range(1, Q+1):
    a=beta()
    X.append(a)
print ("Printing existing objects info:")#to comment
for i in range(1, Q+1):#to comment
    print(X[i-1].__str__())#to comment
print ("Deleting objects:") #to comment  
X=[]

