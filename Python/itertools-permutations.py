from itertools import permutations
a, k = input().split()
print(*[''.join(i) for i in permutations(sorted(a),int(k))],sep='\n')
