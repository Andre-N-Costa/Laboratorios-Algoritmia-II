def aloca(prefs):
    alunos = prefs.keys()
    alunos = sorted(alunos)
    listaproj = []
    retl = []
    for i in range(6):
        listaproj.append(-1)
    for a in alunos:
        for i in range(len(prefs[a])):
            if listaproj[(prefs[a])[i]] == -1:
                listaproj[(prefs[a])[i]] = a
                break
        if listaproj.count(a) == 0:
            retl.append(a)
    return retl
