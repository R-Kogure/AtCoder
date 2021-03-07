A,B = map(int,input().split())
tmp = A+B
if tmp >= 15 and B >= 8:
    print(1)
elif tmp >= 10 and B >= 3:
    print(2)
elif tmp >= 3:
    print(3)
else:
    print(4)
