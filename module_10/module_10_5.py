
from datetime import datetime
from multiprocessing import Pool

files_ = ['file 1.txt',
          'file 2.txt',
          'file 3.txt',
          'file 4.txt'
          ]


def read_info(name):
    all_data = []
    with open(name, mode='r', encoding='utf-8') as ff:
        while ff.readline():
            all_data.append(ff.readline())


def main():
    t1 = datetime.now()
    for file in files_:
        read_info(file)
    t2 = datetime.now()
    print(t2 - t1)


if __name__ == '__main__':
    # линейно
    main()

    # многопроцессно
    t3 = datetime.now()
    with Pool(4) as p:
        p.map(read_info, files_)
    t4 = datetime.now()
    print(t4 - t3)
