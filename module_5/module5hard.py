

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
            for move in self.videos:
                if move.title != video.title:
                    self.videos.append(video)

    def get_videos(self, search_str):
        found_titles = []
        for title in self.videos:
            if search_str.lower() in title.lower():
                found_titles.append(title)
        return found_titles

    def watch_video(self):
        pass



def main():
    pass


if __name__ == '__main__':
    main()
