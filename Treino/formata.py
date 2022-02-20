def formata(codigo):
    nident = 1
    codigo = " ".join(codigo.split())
    codigo = ";".join(codigo.split("; "))
    code = list(codigo)
    newcode = ""
    while len(code) > 0:
        if code.count("{") > 0 and code[0] != "{":
            newcode+="".join(list(map(lambda x : x+"\n" if x == ";" else (x),code[:code.index("{")])))
            for i in range(code.index("{")):
                code.pop(0)
        if code.count("{") > 0 and code[0] == "{":
            while code.count("{") > 1:
                if code[1:].index("{") < code.index("}"):
                    newcode+="".join(list(map(lambda x : x + "\n" + (nident * 2) * " " if x == ";" or x == "{" or x == "}" else (x),code[:code[1:].index("{") +1])))
                    nident+=1
                    for i in range(code[1:].index("{")+1):
                        code.pop(0)
                else:
                    newcode+="".join(list(map(lambda x : x + "\n" + (nident * 2) * " " if x == ";" or x == "{" or x == "}" else (x),code[:code.index("}")])))
                    nident-=1
                    for i in range(code.index("}")):
                        code.pop(0)
            while code.count("}") > 1:
                newcode+="".join(list(map(lambda x : x + "\n" + (nident * 2) * " " if x == ";" or x == "}" or x == "{" else (x),code[:code.index("}")])))
                for i in range(code.index("}")):
                    code.pop(0)
                newcode+=code[0] + "\n" + " " * nident 
                nident-=1
                code.pop(0)
            if code.count("{") == 1:
                newcode+="".join(list(map(lambda x : x + "\n" + (nident * 2) * " " if x == ";" or x == "}" or x == "{" else (x),code[:code.index("}")])))
                nident-=1
                for i in range(code.index("}")):
                    code.pop(0)
        newcode+="".join(list(map(lambda x : x+"\n" if x == ";" or x == "}" or x == "{" else (x),code[:-1])))
        for i in range(len(code)-1):
            code.pop(0)
        if  newcode.endswith(" "):
            newcode = "".join(list(newcode[:-1]))
            newcode = "".join(list(newcode[:-1]))
            newcode+=code[0]
            code.pop(0)
        if len(code) == 1:
            newcode+=code[0]
            code.pop(0)
    return newcode
