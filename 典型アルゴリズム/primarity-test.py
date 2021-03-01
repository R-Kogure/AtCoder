#素数判定
N = int(input())
for i in range(2,int(N**0.5)+1):
    if N%i == 0:
        print(f'{N} is not prime number')
        exit()
print(f'{N} is prime number')
