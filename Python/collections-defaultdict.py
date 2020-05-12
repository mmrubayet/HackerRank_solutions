from collections import defaultdict
n, m = map(int, input().split())
d = defaultdict(list)
ls = []
for i in range(1, n+1):
    d[input()].append(str(i))

for i in range(0,m):
    ls=ls+[input()]

for i in ls:
    if i in d:
        print(' '.join(d[i]))
    else:
        print(-1)
