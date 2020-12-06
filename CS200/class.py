class Record:

   
    def __init__(self,name,scores):
        self.name = name
        self.scores = scores

   


q = Record('hello',20)
print(q.name,q.scores)
print(Dtype(q))