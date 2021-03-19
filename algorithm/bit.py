"""
bit列を生成したい時
"""
N = int(input())
for i in range(N):
    binary = bin(i)[2:]#binは頭に0bがつくので切る
    #欲しい文字列の長さ以下なら頭に0を足りない分補充する
    if  len(binary)< '欲しい長さ':
        binary="0"*('欲しい長さ- len(binary)')+binary
    #print(binary)


"""
ARC061C
bit全探
"""
S = input()
ans = []
for i in range(2**(len(S)-1)):
    binary = bin(i)[2:]
    if  len(binary)<len(S)-1:
        binary="0"*(len(S)-1-len(binary))+binary
    #print(binary)
    cut = 0
    tmp = 0
    for j in range(len(binary)):
        if binary[j] == '1':
            tmp += int(S[cut:j+1])
            cut = j+1
    if S[cut:len(S)] != '':
        tmp += int(S[cut:len(S)])
    ans.append(tmp)
print(sum(ans))

"""
ABC079C
bit全探
"""
s = input()
for i in range(2**(len(s)-1)):
    binary = bin(i)[2:]
    if  len(binary)<3:
        binary="0"*(3-len(binary))+binary
    num = int(s[0])
    ans = s[0]
    for j in range(3):
        if binary[j] == '0':
            num += int(s[j+1])
            ans += '+' + s[j+1]
        else:
            num -= int(s[j+1])
            ans += '-' + s[j+1]
    if num == 7:
        ans += '=7'
        print(ans)
        exit()
