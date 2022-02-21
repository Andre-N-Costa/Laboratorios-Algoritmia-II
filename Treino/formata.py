def formata(codigo):
    nident = 0;
    newcode = ""
    codigo = " ".join(codigo.split())
    codigo = ";".join(codigo.split("; "))
    codigo = "}".join(codigo.split("} "))
    codigo = "{".join(codigo.split("{ "))
    print(codigo)
    for n,elem in enumerate(codigo):
        if n < len(codigo)-1:
            if elem == ";":
                newcode+=";\n" + " "*2*nident
            elif elem == "{":
                nident+=1
                newcode+="{\n" + " "*2*nident
            elif elem == "}":
                nident-=1
                newcode = "".join(list(newcode[:-1]))
                newcode = "".join(list(newcode[:-1]))
                newcode+="}\n" + " "*2*nident
            else:
                newcode+=elem
        else:
            while newcode.endswith(" "):
                newcode = "".join(list(newcode[:-1]))
            newcode+=elem
    return newcode
