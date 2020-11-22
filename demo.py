def f():
  #return 3
  print('A')
  yield 3
  print('B')
  yield 5
  print('C')
  yield 7
  print('D')
  
g=f()  #生成器存到g(generator)裡面
       #生成器是種迭代器(iterator))
print(next(g))
print(next(g))
print(next(g))
next(g)
