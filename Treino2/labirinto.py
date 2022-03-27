def buildG(mapa):
    adj = {}
    for i in range(len(mapa)):
        for j in range(len(mapa)):
            if (i,j) not in adj:
                adj[(i,j)] = []
            if i > 0 and mapa[i-1][j] != "#":
                adj[(i,j)].append((i-1,j))
            if i < len(mapa)-1 and mapa[i+1][j] != "#":
                adj[(i,j)].append((i+1,j))
            if j > 0 and mapa[i][j-1] != "#":
                adj[(i,j)].append((i,j-1))
            if j < len(mapa)-1 and mapa[i][j+1] != "#":
                adj[(i,j)].append((i,j+1))
    return adj
    
def bfs(adj,o):
    pai = {}
    vis = {o}
    queue = [o]
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
    pais = bfs(buildG(mapa),o)
    d = (len(mapa)-1,len(mapa)-1)
    cardeais = ""
    while(d != o):
        x,y = d
        if pais[d] == (x+1,y):
            cardeais+="N"
        if pais[d] == (x-1,y):
            cardeais+="S"
        if pais[d] == (x,y+1):
            cardeais+="O"
        if pais[d] == (x,y-1):
            cardeais+="E"
        d = pais[d]
    return cardeais[::-1]
