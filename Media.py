
#DEFINICAO DE VARIAVEIS
n=1
somanotas = 0
nota = 0

nroprovas = float(input("Quantas provas voce realizou?"))

if (nroprovas <2) or (nroprovas >=5):
    print ("Nao e possivel calcular a media")
else:
    while (n <= nroprovas):
        nota = float(input("Entre com a nota -->"))
        somanotas = somanotas + nota
        n = n+1

    media = somanotas /nroprovas

    print ("O valor da media e" , media)
