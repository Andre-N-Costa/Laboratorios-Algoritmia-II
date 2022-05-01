"""
70% - programação dinâmica
"""

def vendedor(capacidade,objetos):
    if capacidade == 0:
        return 0
    d = {}
    d[0] = (0,[])
    for v in range(1,capacidade+1):
        produtos = []
        valor = float("-inf")
        for m in objetos:
            if m[2] <= v:
                if valor != m[1] + d[v - m[2]][0]:
                    valor = max(valor,m[1] + d[v - m[2]][0])
                    if valor == m[1] + d[v - m[2]][0]:
                        produtos.clear()
                        produtos.append(m[0])
                        produtos += d[v-m[2]][1]
        produtos = sorted(produtos)
        d[v] = (valor,produtos)
    return d[capacidade]