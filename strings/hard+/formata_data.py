import re


def formata_data(date: str, format: str) -> str:
    format_date = {}

    date_separator = re.search(r'[^0-9]', date).group()
    format_separator = re.search(r'[^amd]', format).group()
    date = date.split(date_separator)
    format = format.split(format_separator)

    for i in range(len(date)):
        format_date[format[i]] = int(date[i])
    if format_date['a'] < 1000:
        format_date['a'] += 2000

    format_date = f'{format_date["a"]}-{format_date["m"]:0>2}-{format_date["d"]:0>2}'
    return format_date
