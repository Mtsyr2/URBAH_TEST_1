
class Animal:

    def __init__(self):
        self.alive = True
        self.fed = False

    def eat(self, food):
        self.food = food



class Plant:

    def __init__(self, name):
        self.edible = False
        self.name = name


class Mammal(Animal):

    def __init__(self, name):
        super().__init__()
        self.name = name


class Predator(Animal):

    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name


class Flower(Plant):
    pass

class Fruit(Plant):
    pass


def main():
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    # p1 = Flower('Цветик семицветик')
    #     # p2 = Fruit('Заводной апельсин')

    print(a1.name, a2.name)


if __name__ == '__main__':
    main()
