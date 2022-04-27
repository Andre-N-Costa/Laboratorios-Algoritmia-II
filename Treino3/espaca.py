"""
50%
"""

def espaca(frase,palavras):
    return espacaaux(frase,palavras,0)


def espacaaux(frase,palavras,n):
    if n == len(frase):
        return ""
    palavras = sorted(palavras, key = lambda x: -len(x))
    i = 0
    j = 0
    aux = n
    while aux < len(frase) and j < len(palavras):
        if i == 0:
            while(frase[aux] != palavras[j][i]):
                j+=1
        if frase[aux] == palavras[j][i]:
            if i == len(palavras[j])-1:
                break
            i+=1
            aux+=1
        else:
            i = 0
            aux = n
            j+=1
    print(palavras[j])
    return (palavras[j] + " " + espacaaux(frase,palavras,aux+1)).rstrip()
