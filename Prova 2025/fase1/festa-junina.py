E = int(input())
S = int(input())
L = int(input())

if(E > S and E > L and S > L):
    total = (E - S) + (E - L) + (S - L)
elif(E > S and E > L and L > S):
    total = (E - S) + (E - L) + (L - S)
elif(S > E and S > L and E > L):
    total = (S - E) + (S - L) + (E - L)
elif(S > E and S > L and L > E):
    total = (S - E) + (S - L) + (L - E)
elif(L > S and L > E and S > E):
    total = (L - S) + (L - E) + (S - E)
else:
    total = (L - S) + (L - E) + (E - S)

print(total)