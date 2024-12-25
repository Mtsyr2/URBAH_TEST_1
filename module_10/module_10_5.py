
from datetime import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, mode='r', encoding='utf-8') as ff:
        while ff.readline():
            all_data.append(ff.readline())


if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    # линейно
    t1 = datetime.now()
    for file in filenames:
        read_info(file)
    t2 = datetime.now()
    print(t2 - t1)


    # многопроцессно
    t3 = datetime.now()
    with Pool(4) as p:
        p.map(read_info, filenames)
    t4 = datetime.now()
    print(t4 - t3)
