N = int(input())
if N == 1:
    print('Not Prime')
    exit()
num = 0
for i in range(len(str(N))):
    num += int(str(N)[i])
for i in range(2,int(N**0.5)+1):
    if N%i == 0:
        #not prime
        if int(str(N)[-1]) % 2 == 0 or str(N)[-1] == '5' or num %3 == 0:
            print('Not Prime')
            exit()
print("Prime")
