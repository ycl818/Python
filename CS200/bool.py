class Vector2:
    def __init__(self,x,y):
        self.x =x
        self.y =y

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __add__(self,other):
        return Vector2(self.x+other.x, self.y+other.y)

    def __str__(self):
        return f'({self.x},{self.y})'

    def __getitem__(self,i):
        if i ==0: return self.x
        if i ==1: return self.y
        raise IndexError


# if Vector2(3,4):
#     print('Non-zero')

# if not Vector2(0,0):
#     print('zero')

p =Vector2(3,4)
q =Vector2(5,6)
print(p)
print(q)
print(p+q)
print(p[0])
print(type(p))
for _ in p: print(_)
