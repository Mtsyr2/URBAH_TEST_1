import string


class WordsFinder:

    def __init__(self, *files):
        self.file_names = [*files]

    def get_all_words(self):
        all_words ={}
        for file in self.file_names:
            with open(file, mode='r', encoding='utf-8') as f:
                all_words[file] = f.read().lower().translate(str.maketrans('', '', string.punctuation)).split()
        return all_words

    def find(self, word):
        words_index = {}
        for key in self.get_all_words().keys():
            for word in list(self.get_all_words()[key]):
                if word == word:
                    words_index[key] = int(list(self.get_all_words()[key]).index(word))+1
        return words_index

    def count(self, param):
        pass


def main():
    finder2 = WordsFinder('test_file.txt')
    # print(finder2.get_all_words())  # Все слова

    print(finder2.find('text'))  # 3 слово по счёту

    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте вс


if __name__ == '__main__':
    main()
