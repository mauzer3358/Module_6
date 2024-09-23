import math

# Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
# Атрибуты(публичные): filled(закрашенный, bool)

# И методами:

class Figure:
    def __init__(self, R=0,G=0,B=0, side_count = 0, *side):

        self.RGB = [R,G,B]
        self.side = side[0]
        self.__color = []
        self.__sides = []
        self.len_sides = [] #КОличесвто получаемых сторон
        self.side_count = side_count
        self.filled = False
        ####
        Figure.__is_valid_color(self, self.RGB)
        Figure.set_sides(self, self.side)
        self.len_fig = 0


    # Метод get_color, возвращает список RGB цветов.

    def get_color(self):
        return self.__color


    # Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет
    # корректность переданных значений перед установкой нового цвета. Корректным цвет:
    # все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).

    def __is_valid_color(self, *rgb):
        color = []
        if len(rgb[0]) == 3:   #проверка состава цвета
            for i in rgb[0]:
                if isinstance(i, int) and i>=0 and i<=255: # проверка, что целые числа переданы
                    color.append(i) # переводим в список цвета
            Figure.set_color(self, *color)



    # Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
    # предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.

    def set_color(self,*tuple1):
        color = []
        if len(tuple1) == 3:   #проверка состава цвета
            for i in tuple1:
                if isinstance(i, int) and i>=0 and i<=255: # проверка, что целые числа переданы
                    color.append(i) # переводим в список цвета
                else: return self.__color
            self.__color = color
        return self.__color


# Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые
# положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.

    def __is_valid_sides(self,*args):
        for i in args[0]:
            if isinstance(i,int) and i>0 and len(args[0]) == self.side_count:
                return True
            else:
                return False


    # Метод set_sides(self, *new_sides) должен принимать новые стороны,
    # если их количество не равно sides_count, то не изменять, в противном случае - менять.
    def set_sides(self,*new_sides):
        if type(new_sides[0]) == int:
            self.New_Sides = new_sides
        else:
            self.New_Sides = new_sides[0]

        if self.filled == True and len(self.New_Sides) > 1:
            return self.__sides

        valid = Figure.__is_valid_sides(self, self.New_Sides, int(self.side_count))
        if self.side_count == 1: ### Действия, если количество сторо 1###
            self.__sides = []
            if valid == True:
                self.__sides.append(self.New_Sides[0])
                return self.__sides
            else:
                self.__sides.append(1)
                return self.__sides
        if self.side_count == 12:   # Действия, если количество сторо 12#
            list_sides = []
            if valid == False and len(self.New_Sides)==1:
                for j in range(0, self.side_count):
                    list_sides.append(self.New_Sides[0])
                self.filled = True
                self.__sides = list_sides
                return self.__sides
            elif valid == False or 1 < len(self.New_Sides)< self.side_count:
                for j in range(0, self.side_count):
                    list_sides.append(int(1))
                self.__sides = list_sides
                return self.__sides
        if self.side_count == 3:   # Действия, если количество сторо 3#
            list_sides = []
            if valid == False and len(self.New_Sides)==1:
                for j in range(0, self.side_count):
                    list_sides.append(self.New_Sides[0])
                #self.filled = True
                self.__sides = list_sides
                return self.__sides
            elif valid == False or 1 < len(self.New_Sides) < self.side_count:
                for j in range(0, self.side_count):
                    list_sides.append(int(1))
                self.__sides = list_sides
                return self.__sides


# Метод get_sides должен возвращать значение я атрибута __sides.

    def get_sides(self):
        return self.__sides

    def get_square(self):
        if len(self.__sides) == 1:
            print(len(self.__sides))
            S = pow(self.__sides[0], 2) / (4 * math.pi)
            return S
        if len(self.__sides) == 3:
            pp = 0.5*(self.__sides[0] + self.__sides[1] + self.__sides[2])
            S = math.sqrt (pp*(pp - self.__sides[0])*(pp - self.__sides[1])*(pp - self.__sides[2]))
            return S


# Метод __len__ должен возвращать периметр фигуры.

    def __len__(self):
        self.len_fig = sum(self.__sides)
        return self.len_fig





# Атрибуты класса Circle: sides_count = 1
# Каждый объект класса Circle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
# Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
class Circle(Figure):
    def __init__(self, *args):
        self.RGB = args[0]
        Circle.RGB_int(self,self.RGB)
        self.side = args[1:]
        self.sides_count = 1
        super().__init__(self.R, self.G, self.B,self.sides_count, self.side)
        self.__radius = 0



    def RGB_int(self, *args):
        self.R = args[0][0]
        self.G = args[0][1]
        self.B = args[0][2]


    def radius(self):
        # r = L/2п
        self.__radius = self.len_fig/(2*math.pi)
        return self.__radius

# Атрибуты класса Triangle: sides_count = 3
# Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)

class Triangle(Figure):
    def __init__(self, *args):
        self.RGB = args[0]
        Circle.RGB_int(self, self.RGB)
        self.side = args[1:]
        self.sides_count = 3
        super().__init__(self.R, self.G, self.B, self.sides_count, self.side)


# Атрибуты класса Cube: sides_count = 12
# Каждый объект класса Cube должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure.
# Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
# Метод get_volume, возвращает объём куба.

class Cube(Figure):
    def __init__(self, *args):
        self.RGB = args[0]
        Circle.RGB_int(self,self.RGB)
        self.side = args[1:]
        self.sides_count = 12
        super().__init__(self.R, self.G, self.B,self.sides_count, self.side)


    def get_volume(self):
        V = pow(self._Figure__sides[0],3)
        return V



# Код для проверки:

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
#
#
#
# # # # Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
# # # #
# # # # # Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
#
# # #
# # # # Проверка периметра (круга), это и есть длина:
print(len(circle1))

# # #
# # # # Проверка объёма (куба):
print(cube1.get_volume())


#
#
# #Выходные данные (консоль):
# #
# # [55, 66, 77]
# # [222, 35, 130]
# # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# # [15]
# # 15
# # 216
#
# # ВАЖНО!
# #
# # При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count,
# # то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
#Circle((200, 200, 150), 10, 15, 6), #т.к. сторона у круга всего 1, то его стороны будут - [1]
#Triangle((111, 222, 99), 10, 6) #т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
# Cube((200, 200, 100), 9), # т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
# Cube((200, 200, 100), 9, 12), #т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]


# Примечания (рекомендации):
#
# Рекомендуется сделать дополнительные (свои проверки) работы методов объектов каждого класса.
# Делайте каждый класс и метод последовательно и проверяйте работу каждой части отдельно.
# Для проверки принадлежности к типу рекомендуется использовать функцию isinstance.
# Помните, служебные инкапсулированные методы можно и нужно использовать только внутри текущего класса.
# Вам не запрещается вводить дополнительные атрибуты и методы, творите, но не переборщите!