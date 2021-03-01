def GCD(a,b):
    if b == 0:
        return a
    else :
        return GCD(b,a%b)
n,X = map(int,input().split())
ans = 0
x = list(map(int,input().split()))
for i in range(n):
    ans = GCD(ans,abs(x[i]-X))
print(ans)
