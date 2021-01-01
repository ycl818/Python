def add10(l):
    for v in l:
        yield v+10

s = list(add10([1,2,3,4]))
print(s)

s = [*add10([1,2,3,4])]
print(s)

s = [v+10 for v in [1,2,3,4]]
print(s)