def buildG(artigos):
    adj = {}
    for artigo in list(artigos.values()):
        artigo = list(artigo)
        for i in range(len(artigo)):
            if artigo[i] not in adj:
                adj[artigo[i]] = set()
            for j in range(i+1,len(artigo)):
                if artigo[j] not in adj:
                    adj[artigo[j]] = set()
                adj[artigo[i]].add(artigo[j])
                adj[artigo[j]].add(artigo[i])
    return adj

def bfs(adj):
    nErdos = {"Paul Erdos" : 0}
    queue = ["Paul Erdos"]
    while queue:
        v = queue.pop(0)
        if v in adj:
            for autor in adj[v]:
                if autor not in nErdos:
                    nErdos[autor] = nErdos[v] + 1
                    queue.append(autor)
    return nErdos

def erdos(artigos,n):
    finalt = []
    final = []
    adj = buildG(artigos)
    nErdos = bfs(adj)
    for erdo in nErdos:
        if nErdos[erdo] <= n:
            finalt.append((erdo,nErdos[erdo]))
    finalt = sorted(finalt,key = lambda x : (x[1],x[0]))
    for i in finalt:
        final.append(i[0])
    return final
