# import requests
import pandas as pd
import matplotlib.pyplot as plt



def main():

    filename = 'Euro_2012_stats_TEAM.csv'

    data = pd.read_csv(filename)
    print(data.columns)  # возвращает название столбцов
    print(data[data['Team'] == 'Denmark'])
    avg_goals = data['Goals'].mean()  # возвращает среднее значение
    print(f'Среднее значение забитых голов: {avg_goals}')

    data_plt = data['Yellow Cards'].sort_values(ascending=True)
    data_plt.plot(kind='bar')
    plt.xlabel(data['Team'])
    plt.ylabel(data['Yellow Cards'] > 10)
    plt.title('Жёлтые карточки')
    plt.show()


if __name__ == '__main__':
    main()
