nome = input("Digite o nome do Aluno:")
nome = nome[:26]
matr = input("Digite a Matricula do Aluno:")
matr = matr[:6]

disciplinas = ["Português","Matemática","História","Geografia"]
notas = [0] * len(disciplinas)
m = 0
for i in range(len(disciplinas)):
    notas[i] = float(input("Digite a nota de " + disciplinas[i] + ": "))
    m = m + notas[i]

m = m / len(disciplinas)

print("{0:=>46}".format(" Boletim"))
print("Aluno: {:<26}  Mat: {:>6}".format(nome, matr))
print("{:->46}".format(""))
for i in range(len(disciplinas)):
    print("{0:.<13}: {1:5.2f}".format(disciplinas[i] , notas[i]))

print("{0:15}{0:->5}".format(""))
print("{0:.<13}: {1:5.2f}".format("Média" , m))
