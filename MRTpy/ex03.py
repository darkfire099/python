#A empresa Pioli S.A resolveu dar um aumento de salario aos seus colaboradores. Vovê foi contratado para criar um programa que calculará esses reajustes segundo os seguintes criterios
#salarios até 1240,00: aumento de 20%
#salario entre 1240,01 até 2500,00: aumento de 15%
#salarios entre 2500,01 e 3200,00: aumento de 10%
#salario a partir de 3200,01: aumento de 5%
#Imprima na tela:o valor do salario antes do aumento, o percentual aplicado, o valor do aumento e o novo salario
salario = float(input("qual seu salario?  "))
if salario <= 1240:
    var1 = salario * 0.20
    total1 = salario + var1
    print(f"seu salario foi de {salario} com a variaçao de 20%, e um aumento de {var1:.2f} que da um tota de {total1}")
elif salario >= 1240.01 and salario <= 2500:
    var2 = salario * 0.15
    total2 = salario + var2
    print(f"seu salario foi de {salario} com a variaçao de 15%, e um aumento de {var2:.2f} que da um tota de {total2}")
elif salario >= 2500.01 and salario <= 3200:
    var3 = salario * 0.10
    total3 = salario + var3
    print(f"seu salario foi de {salario} com a variaçao de 10%, e um aumento de {var3:.2f} que da um tota de {total3}")
elif salario >= 3100.01:
    var4 = salario * 0.05
    total4 = salario + var4
    print(f"seu salario foi de {salario} com a variaçao de 5%, e um aumento de {var4:.2f} que da um tota de {total4}")
else:
    print("nao sei")