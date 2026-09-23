# Os exercícios com o número 2 na frente estão corrigidos (ou melhorados)

E = int(input())
S = int(input())
L = int(input())

valorMaximo = max(E, S , L)
valorMinimo = min(E, S, L)

total = 2 * (valorMaximo - valorMinimo)

print(total)