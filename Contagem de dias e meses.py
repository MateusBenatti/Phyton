while (True):
        arquivo = input("Qal o nome do arquivo de Entrada: ")
        try:
            entrada = open (arquivo,"r")
            break
        except:
            print("O arquivo {} não existe".format(arquivo))
while(True):
    arquivo = input("Qual o nome do arquivo de Saida com a contagem de Dias: ")
    try:
        dias = open(arquivo, "w")
        break
    except:
        print("O arquivo {} não pode ser criado".format(arquivo))
while(True):
    arquivo = input("Qual o nome do arquivo de saida com contagem de Meses: ")
    try:
        meses = open(arquivo, "w")
        break
    except:
        print("O arquivo {} não pode ser criado".format(arquivo))
    
Sun = Mon = Tue = Wed = Thu = Fri = Sat = 0
Jan = Feb = Mar = Apr = May = Jun = Jul = Aug = Sep = Oct = Nov = Dec = 0

linha = 0
for l in entrada:
    l = l.rstrip()
    if not l.startswith("From "):
        continue
    tokens = l.split()
    dia = tokens[2].casefold()
    mes = tokens[3].casefold()
    if meses == "Jan".casefold():
        Jan = Jan+1
    if meses == "Feb".casefold():
        Feb = Feb+1
    if meses == "Mar".casefold():
        Mar = Mar+1
    if meses == "Apr".casefold():
        Apr = Apr+1
    if meses == "Jun".casefold():
        Jun = Jun+1
    if meses == "Jul".casefold():
        Jul = Jul+1
    if meses == "Aug".casefold():
        Aug = Aug+1
    if meses == "Sep".casefold():
        Sep = Sep+1
    if meses == "Oct".casefold():
        Oct = Oct+1
    if meses == "Nov".casefold():
        Nov = Nov+1
    if meses == "Dec".casefold():
        Dec = Dec+1
    if meses == "May".casefold():
        May = May+1

    if meses == "Sun".casefold():
        Sun = Sun+1
    if meses == "Mon".casefold():
        Mon = Mon+1
    if meses == "Tue".casefold():
        Tue = Tue+1
    if meses == "Wed".casefold():
        Wed = Wed+1
    if meses == "Thu".casefold():
        Thu = Thu+1
    if meses == "fri".casefold():
        Fri = Fri+1
    if meses == "Sat".casefold():
        Sat = Sat+1

print(linhas)
dias.write("Sun {}\n".format(Sun))
dias.write("Mon {}\n".format(Mon))
dias.write("Tue {}\n".format(Tue))
dias.write("Wed {}\n".format(Wed))
dias.write("Thu {}\n".format(Thu))
dias.write("Fri {}\n".format(Fri))
dias.write("Sat {}\n".format(Sat))

meses.write("Jan {}\n".format(Jan))
meses.write("Feb {}\n".format(Feb))
meses.write("Mar {}\n".format(Mar))
meses.write("Apr {}\n".format(Apr))
meses.write("May {}\n".format(May))
meses.write("Jun {}\n".format(Jun))
meses.write("Jul {}\n".format(Jul))
meses.write("Aug {}\n".format(Aug))
meses.write("Sep {}\n".format(Sep))
meses.write("Oct {}\n".format(Oct))
meses.write("Nov {}\n".format(Nov))
meses.write("Dec {}\n".format(Dec))

entrada.close()
dias.close()
meses.close()
