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
        threading.Thread().__init__(self)
        # super().__init__(self, name)
        # self.name = name


    def run(self):
        sleep(randint(3, 10))


class Cafe:

    def __init__(self, *tables: Table):
        self.tables = [*tables]
        self.queue = Queue()

    def guest_arrival(self, *guests: Guest):
        guests = [*guests]
        for table in self.tables:
            for guest in guests:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    guests.remove(guest)
                else:
                    self.queue.put(guest)

    def discuss_guests(self):
        while not self.queue.empty():
            for table in self.tables:
                if table.guest and table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)\n')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    if not self.queue.empty():
                        new_guest = self.queue.get()
                        table.guest = new_guest
                        print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        new_guest.start()


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