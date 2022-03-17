def buildG(mapa):
    adj = {}
    for i in range(len(mapa)):
        for j in range(len(mapa)):
            if mapa[i][j] != "#":
                if (i,j) not in adj:
                    adj[(i,j)] = set()
                if i > 0 and mapa[i-1][j] != "#":
                    adj[(i,j)].add((i-1,j))
                if i < len(mapa)-1 and mapa[i+1][j] != "#":
                    adj[(i,j)].add((i+1,j))
                if j > 0 and mapa[i][j-1] != "#":
                    adj[(i,j)].add((i,j-1))
                if j < len(mapa)-1 and mapa[i][j+1] != "#":
                    adj[(i,j)].add((i,j+1))
    return adj
                
def bfs(adj):
    pai = {}
    vis = {(0,0)}
    queue = [(0,0)]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)
    return pai
        


def caminho(mapa):
    o = (0,0)
    adj = buildG(mapa)
    pai = bfs(adj)
    point = (len(mapa)-1,len(mapa)-1)
    cardeais = []
    while point != (0,0):
        x,y = point
        if pai[point] == (x-1,y):
            cardeais.append("S")
        elif pai[point] == (x+1,y):
            cardeais.append("N")
        elif pai[point] == (x,y-1):
            cardeais.append("E")
        elif pai[point] == (x,y+1):
            cardeais.append("O")
        point = pai[point]
    cardeais.reverse()
    return "".join(cardeais)
