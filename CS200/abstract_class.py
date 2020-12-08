from abc import ABCMeta, abstractmethod  #abstract base class

class Product(metaclass = ABCMeta): #base class
    @abstractmethod
    def hi(self):
        pass

    @abstractmethod
    def hi2(self):
        pass

class Drink(Product):
    def hi(self):
        print("hi")

    def hi2(self):
        print("hi2")
d = Drink()