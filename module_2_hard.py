import random

first_number = random.randint(3, 20)


def get_password(a):
    result = ''
    for i in range(1, a):
        for j in range(1, a):
            if a % (i+j) == 0:
                if i < j:
                    result+=str(i)
                    result+=str(j)

    return result


print(f'Число на первом камне: {first_number}\nПароль: {get_password(first_number)}')
