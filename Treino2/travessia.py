def buildG(mapa):
    adj = {}
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if (i,j) not in adj:
                adj[(i,j)] = {}
            if i > 0:
                if (i-1,j) not in adj:
                        adj[(i-1,j)] = {}
                if (abs(int(mapa[i][j]) - int(mapa[i-1][j]))) <= 2:
                    adj[(i,j)][(i-1,j)] = abs(int(mapa[i][j]) - int(mapa[i-1][j])) + 1
                    adj[(i-1,j)][(i,j)] = abs(int(mapa[i][j]) - int(mapa[i-1][j])) + 1
            if i < len(mapa) - 1:
                if (i+1,j) not in adj:
                        adj[(i+1,j)] = {}
                if (abs(int(mapa[i][j]) - int(mapa[i+1][j]))) <= 2:
                    adj[(i,j)][(i+1,j)] = abs(int(mapa[i][j]) - int(mapa[i+1][j])) + 1
                    adj[(i+1,j)][(i,j)] = abs(int(mapa[i][j]) - int(mapa[i+1][j])) + 1
            if j > 0:
                if (i,j-1) not in adj:
                        adj[(i,j-1)] = {}
                if (abs(int(mapa[i][j]) - int(mapa[i][j-1]))) <= 2:
                    adj[(i,j)][(i,j-1)] = abs(int(mapa[i][j]) - int(mapa[i][j-1])) + 1
                    adj[(i,j-1)][(i,j)] = abs(int(mapa[i][j]) - int(mapa[i][j-1])) + 1
            if j < len(mapa[i]) - 1:
                if (i,j+1) not in adj:
                        adj[(i,j+1)] = {}
                if (abs(int(mapa[i][j]) - int(mapa[i][j+1]))) <= 2:
                    adj[(i,j)][(i,j+1)] = abs(int(mapa[i][j]) - int(mapa[i][j+1])) + 1
                    adj[(i,j+1)][(i,j)] = abs(int(mapa[i][j]) - int(mapa[i][j+1])) + 1
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

def travessia(mapa):
    adj = buildG(mapa)
    shorterP = float("inf")
    shorterX = 0
    for i in range(len(mapa[0])):
        dist = dijkstra(adj,(0,i))
        for j in range(len(mapa[0])):
            if (len(mapa) - 1,j) in dist:
                if dist[(len(mapa) - 1,j)] < shorterP:
                    shorterP = dist[(len(mapa) - 1,j)]
                    shorterX = i
    return (shorterX,shorterP)
