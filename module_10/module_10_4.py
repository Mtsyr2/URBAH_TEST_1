import threading
from queue import Queue
from random import randint
from time import sleep


class Table:

    def __init__(self, number: int):
        self.number = number
        self.guest = None


class Guest(threading.Thread):

    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))
        print(f'{self.name} покушал(-а) и ушел(-а)')


class Cafe:

    threads = []

    def __init__(self, *tables: Table):
        self.tables = [*tables]
        self.queue = Queue()

    def guest_arrival(self, *guests: Guest):
        guests = [*guests]
        for i in range(len(self.tables)):
            self.tables[i].guest = guests[i]
            self.tables[i].guest.start()
            print(f'{self.tables[i].guest.name} сел(-а) за стол номер {self.tables[i].number}')
        for guest in guests[len(self.tables):]:
            self.queue.put(guest)

    def discuss_guests(self):
        while True:
            for table in self.tables:
                if not table.guest.is_alive() and not self.queue.empty():
                    print(f'Стол номер {table.number} свободен')
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()
                elif self.queue.empty() and not table.guest.is_alive():
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    break


def main():
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()


if __name__ == '__main__':
    main()