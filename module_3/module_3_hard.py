
def calculate_structure_sum(list_: list):
    sum_ = 0
    for item in list_:
        if isinstance(item, tuple):
            for i in item:
                calculate_structure_sum(list(item))
        elif isinstance(item, dict):
            calculate_structure_sum(list(item))
            calculate_structure_sum(list(item.values()))
        elif isinstance(item, list):
            calculate_structure_sum(item)
        elif isinstance(item, str):
            sum_+=len(item)
        elif isinstance(item, int):
            sum_+=item
        elif isinstance(item, float):
            sum_ += item

        else:
            return sum_
    return sum_


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]

result = calculate_structure_sum(data_structure)
print(result)


#
# # print(isinstance([1, 2, 3], tuple))
# print(sum([1,2,3]))