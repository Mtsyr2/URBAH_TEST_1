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
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        timer = randint(3, 10)
        # print(f'{self.name} будет кушать {timer}')
        sleep(timer)


class Cafe:

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
        while not self.queue.empty():
            for table in self.tables:
                if not (table.guest is None) and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    # table.guest.join()
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