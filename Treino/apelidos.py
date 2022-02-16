def apelidos(nomes):
    return sorted(nomes, key = lambda x : ((len(x.split())),x))
