from math import pi


class Figure:
    sides_count = 0
    # __sides: list[int] = []
    # __color: list[tuple] = []

    filled: bool = True

    def __init__(self, color: tuple, *sides):
        self.__sides: list[int] = [*sides]
        self.__color = list(color)

    def get_color(self):
        return self.__color

    def __is_valid_color(self):
        pass

    def set_color(self, r, g, b):
        pass

    def __is_valid_sides(self,):
        pass

    def get_sides(self):
        return self.__sides

    def len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(*new_sides) == self.sides_count:
            self.__sides = [*new_sides]


class Circle(Figure):
    sides_count = 1

    # __radius = __sides[0]/(2*pi)


class Triangle(Figure):
    pass


class Cube(Figure):
    pass


def main():
    circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
    print(circle1.__len__())
    print(circle1.get_color())
    print(circle1.__radius)


if __name__ == '__main__':
    main()
