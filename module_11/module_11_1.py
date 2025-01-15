
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():

    # работа с массивами

    array = np.arange(2, 12)
    print('Массив исходный:', array)

    # Математические операции
    added_array = array + 10
    multiplied_array = array * 2
    mean_value = np.mean(array)
    sum_value = np.sum(array)
    max_value = np.max(array)
    min_value = np.min(array)

    # Вывод результатов
    print("Прибавляем 10 к каждому элементу:", added_array)
    print("Удваиваем каждый элемент:", multiplied_array)
    print("Среднее значение:", mean_value)
    print("Сумма элементов:", sum_value)
    print("Максимальное значение:", max_value)
    print("Минимальное значение:", min_value)
    print('#'*30)

    filename = 'Euro_2012_stats_TEAM.csv'

    data = pd.read_csv(filename)

    # возвращает название столбцов
    print(data.columns)

    # данные выбранной команды
    print(data[data['Team'] == 'Denmark'])
    print(data['Team'])

    # возвращает среднее значение
    avg_goals = data['Goals'].mean()
    print(f'Среднее значение забитых голов: {avg_goals}')

    data_plt = data[['Team','Yellow Cards']].sort_values('Yellow Cards')
    print(data_plt)

    # визуализация полученных желтых карточек
    data_plt.plot(x='Team', y='Yellow Cards', kind='bar')
    plt.xlabel('Страна')
    plt.title('Жёлтые карточки')
    plt.show()


if __name__ == '__main__':
    main()
