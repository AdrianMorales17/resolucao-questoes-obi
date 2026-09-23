# Exercicio das barras corrigida (errei mais nesse do que nos outros)

N = int(input())

X = list(map(int, input().split()))

#pega o maior valor da lista e define como altura
H = max(X)

# o I do for já é imprementado automaticamente
for i in range(H):
    for i2 in range(N):
        if X[i2] >= H:
            # O end = " " define um espaço no final de cada print, ao inves de um \n automatico
            print(1, end=" ")
        else:
            print(0, end=" ")

    H -= 1
    #nao precisa dar o \n pois já vem automatico
    print()