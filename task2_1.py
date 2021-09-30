class Rectangle:
    def __init__(self,length=1,width=1):
        self.setter(length,width)
    def setter(self,length,width):
        if 20>=x>0 and 20>=y>0:
            self.length=length
            self.width=width
        else:
            return None
    def getter(self):
        return self.length,self.width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return (self.length+self.width)*2
try:
    x=float(input())
    y=float(input())
    A=Rectangle(x,y)
    print(A.area())
    print(A.perimeter())
    A.setter(10,10)
    print(A.getter())
except:
    print("None")

 