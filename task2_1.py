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
        if not 20>=length>0:
            raise ValueError
        self.__length=length 
    @width.setter
    def width(self,width):
        if not 20>=width>0:
            raise ValueError
        self.__width=width
    def area(self):
        return self.__length*self.__width
    def perimeter(self):
        return (self.__length+self.__width)*2
try:
    x=float(input())
    y=float(input())
    A=Rectangle(x,y)
    print(f'Area: {A.area()}')
    print(f'Perimeter: {A.perimeter()}')
    A.length=10
    A.width=10
    print(A.length,A.width)
except ValueError:
    print("Enter correct values")
except NameError:
    print("Name error")

 