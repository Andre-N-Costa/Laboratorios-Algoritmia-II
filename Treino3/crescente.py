def crescente(lista):
    dict = {}
    valores = []
    if lista == []:
        return 0
    for i in reversed(list(range(len(lista)))):
        m = lista[i]
        aux = lista[i]
        if i == len(lista)-1:
            valores.append(1)
            dict[lista[i]] = 1
        else:
            for elem in lista[i:]:
                if lista[i] < elem:
                    m = elem
                    break
            if m in dict:
                valores.append(1 + dict[m])
                dict[lista[i]] = 1 + dict[m]
            else:
                valores.append(1)
                dict[lista[i]] = 1
    return max(valores)
