def horario(ucs,alunos):
    final = []
    for aluno in alunos.items():
        semana = {}
        horas = 0
        for cadeiras in aluno[1]:
            if cadeiras not in ucs:
                semana["impossivel"] = -1
                break
            dia,hora,duracao = ucs[cadeiras]
            horas+=duracao
            if dia not in semana:
                semana[dia] = []
                for i in range(duracao):
                    semana[dia].append(hora+i)
            else:
                for i in range(duracao):
                    semana[dia].append(hora+i)
            if len(set(semana[dia])) < len(semana[dia]):
                semana["impossivel"] = -1
            print(semana)
        if "impossivel" not in semana:
            final.append((aluno[0],horas))
        print(final)
    return sorted(final, key = lambda x : (-x[1],x[0]))
