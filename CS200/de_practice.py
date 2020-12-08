

def adjust_func(func):
    def inner(n,d):
        try:
            return func(n,d)
        except:
            if d==0:
                print('Remove the exception "Division by zero"')
                return 0           
    return inner

@adjust_func
def divide(n,d):
    return n/d

print(divide(2,3))
print('-----------------------')
print(divide(3,0))