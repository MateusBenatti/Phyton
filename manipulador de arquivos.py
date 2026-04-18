manipulador = open ("C:\Python33\mbox.txt","r")
linhas = 0
for l in manipulador:
        l = l.rstrip()
        if not l.startswith("From "):
            continue
        inicio = 5
        final = l.find(" ", 6)
        remetente = l[inicio:final]
        print(remetente)
        linhas = linhas +1
print(linhas)
