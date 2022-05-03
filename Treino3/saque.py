"""
50% - recursiva
"""

def saque(mapa):
    return saqueaux(mapa,(0,0),0)

def saqueaux(mapa,coords,valor):
    if mapa[coords[1]][coords[0]].isdigit():
        valor+= int(mapa[coords[1]][coords[0]])
    if coords[0] == len(mapa[0])-1 and coords[1] == len(mapa)-1:
        return valor
    if mapa[coords[1]][coords[0]] == '#':
        return 0
    if coords[0] >= len(mapa[0])-1:
        valor = max(valor,saqueaux(mapa,(coords[0],coords[1]+1),valor))
    elif coords[1] >= len(mapa)-1:
        valor = max(valor,saqueaux(mapa,(coords[0]+1,coords[1]),valor))
    else:
        valor = max(valor,saqueaux(mapa,(coords[0]+1,coords[1]),valor),saqueaux(mapa,(coords[0],coords[1]+1),valor))
    return valor

"""
80% - dinâmica
"""

def saque(mapa):
    return saqueaux(mapa,(0,0),0)

def saqueaux(mapa,coords,valor):
    if mapa == []:
        return 0
    while coords != (len(mapa[0])-1,len(mapa)-1):
        print(coords)
        print(valor)
        if mapa[coords[1]][coords[0]].isdigit():
            valor+= int(mapa[coords[1]][coords[0]])
        countx = 0
        county = 0
        for x in range(coords[0]+1,len(mapa[0])):
            if mapa[coords[1]][x].isdigit():
                countx+=int(mapa[coords[1]][x])
        for y in range(coords[1]+1,len(mapa)):
            if mapa[y][coords[1]].isdigit():
                county+=int(mapa[y][coords[1]])
        if (countx > county and coords[0] != len(mapa[0])-1) or coords[1] == len(mapa)-1:
            coords = (coords[0]+1,coords[1])
        elif (countx <= county and coords[1] != len(mapa)-1) or coords[0] == len(mapa[0])-1:
            coords = (coords[0],coords[1]+1)
    if mapa[coords[1]][coords[0]].isdigit():
            valor+= int(mapa[coords[1]][coords[0]])
    return valor