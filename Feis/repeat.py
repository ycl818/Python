def Repeat (iterable, times):
    for i in range(times):
        for v in iterable:
            yield v

a = (1,2,3)

for v in a*2:
    print(v)

for v in Repeat(a,2):
    print(v)
    
