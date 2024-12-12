
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(x) - len(y)) for x, y in zip(first, second) if len(x) != len(y))
second_result = (len(first[i]) == len(second[j]) for i in range(len(first)) for j in range(len(second)) if i==j)


def main():
    print(list(first_result))
    print(list(second_result))


if __name__ == '__main__':
    main()
