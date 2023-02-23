def valida_data(dia,mes,ano):
    if ano<=0:
        return False
    else:
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia<=31:
                return True
            else:
                return False
        elif mes == 4 or mes==6 or mes == 9 or mes == 11:
            if dia<=30:
                return True
            else:
                return False
        elif mes == 2:
            if ano%4!=0:
                if dia<=28:
                    return True
                else:
                    return False
            elif ano%4==0 and ano%400==0:
                if dia<=29:
                    return True
                else:
                    return False
            elif ano%4==0 and ano%100==0 and not ano%400==0:
                if dia<=28:
                    return True
                else:
                    return False
            else:
                if dia<=29:
                    return True
                else:
                    return False
        else:
            return False


print(valida_data(29,2,2019))