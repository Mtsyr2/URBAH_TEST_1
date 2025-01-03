from time import sleep


def hash_pass(password):
    return hash(password)


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash_pass(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return f'User(nickname = {self.nickname}, age = {self.age})'


class Video:

    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(cls)

    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = 0

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Video(title={self.title}, duration={self.duration}, adult_mode={self.adult_mode})'


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash_pass(password):
                self.current_user = user
                return

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.current_user = new_user
        self.users.append(new_user)

    def log_out(self):
        self.current_user = None

    def add(self, *videos):

        for video in videos:
            if not self.videos:
                self.videos.append(video)
            else:
                for move in self.videos:
                    if move.title != video.title:
                        self.videos.append(video)

    def get_videos(self, search_str):
        found_titles = []
        for video in self.videos:
            if search_str.lower() in video.title.lower():
                found_titles.append(video.title)
        return found_titles

    def watch_video(self, title):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        video = None
        for v in self.videos:
            if v.title == title:
                video = v
        if not video:
            print('Видео не найдено')
            return

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста, покиньте страницу!")
            return

        for second in range(video.time_now+1, video.duration+1):
            print(f" {second} \t")
            sleep(1)

        print('Конец видео')
        video.time_now = 0


def main():
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')


if __name__ == '__main__':
    main()
