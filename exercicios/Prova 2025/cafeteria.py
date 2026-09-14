A = int(input())
B = int(input())
C = int(input())
D = int(input())

# O volume total que tem que ter é o C e D é a dose de café
resposta = "N"

while A <= B:
    resto = C - A

    if resto % D == 0:
        resposta = "S"

    A += 1
    

print(resposta)