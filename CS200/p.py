# products= [("cocoa",45),('milktea',10),('bubbletes',65)]

# def helper_sorted(x):
#     return x[1]

# print(sorted(products,key=lambda x:x[1]))

# p0 = {'name':"cocoa",'price':45}
# p1 = {'name':"milktea",'price':10}
# p2 = {'name':"bubbletes",'price':65}

# products = [p0,p1,p2]
# print(sorted(products,key=lambda x:x['price']))

x=['asdfasdfg','appple','qwedscvhgdfd']

print(list(map(len,x)))

y=[1,2,3,4]

print([i*i for i in y])
print(list(map(lambda x:x*x, y)))

def f(x):
    if x>2:
        return False
    else:
        return True
#filter
print([i for i in y if i<3])
print(list(filter(f, y)))       
print(list(filter(lambda x: x<3, y)))


#zip
a = [1,2,3]
b = [4,5,6]

print(list(zip(a,b)))