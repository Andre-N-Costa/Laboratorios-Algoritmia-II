def formata(codigo):
    newcode = ""
    identation = 0
    codigo = " ".join(codigo.split())
    codigo = ";".join(codigo.split("; "))
    codigo = "{".join(codigo.split("{ "))
    codigo = "}".join(codigo.split("} "))
    for i,caracter in enumerate(codigo):
        if i == len(codigo) -1:
            print(list(newcode))
            newcode = newcode.rstrip(" ")
            print(list(newcode))
            newcode+=caracter
        elif caracter == ";":
            newcode+=caracter + "\n" + "  "*identation
        elif caracter == "{":
            identation+=1
            newcode+=caracter + "\n" + "  "*identation
        elif caracter == "}":
            newcode = "".join(list(newcode[:-2]))
            identation-=1
            newcode+=caracter + "\n" + "  "*identation
        else:
            newcode+=caracter
    return newcode
