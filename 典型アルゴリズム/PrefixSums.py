N,Q = map(int,input().split())
a = list(map(int,input().split()))
Sa = [0]
num = 0
for i in a:
    num += i
    Sa.append(num)
ans = 0
for i in range(Q):
    r,l = map(int,input().split())
    ans = Sa[l] - Sa[r-1]
    print(ans)
