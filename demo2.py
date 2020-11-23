def f():
  i=1
  while i<=5:
    yield i
    i+=1

g=f()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))