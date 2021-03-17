a,b = map(int,input().split())
def GCD(a,b):
    if b == 0:
        return a
    else :
        return GCD(b,a%b)
print(GCD(a,b))
#O(logA)
