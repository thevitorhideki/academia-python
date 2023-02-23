def eh_bissexto(ano):
    if ano%4!=0:
        return False
    elif ano%4==0 and ano%400==0:
        return True
    elif ano%4==0 and ano%100==0 and not ano%400==0:
        return False
    else:
        return True
