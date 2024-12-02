
class Animal:

    def __init__(self):
        self.food = None
        self.alive = True
        self.fed = False
        self.name = None

    def eat(self, food):
        self.food = food
        if self.food.edible:
            print(f'{self.name} съел {self.food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {self.food.name}')
            self.alive = False


class Plant:

    def __init__(self):
        self.edible = False


class Mammal(Animal):

    def __init__(self, name):
        super().__init__()
        self.name = name


class Predator(Animal):

    def __init__(self, name):
        super().__init__()
        self.name = name


class Flower(Plant):

    def __init__(self, name):
        super().__init__()
        self.name = name


class Fruit(Plant):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.edible = True


def main():
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)
    print(a2.name)
    print(p2.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)


if __name__ == '__main__':
    main()
