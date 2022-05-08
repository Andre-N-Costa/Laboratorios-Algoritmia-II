"""
90%
"""
def maxsoma(lista):
    somas = []
    final = []
    somas.append(lista[0])
    for n in lista[1:]:
        somas.append(n + somas[-1])
    final.append(max(somas))
    print(somas)
    print(final)
    for n in range(len(lista)):
        somas = list(map(lambda x: x - somas[0],somas))
        somas.pop(0)
        if somas != []:
            final.append(max(somas))
    return max(final)
