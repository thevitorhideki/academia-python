def maximo_divisor_comum(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
        print(num1, num2) 
    return num1
