class Product:
    def __init__(self,name,price,desc,dimens):
        if not(isinstance(name,str) and isinstance(price,int) and isinstance(desc,str) and isinstance(dimens,str)):
            raise TypeError
        if not(name.isalpha() and price >=0 and desc and dimens):
            raise ValueError
        self.__name=name
        self.price=price
        self.__desc=desc
        self.__dimens=dimens
    def __str__(self):
        return f'Name:{self.__name}, Price:{self.price}, Description:{self.__desc}, Dimensions:{self.__dimens}'
class Customer:
    def __init__(self,surname,name,patronymic,phone,city):
        if not(isinstance(surname,str) and isinstance(name,str) and isinstance(patronymic,str) and isinstance(phone,str) and isinstance(city,str)):
            raise TypeError
        if not(surname.isalpha() and name.isalpha() and patronymic.isalpha() and phone and city):
            raise ValueError
        self.__surname=surname
        self.__name=name
        self.__patronymic=patronymic
        self.__phone=phone
        self.__city=city
    def __str__(self):
        return f'Surname:{self.__surname}, Name:{self.__name}, Patronymic:{self.__patronymic}, Phone:{self.__phone}, City:{self.__city}'
class Order:
    def __init__(self,customer,*products):
        if not(isinstance(customer,Customer) and all(isinstance(product,Product) for product in products)):
            raise TypeError
        self.__customer=customer
        self.__products=list(products)
    def __str__(self):
        return f'{self.__customer}. Total value: {self.total_value()}'
    def total_value(self):
        total=0
        for product in self.__products:
            total+=product.price
        return total
        
    def addproducts(self,*products):
        if not all(isinstance(product,Product) for product in products):
            raise TypeError
        self.__products+=list(products)
        
    def delproducts(self,*products):
        if not all(isinstance(product,Product) for product in products):
            raise TypeError
        for product in products:
            self.__products.remove(product)
            
    def infoprod(self):
        return self.__products
    def infocust(self):
        return self.__customer

try:
    milk=Product("milk",100,"white","1L")
    apple=Product("apple",50,"green","100g")
    orange=Product("orange",20,"orange","50g")
    pavlo=Customer("Nedashkivskiy","Pavlo","Sergiyovich","+564626","Kiev")
    first=Order(pavlo,milk,apple)
    first.addproducts(orange)
    first.delproducts(apple)
    print(first)
except ValueError:
    print("Enter correct values")
except TypeError:
    print("Type error")
except NameError:
    print("Name error")