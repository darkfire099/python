#exercicio 01:
#uma empresa decidiu dar um bonus de 15% sobre o faturamento total para a equipe de vemdas. crie um progama para calcular o valor do bonus e o faturamento final da empresa apos subtrair esse bonus.
#faturamneto inicial: 50.000
#percentual de bonus: 0.15
#ao mostrar o resultado, mostre apenas duas casas decimais

faturainc = float(input("qual sua fatura inicial?"))
bonus = faturainc * 0.15
faturarin= faturainc - bonus
print(f"Com o seu bônus de 15%, a fatura final será {faturarin:.2f}")