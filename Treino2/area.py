def bfs(adj,o):
    pai = {}
    vis = set()
    vis.add(o)
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)
    return vis

def construirG(mapa):
    adj = {}
    for y in range(len(mapa)):
        for x in range(len(mapa)):
            adj[(x,y)] = set()
            if y > 0:
                if mapa[x][y-1] != "*":
                    adj[(x,y)].add((x,y-1))
            if x > 0:
                if mapa[x-1][y] != "*":
                    adj[(x,y)].add((x-1,y))
            if y < len(mapa)-1:
                if mapa[x][y+1] != "*":
                    adj[(x,y)].add((x,y+1))
            if x < len(mapa)-1:
                if mapa[x+1][y] != "*":
                    adj[(x,y)].add((x+1,y))
    return adj

def area(p,mapa):
    p = (p[1],p[0])
    adj = construirG(mapa)
    vis = bfs(adj,p)
    print(vis)
    return len(vis)
