import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self,  speed):
        self.speed = speed
        self._cords=[0, 0, 0]

    def move(self, dx, dy, dz):
        self._cords = [dx * self.speed,  * self.speed, dz * self.speed]

    def get_cords(self):
        print(f'X:{self._cords[0]} Y:{self._cords[1]}, Z:{self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f'Here are(is) {random.randint(1, 4)} eggs for you')


def main():

    bull_ = Animal(20)
    bull_.move(1, 2, 3)
    print(bull_.get_cords())
    # db = Duckbill(10)
    #
    # print(db.live)
    # print(db.beak)
    #
    # db.speak()
    # db.attack()
    #
    # db.move(1, 2, 3)
    # db.get_cords()
    # db.dive_in(6)
    # db.get_cords()
    #
    # db.lay_eggs()


if __name__ == '__main__':
    main()