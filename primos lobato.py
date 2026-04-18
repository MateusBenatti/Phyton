numero = 0
while(numero < 2):
    print("Informe um numero inteiro maior ou igual a 2")
    try:
        numero = int(input("Qual numero vamos testar?"))
    except:
        print("Apenas numeros inteiros")
num_divisor = 0
for divisor in range(1, numero+1):
    qr = divmod (numero, divisor)
    if (qr[1] == 0):
        num_divisor = num_divisor+1
if num_divisor == 2:
    print("Eh primo")
else:
    print("eh composto")
