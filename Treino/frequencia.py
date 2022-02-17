def frequencia(texto):
    return sorted(list(set(texto.split())),key = lambda x : (-(texto.split()).count(x),x))
