
def custom_write(file_name, strings):
    strings_positions = {}
    count_ = 1
    file = open(file_name, mode='a', encoding='utf-8')
    for item in strings:
        pos = file.tell()
        file.write(f'{item}\n')
        strings_positions[count_, pos] = item
        count_+=1
    file.close()
    return strings_positions


def main():
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)


if __name__ == '__main__':
    main()
