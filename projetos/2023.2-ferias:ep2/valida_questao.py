def valida_questao(questao: dict) -> dict:
    correcao = {}

    if len(questao) != 4:
        correcao['outro'] = 'numero_chaves_invalido'

    if not questao.get('titulo'):
        correcao['titulo'] = 'nao_encontrado'
    elif questao.get('titulo').strip() in ['', '\t', '\n']:
        correcao['titulo'] = 'vazio'

    if not questao.get('nivel'):
        correcao['nivel'] = 'nao_encontrado'
    elif questao.get('nivel') not in ['facil', 'medio', 'dificil']:
        correcao['nivel'] = 'valor_errado'

    if questao.get('opcoes') == None:
        correcao['opcoes'] = 'nao_encontrado'
    elif len(questao.get('opcoes')) != 4:
        correcao['opcoes'] = 'tamanho_invalido'
    elif len(questao.get('opcoes')) == 4:
        for chave, valor in questao.get('opcoes').items():
            
            if chave not in ['A', 'B', 'C', 'D']:
                correcao['opcoes'] = 'chave_invalida_ou_nao_encontrada'
                break
            elif valor.strip() in ['', '\t', '\n']:
                if correcao.get('opcoes'):
                    correcao['opcoes'][chave] = 'vazia'
                else:
                    correcao['opcoes'] = {}
                    correcao['opcoes'][chave] = 'vazia'
    
    if not questao.get('correta'):
        correcao['correta'] = 'nao_encontrado'
    elif questao.get('correta') not in ['A', 'B', 'C', 'D']:
        correcao['correta'] = 'valor_errado'

    return correcao 
