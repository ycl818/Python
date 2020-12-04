class Product:

    def __init__(self,name,price):
        self.name = name  #property
        self.price = price #property

    def __str__(self):
        #return self.name+ ' $' +str(self.price)
        return f'{self.name} ${self.price}'

    #representation
    #if we do not have __str__ ,func "print" will pick "repr" result
    def __repr__(self):
        return f'< Product( {self.name}, ${self.price} ) >'

    def __add__(self,other):
        if isinstance(other,str):
            self.name+=other
        if isinstance(other,Product):
            return [self,other]

    def __mul__(self,other):
        re =[]
        if isinstance(other,int):
            for _ in range(other):
                re.append(self)
        return re


p1 = Product('Bubble milk tea',50) #instance
p2 = Product('Ramen',50)
print(p1 * 5)

#print(repr(p))

class ShoppingCart:
    def __init__(self,products):
        self.products = products

    def __getitem__(self,key):
        return self.products[key]
s =ShoppingCart([p1,p2])
print(s[1])