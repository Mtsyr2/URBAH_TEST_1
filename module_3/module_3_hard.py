
def calculate_structure_sum(data):
    sum_ = 0
    for item in data:
        if isinstance(item, (int, float)):
            sum_+=item
        elif isinstance(item, str):
            sum_+=len(item)
        elif isinstance(item, (set, list, tuple)):
            sum_+=calculate_structure_sum(item)
        elif isinstance(item, dict):
            for key, value in item.items():
                sum_+=calculate_structure_sum([key, value])

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


