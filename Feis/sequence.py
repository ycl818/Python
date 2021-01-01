def f(*args):
    #*args = l
    # args =([0,1,2,3,4],)
    print(args)

l = list(range(5))

f(l)

f(*l)

