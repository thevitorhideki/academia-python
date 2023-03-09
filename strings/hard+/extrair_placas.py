import re


def extrair_placas(texts: list) -> dict:
    plates = {}

    if len(texts) == 0:
        return plates

    for i in range(len(texts)):
        texts[i] = re.sub('[!?,;.:!\)\}\]\(\[\{]', '', texts[i]).split()

        for word in texts[i]:
            old_pattern = r'[A-Zºª]{3}\d{4}$'
            new_pattern = r'[A-Zºª]{3}\d{1}[A-Zºª]{1}\d{2}$'
            if re.match(old_pattern, word):
                plates.setdefault('antigo', []).append(
                    {'placa': word, 'indice_lista_texto': i, 'indice_palavra': texts[i].index(word)})
            elif re.match(new_pattern, word):
                plates.setdefault('mercosul', []).append(
                    {'placa': word, 'indice_lista_texto': i, 'indice_palavra': texts[i].index(word)})

    return plates
