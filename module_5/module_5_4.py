from typing import List, Any


class House:
    houses_history: list = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])

        return object.__new__(cls)

    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории')

    def go_to(self, new_floor):
        if 1 < new_floor<= self.number_of_floor:
            for floor in range(1, new_floor+1):
                print(floor)
        else:
            print('Такого этажа не существует!')

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floor}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floor == other.number_of_floor

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor < other.number_of_floor

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floor <= other.number_of_floor

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor > other.number_of_floor

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floor >= other.number_of_floor

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floor != other.number_of_floor

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floor += value
            return self

    def __radd__(self, value):
        if isinstance(value, int):
            self.__add__(value)
            return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.__add__(value)
            return self

    def __sub__(self, value):
        if isinstance(value, int):
            if self.number_of_floor < value:
                return 'Такое количество этажей убрать не получится!'
            else:
                self.number_of_floor -= value
                return self
        if isinstance(value, House):
            diff = abs(self.number_of_floor - value.number_of_floor)

            return f'Разница составит {diff} этажей'

    def __rsub__(self, value):
        if isinstance(value, int):
            if self.number_of_floor > value:
                return 'Такое количество этажей убрать не получится!'
            else:
                self.number_of_floor = value - self.number_of_floor
                return self
        if isinstance(value, House):
            return self.__sub__(value)

    def __isub__(self, value):
        return self.__sub__(value)

    def __mul__(self, value):
        new_num = self.number_of_floor
        if isinstance(value, House):
            new_num *= value.number_of_floor
        elif isinstance(value, int):
            new_num *= value
        else:
            return NotImplemented
        return House(self.name, new_num)

    __rmul__ = __mul__

    def __imul__(self, value):
        if isinstance(value, House):
            self.number_of_floor *= value.number_of_floor
        elif isinstance(value, int):
            self.number_of_floor *= value
        else:
            return NotImplemented
        return self

    def __floordiv__(self, value):
        new_number = self.number_of_floor
        if isinstance(value, House):
            new_number //= value.number_of_floor
        elif isinstance(value, int):
            new_number //= value
        else:
            return NotImplemented
        return House(self.name, new_number)

    __rfloordiv__ = __floordiv__

    def __ifloordiv__(self, value):
        if isinstance(value, House):
            self.number_of_floor //= value.number_of_floor
        elif isinstance(value, int):
            self.number_of_floor //= value
        else:
            return NotImplemented
        return self


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)


