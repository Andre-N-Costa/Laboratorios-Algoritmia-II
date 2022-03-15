def adj(o):
    x,y = o
    adjacentes = []
    adjacentes.append((x-1,y+2))
    adjacentes.append((x-2,y+1))
    adjacentes.append((x+1,y+2))
    adjacentes.append((x+2,y+1))
    adjacentes.append((x-2,y-1))
    adjacentes.append((x-1,y-2))
    adjacentes.append((x+1,y-2))
    adjacentes.append((x+2,y-1))
    print(adjacentes)
    return adjacentes

def bfs(o,d):
    pai = {}
    vis = {o}
    queue = [o]
    while queue:
        if d in vis:
            return pai
        v = queue.pop(0)
        for n in adj(v):
            if n not in vis:
                vis.add(n)
                pai[n] = v
                queue.append(n)
    return pai

    
def saltos(o,d):
    pais = bfs(o,d)
    saltos = 0
    pai = d
    while pai != o:
        pai = pais[pai]
        saltos+=1
    return saltos
