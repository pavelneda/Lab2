import math
class Rational:
    def __init__(self,numerator=1,denominator=1):
        newnumber=self.__reducefraction(numerator,denominator)
        self.__numerator=newnumber[0]
        self.__denominator=newnumber[1]
        
    def __reducefraction(self,x,y):
        k = math.gcd(x,y)
        if y<0:
            y=-y
            x=-x
        return (x//k, y//k)
        
    def numbers(self):
        return f'{self.__numerator}/{self.__denominator}'
        
    def floatingnumbers(self):
        return  float(self.__numerator)/self.__denominator
        
    def __add__(self,other):
        if not isinstance(other,Rational):
            raise TypeError   
        denominator=int(self.__denominator*other.__denominator/math.gcd(self.__denominator,other.__denominator))
        numerator=int(denominator/self.__denominator*self.__numerator+denominator/other.__denominator*other.__numerator)
        k = self.__reducefraction(int(numerator), int(denominator))
        return Rational(k[0],k[1]) 
    
    def __sub__(self,other):
        if not isinstance(other,Rational):
            raise TypeError
        denominator=int(self.__denominator*other.__denominator/math.gcd(self.__denominator,other.__denominator))
        numerator=int(denominator/self.__denominator*self.__numerator-denominator/other.__denominator*other.__numerator) 
        k=self.__reducefraction(int(numerator),int(denominator))
        return Rational(k[0],k[1])
        
    def __mul__(self,other):
        if not isinstance(other,Rational):
            raise TypeError
        denominator=self.__denominator*other.__denominator
        numerator=self.__numerator*other.__numerator
        k=self.__reducefraction(int(numerator),int(denominator))
        return Rational(k[0],k[1])
    
    def __truediv__(self,other):
        if not isinstance(other,Rational):
            raise TypeError
        if not other.floatingnumbers():
            raise ZeroDivisionError
        denominator=self.__denominator*other.__numerator
        numerator=self.__numerator*other.__denominator
        k=self.__reducefraction(int(numerator),int(denominator))   
        return Rational(k[0],k[1])
        
try:
    firstfractione=input()
    secondfractione=input()
    a=list(map(int,firstfractione.split('/')))
    b=list(map(int,secondfractione.split('/')))
    if not(len(a)==2 and a[1] and len(b)==2 and b[1]):
        raise ValueError
    A=Rational(a[0],a[1])
    B=Rational(b[0],b[1])
    print("Form a/b(first): "+A.numbers())
    print("Floatint-point format(first): "+str(A.floatingnumbers()))
    print("Form a/b(second): "+B.numbers())
    print("Floatint-point format(second): "+str(B.floatingnumbers()))
    C=A+B
    print("A+B="+C.numbers())
    C=A*B
    print("A*B="+C.numbers())
    C=A-B
    print("A-B="+C.numbers())
    C=A/B
    print("A/B="+C.numbers())
except TypeError:
    print("Type error")
except ValueError:
    print("Enter correct values")
except ZeroDivisionError:
    print("Вivision by zero")
except NameError:
    print("Name error")
