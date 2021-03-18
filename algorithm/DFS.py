from collections import deque

def DFS(T):
    D = deque()
    if len(T) > 0:
        D.append(T)
    while len(D) > 0:
        L,a,R = D.pop()
        print(a,end = ',')#end＝''は出力の最後を改行ではなく任意の文字列に置き換えることができる
        if len(L) > 0:
            D.append(L)
        if len(R) > 0:
            D.append(R)
    print()
"""
>>> X = ((((),111,()),11,((),112,())),1,(((),121,()),12,((),122,())))
>>> DFS(X)
1,12,122,121,11,112,111,
"""
