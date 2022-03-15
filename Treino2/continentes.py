def buildG(ruas):
    adj = {}
    for rua in ruas:
            if rua[0] not in adj:
                adj[rua[0]] = {}
            if rua[-1] not in adj:
                adj[rua[-1]] = {}
            if rua[-1] in adj[rua[0]]:
                if len(rua) < adj[rua[0]][rua[-1]]:
                    adj[rua[0]][rua[-1]] = len(rua)
            else:
                adj[rua[0]][rua[-1]] = len(rua)
            if rua[0] in adj[rua[-1]]:
                if len(rua) < adj[rua[-1]][rua[0]]:
                    adj[rua[-1]][rua[0]] = len(rua)
            else:
                adj[rua[-1]][rua[0]] = len(rua)
    return adj


def dijkstra(adj,o):
    pai = {}
    dist = {}
    dist[o] = 0
    orla = {o}
    while orla:
        v = min(orla,key=lambda x:dist[x])
        orla.remove(v)
        for d in adj[v]:
            if d not in dist:
                orla.add(d)
                dist[d] = float("inf")
            if dist[v] + adj[v][d] < dist[d]:
                pai[d] = v
                dist[d] = dist[v] + adj[v][d]
    return dist


def tamanho(ruas):
    adj = buildG(ruas)
    distancias = []
    distancias2 = []
    for key in adj:
        distancias.append(dijkstra(adj,key))
    for distancia in distancias:
        distancias2.append(max(list(distancia.values())))
    return max(distancias2)
