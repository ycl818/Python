class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'
p = Vector(3,4)
q = Vector(5,6)

print(object.__str__(p))
print(Vector.__str__(p))
print(p.__str__())
print(str(p))


print(p)
print(type(p))