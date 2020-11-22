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


# name can point to any object
a=3
a='abc'
a=[3,4,5]
a={5,9}
a=print
a('Hello')
################################
a=3
print(id(a))
a=a+5
print(id(a))

####
a=3
a=5
del a
print(a)