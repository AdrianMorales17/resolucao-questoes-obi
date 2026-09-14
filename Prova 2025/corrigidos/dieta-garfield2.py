# versão corrigida do exercicio feito individualmente

N, M = map(int, input().split())

i = 1

while i <= N:
    P, G, C = map(int, input().split())

    M = M - ((P * 4) + (G * 9) + (C * 4))

    #o unico ponto de alteração
    i += 1

print(M)
