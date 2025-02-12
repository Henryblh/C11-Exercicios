nome = input("Digite seu nome completo: ")
print(nome.upper())
print(nome.lower())

letras = len(nome.replace(" ", ""))
print("Seu nome possui ", letras , "letras")

nomeDivido = nome.split()
nomeDivido[-1] = "do Inatel"
print(" ".join(nomeDivido),"\n")

x = int(input("Escolha um número: "))
print("Escolha um intervalo da tabuada")
print("Tabuada do:", x, "\nEntre:", end=" [")
y = int(input())
print(" e", end=" ")
z = int(input())
print("]")

for i in range(y, z + 1):
    print(f"{x} x {i} = {x * i}")

while True:
    print("Você ", nome,". Digite o sexo (M/F): ")
    sexo = input().upper()
    if sexo == "M":
        print("Você é um homem.")
        break
    elif sexo == "F":
        print("Você é uma mulher.")
        break
    else:
        print("Digite apenas M ou F")


distancia = float(input("Qual a distância da viagem? "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print("O preço da passagem é R$ ",preco)

