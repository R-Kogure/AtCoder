import math
a,b,c = map(int,input().split())
if c%2 == 0:
    if abs(a) > abs(b):
        print(">")
    elif abs(a) == abs(b):
        print("=")
    else:
        print("<")
else:
    if a > 0 and b > 0:
        s = math.log(a)
        t = math.log(b)
        if s > t:
            print(">")
        elif s == t:
            print("=")
        else:
            print("<")
    elif a > b:
        print(">")
    elif a == b:
        print("=")
    else:
        print("<")