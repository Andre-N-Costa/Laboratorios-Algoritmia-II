def frequencia(texto):
    return sorted(list(set(texto.split())),key = lambda x : (len(texto.split()) - (texto.split()).count(x),x))
