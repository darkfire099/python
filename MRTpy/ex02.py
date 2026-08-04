#exercicio 02
#Um empresa começou o dia com 320 unidades de mouses gamers no estoque. Durante o dia, foram vendidos 83 unidades e chegaram mais 112 de um fornecedor. Crie um programa que mostre o estoque inicial, a quantidade vendida, a reposição e o estoque final ao final do dia
EstoqueInicial =int(input("Digite o estoque inicial"))
ProdutosVendidos = int(input("Digite a uantidade de mouses vendidos"))
Reposiçao =int(input("Digite o numero Digite a quantidade de produtos que chegaram para a reposição"))
EstoqueFinal = EstoqueInicial - ProdutosVendidos + Reposiçao

print(f"Com a venda e as reposições, o estoque que era de {EstoqueInicial} ficou com {EstoqueFinal}")