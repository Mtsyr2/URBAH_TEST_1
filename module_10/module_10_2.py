import threading
from time import sleep


class Knight(threading.Thread):

    enemy_count = 100

    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали {self.enemy_count} воинов!!!')
        self.fight()
        print(f'{self.name} отправляется на отдых.')

    def fight(self):
        count_days = 0
        while self.enemy_count:
            sleep(1)
            self.enemy_count -= self.power
            count_days += 1
            print(f'{self.name} сражается {count_days} дней(дня), осталось {self.enemy_count} воинов')
        print(f'{self.name} одержал победу спустя {count_days} дней(дня)!')


def main():
    # Создание класса
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    # Запуск потоков и остановка текущего
    first_knight.start()
    second_knight.start()
    first_knight.join()
    second_knight.join()
    print('Все битвы закончились!!!')
    # Вывод строки об окончании сражения


if __name__ == '__main__':
    main()
