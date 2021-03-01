#ABC192-C
N,K = map(int,input().split())
#g(x)動いた
def g(x):
    tmp = len(str(x))
    l = []
    for i in range(tmp):
        l.append(int(str(x)[i]))
    num = 0
    l.sort()
    for i in range(tmp):
        num += l[i]*10**i
    return num
#gg(x)動いた
def gg(x):
    tmp = len(str(x))
    l = []
    for i in range(tmp):
        l.append(int(str(x)[i]))
    num = 0
    l.sort(reverse = True)
    for i in range(tmp):
        num += l[i]*10**i
    return num
#f(x)動いた
def f(x):
    return g(x) - gg(x)
if K == 0:
    print(N)
    exit()
ans = N
for i in range(1,K+1):
    ans = f(ans)
print(ans)
