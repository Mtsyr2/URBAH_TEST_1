from datetime import datetime
from time import sleep
import threading

data = {'example1.txt': 10,
        'example2.txt': 30,
        'example3.txt': 200,
        'example4.txt': 100}

data2 = {'example5.txt': 10,
         'example6.txt': 30,
         'example7.txt': 200,
         'example8.txt': 100}


def write_words(word_count, file_name):
    with open(file_name, mode='w', encoding='utf-8') as ff:
        for i in range(1, word_count+1):
            ff.write(f'Какое-то слово №{i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


def main():
    time1 = datetime.now()
    for k, v in data.items():
        write_words(v, k)
    time2 = datetime.now()
    print(f'Время работы функций {time2-time1}')

    time3 = datetime.now()
    treads = [threading.Thread(target=write_words, args=(v, k)) for k, v in data2.items()]
    for thread in treads:
        thread.start()
    for thread in treads:
        thread.join()

    time4 = datetime.now()
    print(f'Время работы потоков {time4-time3}')


if __name__ == '__main__':
    main()
