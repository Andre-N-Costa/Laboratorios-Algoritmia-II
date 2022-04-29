"""
50%
"""

def ladrao(capacidade,objetos):
    if capacidade == 0:
        return 0
    r = float("-inf")
    for count,m in enumerate(objetos):
        if m[2] <= capacidade:
            r = max(r,m[1]+ladrao(capacidade - m[2],objetos[count+1:]))
    return r