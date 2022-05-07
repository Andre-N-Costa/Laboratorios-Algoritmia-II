"""
70%
"""

def espaca(frase,palavras):
    return espacaaux(frase,sorted(palavras, key = lambda x: -len(x)),0)


def espacaaux(frase,palavras,n):
    if palavras == []:
        return ""
    i = 0
    j = 0
    aux = n
    final = []
    while n != len(frase):
        while aux < len(frase) and j < len(palavras):
            if i == 0:
                while(frase[aux] != palavras[j][i]):
                    j+=1
            if frase[aux] == palavras[j][i]:
                if i == len(palavras[j])-1:
                    j1 = 0
                    if aux+1 < len(frase):
                        while(j1 < len(palavras) and frase[aux+1] != palavras[j1][0]):
                            j1+=1
                        if j1 == len(palavras):
                            i = 0
                            aux = n
                            j+=1
                        else:
                            break
                    else:
                        break
                i+=1
                aux+=1
            else:
                i = 0
                aux = n
                j+=1
        final.append(palavras[j])
        i = 0
        j = 0
        aux+=1
        n = aux
    return " ".join(final)