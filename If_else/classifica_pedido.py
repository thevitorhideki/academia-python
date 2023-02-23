def classifica_pedido(valor,dias,tamanho,avarias,capital):
    if valor<=1000:
        if dias<=1:
            if valor<=150:
                if avarias=='n' or avarias=='N':
                    return 'normal'
                else:
                    return 'reclamacao'
            else:
                return 'reclamacao'
        else:
            return 'reclamacao'
    else:
        if dias<=10:
            if avarias=='n' or avarias=='N':
                if valor<=10000:
                    if valor<=5000:
                        if capital=='n' or capital=='N':
                            return 'normal'
                        else:
                            if tamanho=='p' or tamanho=='P':
                                return 'reclamacao'
                            else:
                                return 'normal'
                    else:
                        return 'reclamacao'
                else:
                    return 'justica'
            else:
                return 'justica'
        else:
            return 'justica'
                            
print(classifica_pedido(2846.65,6,'P','N','S'))