def flip_horizontal_axis(matrix):
    size = len(matrix)
    for i in range(size // 2):
        matrix[i], matrix[size - 1 - i] = matrix[size - 1 - i], matrix[i]