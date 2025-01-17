import numpy as np


class Array:

    def __init__(self, a: int, b: int):
        self.array = np.arange(a, b)
        # print(self.array)

    def add_array(self, number):
        return self.array + number

    def multi_array(self, number):
        return self.array * number

    def mean_value(self):
        return np.mean(self.array)

    def __repr__(self):
        return f'{self.array}'


def main():

    # работа с массивами

    ar = Array(2, 12)
    print(ar)
    print(ar.add_array(23))
    print(ar.mean_value())

    # Математические операции


    # # Вывод результатов
    # print("Прибавляем 10 к каждому элементу:", added_array)
    # print("Удваиваем каждый элемент:", multiplied_array)
    # print("Среднее значение:", mean_value)
    # print("Сумма элементов:", sum_value)
    # print("Максимальное значение:", max_value)
    # print("Минимальное значение:", min_value)
    # print('#'*30)


if __name__ == '__main__':
    main()
