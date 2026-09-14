N, M = map(int, input().split())
contador = 1

while contador <= N:
    P, G, C = map(int, input().split())
    M = M - ((P * 4)+(G * 9)+(C * 4))
    contador = contador + 1


print(M)

