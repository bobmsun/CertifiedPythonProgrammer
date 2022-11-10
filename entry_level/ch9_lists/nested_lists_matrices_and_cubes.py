

# Lists can contain lists within themselves

my_matrix = [[1, 2, 3], [4, 5, 6]]
print(my_matrix)       # [[1, 2, 3], [4, 5, 6]]

row_count = len(my_matrix)
print(row_count)       # 2

column_count = len(my_matrix[0])
print(column_count)      # 3


print(my_matrix[0][1])       # 2
print(my_matrix[1][1])       # 5


# squre = 2 x 2 matrix
# cube = n x n matrix    (2 x 2 matrix -> two cube, 3 x 3 matrix -> 3 cube)
# cube just means we have the same number of columns as rows

