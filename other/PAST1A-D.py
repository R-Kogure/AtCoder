"""
第一回 アルゴリズム実技検定 過去問
"""
#A問題
lis = []
for i in range(10):
    lis.append(str(i))
N = input()
for i in range(3):
    if N[i] not in lis:
        print('error')
        exit()
print(int(N)*2)

#B問題
N = int(input())
A = [int(input()) for i in range(N)]

for i in range(N-1):
    tmp = A[i+1]-A[i]
    if tmp > 0:
        print(f'up {tmp}')
    elif tmp == 0:
        print('stay')
    else:
        print(f'down {abs(tmp)}')

#C問題
tmp = list(map(int,input().split()))
tmp.sort()
print(tmp[-3])

#D問題
N = int(input()) # N <= 2*10**5
A = [int(input()) for i in range(N)]
tmp = set(A)
if len(tmp) == N:
    print('Correct')
    exit()
for i in range(1,N+1):
    A.append(i)
from collections import Counter
c = Counter(A)
ans = []
for k,v in c.items():
    if v == 1:
        y = k
    elif v == 3:
        x = k
print(x,y)
