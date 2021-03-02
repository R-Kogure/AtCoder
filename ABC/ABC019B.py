s = input()
l = len(s)
ans = ''
tmp = s[0]
num = 0
for i in range(l):
    if s[i] == tmp:
        num += 1
    else:
        ans += (tmp + str(num))
        tmp = s[i]
        num = 1
ans += (tmp + str(num))
print(ans)
