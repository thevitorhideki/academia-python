import re


def extract_message(packages: list) -> str:
    message = {}
    final_message = ''

    for package in packages:
        of = re.search(r'OF', package).span()
        size = re.search(r'SIZE', package).span()
        begin = re.search(r'BEGIN', package).span()
        end = re.search(r'END', package).span()

        text = package[begin[1]:end[0]]
        n_packages = package[of[1]:size[0]]
        message_size = package[size[1]:begin[0]]
        num = int(package[:of[0]])

        message[num] = text
        sorted_message = sorted(message.items())

        if len(packages) != int(n_packages):
            print('diferente da quantidade')
            return ''
        elif int(message_size) != len(text):
            print('diferente do size')
            return ''

    for i in sorted_message:
        final_message += i[1]

    return final_message
