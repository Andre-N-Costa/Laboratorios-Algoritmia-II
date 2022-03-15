def dfs_aux(adj,o,vis,pai):
    vis.add(o)
    for d in adj[o]:
        if d not in vis:
            pai[d] = o
            dfs_aux(adj,d,vis,pai)
    return vis

def construirG(adj,mapa):
    for i in range(len(mapa)):
        for j in range(len(mapa)):
            adj[(i,j)] = []
            if mapa[i][j] != "*":
                if i < len(mapa)-1:
                    if mapa[i+1][j] != "*":
                        adj[(i,j)].append((i+1,j))
                if j < len(mapa)-1:
                    if mapa[i][j+1] != "*":
                        adj[(i,j)].append((i,j+1))
                if i > 0:
                    if mapa[i-1][j] != "*":
                        adj[(i,j)].append((i-1,j))
                if j > 0:
                    if mapa[i][j-1] != "*":
                        adj[(i,j)].append((i,j-1))
    return adj

def area(p,mapa):
    adj = {};vis = set();pai = {}
    if mapa[p[0]][p[1]] == "*":
        return 0
    construirG(adj,mapa)
    return len(list(dfs_aux(adj,p,vis,pai)))
