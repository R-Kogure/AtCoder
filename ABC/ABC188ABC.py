x,y = map(int,input().split())
if abs(x-y) >= 2:
    print('Yes')
else:
    print('No')



N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
v = 0
for i in range(N):
    v += A[i]*B[i]
if v == 0:
    print('Yes')
else:
    print('No')

N = int(input())
A = list(map(int,input().split()))
ah = A[:2**(N-1)]
ha = A[2**(N-1):]
nah = ah.index(max(ah))
nha = ha.index(max(ha))
if max(ah) > max(ha):
    print(2**(N-1)+nha+1)
else:
    print(nah + 1)
