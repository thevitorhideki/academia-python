def quadrado_magico(arr: list):
    sum_horizontal = sum(arr[0])
    sum_vertical = 0
    sum_diagonal = 0

    for i in range(len(arr)):
        sum_vertical += arr[0][i]
        sum_diagonal += arr[i][i]

    if sum_vertical == sum_horizontal and sum_horizontal == sum_diagonal:
        return True

    return False
