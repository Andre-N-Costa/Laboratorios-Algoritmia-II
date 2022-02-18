def isbn(livros):
    final = []
    for i,livro in enumerate(livros.values()):
        livroint = list(map(int,list(livro)))
        soma = 0
        for m,code in enumerate(livroint):
            if m%2==0:
                soma += code
            else:
                soma += code*3
        if soma%10 != 0:
            final.append(list(livros.keys())[i])
    return sorted(final)
