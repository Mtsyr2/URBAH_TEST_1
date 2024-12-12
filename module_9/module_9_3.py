
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(x) - len(y)) for x, y in zip(first, second) if len(x) != len(y))
second_result = (len(x[i]) == len(y[i]) for x in first for y in second for i in range(len(first)-1))


def main():
    print(list(first_result))
    print(list(second_result))


if __name__ == '__main__':
    main()
