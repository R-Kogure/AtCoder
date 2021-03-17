import itertools
n = int(input())
l = list(range(n))
permutation_l = itertools.permutations(l)
for i in permutation_l:
    print(i)
