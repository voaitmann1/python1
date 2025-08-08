class beta:
   staticCur=0
   staticMax=0
   def __init__(self):
     self.__class__.staticCur+=1
     self.__class__.staticMax+=1
     self.curN=self.__class__.staticMax
     print("object created: "+self.__str__())

   def __str__(self):
     s1="Object"
     s2=str(self.curN)
     s3="Exists now:"
     s4=str(self.__class__.staticCur)
     s5="Existed max:"
     s6=str(self.__class__.staticMax)
     ss=s1+""+s2+""+s3+""+s4+""+s5+""+s6
     return ss

   def __del__(self):
     self.__class__.staticCur-=1
     print("object deleted: "+self.__str__())
     s1="It`s the last object being deleted"
     s2="Exists now:"
     s3=str(self.__class__.staticCur)
     s4="Existed max"
     s5=str(self.__class__.staticMax)
     ss=s1+""+s2+""+s3+""+s4+""+s5
     if self.__class__.staticCur==1:
         print(ss)

X=[]
Q=4
print("Creating objects:")
for i in range(1, Q+1):
    a=beta()
    X.append(a)
print ("Printing existing objects info:")
for i in range(1, Q+1):
    print(X[i-1].__str__())
    print ("Deleting objects:")
X=[]




    



        



