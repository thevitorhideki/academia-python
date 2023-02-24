import copy


def eh_simetrica(matrix):
    standard_matrix = copy.deepcopy(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if len(matrix) == len(matrix[i]):
                matrix[i][j] = matrix[j][i]
            else:
                return False

    if standard_matrix == matrix:
        return True

    return False


print(eh_simetrica([[50, 52, 55], [55, 56, 57], [57, 58, 59]]))
