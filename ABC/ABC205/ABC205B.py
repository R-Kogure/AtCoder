N = int(input())
A = list(map(int,input().split()))
tmp = [i for i in range(1,N+1)]
A.sort()
if A == tmp:
    print("Yes")
else:
    print("No")