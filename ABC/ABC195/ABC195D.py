N,M,Q = map(int,input().split())
WV = [list(map(int,input().split())) for _ in range(N)]
W = list(map(int,input().split()))

for _ in range(Q):
    l,r = map(int,input().split())
    new_W = W[:l-1] + W[r:]
    tmp_WV = WV[0:]#tmp_WV = WV とするとWVが破壊されてしまう
    if len(new_W) == 0:#全部使えない時
        print(0)
        continue
    new_W.sort()
    ans = 0
    for size in new_W:
        tmp_list = []
        for i in range(N):
            if tmp_WV[i][0] <= size:
                tmp_list.append([tmp_WV[i][1], i])
        if len(tmp_list) != 0:
            tmp_list.sort()
            ans += tmp_list[-1][0]
            tmp_WV[tmp_list[-1][1]] = [0,0]
    print(ans)
