while (True):
        arquivo = input("Qal o nome do arquivo: ")
        try:
            entrada = open (arquivo,"r")
            break
        except:
            print("O arquivo {} não existe".format(arquivo))
while(True):
    arquivo = input("Qual o nome do arquivo de saida: ")
    try:
        saida = open(arquivo, "w")
        break
    except:
        print("O arquivo {} não existe".format(arquivo))

linhas = 0
for l in entrada:
        l = l.rstrip()
        if not l.startswith("From "):
            continue
        inicio = 5
        final = l.find(" ", 6)
        remetente = l[inicio:final]
        saida.write(remetente)
        saida.write("\n")
        linhas = linhas +1
print(linhas)
