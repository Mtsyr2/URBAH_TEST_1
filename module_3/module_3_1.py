
calls = 0


def count_calls():
    global calls
    calls+=1


def string_info(string: str)->tuple:
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string: str, list_to_search: list)->bool:
    count_calls()
    if string.lower() in [item.lower() for item in list_to_search]:
        return True
    else:
        return False


print(string_info('Identification'))
print(string_info('Percussion'))
print(is_contains('МиФ', ['мирР', 'МаФин', 'миФический', 'миф']))
print(is_contains('lab', ['AlaBama', 'Labor', 'Labrador', 'Club']))
print(calls)

