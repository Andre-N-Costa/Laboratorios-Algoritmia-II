def validasaux(soma,lista,elem):
    if lista == []:
        return []
    valor = elem
    for i in lista:
        if valor + i == soma:
            return True
        elif valor + i < soma:
            valor+=i
    if valor == soma:
        return True
    return False

def validas(soma,listas):
    if listas == []:
        return []
    if soma == 0:
        return listas
    final = []
    for lista in listas:
        for elem in range(len(lista)):
            if validasaux(soma,lista[:elem] + lista[elem+1:],lista[elem]):
                final.append(lista)
                break
    return final