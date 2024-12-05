from math import pi, sqrt


class Figure:
    sides_count = 0
    filled: bool = True

    def __init__(self, color: tuple, *sides):
        self.__sides: list[int] = [*sides]
        self.__color = list(color)
        # self.check_side_count()

    def get_color(self):
        return self.__color

    def __is_valid_color(self):
        pass

    def set_color(self, r, g, b):
        pass

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

    def set_sides(self, new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = [new_sides]

    def check_side_count(self):
        if len(self.__sides) != self.sides_count:
            self.set_sides([1] * self.sides_count)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: tuple, *sides):
        super().__init__(color, *sides)

        self.__radius = super(Circle, self).__len__() / (2 * pi)

    def get_square(self):
        return pi * self.__radius * self.__radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: tuple, *sides):
        super().__init__(color, *sides)
        self.check_side_count()
        print(self.get_sides())
        self.pp = super(Triangle, self).__len__() / 2  # полупериметр

    def check_triangle(self):
        if sum(sorted(super().get_sides())[0:2])<=sorted(super().get_sides())[2]:
            return False
        else:
            return True

    def get_square(self):
        if self.check_triangle():
            return sqrt((self.pp * (self.pp - super().get_sides()[0]) * (self.pp - super().get_sides()[1]) * (self.pp - super().get_sides()[2])))
        else:
            return 'Треугольник не существует!'


class Cube(Figure):
    pass


def main():
    # circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    # print(circle1.__len__())
    # print(circle1.get_color())
    # print(circle1.get_square())

    tri1 = Triangle((200, 200, 100), 10, 7, 8, 9)
    print(tri1.check_triangle())
    print(tri1.get_square())


if __name__ == '__main__':
    main()
