import string

def cruzamentos(ruas):
    abc = string.ascii_lowercase
    cruz = []
    for i in abc:
        no = 0
        for rua in ruas:
            if rua[0] == i:
                no += 1
            if rua[len(rua)-1] == i:
                no += 1
        cruz.append((i,no))
    cruz = sorted(cruz,key = lambda x: (x[1],x[0]))
    a,b = cruz[0]
    while b == 0:
        cruz.pop(0)
        a,b = cruz[0]
    return cruz
