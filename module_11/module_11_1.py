import requests


def main():
    response = requests.get('https://api.github.com/events')
    print(response.status_code)  # Вывести статус ответа
    print(response.headers['content-type'])  # Вывести заголовок content-type ответа
    print(response.json())  # Вывести содержимое ответа в формате JSON


if __name__ == '__main__':
    main()