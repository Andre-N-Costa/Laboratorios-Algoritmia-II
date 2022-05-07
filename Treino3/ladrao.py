"""
70% - programação dinâmica
"""

def ladrao(capacidade,objetos):
    if capacidade == 0:
        return 0
    d = {}
    d[0] = 0
    object = objetos.copy()
    for v in range(1,capacidade+1):
        if objetos == []:
            objetos = object.copy()
        aux = objetos.copy()
        valor = float("-inf")
        for m in objetos:
            if m[2] <= v:
                valor = max(valor,m[1] + d[v - m[2]])
                if valor == m[1] + d[v - m[2]]:
                        objetos = aux.copy()
                objetos.remove(m)
        if valor == float("-inf"):
            d[v] = d[v-1]
        else:
            d[v] = valor
    return d[capacidade]

"""
90% - programação recursiva
"""

def ladrao(capacidade,objetos):
    return ladraoaux(capacidade,objetos,{})

def ladraoaux(capacidade,objetos,d):
    r = float("-inf")
    if objetos == []:
        return 0
    if capacidade == 0:
        d[capacidade] = 0
        return 0
    if capacidade-3 in d:
        return d[capacidade-3]
    for count,m in enumerate(objetos):
        if m[2] <= capacidade:
            r = max(r,m[1]+ladraoaux(capacidade - m[2],objetos[count+1:],d))
    d[capacidade] = r 
    return r
