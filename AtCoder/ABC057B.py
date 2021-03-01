from math import *
N,M = map(int,input().split())
ab = [list(map(int,input().split())) for i in range(N)]
cd = [list(map(int,input().split())) for i in range(M)]
for i in range(N):
    a,b = ab[i]
    dis = 10**9
    ans = 1
    for j in range(M):
        c,d = cd[j]
        tmpdis = abs(a-c) + abs(b-d)
        if dis > tmpdis:
            ans = j+1
            dis = tmpdis
    print(ans)

#別解 (あまり速度は変わらなかった)
N,M = map(int,input().split())
ab = [list(map(int,input().split())) for i in range(N)]
cd = [list(map(int,input().split())) for i in range(M)]
for i in range(N):
    dis = []
    a,b = ab[i]
    for j in range(M):
        c,d = cd[j]
        dis.append(abs(a-c) + abs(b-d))
    print(dis.index(min(dis))+1)
