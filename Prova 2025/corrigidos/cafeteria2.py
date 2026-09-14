# resolução melhorada do exercicio da cafeteria

A = int(input())
B = int(input())
C = int(input())
D = int(input())

resposta = "N"

while A <= B:
    resto = C - A

    if resto % D == 0:
        resposta = "S"
        break # para o loop (nao sabia desse comando)

    A += 1

print(resposta)

