import random

numero = random.randint(1, 1000)

print("+"+50*"-"+"+")
print("|"+" "*14 + "Qual numero eu pensei?" + " " *14 +"|")
print("+"+50*"-"+"+")
print ("Eu pensei em um numero entre 1 e 1000. Qual foi?")
tentativas = 0
while True:
    chute = int(input("De um chute(-1 para desistir)..."))
    if(chute == -1):
        print("Você arregou,o numero era!!!!",numero)
        break
    tentativas = tentativas + 1
    if (chute == numero):
        print("Acerto!")
        break
    elif (chute > numero):
        print("Eu escolhi um numero menor que isso...")
    else:
        print("Eu escolhi um numero maior que isso...")

print("Você precisou de ",tentativas,"tentativas")
