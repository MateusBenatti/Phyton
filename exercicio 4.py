TMV = float(input("Quantos minutos voce falou:"))
TMG = float(input("Quantas megabytes voce usou:"))

if (TMV <= 60):
    VMV = TMV*0.20

elif (TMV > 60):
    VMV = TMV*0.45

if (TMG < 4096):
    VMG = TMG*0.035

elif (TMG >= 4096):
    VMG = TGM*0.015

VT = VMV + VMG

if (35.00 < VT < 50.00):
    print("O valor da sua conta e de R$ 35.00")

if (35.00 > VT or VT > 50.00):
    print("o valor da sua conta e de R$", VT)
