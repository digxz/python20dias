operador = int(input("Digite 1 para soma: \nDigite 2 para subtração: \nDigite 3 para multiplicação: \nDigite 4 para divisão: \n"))

valor01 = int(input("Digite o primeiro valor: "))
valor02 = int(input("Digite o segundo valor: "))

soma = valor01 + valor02
subtracao = valor01 - valor02
multiplicacao = valor01 * valor02
divisao = valor01 / valor02


if operador == 1:
    print("O resultado da soma é: ", soma)
if operador == 2:
    print("O resultado da subtração é: ", subtracao) 
if operador == 3:
    print("O resultado da multiplicação é: ", multiplicacao)
if operador == 4:
    print("O resultado da divisão é: ", divisao)