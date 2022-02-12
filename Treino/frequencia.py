def last(n):
    return n[1]

def frequencia(texto):
    sep = texto.split(" ")
    sep = sorted(sep)
    ocorr = []
    new = []
    i = 0
    while i < len(sep):
        if i == len(sep) - 1:
            ocorr.append((sep[i],sep.count(sep[i])))
        elif sep[i] != sep[i+1]:
            ocorr.append((sep[i],sep.count(sep[i])))
        i+=1
    ocorr = sorted(ocorr, key = last, reverse = True)
    for tup in ocorr:
        new.append(tup[0])
    return new
