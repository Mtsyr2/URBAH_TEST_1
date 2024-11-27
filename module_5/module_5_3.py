
class House:

    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

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
        if isinstance(value, (int, House)):
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
        if not isinstance(value, (int, House)):
            return NotImplemented
        new_num = value if isinstance(value, int) else value.number_of_floor
        return House(self.name, new_num)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

# print(h1 == h2)  # __eq__
#
# h1 = h1 + 10  # __add__
# print(h1)
# print(h1 == h2)
#
# h1 += 10  # __iadd__
# print(h1)
#
# h2 = 10 + h2  # __radd__
# print(h2)
#
# print(h1 > h2)  # __gt__
# print(h1 >= h2)  # __ge__
# print(h1 < h2)  # __lt__
# print(h1 <= h2)  # __le__
# print(h1 != h2)  # __ne__
# print(h1+h2)
print(h1-h2)
