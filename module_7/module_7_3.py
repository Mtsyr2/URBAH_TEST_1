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
        words = self.get_all_words()
        for key in words.keys():
            for w in words[key]:
                if w.lower() == word.lower():
                    words_index[key] = int(words[key].index(word.lower()))+1
        return words_index

    def count(self, word):
        words_count = {}
        words = self.get_all_words()
        for key in words.keys():
            count_ = 0
            for w in words[key]:
                if w.lower() == word.lower():
                    count_ += 1
            words_count[key] = count_
        return words_count


def main():
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова

    print(finder2.find('text'))  # 3 слово по счёту

    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте вс
    # finder1 = WordsFinder('Rudyard Kipling - If.txt', )
    #
    # print(finder1.get_all_words())
    # print(finder1.find('if'))
    # print(finder1.count('if'))


if __name__ == '__main__':
    main()
