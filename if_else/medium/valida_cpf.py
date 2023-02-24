def valida_cpf(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11):
    if x1 == x2 == x3 == x4 == x5 == x6 == x7 == x8 == x9 == x10 == x11:
        return False
    else:
        primeiro_digito=((x1*10+x2*9+x3*8+x4*7+x5*6+x6*5+x7*4+x8*3+x9*2)*10)%11
        segundo_digito=((x1*11+x2*10+x3*9+x4*8+x5*7+x6*6+x7*5+x8*4+x9*3+x10*2)*10)%11
        if primeiro_digito == 10:
            primeiro_digito = 0
        if primeiro_digito==x10 and segundo_digito==x11:
            return True
        else:
                return False

print(valida_cpf(1,2,3,4,5,6,7,8,9,0,9))