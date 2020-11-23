x=1

def f():
  def g():
    x=2
    print(x)   #1
  g()
  print(x)     #2

f()
print(x)       #3