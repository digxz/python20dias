numero = int(input("Digite: "))

contador = 0
soma = 0

while numero != -273:
    soma += numero
    contador =+ 1
    numero = int(input("Digite: "))

media = soma / contador
print(f"O valor final é: {media}")