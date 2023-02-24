def eh_fibonacci(list):
    if len(list) < 3:
        return False

    for i in range(len(list) - 2):
        if list[i + 2] != list[i] + list[i + 1]:
            return False
    
    return True
