class Foo:
    bar = 5  # 類別物件內可以定義屬性(attribute)


f = Foo()
g = Foo()  # f, g 根本沒bar 但能用
print(Foo.bar, f.bar, g.bar)
print(Foo.bar)  # 類別裡面取物件

Foo.bar = 10
print(Foo.bar)
print(type(Foo))


class Record:
    pass


p = Record()  # 產生一個物件
print(type(p))
print(id(p))
Record.name = "Yi-Chien Lee"  # 可以
Record.scores = 100
