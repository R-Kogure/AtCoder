#愚直なTLE解法
N,Q = map(int,input().split())
A = list(map(int,input().split()))
tmp = list(i for i in range(10**18 + len(A)))
diff = list(set(tmp) - set(A))
for i in range(Q):
    k = int(input())
    print(diff[k])