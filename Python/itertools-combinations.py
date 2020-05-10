from itertools import combinations
a, k = input().split()
for n in range(1, int(k)+1):
    print(*[''.join(i) for i in combinations(sorted(a), n)],sep='\n')
