t =('YIchien','60','D')

print(t)
print(type(t))

t2 = sorted(t)

print(t2)
print(type(t2))



 # iterator is not a sequence
t3 = reversed(t)
print(type(t3))
print(t3)

for i in t3:
    print(i)