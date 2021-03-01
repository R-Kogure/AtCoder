A,B = map(int,input().split())
def GCD(a,b):
    if b == 0:
        return a
    else :
        return GCD(b,a%b)
print(A*B//GCD(A,B))
#A*Bでオーバーフローしない様に(A//GCD(A,B))*Bとする方が良い
