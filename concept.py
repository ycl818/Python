print(type(3))
print(id(3))
print(type('3'))
print(id('3'))
print(3+4)
print('3'+'4')
print(id(print))


# Both a and b point to an object 3
# a and b are names, and they just point to object 3
a=3
b=a
print(type(a))
print(type(b))
print(id(a))
print(id(b))