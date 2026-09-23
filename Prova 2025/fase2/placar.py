P = list(map(int, input().split()))
C = list(map(int, input().split()))
i = 0 
PI = 1
CI = 1
GP = 0
GC = 0
TG = P[0] + C[0]
print (0 , 0)
for i in range(TG):
    if(CI < C[0] and PI < P[0]):
        if(P[PI] < C[CI]):
            PI=PI + 1
            GP= GP + 1
            print(GP , GC)
        else:
            CI= CI + 1
            GC= GC + 1
            print(GP , GC)
    else:
        if(CI > C[0]):
            PI=PI + 1
            GP= GP + 1
            print(GP , GC)
        else:
            CI= CI + 1
            GC= GC + 1
            print(GP , GC)
    i=+1 

if(TG == 0):
    print(0 , 0)

    