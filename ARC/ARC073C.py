N,T = map(int,input().split())
t = list(map(int,input().split()))
ans = T
for i in range(N-1):
    tmp = t[i+1] - t[i]
    if tmp  <= T:
        ans += tmp
    else:
        ans += T
print(ans)
