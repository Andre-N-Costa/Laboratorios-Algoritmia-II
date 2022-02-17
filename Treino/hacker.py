def hacker(log):
    log = sorted(log,key = lambda x : x[1])
    numeros = []
    emails = []
    newlog = []
    for info in log:
        numeros.append(info[0])
        emails.append(info[1])
    i = 0
    while i < len(log):
        if emails.count(emails[i]) > 1:
            keys = []
            aux = emails[i]
            keys.append(numeros[i])
            i+=1
            while i < len(log) - 1 and emails[i] == aux:
                keys.append(numeros[i])
                i+=1
            if i == len(log) - 1:
                keys.append(numeros[i])
            l = 1
            chave = keys[0]
            print(keys)
            if len(keys) > 1:
                chave = list(map(lambda x,y: -100 if x != "*" and y != "*" and x != y else (x if x != "*" else y),chave,keys[l]))
                l+=1
            while l < len(keys):
                chave = list(map(lambda x,y: -100 if x != "*" and y != "*" and x != y else (x if x != "*" else y),chave,keys[l]))
                l+=1
            chave = list(chave)
            if chave.count(-100) > 0:
                if i == len(log) - 1:
                    newlog.append((numeros[i],emails[i]))
                else:
                    newlog.append((numeros[i-1],emails[i-1]))
            else:
                if i < len(emails):
                    newlog.append(("".join(chave),emails[i-1]))
        else:
            newlog.append((numeros[i],emails[i]))
            i+=1
    return sorted(newlog,key = lambda x: x[0].count("*"))
