# print("Ola, mundo")
# nome = "Miguel"
# idade = 16
# altura = 1.67

# print("Nome:",nome)
# print("Idade:",idade)
# print("Altura:", altura)

# num1 = int(input("Digite o primeiro número"))
# num2 = int(input("Digite o segundo número"))
# soma = num1 + num2
# sub = num1 - num2
# mult = num1 * num2
# div = num1 / num2

# print("soma", soma)
# print("sub", sub)
# print("mult", mult)
# print("div", div)

# Criar uma variavel de salario e dividir esse salario por 30. Em seguida fazer uma condicional para saber se o salario é baixo ou alto
salario = float(input("Meu salário"))
diario = salario / 30
print("salario diario", diario)

if salario > 2000:
    print("Você ganha bem")
else:
    print("Salário Minimo")#print ("olá, mundo!")
#nome= "arhur"
#idade =16
#altura = 1.45

#print("nome:", nome)
#print("idade:", idade)
#print("altura:", altura)

#num2 = int(input("coloque o segundo numero"))
#num1 = int(input("coloque o primeiro numero"))
#soma = num1 + num2
#sub = num1 - num2
#div = num1 / num2 
#mult = num1 * num2
#poten = num1 ** num2

#print(f"a soma do primeiro numero: {num1} com o segundo numero: {num2} dá {soma}")
#print(f"a subtração do primeiro numero: {num1} com o segundo numero: {num2} dá {sub}")
#print(f"a divisão do primeiro numero: {num1} com o segundo numero: {num2} dá {div}")
#print(f"a multiplicação do primeiro numero: {num1} com o segundo numero: {num2} dá {mult}")
#print(f"a potencia do primeiro numero: {num1} com o segundo: {num2} dá: {poten}")

#criar variavel salario e dividir esse salario por 30. Em seguida fazer uma condicional para saber se o salario é baixo ou alto
salario = int(input("coloque quanto voce ganha por mes: "))
dia = salario / 30

if salario >= 3000:
    print(f"Salário muito alto, recebendo {dia:.2f} por dia!")
elif salario >= 1000 and salario <= 2999:
    print(f"Salário na média, recebendo {dia:.2f} por dia.")
else:
    print(f"Salário muito baixo, recebendo {dia:.2f} por dia, o que dá menos que um salário mínimo!")
