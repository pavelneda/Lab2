class Product:
    def __init__(self,price,desc,dimens):
        self.price=price
        self.desc=desc
        self.dimens=dimens
    def info(self):
        return f'Price:{self.price}, Description:{self.desc}, Dimensions:{self.dimens}'
class Customer:
    def __init__(self,surname,name,patronymic,phone,city):
        self.surname=surname
        self.name=name
        self.patronymic=patronymic
        self.phone=phone
        self.city=city
    def info(self):
        return f'Surname:{self.surname}, Name:{self.name}, Patronymic:{self.patronymic}, Phone:{self.phone}, City:{self.city}'
class Order:
    def __init__(self,customer,*products):
        self.customer=customer
        self.products=list(products)
    def total_value(self):
        total=0
        for product in self.products:
            total+=product.price
        return f'Total value: {total}'
    def info(self):
        return self.customer.info()

try:
    milk=Product(100,"white","1L")
    apple=Product(50,"green","100g")
    tom=Customer("Nedashkivskiy","Pavlo","Sergiyovich","+32382","Kiev")
    first=Order(tom,milk,apple)
    print(first.info())
    print(first.total_value())
except:
    print("None")