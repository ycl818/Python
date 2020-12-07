class Vector3:
    def __init__(self,x,y,z):
        self.x,self.y,self.z=x,y,z
    def __str__(self):
        return f'({self.x},{self.y},{self.z})'
    def __add__(self,other):
        return Vector3(self.x+other.x,self.y+other.y,self.z+other.z)
    def length(self):
        return (self.x**2+self.y**2+self.z**2)**0.5
    def __abs__(self):
        return self.length()
    def __getitem__(self,i):
        if i == 0: return self.x
        if i == 1: return self.y
        if i == 2: return self.z
        raise IndexError("Out of range XDDD")


a = Vector3(3,4,5)



# print(a[0])
# print(a.__getitem__(0))
# print(Vector3.__getitem__(a,0))
# print(a[1])
# print(a[2])
# print(a[5])

# print(a)
# print(a.x)
# print(b)
# print(a+b)
# print(a.length())
# print(abs(a))


