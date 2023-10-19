def minimum(array):
    num_col = 0
    num_row = 0
    
    min = sum(array[0])
    for i, row in enumerate(array):
        cur = sum(row)
        if cur < min:
            min = cur
            num_row = i

    min = sum(row[0] for row in array)
    for j in range(len(array[0])):
        cur = sum(array[i][j] for i in range(len(array)))
        if cur < min:
            min = cur
            num_col = j

    return [num_row, num_col]

print(minimum([[7, 2, 7, 2, 8],
               [2, 9, 4, 1, 7],
               [3, 8, 6, 2, 4],
               [2, 5, 2, 9, 1],
               [6, 6, 5, 4, 5]]))
print(minimum([[-7, -2, -7, -2, -8],
               [-2, -9, -4, -1, -7],
               [-3, -8, -6, -2, -4],
               [-2, -5, -2, -9, -1],
               [-6, -6, -5, -4, -5]]))
