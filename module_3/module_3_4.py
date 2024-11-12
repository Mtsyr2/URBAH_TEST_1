
def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word in word:
            print(word)
            same_words += word

    print(other_words)
    return same_words


result1 = single_root_words('1', '11', '123', '234')
print(result1)


