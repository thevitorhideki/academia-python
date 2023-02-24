def quantos_uns(num):
    count = 0
    number = str(num)
    
    for i in range(len(number)):
        if number[i] == '1':
            count += 1
    
    return count

