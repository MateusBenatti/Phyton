email = input("Digite o seu email")
regra1 = False
regra2 = False

##1- somente 1 @
quantosArrobas = email.count("@")
if quantosArrobas == 1:
    regra1 = True
#if "@" in email = 0
#  qunatoArrobas = 0
#  posaArroba =  emial.find("@")
#  while posaArroba != -1:
#      quantosArrobas = quantosArrobas + 1
#      posaArroba = email.fond("@",posaArroba + 1)
#   if quantosArrobas == 1:
#       regra1 = True
##2 - o dominio tem que ter 1+ ponto,e
##    depois do ultimo ponto,2+ letras
dominio = email[email.find("@")+1:]
numPontos = dominio.count(".")
if numPontos >= 1:
  dominioInv = dominio[::- 1]
  posPonto = dominioInv.find(".")
  if posPonto >= 2:
    regra2 = True
if regra1 and regra2:
    print("É um email valido")
else:
    print("Não é valido")
