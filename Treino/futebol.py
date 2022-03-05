def tabela(jogos):
    dados = {}
    final = []
    for jogo in jogos:
        if jogo[0] not in dados:
            dados[jogo[0]] = [0,0]
        if jogo[2] not in dados:
            dados[jogo[2]] = [0,0] 
        dados[jogo[0]][1] += jogo[1] - jogo[3]
        dados[jogo[2]][1] += jogo[3] - jogo[1]
        if jogo[1] < jogo[3]:
            dados[jogo[2]][0] += 3
        elif jogo[3] < jogo[1]:
            dados[jogo[0]][0] += 3
        elif jogo[1] == jogo[3]:
            dados[jogo[2]][0] += 1
            dados[jogo[0]][0] += 1
        dadosord = sorted(dados.items(),key = lambda x :(-x[1][0],-x[1][1],x[0]))
    for dado in dadosord:
        final.append((dado[0],dado[1][0]))
    return final
