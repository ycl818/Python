def avg(a, b=0, c=0):
  return (a+b+c)/3

print(avg(3, 4, 5))
print(avg(3, 4))
print(avg(3))


print('--------------------------------')

def avg2(a=0, b=0, c=0):
  return (a+b+c)/3

print(avg2(3, 4, 5))
print(avg2(3, 4))
print(avg2(3))
print(avg2())

print('--------------------------------')

def avg3(a=0, b=4, c=4):
  return (a+b+c)/3

print(avg3(5,c=2))