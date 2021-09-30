class Rational:
    def __init__(self,numerator=1,denominator=1):
        self.__numerator=numerator
        self.__demominator=denominator
    def printnumbers(self):
        return str(self.__numerator, '/' , self.__denominator)
A=Rational(5,5)
print(A.printnumbers())