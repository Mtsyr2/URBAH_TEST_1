from fake_math import divide as fd
from true_math import divide as td


def main():
    result1 = fd(69, 3)
    result2 = fd(3, 0)
    result3 = td(49, 7)
    result4 = td(15, 0)
    print(result1)
    print(result2)
    print(result3)
    print(result4)


if __name__ == '__main__':
    main()