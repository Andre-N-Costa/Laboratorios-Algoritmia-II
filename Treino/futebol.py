def tabela(jogos):
    equipas = []
    pont = []
    dgolos = []
    sort1 = []
    final = []
    i = 0
    for jogo in jogos:
        if equipas.count(jogo[0]) == 0:
            equipas.append(jogo[0])
        if equipas.count(jogo[2]) == 0:
            equipas.append(jogo[2])
    for p in range(len(equipas)):
        pont.append(0)
    for p in range(len(equipas)):
        dgolos.append(0)
    for jogo in jogos:
        if jogo[1] > jogo[3]:
            pont[equipas.index(jogo[0])]+=3
            dgolos[equipas.index(jogo[0])]+=jogo[1] - jogo[3]
            dgolos[equipas.index(jogo[2])]+=jogo[3] - jogo[1]
        elif jogo[1] < jogo[3]:
            pont[equipas.index(jogo[2])]+=3
            dgolos[equipas.index(jogo[0])]+=jogo[1] - jogo[3]
            dgolos[equipas.index(jogo[2])]+=jogo[3] - jogo[1]
        elif jogo[1] == jogo[3]:
            pont[equipas.index(jogo[0])]+=1
            pont[equipas.index(jogo[2])]+=1
            dgolos[equipas.index(jogo[0])]+=jogo[1] - jogo[3]
            dgolos[equipas.index(jogo[2])]+=jogo[3] - jogo[1]
    while i < len(equipas):
        sort1.append((equipas[i],pont[i],dgolos[i]))
        i+=1
    sort1 = sorted(sort1, key = lambda x: (-x[1],-x[2],x[0]))
    for i in sort1:
        final.append((i[0],i[1]))
    return final
