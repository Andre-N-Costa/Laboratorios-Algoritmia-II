def horario(ucs,alunos):
    consegue = []
    for aluno in list(alunos.keys()):
        horas = 0
        semana = {}
        for UC in list(alunos[aluno]):
            if UC in ucs:
                a,b,c = ucs[UC]
                if a not in semana:
                    semana[a] = (list(range(b, b+c)))
                    horas+=ucs[UC][2]
                else:
                    if len(set(semana[a]).intersection(set(range(b, b+c)))) != 0:
                        semana["notpossible"] = -1
                    elif min(list(semana[a])) > max(list(range(b, b+v))):
                        semana[a] = list(range(b, b+v)) + list(a)
                        horas+=c
                    else:
                        semana[a] = list(semana[a]) + list(range(b, b+c))
                        horas+=c
            else:
                semana["notpossible"] = -1
        if "notpossible" not in semana:
            consegue.append((aluno,horas))
        print(consegue)
                    
    return sorted(consegue,key = lambda x : (-x[1],x[0]))
