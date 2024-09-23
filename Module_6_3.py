class Horse:
    def __init__(self, dx):
        self.x_distance = [0]
        self.sound = 'Frrr'

    def run(self,dx):
         self.x_distance.append(dx)
         return self.x_distance

class Eagle:
    def __init__(self, dy):
        self.y_distance = [0]
        self.sound = 'I train, eat, sleep, and repeat'


    def fly(self,dy):
         self.y_distance.append(dy)
         return self.y_distance


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self, 0)
        Eagle.__init__(self, 0)

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return sum(self.x_distance), sum(self.y_distance)

    def voice(self):
        print(self.sound)
        return self.sound

p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
#
p1.voice()
#
# Вывод на консоль:
#
# (0, 0)
# (10, 15)
# (5, 35)
# I train, eat, sleep, and repeat