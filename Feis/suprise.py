class Record:
    def init(self, n, s):
        Record.name = n
        Record.score = s


p = Record()
q = Record()

p.init('123', 20)
q.init('456', 30)

print(p.name, p.score)
