from math import inf


def divide(first, second):
    if second == 0:
        return inf
    else:
        return first/second

def is_triangle(*args):
    # [*args].sort()
    return sorted([*args])

def main():
    print(is_triangle(8, 3, 5))



if __name__ == '__main__':
    main()
