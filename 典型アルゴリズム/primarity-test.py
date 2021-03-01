#素数判定
N = int(input())
for i in range(2,int(N**0.5)+1):
    if N%i == 0:
        print(str(N) + ' is not prime number')
        exit()
print(str(N) + ' is prime number')
