def flip_vertical_axis(matrix):    
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
    return matrix


print(flip_vertical_axis([[1,2,3],[4,5,6],[7,8,9]]))

#1 2 3  #3 2 1
#4 5 6  #6 5 4
#7 8 9  #9 8 7