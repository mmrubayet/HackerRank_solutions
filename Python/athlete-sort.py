n, m = map(int, input().split())
ls = [input() for _ in range(n)]
k = int(input())
print(*sorted(ls, key=lambda l: int(l.split()[k])), sep='\n')
