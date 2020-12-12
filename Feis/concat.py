# 使用生成器串接迭代器
#沒有產稱新的tuple 就不用複製 效率高
def Concat(x, y):
  for v in x:
    yield v
  for v in y:
    yield v

a = (1, 2, 3)
b = [4, 5]
c=(6,7,8)
# for v in a + b:
#   print(v)

for v in Concat(Concat(a, b),c):
  print(v)