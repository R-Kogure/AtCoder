import bisect
N,Q = map(int, input().split()) 
A = list(map(int, input().split()))

dif=[]
difs=[]
difk={}
tmp=0
num=0
for a in A:
  if a-tmp>1:
    num+=(a-tmp-1)
    difs.append(num)
    difk[num]=[a,tmp]
  tmp=a
if A[-1]!=10**20:
  a=10**20
  num+=(a-tmp-1)
  difs.append(num)
  difk[num]=[a,tmp]
 
for i in range(Q):
  k = int(input())
  index = bisect.bisect_left(difs, k)
  if index!=0:
    pre_index=index-1
    a,b=difk[difs[index]]
    c=difs[index-1]
    print(k-c+b)
  else:
    a,b=difk[difs[index]]
    print(k+b)