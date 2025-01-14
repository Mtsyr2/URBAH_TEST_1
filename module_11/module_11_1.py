
import pandas as pd
import matplotlib.pyplot as plt


def main():

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
