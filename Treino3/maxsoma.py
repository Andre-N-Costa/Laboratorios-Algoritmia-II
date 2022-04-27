"""
80%
"""
def maxsoma(lista):
    if lista == []:
        return 0
    if len(lista) == 1:
        return lista[0]
    somas = []
    final = []
    somas.append(lista[0])
    for n in lista[1:]:
        somas.append(n + somas[-1])
    final.append(max(somas))
    for n in range(len(lista)-1):
        somas = list(map(lambda x: x - somas[0],somas))
        final.append(max(somas))
        somas.pop(0)
    return max(final)
