def adjs(p,mapa):
    x,y = p
    adj = []
    if x < len(mapa)-1:
        if mapa[x+1][y] != "*":
            adj.append((x+1,y))
    if x > 0:
        if mapa[x-1][y] != "*":
            adj.append((x-1,y))
    if y < len(mapa)-1:
        if mapa[x][y+1] != "*":
            adj.append((x,y+1))
    if y > 0:
        if mapa[x][y-1] != "*":
            adj.append((x,y-1))
    return adj


def bfs(mapa,o):
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adjs(v,mapa):
            if d not in vis:
                vis.add(d)
                queue.append(d)
    return vis

def area(p, mapa):
    p = (p[1],p[0])
    return len(bfs(mapa,p))
