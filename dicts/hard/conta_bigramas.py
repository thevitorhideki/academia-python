def conta_bigramas(name: str) -> dict:
    count = {}

    for i in range(len(name) - 1):
        if name[i:i+2] not in count:
            count[name[i:i+2]] = 1
        else:
            count[name[i:i+2]] += 1

    return count


print(conta_bigramas('banana nanica'))
