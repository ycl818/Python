a=3
b=5

def f(x):
  a=6
  print(globals())
  print(locals())

f(4)


#a=3

#def f():
  #global a
 # a=4

#f()
#print(a)