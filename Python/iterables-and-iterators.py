from itertools import combinations
n = int(input())
ar = input().split()
k = int(input())
l = list(combinations(ar, k))
f = filter(lambda cc: 'a' in cc, l)
print("{0:.3}".format(len(list(f))/len(l)))
