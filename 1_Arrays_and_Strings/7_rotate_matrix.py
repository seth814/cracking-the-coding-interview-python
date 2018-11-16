def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n//2):
        for i in range(layer, n - layer - 1):
            # copy top
            top = matrix[layer][i]
            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]
            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]
            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]
            # top -> right
            matrix[i][-layer - 1] = top
    return matrix

mat = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
      ]

print(rotate_matrix(mat))
