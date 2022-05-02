
def probabilidade(passos,probs):
    dict = {}
    if passos == 0:
        return 1
    if passos%2 == 1:
        return 0
    dict = {(0,0):{0:1}}
    return round(probabilidadeaux(passos,probs,(0,0),dict),2)

def probabilidadeaux(passos,probs,coords,dict):
    if coords not in dict:
        dict[coords] = {0:0}
    if passos in dict[coords]:
        return dict[coords][passos]
    if passos == 0:
        if coords[0] == 0 and coords[1] == 0:
            return 1
        else:
            return 0
    dict[coords][passos] = probabilidadeaux(passos-1,probs,(coords[0],coords[1]+1),dict) * probs['U'] + probabilidadeaux(passos-1,probs,(coords[0],coords[1]-1),dict) * probs['D'] + probabilidadeaux(passos-1,probs,(coords[0]+1,coords[1]),dict) * probs['R'] + probabilidadeaux(passos-1,probs,(coords[0]-1,coords[1]),dict) * probs['L']
    return dict[coords][passos]