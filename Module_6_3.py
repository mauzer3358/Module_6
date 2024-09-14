class Horse:
    def __init__(self, dx):
        self.dx = dx
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        #if isinstance(dx, int):
        self.x_distance += dx
        return self.x_distance

class Eagle:
    def __init__(self, dy):
        self.dy = dy
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        if isinstance(dy, int):
            self.y_distance = self.y_distance + dy
        return self.y_distance


class Pegasus(Horse, Eagle):
    list_gpX = []
    list_gpY = []
    def __init__(self):
        Horse.__init__(self, 0)
        Eagle.__init__(self, 0)

    def move(self, dx, dy):
        Horse.__init__(self, dx)
        Eagle.__init__(self, dy)
        super().run(dx)
        super().fly(dy)
        return


    def get_pos(self):
        if self.x_distance == 0 and self.y_distance == 0:
            GP = (self.x_distance, self.y_distance)
            return GP
        else:
            self.list_gpX.append(self.x_distance)
            self.list_gpY.append(self.y_distance)
            GP = (sum(self.list_gpX), sum(self.list_gpY))
            return GP


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
#
# Примечания:
#
# Будьте внимательней, когда вызываете методы классов родителей в классе наследнике при множественном наследовании: при обращении через super() методы будут искаться сначала в первом, потом во втором и т.д. классах по mro().
# Заметьте, что Pegasus издаёт звук "I train, eat, sleep, and repeat", т.к. по порядку сначала идёт наследование от Horse, а после от Eagle.
