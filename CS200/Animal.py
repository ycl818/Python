import abc

class Animal(metaclass= abc.ABCMeta):
    @abc.abstractmethod
    def make_sound(self):
        print('asdfdfg') #won't execute, casuse abstract class will be overided
        pass

class Dog(Animal):
    def make_sound(self):
        print('bark')

class Cat(Animal):
    def make_sound(self):
        print('Meow')

class Person(Animal):
    def make_sound(self):
        print('hi')

d = Dog()
d.make_sound()
c= Cat()
c.make_sound()
p= Person()
p.make_sound()

for _ in [d,c,p]:
    _.make_sound()