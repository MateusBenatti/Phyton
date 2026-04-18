import math
a = float(input("Digite o coeficiente do 2ºgrau:"))
b = float(input("Digite o coeficiente do 1ºgrau:"))
c = float(input("Digite o termo independente:"))

delta = b*b - 4*a*c

if delta < 0:
    print("Não tem raiz real")
else:
    n = (-b + math.sqrt(delta))/2*a
    m = (-b - math.sqrt(delta))/2*a
    print(n, m)
