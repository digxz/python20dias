media = 6
if media < 5:
    print("Você foi reprovado")
elif media >= 5 and media < 7:
    print("Você fará a recuperação")
else:
    print("Você foi aprovado")



for x in range(10,16):
    print(x)


gastos=0
valor_gasto=0
while gastos < 1000:
    valor_gasto = int(input("Digite o valor gasto: "))
    gastos = gastos + valor_gasto
print(gastos)

print(type(gastos))