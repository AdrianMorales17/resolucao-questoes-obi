linha_p = list(map(int, input().split()))
P = linha_p[0]
tempos_p = linha_p[1:]

linha_c = list(map(int, input().split()))
C = linha_c[0]
tempos_c = linha_c[1:]

pi = 0
ci = 0

gp = 0
gc = 0

print(gp, gc)

while pi < P or ci < C:
    if pi >= P:
        ci += 1
        gc += 1
    elif ci >= C:
        pi += 1
        gp += 1
    else:
        if tempos_p[pi] < tempos_c[ci]:
            pi += 1
            gp += 1
        else:
            ci += 1
            gc += 1
            
    print(gp, gc)