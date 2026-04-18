nome = input("Digite o nome do Aluno:")
nome = nome[:26]
matr = input("Digite a Matricula do Aluno:")
matr = matr[:6]
por = float(input("Digite a nota de Português:"))
mat = float(input("Digite a nota de Matemática:"))
his = float(input("Digite a nota de História:"))
m = (por+mat+his)/3

print("{0:=>46}".format(" Boletim"))
print("Aluno: {:<26}  Mat: {:>6}".format(nome, matr))
print("{:->46}".format(""))
print("{0:.<13}: {1:5.2f}".format("Português" , por))
print("{0:.<13}: {1:5.2f}".format("Matemática" , mat))
print("{0:.<13}: {1:5.2f}".format("História" , por))
print("{0:15}{0:->5}".format(""))
print("{0:.<13}: {1:5.2f}".format("Média" , m))
