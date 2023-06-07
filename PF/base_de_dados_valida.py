def base_de_dados_valida(livros):
    isbns = []
    
    for info in livros:
        isbn = info[1]
        if isbn in isbns:
            return False
        isbns.append(isbn)
    
    return True