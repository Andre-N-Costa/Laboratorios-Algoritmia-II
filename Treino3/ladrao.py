"""
90% - memoization
"""

def ladrao(capacidade,objetos):
    if capacidade == 0:
        return 0
    if objetos == []:
        return 0
    return ladraob(capacidade,objetos,0,{})

def ladraoa(capacidade,objetos,objeto,valores,valor,dict):
    if objetos == []:
        return valor
    if capacidade == 0:
        return 0
    if capacidade in dict:
        return dict[capacidade]
    for c,obj in enumerate(objetos):
        if obj[2] <=capacidade:
            valor = max(valor + obj[1],ladraoa(capacidade-obj[2],objetos[c+1:],obj,valores,valor + obj[1],dict))
            valores.append(valor)
            valor = objeto[1]
    if valores == []:
        return 0
    dict[capacidade] = max(valores)
    return dict[capacidade]

def ladraob(capacidade,objetos,dict):
    if capacidade in dict:
        return dict[capacidade]
    valores = []
    for c,objeto in enumerate(objetos):
        if objeto[2] <= capacidade:
            valores.append(ladraoa(capacidade-objeto[2],objetos[c+1:],objeto,[],objeto[1],dict))
    dict[capacidade] = max(valores)
    return dict[capacidade]


"""
90% - dinâmica
"""

def ladraoaux(maxi,capacidade,objetos,objeto,d):
    valor = objeto[1]
    for obj in objetos:
        if obj[2] <= capacidade and capacidade < maxi:
            valor+=obj[1]
            capacidade-=obj[2]
    return valor

def ladrao(capacidade,objetos):
    d = {}
    if capacidade == 0:
        return 0
    if objetos == []:
        return 0
    valores = []
    for cap in range(1,capacidade+1):
        for c,objeto in enumerate(objetos):
            if objeto[2] <=cap:
                valores.append(ladraoaux(capacidade,cap - objeto[2],objetos[:c] + objetos[c+1:],objeto,d))
    return max(valores)
