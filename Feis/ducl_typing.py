class Rectangle:
    def __init__(self,*args):
        self.args =args
    def draw(self):
        print(f'[Triangle]')
        print(f'x :'+str([v for v in self.args][0]),f'y :'+str([v for v in self.args][1]))
r = Rectangle(10,20,30,40)
r.draw()