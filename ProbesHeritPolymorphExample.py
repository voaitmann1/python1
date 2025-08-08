from math import pi


class Shape(object):
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        #super().__init__("Square")
        Shape(self).__init__("Square")#ne objects dagegen
        #super(Square, self).__init__("Square")#super() argument 1 must be type, not classobj
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."

    def __str__(self):
        #return Shape.__str__(self)#Square instance has  no attribute name 
        #return Shape.name#class Shape has no attribute name
        #return Shape(self).__str__() #TypeError: __str__ returned non-string (type instance)
        #return Shape(self).__str__(self) #TypeError: __str__ returned non-string (type instance)
        #return Shape(self).name #TypeError: __str__ returned non-string (type instance)
        #return str(Shape(self).__str__()) #TypeError: __str__ returned non-string (type instance); infinite recursion
        #return str(Shape(self).__str__())
        #return super().name#need 1 arg, 0 given
        #return base.name#base ne def'd
        #return super(Square, self).name#need 1 arg, 0 given
        #return super(Square, self).name #TypeError: super() argument 1 must be type, not classobj
        #return super(self).name#TypeError: super() argument 1 must be type, not instance
        #return super(Square).name#TypeError: super() argument 1 must be type, not classobj
        return super(Square, self).__str__()#python2 #TypeError: super() argument 1 must be type, not classobj #
        #return super().__str__()#python3
        #return Perent.__str__() #glo


class Circle(Shape):
    def __init__(self, radius):
        #super().__init__("Circle")
        Shape(self).__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2

    def __str__(self):
        #return Shape(self).__str__(self) #TypeError: __str__ returned non-string (type instance)
        #return Shape(self).__str__(self) #TypeError: __str__ returned non-string (type instance)
        #return Shape(self).name #TypeError: __str__ returned non-string (type instance)
        #return Super(self).name
        return Super(Circle,self).name

arr=[]
a = Square(4)
b = Circle(7)
arr.append(a)
arr.append(b)
for e in arr:
    print(e)
    print(e.fact())
    print(e.area())
#
#Circle
#I am a two-dimensional shape.
#Squares have each angle equal to 90 degrees.
#153.93804002589985
