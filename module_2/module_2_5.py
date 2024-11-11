
def get_matrix(n: int, m: int, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(4, 5, 42)
result3 = get_matrix(5, 4, 'urban')
print(result1)
print(result2)
print(result3)