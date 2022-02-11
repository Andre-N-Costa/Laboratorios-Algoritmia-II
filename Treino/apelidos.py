def apelidos(nomes):
    napelidos = []
    new = []
    j = 1
    ord = sorted(nomes)
    for i in range(len(nomes)):
        napelidos.append(ord[i].count(" "))
    while j <= max(napelidos):
        while napelidos.count(j) != 0:
            ind = napelidos.index(j)
            napelidos[ind] = -1
            new.append(ord[ind])
        j+=1
    return new
