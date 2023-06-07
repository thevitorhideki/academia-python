import re

def criar_espacos_faltantes(texto: str, palavra: str) -> str:
    if palavra == 'R$':
        return texto.replace('R$', '__')
    return re.sub(rf'\b{palavra}\b', '_' * len(palavra), texto)