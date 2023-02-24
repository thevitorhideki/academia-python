def pacotes_correio(packages: list[list[int]]) -> str:
    package_numbers = []
    package_size = []

    for i in packages:
        package_numbers.append(i[1])
        package_size.append(i[2])

    if package_numbers != sorted(package_numbers):
        return 'ordem errada'
    elif sum(package_size) / len(package_size) != package_size[0]:
        return 'tamanho errado'
    elif packages[0][0] != len(packages):
        return 'pacote perdido'
    else:
        return 'tudo certo'
