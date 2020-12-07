for v in [1,2,3]:
 	print(v)

"""for in 會呼叫 iter() ，可以呼叫iter的物件叫可迭代的(iterable)"""
for v in iter([1,2,3]): 	
    print(v)

""" iter的回傳值是的迭代器物件(iterator)"""
"""迭代器(iterator)可以呼叫 next 得到下一個物件"""

p =(iter([1,2,3]))
v = next(p) 
print(v)
v = next(p)
print(v)
v = next(p)
print(v)
"""迭代器(iterator)沒有下一個物件時會發生 StopIteration 錯誤"""
next(p)



#######################################
p =(iter([1,2,3]))
try:
    while True:
        v = next(p) 
        print(v)
except StopIteration:
    pass