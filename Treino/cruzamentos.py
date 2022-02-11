import string

def cruzamentos(ruas):
    abc = string.ascii_lowercase
    cruz = []
    new = []
    ocorr = []
    for i in abc:
        no = 0
        for rua in ruas:
            if rua[0] == i:
                no += 1
            if rua[len(rua)-1] == i:
                no += 1
        cruz.append((i,no))
    if (cruz[len(cruz) - 1])[1] == 0:
        cruz.pop(len(cruz) - 1)
    for tup in cruz:
        ocorr.append(tup[1])
    for j in range(max(ocorr) + 1):
        for tup in cruz:
            if tup[1] == j:
                new.append(tup)
    for i,tup in enumerate(new):
        if tup[1] == 0:
            new.pop(i)
    if (new[len(new) - 1])[1] == 0:
        new.pop(len(new) - 1)
    return new
