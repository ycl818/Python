#decorator 裝飾器
import time
def print_func(func):
    def inner():
        print('running', func.__name__)
        func()
    return inner

def time_func(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print('elapsed',end - start, 'seconds')
    return inner

def test():
    for i in range(10000000):
        i+=1


@time_func
@print_func
def test2():
    print('ni hao')

# test()
# print('manufactoting~~~~')

# test =print_func(test)
# test()



#test = time_func(test)

test2()