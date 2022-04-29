"""
90%
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