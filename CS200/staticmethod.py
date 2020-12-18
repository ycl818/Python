# @staticmethod
# @classmethod 不創造instance但又想用class裡的東西

#不建立instance的情況下可以直接使用class裡的METHOD

class Batman:
    def __init__(self,hp):
        self.hp = hp

    def f(self):
        print("hello")

    @staticmethod
    def cal_avg(x):
        return sum(x) / len(x)

    @classmethod
    def fffff(cls):  #cls represents class
        cls(100).f()  #like temporary create an instance . method

x= [1,2,3]
print(Batman.cal_avg(x))
Batman.fffff()
