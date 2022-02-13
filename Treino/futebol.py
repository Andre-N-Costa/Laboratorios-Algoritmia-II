def last1(n):
    return n[1]
    
def last2(n):
    return n[2]
    
def tabela(jogos):
    equipas = []
    pont = []
    dgolos = []
    sort1 = []
    sortp = []
    sorte = []
    sortg = []
    final = []
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
    i = 0
    while i < len(equipas):
        sort1.append((equipas[i],pont[i],dgolos[i]))
        i+=1
    sort1 = sorted(sort1, key = last1,reverse = True)
    for i in sort1:
        sortp.append(i[1])
        sorte.append(i[0])
        sortg.append(i[2])
    w = 0
    while w < len(sortp):
        aux = []
        if w == len(sortp) - 1:
            aux.append((sorte[w],sortp[w],sortg[w]))
            w+=1
        else:
            if sortp[w] == sortp[w+1]:
                while w < len(sortp) and sortp[w] == sortp[w+1]:
                    aux.append((sorte[w],sortp[w],sortg[w]))
                    w+=1
                aux.append((sorte[w],sortp[w],sortg[w]))
                w+=1
            else:
                aux.append((sorte[w],sortp[w],sortg[w]))
                w+=1
        print(aux)
        aux = sorted(aux,key = last2, reverse = True)
        print(aux)
        for a in aux:
            final.append((a[0],a[1]))
    return final
