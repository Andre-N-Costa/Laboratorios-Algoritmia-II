def hacker(log):
    atrib = {}
    final = []
    for dados in log:
        if dados[1] not in atrib:
            atrib[dados[1]] = [dados[0]]
        else:
            atrib[dados[1]].append(dados[0])
    print(list(atrib.items()))
    for dado in atrib.items():
        index = 0
        cartoes = dado[1]
        codigo = cartoes[0]
        index+=1
        while index < len(cartoes):
            codigo = list(map(lambda x,y : y if x != "*" and y != "*" and x != y else (x if x != "*" else y), codigo, cartoes[index]))
            index+=1
        final.append(("".join(codigo),dado[0]))
    return sorted(final,key = lambda x : (x[0].count("*"),x[1]))
