class Rectangle:
    def __init__(self,length=1,width=1):
        self.length=length
        self.width=width
    @property
    def length(self):
        return self.__length
    @property
    def width(self):
        return self.__width
    @length.setter
    def length(self,length):
        if 20>=length>0:
            self.__length=length
        else:
            raise ValueError 
    @width.setter
    def width(self,width):
        if 20>=width>0:
            self.__width=width
        else:
            raise ValueError
    def area(self):
        return f'Area: {self.__length*self.__width}'
    def perimeter(self):
        return f'Perimeter: {(self.__length+self.__width)*2}'
try:
    x=float(input())
    y=float(input())
    A=Rectangle(x,y)
    print(A.area())
    print(A.perimeter())
    A.length=10
    A.width=10
    print(A.length,A.width)
except ValueError:
    print("Enter correct values")
except NameError:
    print("Name error")

 