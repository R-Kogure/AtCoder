#ARC115-A
N,M = map(int,input().split())
S = [str(input()).count('1') for _ in range(N)]
#print(S)
from collections import Counter
ans = 0
C = Counter(S)
val = [0 for _ in range(M+1)]
for k,v in C.items():
    val[k] = v

for i in range(M):
    for j in range(i+1,M+1,2):
        ans += val[i]*val[j]
print(ans)
