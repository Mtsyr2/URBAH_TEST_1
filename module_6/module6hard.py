from math import pi, sqrt, pow


class Figure:
    sides_count = 0
    filled: bool = True

    def __init__(self, color: tuple, *sides):
        self.__sides: list[int] = [*sides]
        self.__color = list(color)

    def get_color(self):
        return self.__color

    def __is_valid_color(self,  r: int, g: int, b: int):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, sides):
        if len(self.get_sides()) != self.sides_count:
            return False
        for side in self.get_sides():
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        new = [*new_sides]

        if len(new) == self.sides_count:
            self.__sides = new

    def check_side_count(self):
        if len(self.__sides) != self.sides_count:
            new = [1] * self.sides_count
            self.__sides = new


class Circle(Figure):
    sides_count = 1
    __radius = 0

    def set_radius(self):
        self.__radius = self.__len__() / (2 * pi)
        return self.__radius

    def get_square(self):
        return pi * self.__radius * self.__radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: tuple, *sides):
        super().__init__(color, *sides)
        self.pp = 0
        self.check_side_count()

    def check_triangle(self):
        if sum(sorted(super().get_sides())[0:2])<=sorted(super().get_sides())[2]:
            return False
        else:
            return True

    def get_square(self):
        if self.check_triangle():
            self.pp = super(Triangle, self).__len__() / 2  # полупериметр
            return sqrt((self.pp * (self.pp - super().get_sides()[0]) * (self.pp - super().get_sides()[1]) *
                         (self.pp - super().get_sides()[2])))
        else:
            return 'Треугольник не существует!'


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple, *sides):
        super().__init__(color, *sides)
        self.check_side_cube()

    def check_side_cube(self):
        if len(self.get_sides()) > 1:
            new = [self.get_sides()[0]]*12
            self.set_sides(*new)

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


if __name__ == '__main__':
    main()
