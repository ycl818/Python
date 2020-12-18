# @property

# encapsulation 封裝

class Batman:
    def __init__(self,hp):
        self.hp = hp #property

    @property
    def hp(self):
        print("asdasd")
        return self._hp
    
    @hp.setter
    def hp(self,hp):
        if hp > 100:
            self._hp = 100
        elif hp < 0:
            self._hp = 0
        else:
            self._hp = hp

            g
b1 =Batman(100)

b1.hp = 300

print(b1.hp)