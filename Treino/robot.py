import math

def robot(comandos):
    comandos = list(comandos)
    E = 0
    D = 0
    X = [0]
    Y = [0]
    rect = []
    for com in comandos:
        if com == "E":
            E+=90
        elif com == "D":
            D+=90
        elif com == "A":
            X.append(X[-1] + round(math.cos(math.radians(D-E))))
            Y.append(Y[-1] + round(math.sin(math.radians(D-E))))
        else:
            rect.append((min(Y),min(X),max(Y),max(X)))
            E = 0
            D = 0
            X = [0]
            Y = [0]
    return rect
