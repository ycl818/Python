def f(l):
    for v in l:
        yield v+10

g = f([1,2,3])
print(g)
print(*g)

g = (v+10 for v in [1,2,3])
print(g)
print(*g)