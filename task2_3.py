class Product:
    def __init__(self,name,price,desc,dimens):
        if type(name)==str and type(price)==int and type(desc)==str and type(dimens)==str :
            if name.isalpha() and price >=0 and desc and dimens:
                self.name=name
                self.price=price
                self.desc=desc
                self.dimens=dimens
            else:
                raise ValueError
        else: 
            raise TypeError
    def __str__(self):
        return f'Name:{self.name}, Price:{self.price}, Description:{self.desc}, Dimensions:{self.dimens}'
class Customer:
    def __init__(self,surname,name,patronymic,phone,city):
        if type(surname)==str and type(name)==str and type(patronymic)==str and type(phone)==str and type(city)==str:
            if surname.isalpha() and name.isalpha() and patronymic.isalpha() and phone and city:
                self.surname=surname
                self.name=name
                self.patronymic=patronymic
                self.phone=phone
                self.city=city
            else:
                raise ValueError
        else:
            raise TypeError
    def __str__(self):
        return f'Surname:{self.surname}, Name:{self.name}, Patronymic:{self.patronymic}, Phone:{self.phone}, City:{self.city}'
class Order:
    def __init__(self,customer,*products):
        if isinstance(customer,Customer) and all(isinstance(product,Product) for product in products):
            self.customer=customer
            self.products=list(products)
        else:
            raise TypeError
    def total_value(self):
        total=0
        for product in self.products:
            total+=product.price
        return f'Total value: {total}'
    def addproducts(self,*products):
        if all(isinstance(product,Product) for product in products):
            self.products+=list(products)
        else:
            raise TypeError
    def delproducts(self,*products):
        if all(isinstance(product,Product) for product in products):
            for product in products:
                self.products.remove(product)
        else:
            raise TypeError
    def infoprod(self):
        return self.products
    def infocust(self):
        return self.customer

try:
    milk=Product("milk",100,"white","1L")
    apple=Product("apple",50,"green","100g")
    orange=Product("orange",20,"orange","50g")
    pavlo=Customer("Nedashkivskiy","Pavlo","Sergiyovich","+564626","Kiev")
    first=Order(pavlo,milk,apple)
    first.addproducts(orange)
    first.delproducts(apple)
    print(first.infocust())
    information=list(first.infoprod())
    for x in information:
        print(x)
    print(first.total_value())
except ValueError:
    print("Enter correct values")
except TypeError:
    print("Type error")
except NameError:
    print("Name error")