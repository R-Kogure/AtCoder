def counting(a,b,X):
    """
    縦a，横b，通れない荒天の座標のlist:X
    """
    A = [[-1 for j in range(b+1)] for i in range(a+1)]
    for i in range(a+1):
        A[i][0] = 0
    for j in range(b+1):
        A[0][j] = 0
    for (i,j) in X:
        A[i][j] = 0
    A[1][1] = 1
    for i in range(1,a+1):
        for j in range(1,b+1):
            if A[i][j] == -1:
                #任意の点を通る経路は左と上の和
                A[i][j] = A[i][j-1] + A[i-1][j]
    return A[a][b]

#print(counting(5,6,[(2,3),(4,5)]))
　
