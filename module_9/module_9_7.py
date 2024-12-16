def is_prim(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for i in range(2, result//2+1):
            if result % i==0:
                print('Составное')
                break
        else:
            print('Простое')
        return result
    return wrapper


@is_prim
def sum_three(a: int, b: int, c: int):
    sum_= a+b+c
    return sum_


def main():
    result = sum_three(2, 3, 6)
    print(result)
    # result2 = sum_three(7, 5, 7)
    # print(result2)
    # result3 = sum_three(3, 3, 12)
    # print(result3)


if __name__ == '__main__':
    main()
