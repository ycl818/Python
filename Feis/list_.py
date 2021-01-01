def f(l):
    for v in l:
        yield v+10

l =list(range(5))
print(l)

print(f(l))
print(list(f(l)))


for v in f(l):
    print(v)


