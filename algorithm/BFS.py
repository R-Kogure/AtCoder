from collections import deque
"""
BFSはDFSのコードのpop()をpopleft()に変更するだけ
つまりdequeをキューで使うかスタックで使うかの違い
"""
def BFS(T):
    D = deque()
    if len(T) > 0:
        D.append(T)
    while len(D) > 0:
        L,a,R = D.popleft()
        print(a,end = ',')
        if len(L) > 0:
            D.append(L)
        if len(R) > 0:
            D.append(R)
    print()
