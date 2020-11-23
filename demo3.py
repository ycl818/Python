def f():
  i=1
  while i<=5:
    yield i
    i+=1

for x in f():
  print(x)