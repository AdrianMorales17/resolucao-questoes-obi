N = (int(input()))

X = list(map(int, input().split()))

H = max(X)
altura = H
i = 0

for i in range(H):
    i2 = 0
    for i2 in range(N):
        if X[i2] >= altura:
            print(1, end=" ")
        else:
            print(0, end=" ")
        i2 += 1
    altura = H
    i+=1
    altura -= i
    #fiz errado
    print("\n")