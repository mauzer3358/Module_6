import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = [*color] if self.__is_valid_color(*color) else [0,0,0]
        self.set_color(self.__color)
        self.__sides = [*sides]  if len(sides) == self.sides_count else [1] * self.sides_count
        self.filled = False




    def __is_valid_color(self, *color):
        if type(color[0]) == int:
            valid_color = color
        elif type(color[0]) == tuple:
            valid_color = color[0]

        for i in valid_color:
            if isinstance(i,int) and (0<=i<=255):
                return True
            else:
                return False

        pass
    def set_color(self, *color):
        if type(color) == list:
            set_list = color[0]
        else:
            set_list = color

        if self.__is_valid_color(set_list):
            self.__color = set_list
            return self.__color
        else:
            return self.__color

        pass

    def get_color(self):
        return list(self.__color)


    def __is_valid_sides(self, sides):
        for i in sides:
            if isinstance(i, int):
                return True
            else: False


    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        new_sides = list(new_sides)
        if (self.__is_valid_sides(new_sides) and
                len(new_sides)== self.sides_count):
            self.__sides = new_sides
        return self.__sides


    def __len__(self):
        self.len_fig = sum(self.__sides)
        return self.len_fig




class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *sides):
        self.Circle__color = color
        self.Circle__sides = sides
        super().__init__(self.Circle__color, *self.Circle__sides)
        self._Circle__radius = self.get_sides()[0]/(2*math.pi)
        self.__radius = self.get_sides()[0]/(2*math.pi)

    def get_square(self):
        self.square = math.pi * (self.__radius ** 2)
        return self.square


class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides):
        self.Triangle__color = color
        self.Triangle__sides = sides
        super().__init__(self.Triangle__color, *self.Triangle__sides)

    def get_square(self):
        print('ssss', self.get_sides())
        pp = 0.5 * (self.get_sides()[0] + self.get_sides()[1]
                    + self.get_sides()[2])
        S = math.sqrt(pp * (pp - self.get_sides()[0]) *
                      (pp - self.get_sides()[1]) *
                      (pp - self.get_sides()[2]))
        return S



class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        self.Cube__color = color
        self.Cube__sides = sides
        super().__init__(self.Cube__color, *self.Cube__sides)
        self.set_sides(*list(sides) * 12)

    def get_volume(self):
        V = self.get_sides()[0]**3
        return V

    pass




circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

