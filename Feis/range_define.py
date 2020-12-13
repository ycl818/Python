"""
這種會有問題參數對不好
"""

# class Range:
#     def __init__(self,start=0,stop=10):
#         self.stop = stop


#     def __getitem__(self,i):
#         if i == self.stop:
#             raise IndexError
#         return i

# for v in Range(5):
#     print(v)

# for v in Range(1,5):
#     print(v)

class Range:
    def __init__(self,*args):
        # *args =5  => args =(5,)
        if len(args) == 1:
            self.start = 0
            self.stop =args[0]
            return
        # *args =1,5 =>args = (1,5)
        if len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
            return
        raise TypeError  # when no parameter

    def __getitem__(self,i):
        v = self.start + i
        if v == self.stop:
            raise IndexError
        return v

for v in Range(5):
    print(v)

for v in Range(1,5):
    print(v)