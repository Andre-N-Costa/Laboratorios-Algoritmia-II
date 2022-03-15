def buildG(vizinhos):
    adj = {}
    for vizinho in vizinhos:
        for i in range(len(vizinho)):
            if vizinho[i] not in adj:
                    adj[vizinho[i]] = set()
            for j in range(i+1,len(vizinho)):
                if vizinho[j] not in adj:
                    adj[vizinho[j]] = set()
                adj[vizinho[i]].add(vizinho[j])
                adj[vizinho[j]].add(vizinho[i])
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
    return vis


def maior(vizinhos):
    adj = buildG(vizinhos)
    max = 0
    for pais in adj:
        if len(bfs(adj,pais)) > max:
            max = len(bfs(adj,pais))
    return max
