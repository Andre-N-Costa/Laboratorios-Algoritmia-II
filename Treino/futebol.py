def tabela(jogos):
    equipas = [];pont = [];dgolos = [];sort1 = [];final = []
    i = 0
    for jogo in jogos:
        if jogo[0] not in equipas:
            equipas.append(jogo[0])
            dgolos.append(jogo[1] - jogo[3])
        else:
            dgolos[equipas.index(jogo[0])]+= jogo[1] - jogo[3]
        if jogo[2] not in equipas:
            equipas.append(jogo[2])
            dgolos.append(jogo[3] - jogo[1])
        else:
            dgolos[equipas.index(jogo[2])]+= jogo[3] - jogo[1]
    for p in range(len(equipas)):
        pont.append(0)
        dgolos.append(0)
    for jogo in jogos:
        if jogo[1] > jogo[3]:
            pont[equipas.index(jogo[0])]+=3
        elif jogo[1] < jogo[3]:
            pont[equipas.index(jogo[2])]+=3
        elif jogo[1] == jogo[3]:
            pont[equipas.index(jogo[0])]+=1
            pont[equipas.index(jogo[2])]+=1
    for i in range(len(equipas)):
        sort1.append((equipas[i],pont[i],dgolos[i]))
    sort1 = sorted(sort1, key = lambda x: (-x[1],-x[2],x[0]))
    for i in sort1:
        final.append((i[0],i[1]))
    return final
