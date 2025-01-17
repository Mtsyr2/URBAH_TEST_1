from math import pi, sqrt, pow


class Figure:
    sides_count = 0
    filled: bool = False

    def __init__(self, color: tuple, *sides):
        self.__sides: list[int] = [*sides]
        self.__color = list(color)
        self.check_side_count()
        if self.get_color():
            self.filled = True

    def __len__(self):
        return sum(self.__sides)

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_color(self,  r: int, g: int, b: int)-> bool:
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def __is_valid_sides(self, sides) -> bool:
        if len(self.get_sides()) != self.sides_count:
            return False
        for side in self.get_sides():
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        new = [*new_sides]

        if len(new) == self.sides_count:
            self.__sides = new

    def check_side_count(self):
        if len(self.__sides) != self.sides_count:
            if self.sides_count == 12:
                new = [self.get_sides()[0]] * 12
            else:
                new = [1] * self.sides_count
            self.__sides = new


class Circle(Figure):
    sides_count = 1
    __radius = 0

    def set_radius(self):
        self.__radius = self.__len__()/(2 * pi)
        return self.__radius

    def get_radius(self):
        return self.__radius

    def get_square(self):
        return pi * pow(self.__radius, 2)


class Triangle(Figure):
    sides_count = 3
    half_perimeter = None

    def check_triangle(self)-> bool:
        """ Проверка треугольника на существование: сумма
        2-х малых сторон больше 3-ей(самой длинной)
        """
        if sum(sorted(self.get_sides())[0:2])<=sorted(self.get_sides())[2]:
            return False
        else:
            return True

    def get_square(self):
        if self.check_triangle():
            self.half_perimeter = self.__len__()/2
            return sqrt((self.half_perimeter * (self.half_perimeter - super().get_sides()[0]) * (self.half_perimeter - super().get_sides()[1]) *
                         (self.half_perimeter - super().get_sides()[2])))
        else:
            return 'Треугольник не существует!'


class Cube(Figure):
    sides_count = 12

    def get_volume(self):
        return pow(self.get_sides()[0], 3)


def main():
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())

    # cube1.set_sides(8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8)
    # print(cube1.get_sides())
    #

    # tri1 = Triangle((200, 200, 100), 10, 3, 2)
    # print(tri1.get_square())
    # tri2 = Triangle((200, 200, 100), 10, 3, 9)
    # print(tri2.get_square())


if __name__ == '__main__':
    main()
