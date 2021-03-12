"""
再帰によるfibonacci
分割統治？
"""
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
N = int(input())
print(fib(N))


"""
DPによるfibonacci
"""
N = int(input())
fib = [0,1]
for i in range(2,N+1):
    fib.append(fib[i-1] + fib[i-2])
print(fib[N])


"""
tupleによる効率的なfibonacci
n項目の受け取りはfib(n)[-1]
"""
def fib(n):
    if n == 0:
        return (0,0)
    elif n == 1:
        return (0,1)
    else:
        (a,b) = fib(n-1)
        return (b, a+b)   
