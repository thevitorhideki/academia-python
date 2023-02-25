def monta_dicionario(arr1: list, arr2: list) -> dict:
    merge_arr = {}

    for i in range(len(arr1)):
        merge_arr[arr1[i]] = arr2[i]

    return merge_arr
