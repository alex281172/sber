matrix = [[0 for i in range(5)] for j in range(5)]
for i in range(5):
    matrix[i][4-i] = 1
print(matrix)


