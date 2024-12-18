from time import sleep
import threading


def write_words(word_count, file_name):
    with open(file_name, mode='w', encoding='utf-8') as ff:
        for i in range(1, word_count+1):
            ff.write(f'Какое-то слово №{i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


def main():
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')
    thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
    thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
    thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
    thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()


if __name__ == '__main__':
    main()
