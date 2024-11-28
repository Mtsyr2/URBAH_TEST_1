

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

    def log_in(self):
        pass

    def register(self):
        pass

    def log_out(self):
        pass

    def add(self):
        pass

    def get_videos(self):
        pass

    def watch_video(self):
        pass



def main():
    pass


if __name__ == '__main__':
    main()
