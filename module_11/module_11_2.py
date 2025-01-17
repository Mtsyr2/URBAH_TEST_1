import inspect
from pprint import pprint
from test2 import Array

test = 'Строка'

def introspection_info(obj):
    attr = []
    methods = []
    for item in dir(obj):
        if callable(getattr(obj, item)):
            methods.append(item)
        else:
            attr.append(item)

    result = {'type': type(obj).__name__, 'attributes': attr, 'methods': methods}

    return result


def main():
    # some_number = 43
    # pprint(introspection_info(some_number))
    # pprint(introspection_info(Array))
    pprint(introspection_info(test))


if __name__ == '__main__':
    main()
