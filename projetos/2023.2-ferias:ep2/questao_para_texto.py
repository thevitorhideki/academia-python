def questao_para_texto(questao: dict, id: int) -> str:
    retorno = f'----------------------------------------\n
    QUESTAO {id}\n
    \n
    {questao["titulo"]}\n
    \n
    RESPOSTAS:\n
    A: {questao["opcoes"]["A"]}\n
    B: {questao["opcoes"]["B"]}\n
    C: {questao["opcoes"]["C"]}\n
    D: {questao["opcoes"]["D"]}'
    
    return retorno
